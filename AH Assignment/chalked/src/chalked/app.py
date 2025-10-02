"""
Log Climbs
"""

import toga
from toga.style.pack import COLUMN, ROW

from pathlib import Path

import sqlite3


toga.Widget.DEBUG_LAYOUT_ENABLED = True

class Entry():
    def __init__(self, date, type, grade, attempts):
        self.__date = date
        self.__type = type
        self.__grade = grade
        self.__attempts = attempts

    def getDate(self):
        return self.__date
    def setDate(self, newDate):
        self.__date = newDate

    def getType(self):
        return self.__type
    def setType(self, newType):
        self.__type = newType

    def getGrade(self):
        return self.__grade
    def setGrade(self, newGrade):
        self.__grade = newGrade

    def getAttempts(self):
        return self.__attempts
    def increaseAttempts(self):
        self.__attempts += 1

    def getDetails(self):
        return f"{self.__type}, {self.__grade}, {self.__attempts}"


class Chalked(toga.App):
    def startup(self):
        self.con = sqlite3.connect(Path(__file__).parent / "resources/entriesDatabase.db")
        self.cur = self.con.cursor()

        self.entries = []

        self.activeScreen = mainScreen(self)

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


class mainScreen():
    def __init__(self, app):

        self.app = app
        self.cur = app.getCursor()
        self.entries = app.getEntries()

        self.mainBox = toga.Box(direction = COLUMN)
        self.searchBox = toga.Box(direction = ROW)
        self.filterBox = toga.Box(direction = ROW)
        self.listBox = toga.Box(direction = COLUMN, flex = 1)
        self.navBox = toga.Box(direction = ROW)

        self.searchBar = toga.TextInput(value = "Enter Search Term...", flex = 7)
        self.searchButton = toga.Button("Search", on_press = self.search_press, flex = 1)
        self.filter1 = toga.Button("Lead Climbs", on_press = self.filterLead, flex = 1)
        self.filter2 = toga.Button("Boulders", on_press = self.filterBoulder, flex = 1)
        self.reset = toga.Button("Reset", on_press = self.resetFilter, flex = 0.5)

        self.table = toga.DetailedList(flex = 1)

        self.addButton = toga.Button("Add Entry")

        self.mainBox.add(self.searchBox, self.filterBox, self.listBox, self.navBox)
        self.searchBox.add(self.searchBar, self.searchButton)
        self.filterBox.add(self.filter1, self.filter2)
        self.listBox.add(self.table)
        self.navBox.add(self.addButton)

        self.resetFilter(None)


    def filterList(self, type):
        newList = []
        for row in self.cur.execute(f"SELECT * FROM Entries WHERE Type LIKE '{type}%'"):
            newList.append(Entry(row[0], row[1], row[2], row[3]))
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
    
    def search_press(self, widget):
        self.app.switchScreen(Test())


class Test():
    def __init__(self):
        self.box = toga.Box()

    def getScreen(self):
        return self.box

        
def main():
    return Chalked()
