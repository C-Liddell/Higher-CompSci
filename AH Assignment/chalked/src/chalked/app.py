"""
Log Climbs
"""

import toga
from toga.style.pack import COLUMN, ROW

class Entry():
    def __init__(self):
        self.__date = "01/01/25"
        self.__type = "Climb"
        self.__grade = "V0"
        self.__attempts = 0

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

entries = [Entry() for x in range(10)]



class Chalked(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        mainBox = toga.Box(direction = COLUMN)
        searchBox = toga.Box(direction = ROW)
        filterBox = toga.Box(direction = ROW)
        listBox = toga.Box(direction = COLUMN)
        navBox = toga.Box(direction = ROW)


        searchBar = toga.TextInput(value = "Enter Search Term...", flex = 7)
        searchButton = toga.Button("Search", flex = 1)

        filter1 = toga.Button("Lead Climbs", flex = 1)
        filter2 = toga.Button("Top Rope Climbs", flex = 1)
        filter3 = toga.Button("Boulders", flex = 1)

        table = toga.DetailedList(
            data = [{
                "icon": None,
                "title": i.getDate(),
                "subtitle": i.getDetails()
                } for i in entries]
        )

        addButton = toga.Button("Add Entry")

        mainBox.add(searchBox, filterBox, listBox, navBox)
        searchBox.add(searchBar, searchButton)
        filterBox.add(filter1, filter2, filter3)
        listBox.add(table)
        navBox.add(addButton)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = mainBox
        self.main_window.show()


def main():
    return Chalked()
