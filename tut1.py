
#Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

#The sys module is responsible for processing command line argument
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("My First App")

button = QPushButton()
button.setText("Click Me")

window.setCentralWidget(button)

window.show()

#Start the event loop
app.exec_()
