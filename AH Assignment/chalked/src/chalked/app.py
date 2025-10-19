"""
Log Climbs
"""

import toga
from toga.style.pack import COLUMN, ROW, CENTER
from pathlib import Path
import sqlite3

toga.Widget.DEBUG_LAYOUT_ENABLED = True



class Entry():
    def __init__(self, date, type, grade, notes, attempts):
        self.__date = date
        self.__type = type
        self.__grade = grade
        self.__notes = notes
        self.__attempts = attempts

    def getDate(self):
        return f"{self.__date[8:]}/{self.__date[5:7]}/{self.__date[0:4]}"

    def getDetails(self):
        return f"{self.__type}: {self.__grade}, {self.__notes}"



class Chalked(toga.App):
    def startup(self):
        self.con = sqlite3.connect(Path(__file__).parent / "resources/entriesDatabase.db")
        self.cur = self.con.cursor()

        self.entries = []

        self.navBox = toga.Box(direction = ROW)
        self.homeButton = toga.Button("Home", on_press = self.switchScreenMain, flex = 1)
        self.addButton = toga.Button("Add Entry", on_press = self.switchScreenAdd, flex = 2)
        self.statsButton = toga.Button("Stats", on_press = self.switchScreenStats, flex = 1)

        self.navBox.add(self.homeButton, self.addButton, self.statsButton)

        self.activeScreen = MainScreen(self)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.activeScreen.getScreen()
        self.main_window.show()
    

    def getCursor(self):
        return self.cur
    
    def getEntries(self):
        return self.entries
    
    def setEntries(self, newList):
        self.entries = newList

    def switchScreen(self, newScreen):
        self.activeScreen = newScreen
        self.main_window.content = self.activeScreen.getScreen()

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
        self.entries = app.getEntries()

        self.mainBox = toga.Box(direction = COLUMN)
        self.searchBox = toga.Box(direction = ROW)
        self.filterBox = toga.Box(direction = ROW)
        self.listBox = toga.Box(direction = COLUMN, flex = 1)

        self.searchBar = toga.TextInput(value = "Enter Search Term...", flex = 7)
        self.searchButton = toga.Button("Search", flex = 1)
        self.filter1 = toga.Button("Lead Climbs", on_press = self.filterLead, flex = 1)
        self.filter2 = toga.Button("Boulders", on_press = self.filterBoulder, flex = 1)
        self.reset = toga.Button("Reset", on_press = self.resetFilter, flex = 0.5)

        self.table = toga.DetailedList(flex = 1)

        self.mainBox.add(self.searchBox, self.filterBox, self.listBox, self.app.navBox)
        self.searchBox.add(self.searchBar, self.searchButton)
        self.filterBox.add(self.filter1, self.filter2)
        self.listBox.add(self.table)

        self.resetFilter(None)


    def filterList(self, type):
        newList = []
        for row in self.cur.execute(f"SELECT * FROM Entries WHERE Type LIKE '{type}%'"):
            newList.append(Entry(row[0], row[1], row[2], row[3], row[4]))
        self.table.data = [{
            "icon": None,
            "title": i.getDate(),
            "subtitle": i.getDetails()
        } for i in newList]
        self.app.setEntries(newList)

        if self.reset not in self.filterBox.children:
            self.filterBox.add(self.reset)
        
    def filterLead(self, widget):
        self.filterList("Lead")

    def filterBoulder(self, widget):
        self.filterList("Boulder")

    def resetFilter(self, widget):
        self.filterList("%")
        self.filterBox.remove(self.reset)

    def getScreen(self):
        return self.mainBox



class AddScreen():
    def __init__(self, app):
        self.app = app
        self.cur = app.getCursor()

        #Defining Layout Boxes
        self.mainBox = toga.Box(direction = COLUMN)
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
        self.mainBox.add(self.formBox, self.addButton, self.app.navBox)


    def addEntry(self, widget):
        self.cur.execute(f"INSERT INTO Entries VALUES ('{self.dateInput.value}', '{self.typeInput.value}', '{self.gradeInput.value}', '{self.notesInput.value}', {self.attemtpsInput.value});")
        self.app.con.commit()

    def getScreen(self):
        return self.mainBox



class StatsScreen():
    def __init__(self, app):
        self.app = app

        self.mainBox = toga.Box()
        self.mainBox.add(self.app.navBox)

    def getScreen(self):
        return self.mainBox

        
def main():
    return Chalked() 
