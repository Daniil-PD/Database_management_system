
import os, platform, logging

# модули графики
import sys
import main_window
import buyer_window
from PyQt5 import QtWidgets, uic, QtCore, QtGui
# модули графики

# модули базы данных
import DataManager
# модули базы данных


class BuyerWindow():
    '''Класс графики одного покупателя'''
    def __init__(self, dat_manager, buyer_id):
        '''
        :param: dat_manager класс базы данных
        :param: buyer_id id покупателя
        '''
        self.buyer_id = buyer_id


        logging.debug("Запуск экрана данных покупателя")
        self.dat_manager = DataManager.DataManager()

        self.setupUi(self)

    # Переопределяем конструктор класса
def disconnect(signal):
    try:
        signal.disconnect()
    except TypeError:
        pass


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):

    class CurrentView:
        BUYERS = 12323
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QtWidgets.QMainWindow.__init__(self)

        logging.debug("Подключение к базе данных")
        self.dat_manager = DataManager.DataManager()

        self.setupUi(self)

        self.current_view = None
        self.tableWidget_load_buyers()

    def open_buyer_win(self, row, column):
        id_buyers = self.tableWidget.item(row,0).text()
        buyer_win = BuyerWindow(self.dat_manager, id_buyers)
        buyer_win.show()
        buyer_win.setParent(self)




    def tableWidget_load_buyers(self, filters = None):
        '''Загружает в таблицу данные пользователей с фильтром или без него'''

        buyers = self.dat_manager.get_buyers(filters)
        if not self.current_view == MainWindow.CurrentView.BUYERS:
            disconnect(self.tableWidget.cellActivated)
            disconnect(self.lineEdit_filter.textChanged)
            disconnect(self.comboBox_filter.currentIndexChanged)

            self.tableWidget.setColumnCount(5)


            self.tableWidget.setHorizontalHeaderLabels(["id","name","email","address", "phone"])
            self.tableWidget.setColumnWidth(0, 40)
            self.tableWidget.setColumnWidth(1, 200)
            self.tableWidget.setColumnWidth(2, 200)
            self.tableWidget.setColumnWidth(3, 200)
            self.tableWidget.setColumnWidth(4, 140)

            #определение comboBox
            self.comboBox_filter.clear()
            self.comboBox_filter.addItems(("id","name","email","address", "phone"))

            self.tableWidget.cellActivated.connect(self.open_buyer_win)
            self.lineEdit_filter.textChanged.connect(self.filter)
            self.comboBox_filter.currentIndexChanged.connect(self.filter)


        self.current_view = MainWindow.CurrentView.BUYERS

        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(buyers))
        for row, buyer in enumerate(buyers):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(buyer.id)))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(buyer.name))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(buyer.email))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(buyer.address))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(", ".join(buyer.phones)))

    def filter(self):
        text_filter = self.lineEdit_filter.text()
        if text_filter == "":
            self.tableWidget_load_buyers()
        else:
            if self.current_view is MainWindow.CurrentView.BUYERS:
                column = self.comboBox_filter.currentText()
                self.tableWidget_load_buyers((column, text_filter))




def main():

    if platform.platform().startswith('Windows'):  # определение куда сохранять логи

        logging_file = os.path.join(os.getenv('HOMEDRIVE'),os.getenv('HOMEPATH'), 'DMS.log')
    else:
        logging_file = os.path.join(os.getenv('HOME'), 'DMS.log')

    logging.basicConfig(  # настройки для модуля записи логгов
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s : %(message)s',
        filename=logging_file,
        filemode='w',
    )
    logging.debug("старт приложения")

    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec_())




if __name__ == '__main__':
    main()
