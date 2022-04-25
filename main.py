import sqlite3
import os, platform, logging

# модули графики
import sys

import main_window

from PyQt5 import QtWidgets, uic, QtCore, QtGui

if platform.platform().startswith('Windows'):  # определение куда сохранять логи
    logging_file = './data/SamGTU_tool.log'
else:
    logging_file = '.\\data\\SamGTU_tool.log'




class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    # Переопределяем конструктор класса

    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QtWidgets.QMainWindow.__init__(self)

        self.setupUi(self)


        self.updating_schedule()






def main():


    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())




if __name__ == '__main__':
    main()
