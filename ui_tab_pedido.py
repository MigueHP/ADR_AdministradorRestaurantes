# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_pedido.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Pedidos(object):
    def setupUi(self, Pedidos):
        if not Pedidos.objectName():
            Pedidos.setObjectName(u"Pedidos")
        Pedidos.resize(481, 324)
        self.tableWidget1 = QTableWidget(Pedidos)
        if (self.tableWidget1.columnCount() < 4):
            self.tableWidget1.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget1.setObjectName(u"tableWidget1")
        self.tableWidget1.setGeometry(QRect(15, 60, 451, 231))

        self.retranslateUi(Pedidos)

        QMetaObject.connectSlotsByName(Pedidos)
    # setupUi

    def retranslateUi(self, Pedidos):
        Pedidos.setWindowTitle(QCoreApplication.translate("Pedidos", u"Dialog", None))
        ___qtablewidgetitem = self.tableWidget1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Pedidos", u"ID Pedido", None));
        ___qtablewidgetitem1 = self.tableWidget1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Pedidos", u"Fecha", None));
        ___qtablewidgetitem2 = self.tableWidget1.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Pedidos", u"Proveedor", None));
        ___qtablewidgetitem3 = self.tableWidget1.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Pedidos", u"Empleado", None));
    # retranslateUi

