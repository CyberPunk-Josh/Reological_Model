# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subventanaJSjUNR.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Descripcion(object):
    def setupUi(self, Descripcion):
        if not Descripcion.objectName():
            Descripcion.setObjectName(u"Descripcion")
        Descripcion.resize(666, 331)
        self.label = QLabel(Descripcion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 241, 41))
        self.label.setAlignment(Qt.AlignCenter)
        self.textEdit = QTextEdit(Descripcion)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(110, 80, 481, 107))
        self.aceptarButton = QPushButton(Descripcion)
        self.aceptarButton.setObjectName(u"aceptarButton")
        self.aceptarButton.setGeometry(QRect(120, 230, 112, 35))
        self.cancelarButton = QPushButton(Descripcion)
        self.cancelarButton.setObjectName(u"cancelarButton")
        self.cancelarButton.setGeometry(QRect(460, 230, 112, 35))

        self.retranslateUi(Descripcion)

        QMetaObject.connectSlotsByName(Descripcion)
    # setupUi

    def retranslateUi(self, Descripcion):
        Descripcion.setWindowTitle(QCoreApplication.translate("Descripcion", u"Form", None))
        self.label.setText(QCoreApplication.translate("Descripcion", u"Ingresa una Descripci\u00f3n", None))
        self.aceptarButton.setText(QCoreApplication.translate("Descripcion", u"Aceptar", None))
        self.cancelarButton.setText(QCoreApplication.translate("Descripcion", u"Cancelar", None))
    # retranslateUi

