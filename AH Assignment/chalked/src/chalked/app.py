"""
Log Climbs
"""

import toga
from toga.style.pack import COLUMN, ROW, CENTER
from pathlib import Path
import sqlite3
import asyncio

toga.Widget.DEBUG_LAYOUT_ENABLED = True



class Entry():
    def __init__(self, ID, date, type, grade, attempts, notes):
        self.__ID = ID
        self.__date = date
        self.__type = type
        self.__grade = grade
        self.__attempts = attempts
        self.__notes = notes

    def getID(self):
        return self.__ID
    
    def getDate(self):
        return f"{self.__date[8:]}/{self.__date[5:7]}/{self.__date[0:4]}"
    
    def getType(self):
        return self.__type
    
    def getGrade(self):
        return self.__grade
    
    def getAttempts(self):
        return self.__attempts
    
    def getNotes(self):
        return self.__notes

    def getDetails(self):
        return f"{self.__type}: {self.__grade}, {self.__notes}"



class Chalked(toga.App):
    def startup(self):
        self.path = self.paths.data / "entriesDatabase.db"
        
        #Checking for/Creating Database
        try:
            database = open(self.path, "x")
            self.connectToDB()
            self.cur.execute("CREATE TABLE 'Entries' ('ID' INTEGER, 'Date' TEXT, 'Type' TEXT, 'Grade' TEXT, 'Notes' TEXT, 'Attempts' INTEGER);")
        except:
            self.connectToDB()

        #Defining Nav Bar
        self.navBox = toga.Box(direction = ROW)
        self.homeButton = toga.Button("Home", on_press = self.switchScreenMain, flex = 1)
        self.addButton = toga.Button("Add Entry", on_press = self.switchScreenAdd, flex = 2)
        self.statsButton = toga.Button("Stats", on_press = self.switchScreenStats, flex = 1)
        self.navBox.add(self.homeButton, self.addButton, self.statsButton)

        self.mainBox = toga.Box(direction = COLUMN, flex = 1)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.switchScreenMain(None)
        self.main_window.show()


    def connectToDB(self):
        self.con = sqlite3.connect(self.path)
        self.cur = self.con.cursor()
    
    def getCursor(self):
        return self.cur

    def switchScreen(self, newScreen):
        self.activeScreen = newScreen
        self.mainBox.clear()
        self.mainBox.add(self.activeScreen.getContent(), self.navBox)
        self.main_window.content = self.mainBox

    def switchScreenMain(self, widget):
        self.switchScreen(MainScreen(self))

    def switchScreenAdd(self, widget):
        self.switchScreen(AddScreen(self))

    def switchScreenStats(self, widget):
        self.switchScreen(StatsScreen(self))

    

class MainScreen():
    def __init__(self, app):
        self.app = app
        self.cur = app.getCursor()
        self.entries = []

        #Defining Layout Boxes
        self.contentBox = toga.Box(direction = COLUMN, flex = 1)
        self.searchBox = toga.Box(direction = ROW)
        self.filterBox = toga.Box(direction = ROW)
        self.listBox = toga.Box(direction = COLUMN, flex = 1)

        #Defining Widgets
        self.searchBar = toga.TextInput(value = "Enter Search Term...", flex = 7)
        self.searchButton = toga.Button("Search", flex = 1)
        self.filter1 = toga.Button("Lead Climbs", on_press = self.filterLead, flex = 1)
        self.filter2 = toga.Button("Boulders", on_press = self.filterBoulder, flex = 1)
        self.reset = toga.Button("Reset", on_press = self.resetFilter, flex = 0.5)
        self.table = toga.DetailedList(on_primary_action = self.deleteItem, on_secondary_action = self.viewItem, flex = 1)

        #Adding Widgets to Boxes
        self.contentBox.add(self.searchBox, self.filterBox, self.listBox)
        self.searchBox.add(self.searchBar, self.searchButton)
        self.filterBox.add(self.filter1, self.filter2)
        self.listBox.add(self.table)

        self.resetFilter(None)


    def filterList(self, type):
        newList = []
        for row in self.cur.execute(f"SELECT * FROM Entries WHERE Type LIKE '{type}%';"):
            newList.append(Entry(row[0], row[1], row[2], row[3], row[4], row[5]))
        self.entries = newList
        self.updateTable()

        if self.reset not in self.filterBox.children:
            self.filterBox.add(self.reset)
        
    def filterLead(self, widget):
        self.filterList("Lead")

    def filterBoulder(self, widget):
        self.filterList("Boulder")

    def resetFilter(self, widget):
        self.filterList("%")
        self.filterBox.remove(self.reset)

    def updateTable(self):
        self.table.data = [{
            "icon": None,
            "title": i.getDate(),
            "subtitle": i.getDetails(),
            "data": i.getID()
        } for i in self.entries]

    def deleteItem(self, widget, row):
        self.cur.execute(f"DELETE FROM Entries WHERE ID = '{row.data}';")
        self.entries.pop(row.data)
        self.app.con.commit()
        self.updateTable()

    def viewItem(self, widget, row):
        self.app.switchScreen(ViewScreen(Chalked, row.data))

    def getContent(self):
        return self.contentBox



class AddScreen():
    def __init__(self, app):
        self.app = app
        self.cur = app.getCursor()

        #Defining Layout Boxes
        self.contentBox = toga.Box(direction = COLUMN, flex = 1)
        self.formBox = toga.Box(direction = COLUMN, flex = 1)
        self.gradeBox = toga.Box(direction = ROW, flex = 1, align_items = CENTER)
        self.attemptsBox = toga.Box(direction = ROW, flex = 1, align_items = CENTER)
        self.notesBox = toga.Box(direction = ROW, flex = 1, align_items = CENTER)

        #Defining Widgets
        self.dateInput = toga.DateInput()
        self.typeInput = toga.Selection(items = ["Lead Climb", "Boulder"])
        self.gradeLabel = toga.Label(text = "Grade:", flex = 1)
        self.gradeInput = toga.TextInput(flex = 3)
        self.attemptsLabel = toga.Label(text = "Attempts:", flex = 1)
        self.attemtpsInput = toga.NumberInput(flex = 3)
        self.notesLabel = toga.Label(text = "Notes:", flex = 1)
        self.notesInput = toga.MultilineTextInput(flex = 3)
        self.addButton = toga.Button(direction = ROW, text = "Add", flex = 1, on_press = self.addEntry)

        #Adding Widgets to Boxes
        self.gradeBox.add(self.gradeLabel, self.gradeInput)
        self.attemptsBox.add(self.attemptsLabel, self.attemtpsInput)
        self.notesBox.add(self.notesLabel, self.notesInput)
        self.formBox.add(self.dateInput, self.typeInput, self.gradeBox, self.attemptsBox, self.notesBox)
        self.contentBox.add(self.formBox, self.addButton)


    async def addEntry(self, widget):
        try:
            for col in self.cur.execute("SELECT MAX(ID) FROM Entries"):
                previousID = col[0]
            nextID = previousID + 1
        except:
            nextID = 0

        self.cur.execute(f"INSERT INTO Entries VALUES ('{nextID}', '{self.dateInput.value}', '{self.typeInput.value}', '{self.gradeInput.value}', '{self.notesInput.value}', {self.attemtpsInput.value});")
        self.app.con.commit()
        self.gradeInput.value = None
        self.attemtpsInput.value = None
        self.notesInput.value = None
        addedEntryDialog = toga.InfoDialog("Entry Added", "Entry Added to Database")
        await self.app.main_window.dialog(addedEntryDialog)

    def getContent(self):
        return self.contentBox



class ViewScreen():
    def __init__(self, app, rowID):
        self.app = app
        self.rowID = rowID

        for col in self.app.cur.execute(f"FROM Entries WHERE ID = {self.rowID}"):
            viewedRow = Entry(col[0], col[1], col[2], col[3], col[4], col[5])

        #Defining Layout Boxes
        self.contentBox = toga.Box(direction = COLUMN)
        self.dateClimbBox = toga.Box(direction = ROW)
        self.gradeAttemptsBox  = toga.Box(direction = ROW)
        self.notesBox = toga.Box(direction = COLUMN)

        #Defining Widgets
        self.dataLabel = toga.Label(text = viewedRow.getDate())
        self.typeLabel = toga.Label(text = viewedRow.getType())
        self.gradeLabel = toga.Label(text = viewedRow.getGrade())
        self.attemptsLabel = toga.Label(text = viewedRow.getAttempts())
        self.notesLabel = toga.Label(text = viewedRow.getNotes())
        
        #Adding Widgets to Boxes




class StatsScreen():
    def __init__(self, app):
        self.app = app

        self.contentBox = toga.Box()
        self.contentBox.add()

    def getContent(self):
        return self.contentBox

        
        
def main():
    return Chalked() 
