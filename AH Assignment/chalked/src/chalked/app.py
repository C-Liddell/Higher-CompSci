"""
Log Climbs
"""

import toga
from toga.style.pack import COLUMN, ROW

class Entry():
    def __init__(self):
        self.__date = ""
        self.__type = ""
        self.__grade = ""
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

testEntry = Entry()
testEntry.setDate("24/09/25")
testEntry.setType("Boulder")
testEntry.setGrade("V6")


class Chalked(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(direction = COLUMN)

        table = toga.DetailedList(
            data = [{
                "icon": None,
                "title": testEntry.getDate(),
                "subtitle": f"{testEntry.getType()}, {testEntry.getGrade()}, {testEntry.getAttempts()}"
            }]
        )

        main_box.add(table)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Chalked()
