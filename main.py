import sqlite3
import os, platform, logging

# модули графики
import main_window
import block
from PyQt5 import QtWidgets, uic, QtCore, QtGui

if platform.platform().startswith('Windows'):  # определение куда сохранять логи
    logging_file = './data/SamGTU_tool.log'
else:
    logging_file = '.\\data\\SamGTU_tool.log'



class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    # Переопределяем конструктор класса

    def __init__(self, data_men):
        # Обязательно нужно вызвать метод супер класса
        QtWidgets.QMainWindow.__init__(self)
        self.data_men = data_men
        self.selector_day = datetime.now()
        for day_chek in range(120):  # ищем первый день с занятием
            data = self.data_men.get_data_one_day(
                (datetime.date(datetime.now()) + timedelta(days=day_chek)).strftime("%Y-%m-%d"))
            # print((self.selector_day + timedelta(days=day_chek)).strftime("%Y-%m-%d"))
            if not data == []:
                self.selector_day = datetime.date(datetime.now()) + timedelta(days=day_chek)
                break

        self.setupUi(self)

        # скрываю progressBarы
        self.progressBar_schedule.hide()
        self.progressBar_messeges.hide()
        self.progressBar_news.hide()

        self.pushButton_schedule.clicked.connect(self.updating_schedule_from_site)
        self.pushButton_schedule_left.clicked.connect(self.schedule_left)
        self.pushButton_schedule_right.clicked.connect(self.schedule_right)

        self.updating_schedule()

    def schedule_left(self):
        """Показывает предыдущий день"""
        self.selector_day -= timedelta(days=1)
        self.updating_schedule()

    def schedule_right(self):
        """Показываем следующий день"""
        self.selector_day += timedelta(days=1)
        self.updating_schedule()

    def updating_schedule_from_site(self):
        """обнавление инфы по календарю по инфе с сайта"""
        logging.debug("Начато обновление расписания")

        self.thread = Thread_updating_schedule(self.data_men)  # Создаем поток

        # --- Подключаем сигнал к слоту, слот будет вызываться с параметрами сигнала в нужное время.
        self.thread.threadSignal.connect(self.on_threadSignal_updating_schedule)
        self.thread.threadFinish.connect(self.updating_schedule)

        self.thread.start()  # Стартуем поток
        self.pushButton_schedule.setEnabled(False)
        self.progressBar_schedule.show()

    def on_threadSignal_updating_schedule(self, value):  # функция вывода чисел
        """ Визуализация потоковых данных-WorkThread.  """
        self.progressBar_schedule.setValue(value)

    def updating_schedule(self):
        """ Просто обновляет расписание на главном экране"""

        data = self.data_men.get_data_one_day(self.selector_day.strftime("%Y-%m-%d"))

        self.pushButton_schedule.setEnabled(True)
        # self.progressBar_schedule.hide()
        # self.progressBar_schedule.setValue(0)
        # print(data.values())
        # self.layout_schedule = QtWidgets.QFormLayout()

        self.label_schedule.setText(
            str(self.selector_day.strftime("%Y-%m-%d") + "   " + weekdey[self.selector_day.weekday()]))

        list = []
        self.listWidget.clear()
        for para in data:
            # Form = QtWidgets.QListWidgetItem()
            # Form.setText(para['Дисциплина'])

            item = QtWidgets.QListWidgetItem()  # Создать объект QListWidgetItem
            item.setSizeHint(QtCore.QSize(300, 100))  # Установить размер QListWidgetItem

            self.tab1 = QtWidgets.QWidget()
            ui = block.Ui_Form()
            ui.setupUi(self.tab1)
            ui.label_title.setText(para["Дисциплина"])
            ui.label_description.setText(para["Вид занятия"])
            ui.label_tutor.setText(para["Группы"])
            ui.label_time.setText(para["Время проведения занятия"])

            self.listWidget.addItem(item)  # Добавить элемент
            self.listWidget.setItemWidget(item, self.tab1)  # Установить виджет для элемента
            #
            # ui = block.Ui_Form()
            # ui.setupUi(Form)
            # ui.label_title.setText(para["Дисциплина"])
            # ui.label_description.setText(para["Вид занятия"])
            # ui.label_time.setText(para["Время проведения занятия"])
            # Form.setObjectName(str(para)[0:30:2])

            # self.listWidget.addItem(para['Дисциплина'])
            # list.append(Form)

        # self.scrollArea_schedule.setLayout(self.layout_schedule)




def main():
    pass


if __name__ == '__main__':
    main('PyCharm')
