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
        #for row in self.cur.execute("SELECT * FROM Entries"):
            #self.entries.append(Entry(row[0], row[1], row[2], row[3]))

        mainBox = toga.Box(direction = COLUMN)
        searchBox = toga.Box(direction = ROW)
        self.filterBox = toga.Box(direction = ROW)
        listBox = toga.Box(direction = COLUMN, flex = 1)
        navBox = toga.Box(direction = ROW)

        searchBar = toga.TextInput(value = "Enter Search Term...", flex = 7)
        searchButton = toga.Button("Search", flex = 1)

        filter1 = toga.Button("Lead Climbs", on_press = self.filterLead, flex = 1)
        filter2 = toga.Button("Top Rope Climbs", on_press = self.filterTR, flex = 1)
        filter3 = toga.Button("Boulders", on_press = self.filterBoulder, flex = 1)
        self.reset = toga.Button("Reset", on_press = self.resetFilter, flex = 0.5)

        self.table = toga.DetailedList(flex = 1)
        self.resetFilter(None)

        addButton = toga.Button("Add Entry")

        mainBox.add(searchBox, self.filterBox, listBox, navBox)
        searchBox.add(searchBar, searchButton)
        self.filterBox.add(filter1, filter2, filter3)
        listBox.add(self.table)
        navBox.add(addButton)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = mainBox
        self.main_window.show()


    def filterList(self, type):
        newList = []
        for row in self.cur.execute(f"SELECT * FROM Entries WHERE Type LIKE '{type}%'"):
            newList.append(Entry(row[0], row[1], row[2], row[3]))
        self.entries = newList
        self.table.data = [{
            "icon": None,
            "title": i.getDate(),
            "subtitle": i.getDetails()
        } for i in self.entries]

        if self.reset not in self.filterBox.children:
            self.filterBox.add(self.reset)
        
    def filterLead(self, widget):
        self.filterList("Lead")

    def filterTR(self, widget):
        self.filterList("Top Rope")

    def filterBoulder(self, widget):
        self.filterList("Boulder")

    def resetFilter(self, widget):
        self.filterList("%")
        self.filterBox.remove(self.reset)


def main():
    return Chalked()
