# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar_receta.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Edit_Receta(object):
    def setupUi(self, Edit_Receta):
        if not Edit_Receta.objectName():
            Edit_Receta.setObjectName(u"Edit_Receta")
        Edit_Receta.resize(654, 554)
        self.label = QLabel(Edit_Receta)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 101, 16))
        self.label_2 = QLabel(Edit_Receta)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 71, 16))
        self.pushButton_3 = QPushButton(Edit_Receta)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 220, 75, 23))
        self.label_7 = QLabel(Edit_Receta)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(180, 10, 71, 16))
        self.x = QPushButton(Edit_Receta)
        self.x.setObjectName(u"x")
        self.x.setGeometry(QRect(100, 180, 75, 23))
        self.pushButton = QPushButton(Edit_Receta)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 180, 75, 23))
        self.nombre_producto = QLineEdit(Edit_Receta)
        self.nombre_producto.setObjectName(u"nombre_producto")
        self.nombre_producto.setGeometry(QRect(30, 50, 121, 20))
        self.id_producto = QLineEdit(Edit_Receta)
        self.id_producto.setObjectName(u"id_producto")
        self.id_producto.setGeometry(QRect(250, 10, 113, 20))
        self.tableWidget = QTableWidget(Edit_Receta)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(200, 50, 381, 192))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.spinBox = QSpinBox(Edit_Receta)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(30, 100, 42, 22))
        self.pushButton_4 = QPushButton(Edit_Receta)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 460, 75, 23))
        self.nombre_producto_2 = QLineEdit(Edit_Receta)
        self.nombre_producto_2.setObjectName(u"nombre_producto_2")
        self.nombre_producto_2.setGeometry(QRect(20, 340, 121, 20))
        self.label_4 = QLabel(Edit_Receta)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 370, 71, 16))
        self.label_3 = QLabel(Edit_Receta)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 280, 141, 31))
        self.spinBox_2 = QSpinBox(Edit_Receta)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(20, 390, 42, 22))
        self.label_5 = QLabel(Edit_Receta)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 310, 81, 20))
        self.tableWidget_2 = QTableWidget(Edit_Receta)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(200, 290, 381, 191))
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(125)
        self.label_6 = QLabel(Edit_Receta)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(490, 260, 81, 20))
        self.pushButton_5 = QPushButton(Edit_Receta)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(464, 490, 121, 23))
        self.label_8 = QLabel(Edit_Receta)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(490, 20, 81, 20))
        self.pushButton_2 = QPushButton(Edit_Receta)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 510, 81, 31))

        self.retranslateUi(Edit_Receta)

        QMetaObject.connectSlotsByName(Edit_Receta)
    # setupUi

    def retranslateUi(self, Edit_Receta):
        Edit_Receta.setWindowTitle(QCoreApplication.translate("Edit_Receta", u"Editar Receta", None))
        self.label.setText(QCoreApplication.translate("Edit_Receta", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("Edit_Receta", u"Cantidad", None))
        self.pushButton_3.setText(QCoreApplication.translate("Edit_Receta", u"Eliminar", None))
        self.label_7.setText(QCoreApplication.translate("Edit_Receta", u"ID Producto", None))
        self.x.setText(QCoreApplication.translate("Edit_Receta", u"Actualizar", None))
        self.pushButton.setText(QCoreApplication.translate("Edit_Receta", u"Mostrar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Edit_Receta", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Edit_Receta", u"Ingrediente", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Edit_Receta", u"Cantidad", None));
        self.pushButton_4.setText(QCoreApplication.translate("Edit_Receta", u"Agregar", None))
        self.label_4.setText(QCoreApplication.translate("Edit_Receta", u"Cantidad", None))
        self.label_3.setText(QCoreApplication.translate("Edit_Receta", u"Agregar nuevo Ingrediente", None))
        self.label_5.setText(QCoreApplication.translate("Edit_Receta", u"ID Ingrediente", None))
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Edit_Receta", u"ID Ingrediente", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Edit_Receta", u"Ingrediente", None));
        self.label_6.setText(QCoreApplication.translate("Edit_Receta", u"Ingredientes", None))
        self.pushButton_5.setText(QCoreApplication.translate("Edit_Receta", u"Mostrar Ingredientes", None))
        self.label_8.setText(QCoreApplication.translate("Edit_Receta", u"Receta", None))
        self.pushButton_2.setText(QCoreApplication.translate("Edit_Receta", u"Terminar", None))
    # retranslateUi

