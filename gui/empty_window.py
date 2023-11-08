# import modules
import sys

from PyQt5.QtWidgets import QApplication, QWidget

class ExampleClass(QWidget): # inherits all of QWidget properties and methods

    def __init__(self): # create default constructor
        super().__init__() # super used to inherit from QWidget class
        self.initializeUI()
    
    def initializeUI(self):
        """Initialize the window and display its contents to the screen."""
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Empty Window in PyQt')
        self.show() # displaying window to screen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExampleClass()
    sys.exit(app.exec())