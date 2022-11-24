import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        temp = QLabel("Température")
        unit = QLabel("C°")
        self.__text = QLineEdit("")
        aide = QPushButton("?")
        self.__convaff = QLineEdit("")
        self.__convaff.setFrame(False)
        unitresult = QLabel("K")
        result = QComboBox(self)
        conv = QPushButton("Convertir")
        nom = QLabel("conversion")
        result.addItem("°C -> K")
        result.addItem("K -> °C")
        grid.addWidget(temp, 0, 0)
        grid.addWidget(self.__text, 0, 1)
        grid.addWidget(unit, 0, 2)
        grid.addWidget(conv, 2, 1)
        grid.addWidget(result,2,2)
        grid.addWidget(aide, 4, 3)
        grid.addWidget(nom, 3, 0)
        grid.addWidget(self.__convaff, 3, 1)
        grid.addWidget(unitresult, 3, 2)

        aide.clicked.connect(self.__actionaide)
        conv.clicked.connect(self.__actionconv)
        self.setWindowTitle("Une première fenêtre")
    def __actionaide(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("convertion de K vers °C et inversement")
        msgBox.setWindowTitle("Aide")


        returnValue = msgBox.exec()

    def __actionconv(self):
        chiffre = self.__text.text()
        chiffre = chiffre + 273.15
        self.__convaff.setText(chiffre)
        #if self.__text < -273.15 :
        #   self.__text.setText(f"En-dessous du zero absolue")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()