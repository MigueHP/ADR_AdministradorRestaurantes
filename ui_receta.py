# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'receta.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLCDNumber,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QWidget)

class Ui_receta_ventana(object):
    def setupUi(self, receta_ventana):
        if not receta_ventana.objectName():
            receta_ventana.setObjectName(u"receta_ventana")
        receta_ventana.resize(613, 581)
        self.tableWidget = QTableWidget(receta_ventana)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(180, 60, 361, 201))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(175)
        self.lineEdit_3 = QLineEdit(receta_ventana)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 80, 121, 20))
        self.label_2 = QLabel(receta_ventana)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 81, 16))
        self.label_3 = QLabel(receta_ventana)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 51, 16))
        self.pushButton = QPushButton(receta_ventana)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 170, 75, 23))
        self.pushButton_2 = QPushButton(receta_ventana)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 280, 91, 41))
        self.tableWidget_2 = QTableWidget(receta_ventana)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 270, 321, 281))
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)
        self.label_4 = QLabel(receta_ventana)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 240, 81, 16))
        self.spinBox = QSpinBox(receta_ventana)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(10, 140, 42, 22))
        self.lcdNumber = QLCDNumber(receta_ventana)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(200, 20, 91, 31))

        self.retranslateUi(receta_ventana)

        QMetaObject.connectSlotsByName(receta_ventana)
    # setupUi

    def retranslateUi(self, receta_ventana):
        receta_ventana.setWindowTitle(QCoreApplication.translate("receta_ventana", u"Receta", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("receta_ventana", u"Nombre Ingrediente", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("receta_ventana", u"Cantidad", None));
        self.lineEdit_3.setText("")
        self.label_2.setText(QCoreApplication.translate("receta_ventana", u"ID Ingrediente", None))
        self.label_3.setText(QCoreApplication.translate("receta_ventana", u"Cantidad", None))
        self.pushButton.setText(QCoreApplication.translate("receta_ventana", u"Agregar", None))
        self.pushButton_2.setText(QCoreApplication.translate("receta_ventana", u"Terminar Receta", None))
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("receta_ventana", u"ID Ingrediente", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("receta_ventana", u"Nombre", None));
        self.label_4.setText(QCoreApplication.translate("receta_ventana", u"Ingredientes", None))
    # retranslateUi

