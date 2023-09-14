# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mostrar_ordenes.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDialog, QFrame,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Orden_Mostrar(object):
    def setupUi(self, Orden_Mostrar):
        if not Orden_Mostrar.objectName():
            Orden_Mostrar.setObjectName(u"Orden_Mostrar")
        Orden_Mostrar.resize(810, 534)
        self.tabWidget = QTabWidget(Orden_Mostrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, -10, 801, 521))
        self.tab_32 = QWidget()
        self.tab_32.setObjectName(u"tab_32")
        self.MostrarPedido_button = QPushButton(self.tab_32)
        self.MostrarPedido_button.setObjectName(u"MostrarPedido_button")
        self.MostrarPedido_button.setGeometry(QRect(200, 380, 101, 31))
        self.label_67 = QLabel(self.tab_32)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(40, 360, 71, 16))
        self.ID_pedido_All = QLineEdit(self.tab_32)
        self.ID_pedido_All.setObjectName(u"ID_pedido_All")
        self.ID_pedido_All.setGeometry(QRect(40, 390, 131, 20))
        self.tab_Pedido = QTableWidget(self.tab_32)
        if (self.tab_Pedido.columnCount() < 5):
            self.tab_Pedido.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_Pedido.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_Pedido.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tab_Pedido.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tab_Pedido.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tab_Pedido.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tab_Pedido.setObjectName(u"tab_Pedido")
        self.tab_Pedido.setGeometry(QRect(20, 20, 751, 321))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_Pedido.sizePolicy().hasHeightForWidth())
        self.tab_Pedido.setSizePolicy(sizePolicy)
        self.tab_Pedido.setFrameShape(QFrame.Box)
        self.tab_Pedido.setFrameShadow(QFrame.Sunken)
        self.tab_Pedido.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tab_Pedido.setGridStyle(Qt.SolidLine)
        self.tab_Pedido.setSortingEnabled(False)
        self.tab_Pedido.setWordWrap(True)
        self.tab_Pedido.setCornerButtonEnabled(True)
        self.tab_Pedido.horizontalHeader().setCascadingSectionResizes(False)
        self.tab_Pedido.horizontalHeader().setDefaultSectionSize(150)
        self.tab_Pedido.horizontalHeader().setProperty("showSortIndicator", True)
        self.tab_Pedido.horizontalHeader().setStretchLastSection(False)
        self.tab_Pedido.verticalHeader().setCascadingSectionResizes(False)
        self.tab_Pedido.verticalHeader().setStretchLastSection(False)
        self.mostralall = QPushButton(self.tab_32)
        self.mostralall.setObjectName(u"mostralall")
        self.mostralall.setGeometry(QRect(330, 380, 101, 31))
        self.tabWidget.addTab(self.tab_32, "")

        self.retranslateUi(Orden_Mostrar)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Orden_Mostrar)
    # setupUi

    def retranslateUi(self, Orden_Mostrar):
        Orden_Mostrar.setWindowTitle(QCoreApplication.translate("Orden_Mostrar", u"Dialog", None))
        self.MostrarPedido_button.setText(QCoreApplication.translate("Orden_Mostrar", u"Mostrar orden", None))
        self.label_67.setText(QCoreApplication.translate("Orden_Mostrar", u"ID Orden", None))
        ___qtablewidgetitem = self.tab_Pedido.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Orden_Mostrar", u"Fecha", None));
        ___qtablewidgetitem1 = self.tab_Pedido.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Orden_Mostrar", u"Empleado", None));
        ___qtablewidgetitem2 = self.tab_Pedido.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Orden_Mostrar", u"Numero de mesa", None));
        ___qtablewidgetitem3 = self.tab_Pedido.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Orden_Mostrar", u"Producto", None));
        ___qtablewidgetitem4 = self.tab_Pedido.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Orden_Mostrar", u"Cantidad", None));
        self.mostralall.setText(QCoreApplication.translate("Orden_Mostrar", u"Mostrar todos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_32), QCoreApplication.translate("Orden_Mostrar", u"Mostrar Orden", None))
    # retranslateUi

