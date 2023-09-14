# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_producto.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_edit_prod(object):
    def setupUi(self, edit_prod):
        if not edit_prod.objectName():
            edit_prod.setObjectName(u"edit_prod")
        edit_prod.resize(537, 343)
        self.label_3 = QLabel(edit_prod)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 130, 47, 13))
        self.label = QLabel(edit_prod)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 101, 16))
        self.precio_producto = QLineEdit(edit_prod)
        self.precio_producto.setObjectName(u"precio_producto")
        self.precio_producto.setGeometry(QRect(40, 150, 113, 20))
        self.plainTextEdit = QPlainTextEdit(edit_prod)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(240, 60, 251, 121))
        self.x = QPushButton(edit_prod)
        self.x.setObjectName(u"x")
        self.x.setGeometry(QRect(100, 200, 75, 23))
        self.nombre_producto = QLineEdit(edit_prod)
        self.nombre_producto.setObjectName(u"nombre_producto")
        self.nombre_producto.setGeometry(QRect(40, 70, 121, 20))
        self.pushButton_3 = QPushButton(edit_prod)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 240, 75, 23))
        self.desc_producto = QLineEdit(edit_prod)
        self.desc_producto.setObjectName(u"desc_producto")
        self.desc_producto.setGeometry(QRect(40, 110, 113, 20))
        self.label_2 = QLabel(edit_prod)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 90, 71, 16))
        self.id_producto = QLineEdit(edit_prod)
        self.id_producto.setObjectName(u"id_producto")
        self.id_producto.setGeometry(QRect(280, 20, 113, 20))
        self.pushButton = QPushButton(edit_prod)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 200, 75, 23))
        self.label_7 = QLabel(edit_prod)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(200, 20, 91, 16))
        self.pushButton_4 = QPushButton(edit_prod)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(440, 300, 75, 23))

        self.retranslateUi(edit_prod)

        QMetaObject.connectSlotsByName(edit_prod)
    # setupUi

    def retranslateUi(self, edit_prod):
        edit_prod.setWindowTitle(QCoreApplication.translate("edit_prod", u"Editar Producto", None))
        self.label_3.setText(QCoreApplication.translate("edit_prod", u"Precio", None))
        self.label.setText(QCoreApplication.translate("edit_prod", u"Nombre Producto", None))
        self.x.setText(QCoreApplication.translate("edit_prod", u"Actualizar", None))
        self.pushButton_3.setText(QCoreApplication.translate("edit_prod", u"Eliminar", None))
        self.label_2.setText(QCoreApplication.translate("edit_prod", u"Descripcion", None))
        self.pushButton.setText(QCoreApplication.translate("edit_prod", u"Mostrar", None))
        self.label_7.setText(QCoreApplication.translate("edit_prod", u"ID Producto", None))
        self.pushButton_4.setText(QCoreApplication.translate("edit_prod", u"Terminar", None))
    # retranslateUi

