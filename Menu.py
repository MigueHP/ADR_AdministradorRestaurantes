import sys

from PySide6 import QtWidgets, QtGui
from PySide6.QtGui import QIntValidator

from PySide6.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QLCDNumber, QMessageBox
from decimal import Decimal
from Empleado import Empleado
from empleado_d import EmpleadoDao
from ui_mainwindow import Ui_Dialog
from Proveedor import Proveedor
from proveedor_d import ProveedorDaO
from ing_d import IngredienteDao
from Ingredientes import Ingrediente
from Pedido import Pedido
from pedido_d import PedidoDaO
from Detalle_Pedido import Detalle_Pedido
from pedido_detalle_d import Detalle_PedidoDAO
from ui_ventana import Ui_Ingredientes
from todotable import TodoP
from ui_tab_pedido import Ui_Pedidos
from ui_receta import Ui_receta_ventana
from producto_d import ProductoDAO
from Producto import Producto
from ui_edit_producto import Ui_edit_prod
from producto_detalle_p import Producto_detalleDAO
from editar_receta import Ui_Edit_Receta
from Producto_detalle import Producto_Detalle
from orden import Ui_Orden
from Oden_P import Orden
from orden_D import OrdenDAO
import datetime
from ui_orden_mostrar import Ui_Orden_Mostrar
from Orden_Detalle import Orden_Detalle
from Orden_Detalle_P import Orden_DetalleDAO
from orden_todas import Ui_orden_todas
from Factura import Factura
from factura_d import FacturaDAO
from ui_mostrar_facturas import Ui_facturacion


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tab8 = QtWidgets.QMainWindow()
        self.facm = Ui_facturacion()
        self.facm.setupUi(self.tab8)
        self.factura = FacturaDAO
        self.tab7 = QtWidgets.QMainWindow()
        self.ordmt = Ui_orden_todas()
        self.ordmt.setupUi(self.tab7)
        self.ordenD = Orden_DetalleDAO()
        self.producto_detalle = Producto_detalleDAO
        self.orden = OrdenDAO()
        self.tabp = QtWidgets.QMainWindow()
        self.tab2 = QtWidgets.QMainWindow()
        self.tab3 = QtWidgets.QMainWindow()
        self.tab4 = QtWidgets.QMainWindow()
        self.tab5 = QtWidgets.QMainWindow()
        self.tab6 = QtWidgets.QMainWindow()
        self.ordm = Ui_Orden_Mostrar()
        self.ordm.setupUi(self.tab6)
        self.ord = Ui_Orden()
        self.ord.setupUi(self.tab5)
        self.edrec = Ui_Edit_Receta()
        self.edrec.setupUi(self.tab4)
        self.pe = Ui_edit_prod()
        self.pe.setupUi(self.tab3)
        self.rec = Ui_receta_ventana()
        self.rec.setupUi(self.tab2)
        self.au = Ui_Pedidos()
        self.au.setupUi(self.tabp)
        self.ventana = QtWidgets.QMainWindow()
        self.ou = Ui_Ingredientes()
        self.ou.setupUi(self.ventana)
        self.proveedores = ProveedorDaO()
        self.empleados = EmpleadoDao()
        self.ing = IngredienteDao()
        self.pedidos = PedidoDaO()
        self.detalleP = Detalle_PedidoDAO()
        self.producto = ProductoDAO()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click_add)
        self.ui.mostrar_all_empleados.clicked.connect(self.mostrarEmpleados)
        self.ui.ActualizarEmp.clicked.connect(self.actualizar)
        self.ui.mostrar_edit.clicked.connect(self.mostrarEditEm)
        self.ui.pushbutton_EliminarEm.clicked.connect(self.eliminarEmp)
        self.ui.mostrar_all_prov_3.clicked.connect(self.mostrar_proveedores)
        self.ui.agregar_prov.clicked.connect(self.agregar_proveedores)
        self.ui.actualizar_prov.clicked.connect(self.actualizar_proveedor)
        self.ui.eliminar_prov.clicked.connect(self.eliminar_proveedor)
        self.ui.mostrar_prov.clicked.connect(self.mostrar_1prov)
        self.ui.mostrar_all_Ing_4.clicked.connect(self.mostrar_ingredientes)
        self.ui.add_ing.clicked.connect(self.insertar_ingredientes)
        self.ui.eliminar_ing_edit.clicked.connect(self.eliminar_ing)
        self.ui.mostrar_ing_edit.clicked.connect(self.mostrar_1ing)
        self.ui.actualizar_ing_edit.clicked.connect(self.actualizar_ing)
        self.ou.pushButton.clicked.connect(self.add_detalle_P)
        self.ui.MostrarPedido_button.clicked.connect(self.PEDIDO)
        self.ui.crear_P.clicked.connect(self.add_pedido)
        self.ui.mostralall.clicked.connect(self.m_todo_pedido)
        self.ou.terminar_P.clicked.connect(self.terminar_pedido)
        self.ui.Crear_receta.clicked.connect(self.openR)
        #        self.ui.pushButton_5.clicked.connect(self.Insertar_Productos)
        self.ui.Crear_receta_3.clicked.connect(self.abrireditarP)
        self.pe.pushButton.clicked.connect(self.mostrarProducto)
        self.pe.x.clicked.connect(self.editarProducto)
        self.pe.pushButton_3.clicked.connect(self.eliminarProducto)
        self.ui.pushButton_4.clicked.connect(self.mostrarMenu)
        self.rec.pushButton.clicked.connect(self.add_receta)
        self.edrec.pushButton.clicked.connect(self.mostrar_receta)
        self.ui.Crear_receta_2.clicked.connect(self.openeditrec)
        self.edrec.x.clicked.connect(self.actualizar_rec)
        self.edrec.pushButton_3.clicked.connect(self.eliminar_ing_receta)
        self.edrec.pushButton_4.clicked.connect(self.add_more_ing)
        self.edrec.pushButton_5.clicked.connect(self.mostrarIng)
        self.edrec.pushButton_2.clicked.connect(self.close_edit_rec)
        self.pe.pushButton_4.clicked.connect(self.close_edit_prod)
        self.rec.pushButton_2.clicked.connect(self.close_rec)
        self.ui.pushButton_7.clicked.connect(self.insertar_orden)
        self.ui.pushButton_9.clicked.connect(self.mosO)
        self.ord.pushButton_18.clicked.connect(self.insertar_detalle_orden)
        self.ord.pushButton_19.clicked.connect(self.eliminarorden)
        self.ord.pushButton_21.clicked.connect(self.actualizarorden)
        self.ordm.MostrarPedido_button.clicked.connect(self.mostrarOrden)
        self.ord.pushButton_20.clicked.connect(self.closeOrden)
        self.ordm.mostralall.clicked.connect(self.mostrarTO)
        self.ui.pushButton_11.clicked.connect(self.insertar_factura)
        self.ui.pushButton_5.clicked.connect(self.mf)

        date = datetime.datetime.now()
        fecha = date.strftime('%d/%m/%Y')
        self.ui.label.setText(fecha)
        self.ui.label.setText(fecha)
        ID = self.pedidos.id()
        ID = ID + 1
        self.ui.id_pedido.display(ID)
        self.ui.label_15.setText(fecha)
        id_orden = self.orden.id()
        id_orden = id_orden + 1
        self.ui.id_pedido_2.display(id_orden)
        # TABLA PROVEEDORES EN INGREDIENTES
        datos = self.proveedores.seleccionar_2()
        i = len(datos)
        self.ui.Mostrar_table_prov_3.setColumnCount(2)

        self.ui.Mostrar_table_prov_3.setRowCount(i)
        trow = 0
        for p in datos:
            id_prov = QTableWidgetItem(str(p.id_proveedor))
            nombre_prov = QTableWidgetItem(str(p.nombre_proveedor))

            self.ui.Mostrar_table_prov_3.setItem(trow, 0, id_prov)
            self.ui.Mostrar_table_prov_3.setItem(trow, 1, nombre_prov)

            trow += 1
        # FIN TABLA
        # TABLA PROVEEDORES PEDIDO
        datos = self.proveedores.seleccionar_2()
        i = len(datos)
        self.ui.Mostrar_table_prov_2.setColumnCount(2)

        self.ui.Mostrar_table_prov_2.setRowCount(i)
        trow = 0
        for p in datos:
            id_prov = QTableWidgetItem(str(p.id_proveedor))
            nombre_prov = QTableWidgetItem(str(p.nombre_proveedor))

            self.ui.Mostrar_table_prov_2.setItem(trow, 0, id_prov)
            self.ui.Mostrar_table_prov_2.setItem(trow, 1, nombre_prov)

            trow += 1

        # FIN TABLA

        # validaciones
        # Empleados
        validator = QIntValidator(1000, 1100, self)
        self.ui.lineEdit_IDEMPLEADOEDIT.setValidator(validator)
        self.ui.lineeditCURPempleado.setMaxLength(18)
        self.ui.lineeditRFCempleado.setMaxLength(13)
        self.ui.lineeditTELEmpleado7.setValidator(QIntValidator())
        self.ui.lineeditTELEmpleado7.setMaxLength(10)
        # editarempleados
        self.ui.lineEdit_EDITCURP.setMaxLength(18)
        self.ui.lineEdit_EDITRFC.setMaxLength(13)
        self.ui.lineEdit_EDITTEL.setMaxLength(10)
        self.ui.lineEdit_EDITTEL.setValidator(QIntValidator())
        # Proveedores
        self.ui.telefono_prov.setMaxLength(10)
        self.ui.telefono_prov.setValidator(QIntValidator())
        # editar prove
        self.ui.lineEdit_3.setMaxLength(10)
        self.ui.lineEdit_3.setValidator(QIntValidator())
        self.ui.lineEdit_edit_prov.setMaxLength(4)
        self.ui.lineEdit_edit_prov.setValidator(QIntValidator())
        # Ingredientees
        self.ui.id_prov_ingg.setMaxLength(4)
        self.ui.id_prov_ingg.setValidator(QIntValidator())
        self.ui.cant_ing.setMaxLength(2)
        self.ui.cant_ing.setValidator(QIntValidator())
        # EditarIngredientes
        self.ui.id_ingrediente_edit.setMaxLength(4)
        self.ui.id_ingrediente_edit.setValidator(QIntValidator())
        self.ui.nombre_ingrediente_edit_2.setMaxLength(4)
        self.ui.nombre_ingrediente_edit_2.setValidator(QIntValidator())
        # ORDEN
        self.ui.lineEdit_19.setMaxLength(4)
        self.ui.lineEdit_19.setValidator(QIntValidator())
        self.ui.lineEdit_20.setMaxLength(1)
        self.ui.lineEdit_20.setValidator(QIntValidator())
        self.ord.lineEdit_18.setValidator(QIntValidator())
        self.ord.lineEdit_18.setMaxLength(4)

        # PRODUCTOS
        self.ui.lineEdit_6.setMaxLength(3)
        self.ui.lineEdit_6.setValidator(QIntValidator())
        self.rec.lineEdit_3.setValidator(QIntValidator())
        self.rec.lineEdit_3.setMaxLength(4)
        self.edrec.nombre_producto.setMaxLength(2)
        self.edrec.nombre_producto_2.setMaxLength(4)
        self.edrec.id_producto.setMaxLength(4)
        self.edrec.nombre_producto.setValidator(QIntValidator())
        self.edrec.nombre_producto_2.setValidator(QIntValidator())
        self.edrec.id_producto.setValidator(QIntValidator())
        self.pe.id_producto.setMaxLength(4)
        self.pe.id_producto.setValidator(QIntValidator())
        self.pe.precio_producto.setMaxLength(3)
        self.pe.precio_producto.setValidator(QIntValidator())
        # pedido
        self.ui.id_proveedor.setMaxLength(4)
        self.ui.id_proveedor_2.setMaxLength(4)
        self.ui.id_proveedor_2.setValidator(QIntValidator())
        self.ui.id_proveedor.setValidator(QIntValidator())
        self.ui.ID_pedido_All.setMaxLength(4)
        self.ui.ID_pedido_All.setValidator(QIntValidator())

        # ventana ingredeientess
        self.ou.id_ingP.setMaxLength(4)
        self.ou.id_ingP.setValidator((QIntValidator()))

        # ORDEN
        self.ordm.ID_pedido_All.setMaxLength(4)
        self.ordm.ID_pedido_All.setValidator(QIntValidator())

        # FACTURACION
        self.ui.rfc.setMaxLength(13)
        self.ui.id_orden.setMaxLength(4)
        self.ui.id_orden.setValidator(QIntValidator())
        self.ui.nombre_ingrediente_edit_3.setMaxLength(2)
        self.ui.nombre_ingrediente_edit_3.setValidator(QIntValidator())

        # combobox

    def mf(self):
        self.tab8.show()
        datos = self.factura.seleccionar()
        i = len(datos)
        self.facm.tableWidget.setColumnCount(7)

        self.facm.tableWidget.setRowCount(i)
        trow = 0
        for x in datos:
            id_empleado = QTableWidgetItem(str(x.nombre_factura))
            nombre_empleado = QTableWidgetItem(str(x.rfc_factura))
            rol_empleado = QTableWidgetItem(str(x.regimen_fiscal))
            CURP = QTableWidgetItem(str(x.dire_factura))
            rfc = QTableWidgetItem(str(x.concepto))
            dire = QTableWidgetItem(str(x.id_orden_fac))
            telf = QTableWidgetItem("Consumo")

            self.facm.tableWidget.setItem(trow, 0, id_empleado)
            self.facm.tableWidget.setItem(trow, 1, nombre_empleado)
            self.facm.tableWidget.setItem(trow, 2, rol_empleado)
            self.facm.tableWidget.setItem(trow, 3, CURP)
            self.facm.tableWidget.setItem(trow, 4, rfc)
            self.facm.tableWidget.setItem(trow, 5, dire)
            self.facm.tableWidget.setItem(trow, 6, telf)
            trow += 1

    def Insertar_Productos(self):

        global nom_p
        nom_p = self.ui.nom_producto.text()
        if nom_p == '':
            QMessageBox.warning(self, "ERROR", "Nombre no ingresado")
        else:
            descripcion_producto = self.ui.lineEdit_5.text()
            if descripcion_producto == '':
                QMessageBox.warning(self, "ERROR", "descripcion no ingresada")
            else:
                precio_producto = self.ui.lineEdit_6.text()
                if precio_producto == '':
                    QMessageBox.warning(self, "ERROR", "precio no ingresado")
                else:
                    self.producto.insertar(Producto(None, nom_p, descripcion_producto, precio_producto))
                    QMessageBox.information(self, "Guardado", "Producto Guardado ")

                    self.ui.nom_producto.clear()
                    self.ui.lineEdit_5.clear()
                    self.ui.lineEdit_6.clear()

    def abrireditar(self):
        self.tab2.show()

    def abrireditarP(self):
        self.tab3.show()

    def mostrarProducto(self):

        id_p = self.pe.id_producto.text()
        if id_p == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(id_p)
            if id >= 4000 and id <= 4999:
                try:
                    id_p = str(id_p)
                    select_p = self.producto.buscar(Producto(id_producto=id_p))
                    self.pe.plainTextEdit.insertPlainText("ID Producto: " + str(select_p[0]) + "\n")
                    self.pe.plainTextEdit.insertPlainText("Nombre: " + str(select_p[1]) + "\n")
                    self.pe.plainTextEdit.insertPlainText("Descripcion: " + str(select_p[2]) + "\n")
                    self.pe.plainTextEdit.insertPlainText("Precio: " + str(select_p[3]) + "\n")
                except:
                    QMessageBox.information(self, "ERROR", "Producto no existe")

            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto Producto(4000-4999)")

    def editarProducto(self):

        id_p = self.pe.id_producto.text()
        id_p = str(id_p)
        idXX = self.producto.seleccionar()

        if idXX != None:

            nombreP = self.pe.nombre_producto.text()
            Desc = self.pe.desc_producto.text()
            precio = self.pe.precio_producto.text()

            act = self.producto.actualizar(Producto(id_p, nombreP, Desc, precio, ))
            if act == 1:
                self.pe.nombre_producto.clear()
                self.pe.id_producto.clear()
                self.pe.desc_producto.clear()
                self.pe.precio_producto.clear()
                self.pe.plainTextEdit.clear()

            elif act == 0:
                print("ERROR")

    def eliminarProducto(self):

        id_P = self.pe.id_producto.text()
        id_P = str(id_P)
        self.producto.eliminar(Producto(id_producto=id_P))
        self.pe.id_producto.clear()
        self.pe.plainTextEdit.clear()
        self.pe.desc_producto.clear()
        self.pe.precio_producto.clear()
        self.pe.nombre_producto.clear()

        insertados = True
        if insertados:
            QMessageBox.information(self, "Eliminado", " Producto Eliminado")

    def openR(self):

        global nom_p
        nom_p = self.ui.nom_producto.text()
        if nom_p == '':
            QMessageBox.warning(self, "ERROR", "Nombre no ingresado")
        else:
            descripcion_producto = self.ui.lineEdit_5.text()
            if descripcion_producto == '':
                QMessageBox.warning(self, "ERROR", "Descripcion no ingresada")
            else:
                precio_producto = self.ui.lineEdit_6.text()
                if precio_producto == '':
                    QMessageBox.warning(self, "ERROR", "Precio no ingresado")
                else:
                    self.producto.insertar(Producto(None, nom_p, descripcion_producto, precio_producto))
                    self.tab2.show()
                    prod_id = self.producto.id()
                    self.rec.lcdNumber.display(prod_id)

                    # tabla Ingredientes
                    datos = self.ing.seleccionar()
                    i = len(datos)
                    self.rec.tableWidget_2.setColumnCount(2)

                    self.rec.tableWidget_2.setRowCount(i)
                    trow = 0
                    for p in datos:
                        id_ing = QTableWidgetItem(str(p.id_ingrediente))
                        nombre_ing = QTableWidgetItem(str(p.nombre_ingrediente))

                        self.rec.tableWidget_2.setItem(trow, 0, id_ing)
                        self.rec.tableWidget_2.setItem(trow, 1, nombre_ing)

                        trow += 1

    def add_receta(self):

        prod_id = self.producto.id()
        id_ing = self.rec.lineEdit_3.text()
        if id_ing == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(id_ing)
            if id >= 3000 and id <= 3999:
                rec_cant = self.rec.spinBox.text()
                self.producto_detalle.insertar(Producto_Detalle(None, prod_id, id_ing, rec_cant))

                datos = self.producto_detalle.consulta(Producto_Detalle(id_producto_=prod_id))
                i = len(datos)
                self.rec.tableWidget.setColumnCount(2)
                self.rec.tableWidget.setRowCount(i)
                trow = 0
                for p in datos:
                    id_in = QTableWidgetItem(str(p.id_producto_detalle))
                    cant = QTableWidgetItem(str(p.id_producto_))

                    self.rec.tableWidget.setItem(trow, 0, id_in)
                    self.rec.tableWidget.setItem(trow, 1, cant)

                    trow += 1
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto Ingredientes(3000-3999)")

    def mostrarMenu(self):

        datos = self.producto.seleccionar()
        i = len(datos)
        self.ui.table_menu.setColumnCount(4)

        self.ui.table_menu.setRowCount(i)
        trow = 0
        for p in datos:
            id_prod = QTableWidgetItem(str(p.id_producto))
            nombre_prod = QTableWidgetItem(str(p.nombre_producto))
            desc_p = QTableWidgetItem(str(p.descripcion_producto))
            precio_p = QTableWidgetItem(str(p.precio_producto))

            self.ui.table_menu.setItem(trow, 0, id_prod)
            self.ui.table_menu.setItem(trow, 1, nombre_prod)
            self.ui.table_menu.setItem(trow, 2, desc_p)
            self.ui.table_menu.setItem(trow, 3, precio_p)
            trow += 1

    def openeditrec(self):
        self.tab4.show()

    def mostrar_receta(self):

        prod_id = self.edrec.id_producto.text()
        if prod_id == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(prod_id)
            if 4000 <= id <= 4999:
                datos = self.producto_detalle.seleccionar(Producto_Detalle(id_producto_=prod_id))
                i = len(datos)
                self.edrec.tableWidget.setColumnCount(3)
                self.edrec.tableWidget.setRowCount(i)
                trow = 0
                for p in datos:
                    id_in = QTableWidgetItem(str(p.id_producto_detalle))
                    ing = QTableWidgetItem(str(p.id_ingrediente_receta))
                    cant = QTableWidgetItem(str(p.id_producto_))

                    self.edrec.tableWidget.setItem(trow, 0, id_in)
                    self.edrec.tableWidget.setItem(trow, 1, cant)
                    self.edrec.tableWidget.setItem(trow, 2, ing)

                    trow += 1
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto PRODUCTO(4000-4999)")

    def actualizar_rec(self):
        id_p = self.edrec.nombre_producto.text()
        if id_p == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id_p = str(id_p)
            idXX = self.producto_detalle.seleccionar1()

            if idXX != None:

                cant = self.edrec.spinBox.text()

                act = self.producto_detalle.actualizar(Producto_Detalle(id_p, None, None, cant))
                if act == 1:
                    self.edrec.id_producto.clear()
                    self.edrec.nombre_producto.clear()

    def eliminar_ing_receta(self):

        iding = self.edrec.nombre_producto.text()
        if iding == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            iding = str(iding)
            self.producto_detalle.eliminar(Producto_Detalle(id_producto_detalle=iding))
            insertados = True
            if insertados:
                QMessageBox.information(self, "Eliminado", "ID: " + iding + " Eliminado")

            prod_id = self.edrec.id_producto.text()
            datos = self.producto_detalle.seleccionar(Producto_Detalle(id_producto_=prod_id))
            i = len(datos)
            self.edrec.tableWidget.setColumnCount(3)
            self.edrec.tableWidget.setRowCount(i)
            trow = 0
            for p in datos:
                id_in = QTableWidgetItem(str(p.id_producto_detalle))
                ing = QTableWidgetItem(str(p.id_ingrediente_receta))
                cant = QTableWidgetItem(str(p.id_producto_))

                self.edrec.tableWidget.setItem(trow, 0, id_in)
                self.edrec.tableWidget.setItem(trow, 1, cant)
                self.edrec.tableWidget.setItem(trow, 2, ing)

                trow += 1

    def add_more_ing(self):

        prod_id = self.edrec.id_producto.text()
        id_ing = self.edrec.nombre_producto_2.text()
        if id_ing == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(id_ing)
            if id >= 3000 and id <= 3999:
                rec_cant = self.edrec.spinBox_2.text()
                self.producto_detalle.insertar(Producto_Detalle(None, prod_id, id_ing, rec_cant))

                self.edrec.nombre_producto_2.clear()
                self.edrec.spinBox_2.clear()

                prod_id = self.edrec.id_producto.text()
                datos = self.producto_detalle.seleccionar(Producto_Detalle(id_producto_=prod_id))
                i = len(datos)
                self.edrec.tableWidget.setColumnCount(3)
                self.edrec.tableWidget.setRowCount(i)
                trow = 0
                for p in datos:
                    id_in = QTableWidgetItem(str(p.id_producto_detalle))
                    ing = QTableWidgetItem(str(p.id_ingrediente_receta))
                    cant = QTableWidgetItem(str(p.id_producto_))

                    self.edrec.tableWidget.setItem(trow, 0, id_in)
                    self.edrec.tableWidget.setItem(trow, 1, cant)
                    self.edrec.tableWidget.setItem(trow, 2, ing)

                    trow += 1
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto INGREDIENTE(3000-3999)")

    def mostrarIng(self):
        datos = self.ing.seleccionar()
        i = len(datos)
        self.edrec.tableWidget_2.setColumnCount(2)

        self.edrec.tableWidget_2.setRowCount(i)
        trow = 0
        for p in datos:
            id_ing = QTableWidgetItem(str(p.id_ingrediente))
            nombre_ing = QTableWidgetItem(str(p.nombre_ingrediente))

            self.edrec.tableWidget_2.setItem(trow, 0, id_ing)
            self.edrec.tableWidget_2.setItem(trow, 1, nombre_ing)

            trow += 1

    def close_edit_prod(self):
        self.tab3.close()

    def close_edit_rec(self):
        self.tab4.close()

    def close_rec(self):
        self.tab2.close()

    # Funciones Empleados

    def mostrarEmpleados(self):
        datos = self.empleados.seleccionar()
        i = len(datos)
        self.ui.tableEmpleado.setColumnCount(6)

        self.ui.tableEmpleado.setRowCount(i)
        trow = 0
        for p in datos:
            id_empleado = QTableWidgetItem(str(p.id_empleado))
            nombre_empleado = QTableWidgetItem(str(p.nombre_empleado))
            rol_empleado = QTableWidgetItem(str(p.rol_empleado))
            CURP = QTableWidgetItem(str(p.curp_empleado))
            rfc = QTableWidgetItem(str(p.rfc_empleado))
            dire = QTableWidgetItem(str(p.domicilio_empleado))
            telf = QTableWidgetItem(str(p.telefono_empleado))

            self.ui.tableEmpleado.setItem(trow, 0, id_empleado)
            self.ui.tableEmpleado.setItem(trow, 1, nombre_empleado)
            self.ui.tableEmpleado.setItem(trow, 2, rol_empleado)
            self.ui.tableEmpleado.setItem(trow, 3, CURP)
            self.ui.tableEmpleado.setItem(trow, 4, rfc)
            self.ui.tableEmpleado.setItem(trow, 5, dire)
            self.ui.tableEmpleado.setItem(trow, 6, telf)
            trow += 1

    def click_add(self):
        id_empleado = None
        nombre_empleado = self.ui.lineeditNombreempleado.text()
        if nombre_empleado == '':
            QMessageBox.warning(self, "ERROR", "Nombre no ingresado")
        else:
            rol_empleado = self.ui.lineeditRollempleado.text()
            if rol_empleado == '':
                QMessageBox.warning(self, "ERROR", "Rol no ingresado")
            else:
                mayus = self.ui.lineeditCURPempleado.text()
                if mayus == '':
                    QMessageBox.warning(self, "ERROR", "CURP no ingresada")
                else:
                    curp_empleado = mayus.upper()
                    curp_empleado.upper()
                    rfcm = self.ui.lineeditRFCempleado.text()
                    if rfcm == '':
                        QMessageBox.warning(self, "Error", "RFC no ingresado")
                    else:
                        rfc_empleado = rfcm.upper()
                        rfc_empleado.upper()
                        domicilio_empleado = self.ui.lineeditDireccionempleado.text()
                        if domicilio_empleado == '':
                            QMessageBox.warning(self, "ERROR", "Domicilio no ingresado")
                        else:
                            telefono_empleado = self.ui.lineeditTELEmpleado7.text()
                            if telefono_empleado == '':
                                QMessageBox.warning(self, "ERROR", "Telefono no ingresado")
                            else:
                                self.empleados.insertar(
                                    Empleado(id_empleado, nombre_empleado, rol_empleado, curp_empleado, rfc_empleado,
                                             domicilio_empleado,
                                             telefono_empleado))
                            insertados = True
                            if insertados:
                                QMessageBox.information(self, "Guardado", " Guardado")
                                self.clearUI()
                            elif not insertados:
                                QMessageBox.warning(self, "Error", "Datos incorrectos")

    def clearUI(self):

        self.ui.lineeditNombreempleado.clear()
        self.ui.lineeditRollempleado.clear()
        self.ui.lineeditCURPempleado.clear()
        self.ui.lineeditRFCempleado.clear()
        self.ui.lineeditDireccionempleado.clear()
        self.ui.lineeditTELEmpleado7.clear()

    def actualizar(self):

        id_employable = self.ui.lineEdit_IDEMPLEADOEDIT.text()
        if id_employable == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(id_employable)
            if id >= 1000 and id <= 1999:
                id_employable = str(id_employable)
                idXX = self.empleados.seleccionar()

                if idXX != None:

                    nombreA = self.ui.lineEdit_EDITEMPLEADO.text()
                    rollA = self.ui.lineEdit_EDITROLL.text()
                    cM = self.ui.lineEdit_EDITCURP.text()
                    curpA = cM.upper()
                    RFCM = self.ui.lineEdit_EDITRFC.text()
                    rfcA = RFCM.upper()
                    domicilioA = self.ui.lineEdit_EDITDOMIC.text()
                    telA = self.ui.lineEdit_EDITTEL.text()

                    act = self.empleados.actualizar(
                        Empleado(id_employable, nombreA, rollA, curpA, rfcA, domicilioA, telA))
                    if act == 1:
                        self.ui.lineEdit_EDITEMPLEADO.clear()
                        self.ui.lineEdit_EDITROLL.clear()
                        self.ui.lineEdit_EDITCURP.clear()
                        self.ui.lineEdit_EDITRFC.clear()
                        self.ui.lineEdit_EDITDOMIC.clear()
                        self.ui.lineEdit_EDITTEL.clear()
                        self.ui.lineEdit_EDITEMPLEADO.clear()
                        self.ui.plainTextEdit.clear()
                    elif act == 0:
                        print("ERROR")
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto EMPLEADOS(1000-1999)")

    def mostrarEditEm(self):
        self.ui.plainTextEdit.clear()
        idempleado = self.ui.lineEdit_IDEMPLEADOEDIT.text()
        if idempleado == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(idempleado)
            if id >= 1000 and id <= 1999:
                try:
                    idempleado = str(idempleado)
                    selec_empleado = self.empleados.buscar(Empleado(id_empleado=idempleado))
                    print(selec_empleado)

                    self.ui.plainTextEdit.insertPlainText("Codigo: " + str(selec_empleado[0]) + "\n")
                    self.ui.plainTextEdit.insertPlainText("Nombre: " + str(selec_empleado[1]) + "\n")
                    self.ui.plainTextEdit.insertPlainText("Roll: " + str(selec_empleado[2]) + "\n")
                    self.ui.plainTextEdit.insertPlainText("CURP: " + str(selec_empleado[3]) + "\n")
                    self.ui.plainTextEdit.insertPlainText("RFC: " + str(selec_empleado[4]) + "\n")
                    self.ui.plainTextEdit.insertPlainText("Direccion: " + str(selec_empleado[5]) + "\n")
                    self.ui.plainTextEdit.insertPlainText("Telefono: " + str(selec_empleado[6]) + "\n")
                except:
                    QMessageBox.information(self, "ERROR", "Empleado no existe")
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto EMPLEADOS(1000-1999)")

    def eliminarEmp(self):
        self.ui.plainTextEdit.clear()
        idempleado = self.ui.lineEdit_IDEMPLEADOEDIT.text()
        if idempleado == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(idempleado)
            if id >= 1000 and id <= 1999:
                idempleado = str(idempleado)
                personas_eliminadas = self.empleados.eliminar(Empleado(id_empleado=idempleado))
                log.debug(F'Personas eliminadas : {personas_eliminadas}')
                self.ui.plainTextEdit.insertPlainText("Empleado Eliminado")

                insertados = True
                if insertados:
                    QMessageBox.information(self, "Eliminado", "ID: " + idempleado + " Eliminado")
                    self.clearUI()
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto EMPLEADOS(1000-1999)")

    # Terminan funciones de empleados

    # ***-----------------------------INICIO DE METODOS DE PROVEEDOR-------------------------***

    def mostrar_proveedores(self):

        datos = self.proveedores.seleccionar()
        i = len(datos)
        self.ui.Mostrar_table_prov.setColumnCount(3)

        self.ui.Mostrar_table_prov.setRowCount(i)
        trow = 0
        for p in datos:
            id_prov = QTableWidgetItem(str(p.id_proveedor))
            nombre_prov = QTableWidgetItem(str(p.nombre_proveedor))
            tel_prov = QTableWidgetItem(str(p.telefono_proveedor))
            dire_prov = QTableWidgetItem(str(p.dire_proveedor))

            self.ui.Mostrar_table_prov.setItem(trow, 0, id_prov)
            self.ui.Mostrar_table_prov.setItem(trow, 1, nombre_prov)
            self.ui.Mostrar_table_prov.setItem(trow, 2, tel_prov)
            self.ui.Mostrar_table_prov.setItem(trow, 3, dire_prov)
            trow += 1

    def agregar_proveedores(self):

        id_proveedor = None
        nombre_proveedor = self.ui.nombre_prov.text()
        if nombre_proveedor == '':
            QMessageBox.warning(self, "ERROR", "nombre no ingresado")
        else:
            tel_prov = self.ui.telefono_prov.text()
            if tel_prov == '':
                QMessageBox.warning(self, "ERROR", "Telefono no ingresado")
            else:
                dir_prov = self.ui.dire_prov.text()
                if dir_prov == '':
                    QMessageBox.warning(self, "ERROR", "Direccion no ingresada")
                else:
                    self.proveedores.insertar(Proveedor(id_proveedor, nombre_proveedor, tel_prov, dir_prov))
                    insertados = True
                    if insertados:
                        QMessageBox.information(self, "Guardado", " Guardado")
                        self.clearUI()

                    self.ui.id_prov.clear()
                    self.ui.nombre_prov.clear()
                    self.ui.telefono_prov.clear()
                    self.ui.dire_prov.clear()

    def actualizar_proveedor(self):

        id_prov = self.ui.lineEdit_edit_prov.text()
        if id_prov == '':
            QMessageBox.warning(self, "ERROR", "ID No ingresado")
        else:
            id = int(id_prov)
            if id >= 2000 and id <= 2999:
                id_prov = str(id_prov)
                idXX = self.proveedores.seleccionar()

                if idXX != None:

                    nombreP = self.ui.lineEdit_2.text()
                    telP = self.ui.lineEdit_3.text()
                    dirP = self.ui.lineEdit_4.text()

                    act = self.proveedores.actualizar(Proveedor(id_prov, nombreP, telP, dirP))
                    if act == 1:
                        self.ui.lineEdit_2.clear()
                        self.ui.lineEdit_3.clear()
                        self.ui.lineEdit_4.clear()
                        self.ui.plainTextEdit_2.clear()
                else:
                    QMessageBox.Information(self, "Error", "ID invalido, PROVEEDOR(2000-2999")

    def eliminar_proveedor(self):

        self.ui.plainTextEdit_2.clear()
        idprov = self.ui.lineEdit_edit_prov.text()
        if idprov == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(idprov)
            if id >= 2000 and id <= 2999:
                idprov = str(idprov)
                personas_eliminadas = self.proveedores.eliminar(Proveedor(id_proveedor=idprov))
                log.debug(F'Personas eliminadas : {personas_eliminadas}')
                self.ui.plainTextEdit.insertPlainText("Proveedor Eliminado")
                insertados = True
                if insertados:
                    self.ui.plainTextEdit_2.clear()
                    QMessageBox.information(self, "Eliminado", "ID: " + idprov + " Eliminado")
                    self.clearUI()
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto PROVEEDORES(2000-2999)")

    def mostrar_1prov(self):
        self.ui.plainTextEdit_2.clear()
        idprov = self.ui.lineEdit_edit_prov.text()
        if idprov == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(idprov)
            if id >= 2000 and id <= 2999:
                try:
                    idprov = str(idprov)
                    selec_prov = self.proveedores.buscar(Proveedor(id_proveedor=idprov))
                    print(selec_prov)

                    self.ui.plainTextEdit_2.insertPlainText("Codigo: " + str(selec_prov[0]) + "\n")
                    self.ui.plainTextEdit_2.insertPlainText("Nombre: " + str(selec_prov[1]) + "\n")
                    self.ui.plainTextEdit_2.insertPlainText("Telefono: " + str(selec_prov[2]) + "\n")
                    self.ui.plainTextEdit_2.insertPlainText("Direccion: " + str(selec_prov[3]) + "\n")
                except:
                    QMessageBox.information(self, "ERROR", "Proveedor no existe")
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto PROVEEDORES(2000-2999)")

    # ***-----------------------------FIN METODOS DE PROVEEDOR-------------------------***

    # ***-----------------------------INICIO DE METODOS INGREDIENTES-------------------------***

    def mostrar_ingredientes(self):

        datos = self.ing.seleccionar()
        i = len(datos)
        self.ui.tabl_Ing.setColumnCount(4)

        self.ui.tabl_Ing.setRowCount(i)
        trow = 0
        for p in datos:
            id_ing = QTableWidgetItem(str(p.id_ingrediente))
            nombre_ing = QTableWidgetItem(str(p.nombre_ingrediente))
            idp = QTableWidgetItem(str(p.id_prov))
            cant = QTableWidgetItem(str(p.cantidad))

            self.ui.tabl_Ing.setItem(trow, 0, id_ing)
            self.ui.tabl_Ing.setItem(trow, 1, nombre_ing)
            self.ui.tabl_Ing.setItem(trow, 2, idp)
            self.ui.tabl_Ing.setItem(trow, 3, cant)
            trow += 1

    def insertar_ingredientes(self):

        id_ing = None
        nombre_ing = self.ui.nombre_ing.text()
        if nombre_ing == '':
            QMessageBox.warning(self, "ERROR", "Nombre no ingresado")
        else:
            idpr = self.ui.id_prov_ingg.text()
            if idpr == '':
                QMessageBox.warning(self, "ERROR", "ID proveedor no ingresado")
            else:
                id = int(idpr)
                if id >= 2000 and id <= 2999:
                    cant = self.ui.cant_ing.text()

                    self.ing.insertar(Ingrediente(id_ing, nombre_ing, idpr, cant))
                    insertados = True
                    if insertados:
                        QMessageBox.information(self, "Guardado", " Guardado")
                        self.clearUI()

                    self.ui.nombre_ing.clear()
                    self.ui.id_prov_ingg.clear()
                    self.ui.cant_ing.clear()
                else:
                    QMessageBox.information(self, "ERROR", "ID incorrecto PROVEEDORES(2000-2999)")

    def eliminar_ing(self):

        self.ui.edit_text_ing.clear()
        iding = self.ui.id_ingrediente_edit.text()
        if iding == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(iding)
            if id >= 3000 and id <= 3999:
                iding = str(iding)
                ing_eliminados = self.ing.eliminar(Ingrediente(id_ingrediente=iding))
                log.debug(F'Personas eliminadas : {ing_eliminados}')
                self.ui.id_ingrediente_edit.insertPlainText("Ingrediente Eliminado")
                insertados = True
                if insertados:
                    QMessageBox.information(self, "Eliminado", "ID: " + iding + " Eliminado")
                    self.clearUI()
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto Ingredientes(3000-3999)")

    def mostrar_1ing(self):

        self.ui.edit_text_ing.clear()
        iding = self.ui.id_ingrediente_edit.text()
        if iding == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(iding)
            if id >= 3000 and id <= 3999:
                try:
                    iding = str(iding)
                    selec_ing = self.ing.buscar(Ingrediente(id_ingrediente=iding))

                    self.ui.edit_text_ing.insertPlainText("Nombre: " + str(selec_ing[1]) + "\n")
                    self.ui.edit_text_ing.insertPlainText("ID Proveedor: " + str(selec_ing[2]) + "\n")
                    self.ui.edit_text_ing.insertPlainText("Cantidad: " + str(selec_ing[3]) + "\n")
                except:
                    QMessageBox.information(self, "ERROR", "Ingrediente no existe")
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto INGREDIENTES(3000-3999)")

    def actualizar_ing(self):

        id_prov = self.ui.id_ingrediente_edit.text()
        if id_prov == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(id_prov)
            if id >= 3000 and id <= 3999:
                id_prov = str(id_prov)
                idXX = self.ing.seleccionar()

                if idXX != None:

                    nombreI = self.ui.nombre_ingrediente_edit.text()
                    IDprov = self.ui.nombre_ingrediente_edit_2.text()
                    id = int(IDprov)
                    if id >= 2000 and id <= 2999:
                        cantI = self.ui.nombre_ingrediente_edit_3.text()

                        act = self.ing.actualizar(Ingrediente(id_prov, nombreI, IDprov, cantI))
                        if act == 1:
                            self.ui.nombre_ingrediente_edit.clear()
                            self.ui.nombre_ingrediente_edit_2.clear()
                            self.ui.nombre_ingrediente_edit_3.clear()
                            self.ui.edit_text_ing.clear()
                        elif act == 0:
                            print("ERROR")
                    else:
                        QMessageBox.information(self, "ERROR", "ID incorrecto PROVEEDORES(2000-2999)")
                else:
                    QMessageBox.information(self, "ERROR", "ID incorrecto PROVEEDORES(2000-2999)")

    # ***-----------------------------FIN METODOS DE INGREDIENTES-------------------------***
    # ***----------------------------- METODOS DE PEDIDOS-------------------------***

    def add_pedido(self):

        global id_P

        date = datetime.datetime.now()
        fecha = date.strftime('%d/%m/%Y %H:%M:%S')
        idprov = self.ui.id_proveedor.text()
        if idprov == '':
            QMessageBox.warning(self, "ERROR", "ID proveedor no ingresado")
        else:
            idemp = self.ui.id_proveedor_2.text()
            if idemp == '':
                QMessageBox.warning(self, "ERROR", "ID empleado no ingresado")
            else:
                id1 = int(idprov)
                id = int(idemp)
                if 2000 <= id1 <= 2999 and id >= 1000 and id <= 1999:
                    try:
                        self.pedidos.insertar(Pedido(None, fecha, idprov, idemp))

                        id_P = self.pedidos.id()
                        self.ou.lcdNumber.display(id_P)
                        self.ui.id_proveedor.clear()
                        self.ui.id_proveedor_2.clear()
                        self.ventana.show()
                        l = idprov
                        datos = self.ing.filtro(Ingrediente(id_prov=l))
                        i = len(datos)
                        self.ou.detalle_Ingre.setColumnCount(2)

                        self.ou.detalle_Ingre.setRowCount(i)
                        trow = 0
                        for p in datos:
                            id_ingrediente1 = QTableWidgetItem(str(p.id_ingrediente))
                            NI = QTableWidgetItem(str(p.nombre_ingrediente))

                            self.ou.detalle_Ingre.setItem(trow, 0, id_ingrediente1)
                            self.ou.detalle_Ingre.setItem(trow, 1, NI)
                            trow += 1
                    except:
                        QMessageBox.information(self, "ERROR", "Empleado o Proveedor no existe")
                else:
                    QMessageBox.information(self, "ERROR", "ID incorrecto Empleado(1000-1999) o Proveedor(2000-2999)")

    def act_pedido(self):
        id_ped = self.ui.lineEdit.text()
        id_ped = str(id_ped)
        idXX = self.pedidos.seleccionar()

        if idXX != None:

            fechap = self.ui.dateEdit.text()
            IDprovp = self.ui.lineEdit_6.text()
            IDempl = self.ui.lineEdit_10.text()

            act = self.pedidos.actualizar(Pedido(id_ped, fechap, IDprovp, IDempl))
            if act == 1:
                self.ui.nombre_ingrediente_edit.clear()
                self.ui.nombre_ingrediente_edit_2.clear()
                self.ui.nombre_ingrediente_edit_3.clear()

            elif act == 0:
                print("ERROR")

    def elim_ped(self):

        self.ui.textBrowser.clear()
        id_ped = self.ui.lineEdit.text()
        id_ped = str(id_ped)
        ped_eliminados = self.pedidos.eliminar(Pedido(id_pedido_stock=id_ped))
        log.debug(F'Personas eliminadas : {ped_eliminados}')
        self.ui.textBrowser.insertPlainText("Pedido Eliminado")

    def m_todo_pedido(self):
        self.tabp.show()

        datos = self.pedidos.seleccionar()
        i = len(datos)
        self.au.tableWidget1.setColumnCount(4)

        self.au.tableWidget1.setRowCount(i)
        trow = 0
        for p in datos:
            id_p = QTableWidgetItem(str(p.id_pedido_stock))
            fecha_p = QTableWidgetItem(str(p.fecha))
            idp_ = QTableWidgetItem(str(p.id_proveedor_))
            cant_ = QTableWidgetItem(str(p.id_empleado_))

            self.au.tableWidget1.setItem(trow, 0, id_p)
            self.au.tableWidget1.setItem(trow, 1, fecha_p)
            self.au.tableWidget1.setItem(trow, 2, idp_)
            self.au.tableWidget1.setItem(trow, 3, cant_)
            trow += 1

    # ***-----------------------------FIN METODOS DE PEDIDO-------------------------***
    # ***-----------------------------METODOS DE DETALLE PEDIDO-------------------------***
    def add_detalle_P(self):

        id_P = self.pedidos.id()
        id_Ing = self.ou.id_ingP.text()
        if id_Ing == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(id_Ing)
            if id >= 3000 and id <= 3999:
                cantidad_I = self.ou.cant_ing_2.text()
                self.detalleP.insertar(Detalle_Pedido(id_P, id_Ing, cantidad_I, ))

                self.ou.id_ingP.clear()
                self.ou.cant_ing_2.clear()

                l = id_P
                datos = self.detalleP.filtro(Detalle_Pedido(id_PStock=l))
                i = len(datos)
                self.ou.Detalle_Pedido.setColumnCount(2)

                self.ou.Detalle_Pedido.setRowCount(i)
                trow = 0
                for p in datos:
                    inggrediente = QTableWidgetItem(str(p.id_PStock))
                    c = QTableWidgetItem(str(p.id_INGD))

                    self.ou.Detalle_Pedido.setItem(trow, 0, inggrediente)
                    self.ou.Detalle_Pedido.setItem(trow, 1, c)
                    trow += 1
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto INGREDIENTE(3000-3999)")

    def act_pedidoD(self):
        idDet = self.ui.lineEdit_22.text()
        idDet = str(idDet)
        idXX = self.detalleP.seleccionar()

        if idXX != None:

            id_pr = self.ui.lineEdit_24.text()
            idIngre = self.ui.lineEdit_23.text()
            canti = self.ui.spinBox_3.text()

            act = self.detalleP.actualizar(Detalle_Pedido(id_pr, idIngre, canti))
            if act == 1:
                self.ui.lineEdit_24.clear()
                self.ui.lineEdit_23.clear()
                self.ui.spinBox_3.clear()

            elif act == 0:
                print("ERROR")

    def elim_ped_d(self):

        self.ui.textBrowser_4.clear()
        id_dp = self.ui.lineEdit_22.text()
        id_dp = str(id_dp)
        ped_d_eliminados = self.detalleP.eliminar(Detalle_Pedido(id_INGD=id_dp))
        log.debug(F'Personas eliminadas : {ped_d_eliminados}')
        self.ui.textBrowser_4.insertPlainText("Pedido Eliminado")

    def mostrar_p_d(self):

        self.ui.textBrowser_4.clear()
        id_de = self.ui.lineEdit_22.text()
        id_de = str(id_de)
        selec_de = self.detalleP.buscar(Detalle_Pedido(id_INGD=id_de))

        self.ui.textBrowser_4.insertPlainText("Codigo detalle pedido: " + str(selec_de[0]) + "\n")
        self.ui.textBrowser_4.insertPlainText("Codigo pedido: " + str(selec_de[1]) + "\n")
        self.ui.textBrowser_4.insertPlainText("ID Ingrediente: " + str(selec_de[2]) + "\n")
        self.ui.textBrowser_4.insertPlainText("Cantidad: " + str(selec_de[3]) + "\n")

    def PEDIDO(self):
        l = self.ui.ID_pedido_All.text()
        if l == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(l)
            if id >= 7000 and id <= 7999:
                try:
                    d = self.pedidos.completo(TodoP(ID=l))
                    i = len(d)
                    self.ui.tab_Pedido.setColumnCount(5)

                    self.ui.tab_Pedido.setRowCount(i)
                    trow = 0
                    for x in d:
                        fecha = QTableWidgetItem(str(x.fecha_pedidoP))
                        n_pr = QTableWidgetItem(str(x.nombre_proveedorP))
                        n_em = QTableWidgetItem(str(x.nombre_empleadoP))
                        n_ing = QTableWidgetItem(str(x.nombre_ingredienteP))
                        n_ca = QTableWidgetItem(str(x.cantidadP))

                        self.ui.tab_Pedido.setItem(trow, 0, fecha)
                        self.ui.tab_Pedido.setItem(trow, 1, n_pr)
                        self.ui.tab_Pedido.setItem(trow, 2, n_em)
                        self.ui.tab_Pedido.setItem(trow, 3, n_ing)
                        self.ui.tab_Pedido.setItem(trow, 4, n_ca)

                        trow += 1
                except:
                    QMessageBox.information(self, "ERROR", "ID PEDIDOS no existe")
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto PEDIDOS(7000-7999)")

    def terminar_pedido(self):

        encontrado = True
        if encontrado:
            QMessageBox.information(self, "Pedido guardado", "Pedido Guardado")
            self.ventana.close()
            ID = self.pedidos.id()
            ID = ID + 1
            self.ui.id_pedido.display(ID)

    # ORDEN

    def insertar_orden(self):

        date = datetime.datetime.now()
        fecha_orden = date.strftime('%d/%m/%Y %H:%M:%S')
        idempleado = self.ui.lineEdit_19.text()
        num_mesa = self.ui.lineEdit_20.text()
        if idempleado == '' or num_mesa == '':
            QMessageBox.warning(self, "ERROR", "Datos no ingresados")
        else:
            id = int(idempleado)
            if id >= 1000 and id <= 1999:
                try:

                    self.orden.insertar(Orden(None, fecha_orden, idempleado, num_mesa))

                    ID_O = self.orden.id()
                    self.ord.lcdNumber_7.display(ID_O)
                    self.ord.label_3.setText(fecha_orden)
                    self.ui.lineEdit_19.clear()
                    self.ui.lineEdit_20.clear()
                    self.tab5.show()
                except:
                    QMessageBox.information(self, "ERROR", "ERROR Empleado no existe")
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto EMPLEADOS(1000-1999)")

    def mosO(self):
        self.tab6.show()

    def insertar_detalle_orden(self):
        id_orden = self.orden.id()
        id_producto = self.ord.lineEdit_18.text()
        if id_producto == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(id_producto)
            if id >= 4000 and id <= 4999:
                cantidad = self.ord.spinBox_2.text()
                precio1 = self.producto.precio(Producto(id_producto=id_producto))
                precio_Act = int(precio1) * int(cantidad)
                self.ordenD.insertar(Orden_Detalle(None, id_orden, id_producto, cantidad, precio_Act))

                TOTAL = self.ordenD.suma(Orden_Detalle(id_orden_=id_orden))
                print(TOTAL)
                myfloat = Decimal('1.16')
                myfloat2 = Decimal('0.16')
                SUBTOTAL = TOTAL / myfloat
                round(SUBTOTAL, 3)

                IVA = SUBTOTAL * myfloat2
                round(IVA, 3)

                subtotal = round(SUBTOTAL, 2)
                total = round(TOTAL, 2)
                iva = round(IVA, 2)

                subtotal = str(subtotal)
                total = str(total)
                iva = str(iva)
                self.ord.subtotallabel.setText(subtotal)
                self.ord.subtotallabel_2.setText(iva)
                self.ord.subtotallabel_3.setText(total)

                datos = self.ordenD.completo(Orden_Detalle(id_orden_=id_orden))
                i = len(datos)
                self.ord.tableWidget_3.setColumnCount(4)

                self.ord.tableWidget_3.setRowCount(i)
                trow = 0
                for p in datos:
                    uno = QTableWidgetItem(str(p.id_detalle_orden))
                    dos = QTableWidgetItem(str(p.id_orden_))
                    tres = QTableWidgetItem(str(p.id_prod))
                    cuatro = QTableWidgetItem(str(p.cant_p))

                    self.ord.tableWidget_3.setItem(trow, 0, uno)
                    self.ord.tableWidget_3.setItem(trow, 1, dos)
                    self.ord.tableWidget_3.setItem(trow, 2, tres)
                    self.ord.tableWidget_3.setItem(trow, 3, cuatro)
                    trow += 1
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto PRODUCTOS(4000-4999)")

    def actualizarorden(self):

        id_producto = self.ord.lineEdit_18.text()
        if id_producto == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(id_producto)
            if id >= 4000 and id <= 4999:
                id_producto = str(id_producto)
                id_orden = self.orden.id()
                cantidad = self.ord.spinBox_2.text()
                precio1 = self.producto.precio(Producto(id_producto=id_producto))
                precio_Act = int(precio1) * int(cantidad)
                self.ordenD.actualizar(
                    Orden_Detalle(id_prod=id_producto, cant_p=cantidad, precio_actual=precio_Act, id_orden_=id_orden))
                TOTAL = self.ordenD.suma(Orden_Detalle(id_orden_=id_orden))
                print(TOTAL)
                myfloat = Decimal('1.16')
                myfloat2 = Decimal('0.16')
                SUBTOTAL = TOTAL / myfloat
                round(SUBTOTAL, 3)

                IVA = SUBTOTAL * myfloat2
                round(IVA, 3)

                subtotal = round(SUBTOTAL, 2)
                total = round(TOTAL, 2)
                iva = round(IVA, 2)

                subtotal = str(subtotal)
                total = str(total)
                iva = str(iva)
                self.ord.subtotallabel.setText(subtotal)
                self.ord.subtotallabel_2.setText(iva)
                self.ord.subtotallabel_3.setText(total)

                datos = self.ordenD.completo(Orden_Detalle(id_orden_=id_orden))
                i = len(datos)
                self.ord.tableWidget_3.setColumnCount(4)

                self.ord.tableWidget_3.setRowCount(i)
                trow = 0
                for p in datos:
                    uno = QTableWidgetItem(str(p.id_detalle_orden))
                    dos = QTableWidgetItem(str(p.id_orden_))
                    tres = QTableWidgetItem(str(p.id_prod))
                    cuatro = QTableWidgetItem(str(p.cant_p))

                    self.ord.tableWidget_3.setItem(trow, 0, uno)
                    self.ord.tableWidget_3.setItem(trow, 1, dos)
                    self.ord.tableWidget_3.setItem(trow, 2, tres)
                    self.ord.tableWidget_3.setItem(trow, 3, cuatro)
                    trow += 1
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto PRODUCTOS(4000-4999)")

    def eliminarorden(self):
        id_orden = self.orden.id()
        id_producto = self.ord.lineEdit_18.text()
        if id_producto == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(id_producto)
            if id >= 4000 and id <= 4999:
                id_producto = str(id_producto)
                self.ordenD.eliminar(Orden_Detalle(id_prod=id_producto, id_orden_=id_orden))
                id_orden = self.orden.id()
                TOTAL = self.ordenD.suma(Orden_Detalle(id_orden_=id_orden))
                print(TOTAL)
                myfloat = Decimal('1.16')
                myfloat2 = Decimal('0.16')
                SUBTOTAL = TOTAL / myfloat
                round(SUBTOTAL, 3)

                IVA = SUBTOTAL * myfloat2
                round(IVA, 3)

                subtotal = round(SUBTOTAL, 2)
                total = round(TOTAL, 2)
                iva = round(IVA, 2)

                subtotal = str(subtotal)
                total = str(total)
                iva = str(iva)
                self.ord.subtotallabel.setText(subtotal)
                self.ord.subtotallabel_2.setText(iva)
                self.ord.subtotallabel_3.setText(total)

                datos = self.ordenD.completo(Orden_Detalle(id_orden_=id_orden))
                i = len(datos)
                self.ord.tableWidget_3.setColumnCount(4)

                self.ord.tableWidget_3.setRowCount(i)
                trow = 0
                for p in datos:
                    uno = QTableWidgetItem(str(p.id_detalle_orden))
                    dos = QTableWidgetItem(str(p.id_orden_))
                    tres = QTableWidgetItem(str(p.id_prod))
                    cuatro = QTableWidgetItem(str(p.cant_p))

                    self.ord.tableWidget_3.setItem(trow, 0, uno)
                    self.ord.tableWidget_3.setItem(trow, 1, dos)
                    self.ord.tableWidget_3.setItem(trow, 2, tres)
                    self.ord.tableWidget_3.setItem(trow, 3, cuatro)
                    trow += 1

            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto PRODUCTOS(4000-4999)")

    def closeOrden(self):
        self.tab5.close()

    def mostrarOrden(self):
        id_orden = self.ordm.ID_pedido_All.text()
        if id_orden == '':
            QMessageBox.warning(self, "ERROR", "ID no ingresado")
        else:
            id = int(id_orden)
            if id >= 5000 and id <= 5999:
                datos = self.ordenD.seleccionar(Orden_Detalle(id_orden_=id_orden))
                i = len(datos)
                self.ordm.tab_Pedido.setColumnCount(5)

                self.ordm.tab_Pedido.setRowCount(i)
                self.ordm.tab_Pedido.clear()
                trow = 0
                for p in datos:
                    uno = QTableWidgetItem(str(p.fecha_ordenT))
                    dos = QTableWidgetItem(str(p.nombre_empleadoO))
                    tres = QTableWidgetItem(str(p.num_Mesa))
                    cuatro = QTableWidgetItem(str(p.nombre_productoO))
                    cinco = QTableWidgetItem(str(p.cantidadO))

                    self.ordm.tab_Pedido.setItem(trow, 0, uno)
                    self.ordm.tab_Pedido.setItem(trow, 1, dos)
                    self.ordm.tab_Pedido.setItem(trow, 2, tres)
                    self.ordm.tab_Pedido.setItem(trow, 3, cuatro)
                    self.ordm.tab_Pedido.setItem(trow, 4, cinco)
                    trow += 1
            else:
                QMessageBox.information(self, "ERROR", "ID incorrecto ORDEN(5000-5999)")

    def mostrarTO(self):
        self.tab7.show()
        datos = self.orden.seleccionar()
        i = len(datos)
        self.ordmt.tableWidget.setColumnCount(4)

        self.ordmt.tableWidget.setRowCount(i)
        trow = 0
        for p in datos:
            uno = QTableWidgetItem(str(p.id_orden))
            dos = QTableWidgetItem(str(p.fecha_orden))
            tres = QTableWidgetItem(str(p.id_empleado_orden))
            cuatro = QTableWidgetItem(str(p.num_mesa))

            self.ordmt.tableWidget.setItem(trow, 0, uno)
            self.ordmt.tableWidget.setItem(trow, 1, dos)
            self.ordmt.tableWidget.setItem(trow, 2, tres)
            self.ordmt.tableWidget.setItem(trow, 3, cuatro)
            trow += 1

    def insertar_factura(self):

        nombre_factura = self.ui.nombre.text()
        if nombre_factura == '':
            QMessageBox.warning(self, "ERROR", "Nombre no ingresado")
        else:
            rfc_factura = self.ui.rfc.text()
            if rfc_factura == '':
                QMessageBox.warning(self, "ERROR", "RFC no ingresado")
            else:
                regimen = self.ui.rf.text()
                if regimen == '':
                    QMessageBox.warning(self, "ERROR", "Regimen no ingresado")
                else:
                    dir_fiscal = self.ui.df.text()
                    if dir_fiscal == '':
                        QMessageBox.warning(self, "ERROR", "Direccion no ingresada")
                    else:
                        concepto = self.ui.concepto.text()
                        id_orden = self.ui.id_orden.text()
                        if id_orden == '':
                            QMessageBox.warning(self, "ERROR", "ID no ingresado")
                        else:
                            id = int(id_orden)
                            if id >= 5000 and id <= 5999:
                                self.factura.insertar(
                                    Factura(nombre_factura, rfc_factura, regimen, dir_fiscal, id_orden, concepto))
                                QMessageBox.information(self, "Guardado", " Factura Guardada")
                            else:
                                QMessageBox.information(self, "ERROR", "ID incorrecto ORDEN(5000-5999)")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
