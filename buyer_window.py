# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sourse\buyer_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 382)
        self.Button_close = QtWidgets.QPushButton(Dialog)
        self.Button_close.setGeometry(QtCore.QRect(440, 340, 93, 28))
        self.Button_close.setObjectName("Button_close")
        self.Button_save = QtWidgets.QPushButton(Dialog)
        self.Button_save.setGeometry(QtCore.QRect(340, 340, 93, 28))
        self.Button_save.setObjectName("Button_save")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 250, 201, 31))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_2.addWidget(self.textBrowser_3, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout_2.addWidget(self.textBrowser_4, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Button_close.setText(_translate("Dialog", "Отмена"))
        self.Button_save.setText(_translate("Dialog", "Сохранить"))
        self.pushButton.setText(_translate("Dialog", "Заказы клиента"))
        self.label_2.setText(_translate("Dialog", "Имя"))
        self.label_7.setText(_translate("Dialog", "Адрес"))
        self.label_5.setText(_translate("Dialog", "Телефоны"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())