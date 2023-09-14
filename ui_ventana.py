# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana2.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Ingredientes(object):
    def setupUi(self, Ingredientes):
        if not Ingredientes.objectName():
            Ingredientes.setObjectName(u"Ingredientes")
        Ingredientes.resize(559, 354)
        self.id_ingP = QLineEdit(Ingredientes)
        self.id_ingP.setObjectName(u"id_ingP")
        self.id_ingP.setGeometry(QRect(20, 90, 113, 20))
        self.cant_ing_2 = QSpinBox(Ingredientes)
        self.cant_ing_2.setObjectName(u"cant_ing_2")
        self.cant_ing_2.setGeometry(QRect(20, 170, 42, 22))
        self.lcdNumber = QLCDNumber(Ingredientes)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(340, 180, 64, 23))
        self.lcdNumber.setFrameShape(QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QFrame.Plain)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.label_43 = QLabel(Ingredientes)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(20, 50, 81, 16))
        self.label_44 = QLabel(Ingredientes)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(20, 140, 111, 16))
        self.pushButton = QPushButton(Ingredientes)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 230, 91, 31))
        self.terminar_P = QPushButton(Ingredientes)
        self.terminar_P.setObjectName(u"terminar_P")
        self.terminar_P.setGeometry(QRect(10, 270, 101, 31))
        self.detalle_Ingre = QTableWidget(Ingredientes)
        if (self.detalle_Ingre.columnCount() < 2):
            self.detalle_Ingre.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.detalle_Ingre.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.detalle_Ingre.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.detalle_Ingre.setObjectName(u"detalle_Ingre")
        self.detalle_Ingre.setGeometry(QRect(205, 40, 351, 121))
        self.detalle_Ingre.horizontalHeader().setDefaultSectionSize(130)
        self.label = QLabel(Ingredientes)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 71, 16))
        self.label_2 = QLabel(Ingredientes)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 180, 71, 16))
        self.Detalle_Pedido = QTableWidget(Ingredientes)
        if (self.Detalle_Pedido.columnCount() < 2):
            self.Detalle_Pedido.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Detalle_Pedido.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Detalle_Pedido.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.Detalle_Pedido.setObjectName(u"Detalle_Pedido")
        self.Detalle_Pedido.setGeometry(QRect(200, 210, 351, 121))
        self.Detalle_Pedido.horizontalHeader().setDefaultSectionSize(130)

        self.retranslateUi(Ingredientes)

        QMetaObject.connectSlotsByName(Ingredientes)
    # setupUi

    def retranslateUi(self, Ingredientes):
        Ingredientes.setWindowTitle(QCoreApplication.translate("Ingredientes", u"Ingredientes", None))
        self.label_43.setText(QCoreApplication.translate("Ingredientes", u"ID Ingrediente", None))
        self.label_44.setText(QCoreApplication.translate("Ingredientes", u"Cantidad ", None))
        self.pushButton.setText(QCoreApplication.translate("Ingredientes", u"Agregar", None))
        self.terminar_P.setText(QCoreApplication.translate("Ingredientes", u"Terminar Pedido", None))
        ___qtablewidgetitem = self.detalle_Ingre.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Ingredientes", u"ID Ingrediente", None));
        ___qtablewidgetitem1 = self.detalle_Ingre.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Ingredientes", u"Nombre", None));
        self.label.setText(QCoreApplication.translate("Ingredientes", u"Ingredientes", None))
        self.label_2.setText(QCoreApplication.translate("Ingredientes", u"Pedido", None))
        ___qtablewidgetitem2 = self.Detalle_Pedido.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Ingredientes", u"Ingrediente", None));
        ___qtablewidgetitem3 = self.Detalle_Pedido.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Ingredientes", u"Cantidad", None));
    # retranslateUi

