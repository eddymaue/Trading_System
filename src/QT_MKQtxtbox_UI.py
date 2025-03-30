# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QT_MKQtxtboxARUrcu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.resize(106, 31)
        font = QFont()
        font.setBold(True)
        Form.setFont(font)
        Form.setWindowOpacity(1.000000000000000)
        Form.setProperty("FramelessWindowHint", False)
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 81, 31))
        self.PushButton = QPushButton(Form)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setGeometry(QRect(80, 0, 20, 20))
        self.PushButton.setStyleSheet(u"QPushButton:hover {\n"
"    color: red;\n"
"}")
        self.PushButton.setFlat(True)
        self.PushButton.raise_()
        self.textEdit.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PushButton.setText(QCoreApplication.translate("Form", u"X", None))
    # retranslateUi

