# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget, QButtonGroup)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/newPrefix/stethoscope.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setIconSize(QSize(30, 30))
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/new.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionNew.setIcon(icon1)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/open.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionOpen.setIcon(icon2)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionSave.setIcon(icon3)
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/print.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionPrint.setIcon(icon4)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionClose.setIcon(icon5)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionQuit.setIcon(icon6)
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/cut.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionCut.setIcon(icon7)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionCopy.setIcon(icon8)
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/paste.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionPaste.setIcon(icon9)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/undo.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionUndo.setIcon(icon10)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/redo.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionRedo.setIcon(icon11)
        self.actionPrescription = QAction(MainWindow)
        self.actionPrescription.setObjectName(u"actionPrescription")
        self.actionInvestigation = QAction(MainWindow)
        self.actionInvestigation.setObjectName(u"actionInvestigation")
        self.actionMinimize = QAction(MainWindow)
        self.actionMinimize.setObjectName(u"actionMinimize")
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionMinimize.setIcon(icon12)
        self.actionMaximize = QAction(MainWindow)
        self.actionMaximize.setObjectName(u"actionMaximize")
        icon13 = QIcon()
        icon13.addFile(u":/newPrefix/maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionMaximize.setIcon(icon13)
        self.actionFont_Size = QAction(MainWindow)
        self.actionFont_Size.setObjectName(u"actionFont_Size")
        icon14 = QIcon()
        icon14.addFile(u":/newPrefix/font.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionFont_Size.setIcon(icon14)
        self.actionFont_Family = QAction(MainWindow)
        self.actionFont_Family.setObjectName(u"actionFont_Family")
        icon15 = QIcon()
        icon15.addFile(u":/newPrefix/font-family.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionFont_Family.setIcon(icon15)
        self.actionFont_Color = QAction(MainWindow)
        self.actionFont_Color.setObjectName(u"actionFont_Color")
        icon16 = QIcon()
        icon16.addFile(u":/newPrefix/font-color.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionFont_Color.setIcon(icon16)
        self.actionBackground = QAction(MainWindow)
        self.actionBackground.setObjectName(u"actionBackground")
        icon17 = QIcon()
        icon17.addFile(u":/newPrefix/background.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionBackground.setIcon(icon17)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_130 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -2319, 1172, 3288))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_33 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(25)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.header_label = QLabel(self.scrollAreaWidgetContents)
        self.header_label.setObjectName(u"header_label")
        font1 = QFont()
        font1.setFamilies([u"DejaVu Serif"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.header_label.setFont(font1)
        self.header_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.header_label)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(90)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(100)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.id_label = QLabel(self.groupBox)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setFont(font)
        self.id_label.setLineWidth(0)
        self.id_label.setIndent(0)

        self.horizontalLayout.addWidget(self.id_label)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.id_lineEdit.sizePolicy().hasHeightForWidth())
        self.id_lineEdit.setSizePolicy(sizePolicy2)
        self.id_lineEdit.setFont(font)
        self.id_lineEdit.setFocusPolicy(Qt.NoFocus)
        self.id_lineEdit.setCursorPosition(0)
        self.id_lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.id_lineEdit)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.name_label = QLabel(self.groupBox)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.name_label)

        self.name_lineEdit = QLineEdit(self.groupBox)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.name_lineEdit.sizePolicy().hasHeightForWidth())
        self.name_lineEdit.setSizePolicy(sizePolicy3)
        self.name_lineEdit.setFont(font)

        self.horizontalLayout_2.addWidget(self.name_lineEdit)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.date_label = QLabel(self.groupBox)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.date_label)

        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font)
        self.dateEdit.setFocusPolicy(Qt.NoFocus)
        self.dateEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.dateEdit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(80)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(100)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sex_label = QLabel(self.groupBox)
        self.sex_label.setObjectName(u"sex_label")
        sizePolicy1.setHeightForWidth(self.sex_label.sizePolicy().hasHeightForWidth())
        self.sex_label.setSizePolicy(sizePolicy1)
        self.sex_label.setFont(font)
        self.sex_label.setIndent(0)

        self.horizontalLayout_6.addWidget(self.sex_label)

        self.male_radiobtn = QRadioButton(self.groupBox)
        self.male_radiobtn.setObjectName(u"male_radiobtn")
        sizePolicy1.setHeightForWidth(self.male_radiobtn.sizePolicy().hasHeightForWidth())
        self.male_radiobtn.setSizePolicy(sizePolicy1)
        self.male_radiobtn.setFont(font)
        self.male_radiobtn.setTabletTracking(True)

        self.horizontalLayout_6.addWidget(self.male_radiobtn)

        self.female_radiobtn = QRadioButton(self.groupBox)
        self.female_radiobtn.setObjectName(u"female_radiobtn")
        sizePolicy1.setHeightForWidth(self.female_radiobtn.sizePolicy().hasHeightForWidth())
        self.female_radiobtn.setSizePolicy(sizePolicy1)
        self.female_radiobtn.setFont(font)
        self.female_radiobtn.setTabletTracking(True)

        self.sex_btn_group = QButtonGroup(self.groupBox)
        self.sex_btn_group.setObjectName(u"sex_btn_group")
        self.sex_btn_group.addButton(self.male_radiobtn)
        self.sex_btn_group.addButton(self.female_radiobtn)

        self.horizontalLayout_6.addWidget(self.female_radiobtn)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.age_label = QLabel(self.groupBox)
        self.age_label.setObjectName(u"age_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.age_label.sizePolicy().hasHeightForWidth())
        self.age_label.setSizePolicy(sizePolicy4)
        self.age_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.age_label)

        self.age_lineEdit = QLineEdit(self.groupBox)
        self.age_lineEdit.setObjectName(u"age_lineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.age_lineEdit.sizePolicy().hasHeightForWidth())
        self.age_lineEdit.setSizePolicy(sizePolicy5)
        self.age_lineEdit.setFont(font)

        self.horizontalLayout_8.addWidget(self.age_lineEdit)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(80)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.job_label = QLabel(self.groupBox)
        self.job_label.setObjectName(u"job_label")
        self.job_label.setFont(font)

        self.horizontalLayout_10.addWidget(self.job_label)

        self.job_comboBox = QComboBox(self.groupBox)
        self.job_comboBox.addItem("")
        self.job_comboBox.addItem("")
        self.job_comboBox.addItem("")
        self.job_comboBox.addItem("")
        self.job_comboBox.addItem("")
        self.job_comboBox.addItem("")
        self.job_comboBox.setObjectName(u"job_comboBox")
        sizePolicy5.setHeightForWidth(self.job_comboBox.sizePolicy().hasHeightForWidth())
        self.job_comboBox.setSizePolicy(sizePolicy5)
        self.job_comboBox.setFont(font)

        self.horizontalLayout_10.addWidget(self.job_comboBox)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.marriage_label = QLabel(self.groupBox)
        self.marriage_label.setObjectName(u"marriage_label")
        sizePolicy4.setHeightForWidth(self.marriage_label.sizePolicy().hasHeightForWidth())
        self.marriage_label.setSizePolicy(sizePolicy4)
        self.marriage_label.setFont(font)

        self.horizontalLayout_7.addWidget(self.marriage_label)

        self.Marriage_comboBox = QComboBox(self.groupBox)
        self.Marriage_comboBox.addItem("")
        self.Marriage_comboBox.addItem("")
        self.Marriage_comboBox.addItem("")
        self.Marriage_comboBox.addItem("")
        self.Marriage_comboBox.setObjectName(u"Marriage_comboBox")
        sizePolicy5.setHeightForWidth(self.Marriage_comboBox.sizePolicy().hasHeightForWidth())
        self.Marriage_comboBox.setSizePolicy(sizePolicy5)
        self.Marriage_comboBox.setFont(font)

        self.horizontalLayout_7.addWidget(self.Marriage_comboBox)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(100)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Religion_label = QLabel(self.groupBox)
        self.Religion_label.setObjectName(u"Religion_label")
        self.Religion_label.setFont(font)

        self.horizontalLayout_13.addWidget(self.Religion_label)

        self.Religion_comboBox = QComboBox(self.groupBox)
        self.Religion_comboBox.addItem("")
        self.Religion_comboBox.addItem("")
        self.Religion_comboBox.addItem("")
        self.Religion_comboBox.addItem("")
        self.Religion_comboBox.addItem("")
        self.Religion_comboBox.setObjectName(u"Religion_comboBox")
        sizePolicy2.setHeightForWidth(self.Religion_comboBox.sizePolicy().hasHeightForWidth())
        self.Religion_comboBox.setSizePolicy(sizePolicy2)
        self.Religion_comboBox.setFont(font)

        self.horizontalLayout_13.addWidget(self.Religion_comboBox)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(90)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Address_label = QLabel(self.groupBox)
        self.Address_label.setObjectName(u"Address_label")
        self.Address_label.setFont(font)

        self.horizontalLayout_14.addWidget(self.Address_label)

        self.Address_lineEdit = QLineEdit(self.groupBox)
        self.Address_lineEdit.setObjectName(u"Address_lineEdit")
        self.Address_lineEdit.setFont(font)

        self.horizontalLayout_14.addWidget(self.Address_lineEdit)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.contact_label = QLabel(self.groupBox)
        self.contact_label.setObjectName(u"contact_label")
        self.contact_label.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.contact_label.sizePolicy().hasHeightForWidth())
        self.contact_label.setSizePolicy(sizePolicy2)
        self.contact_label.setFont(font)
        self.contact_label.setIndent(5)

        self.horizontalLayout_16.addWidget(self.contact_label)

        self.contact_lineEdit = QLineEdit(self.groupBox)
        self.contact_lineEdit.setObjectName(u"contact_lineEdit")
        sizePolicy2.setHeightForWidth(self.contact_lineEdit.sizePolicy().hasHeightForWidth())
        self.contact_lineEdit.setSizePolicy(sizePolicy2)
        self.contact_lineEdit.setFont(font)

        self.horizontalLayout_16.addWidget(self.contact_lineEdit)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_15)


        self.verticalLayout.addLayout(self.horizontalLayout_17)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setSpacing(25)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.illness_label = QLabel(self.groupBox_2)
        self.illness_label.setObjectName(u"illness_label")
        font2 = QFont()
        font2.setFamilies([u"DejaVu Serif"])
        font2.setPointSize(12)
        self.illness_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.illness_label)

        self.illness_textEdit = QTextEdit(self.groupBox_2)
        self.illness_textEdit.setObjectName(u"illness_textEdit")
        self.illness_textEdit.setFont(font)
        self.illness_textEdit.setTabChangesFocus(True)

        self.verticalLayout_2.addWidget(self.illness_textEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.history_label = QLabel(self.groupBox_2)
        self.history_label.setObjectName(u"history_label")
        self.history_label.setFont(font2)

        self.verticalLayout_3.addWidget(self.history_label)

        self.Past_illness_textEdit = QTextEdit(self.groupBox_2)
        self.Past_illness_textEdit.setObjectName(u"Past_illness_textEdit")
        self.Past_illness_textEdit.setFont(font)
        self.Past_illness_textEdit.setTabChangesFocus(True)

        self.verticalLayout_3.addWidget(self.Past_illness_textEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addWidget(self.groupBox_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_33.addLayout(self.verticalLayout_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(25)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 30, -1, -1)
        self.header_label2 = QLabel(self.scrollAreaWidgetContents)
        self.header_label2.setObjectName(u"header_label2")
        self.header_label2.setFont(font1)
        self.header_label2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.header_label2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 15, 10, 15)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.thermal_label = QLabel(self.groupBox_3)
        self.thermal_label.setObjectName(u"thermal_label")
        self.thermal_label.setFont(font)

        self.horizontalLayout_18.addWidget(self.thermal_label)

        self.thermal_lineEdit = QLineEdit(self.groupBox_3)
        self.thermal_lineEdit.setObjectName(u"thermal_lineEdit")
        self.thermal_lineEdit.setFont(font)

        self.horizontalLayout_18.addWidget(self.thermal_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.thirst_label = QLabel(self.groupBox_3)
        self.thirst_label.setObjectName(u"thirst_label")
        self.thirst_label.setFont(font)

        self.horizontalLayout_19.addWidget(self.thirst_label)

        self.thirst_lineEdit = QLineEdit(self.groupBox_3)
        self.thirst_lineEdit.setObjectName(u"thirst_lineEdit")
        self.thirst_lineEdit.setFont(font)

        self.horizontalLayout_19.addWidget(self.thirst_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.tongue_label = QLabel(self.groupBox_3)
        self.tongue_label.setObjectName(u"tongue_label")
        self.tongue_label.setFont(font)

        self.horizontalLayout_20.addWidget(self.tongue_label)

        self.tongue_lineEdit = QLineEdit(self.groupBox_3)
        self.tongue_lineEdit.setObjectName(u"tongue_lineEdit")
        self.tongue_lineEdit.setFont(font)

        self.horizontalLayout_20.addWidget(self.tongue_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.appetite_label = QLabel(self.groupBox_3)
        self.appetite_label.setObjectName(u"appetite_label")
        self.appetite_label.setFont(font)

        self.horizontalLayout_21.addWidget(self.appetite_label)

        self.appetite_lineEdit = QLineEdit(self.groupBox_3)
        self.appetite_lineEdit.setObjectName(u"appetite_lineEdit")
        self.appetite_lineEdit.setFont(font)

        self.horizontalLayout_21.addWidget(self.appetite_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.craving_label = QLabel(self.groupBox_3)
        self.craving_label.setObjectName(u"craving_label")
        self.craving_label.setFont(font)

        self.horizontalLayout_22.addWidget(self.craving_label)

        self.cravings_lineEdit = QLineEdit(self.groupBox_3)
        self.cravings_lineEdit.setObjectName(u"cravings_lineEdit")
        self.cravings_lineEdit.setFont(font)

        self.horizontalLayout_22.addWidget(self.cravings_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.dislike_label = QLabel(self.groupBox_3)
        self.dislike_label.setObjectName(u"dislike_label")
        self.dislike_label.setFont(font)

        self.horizontalLayout_23.addWidget(self.dislike_label)

        self.dislike_lineEdit = QLineEdit(self.groupBox_3)
        self.dislike_lineEdit.setObjectName(u"dislike_lineEdit")
        self.dislike_lineEdit.setFont(font)

        self.horizontalLayout_23.addWidget(self.dislike_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.intolerance_label = QLabel(self.groupBox_3)
        self.intolerance_label.setObjectName(u"intolerance_label")
        self.intolerance_label.setFont(font)

        self.horizontalLayout_24.addWidget(self.intolerance_label)

        self.intolerance_lineEdit = QLineEdit(self.groupBox_3)
        self.intolerance_lineEdit.setObjectName(u"intolerance_lineEdit")
        self.intolerance_lineEdit.setFont(font)

        self.horizontalLayout_24.addWidget(self.intolerance_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.hunger_label = QLabel(self.groupBox_3)
        self.hunger_label.setObjectName(u"hunger_label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.hunger_label.sizePolicy().hasHeightForWidth())
        self.hunger_label.setSizePolicy(sizePolicy6)
        self.hunger_label.setFont(font)

        self.horizontalLayout_25.addWidget(self.hunger_label)

        self.aggravation_radiobtn = QRadioButton(self.groupBox_3)
        self.aggravation_radiobtn.setObjectName(u"aggravation_radiobtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.aggravation_radiobtn.sizePolicy().hasHeightForWidth())
        self.aggravation_radiobtn.setSizePolicy(sizePolicy7)
        self.aggravation_radiobtn.setFont(font)

        self.horizontalLayout_25.addWidget(self.aggravation_radiobtn)

        self.amelioration_radiobtn = QRadioButton(self.groupBox_3)
        self.amelioration_radiobtn.setObjectName(u"amelioration_radiobtn")
        sizePolicy7.setHeightForWidth(self.amelioration_radiobtn.sizePolicy().hasHeightForWidth())
        self.amelioration_radiobtn.setSizePolicy(sizePolicy7)
        self.amelioration_radiobtn.setFont(font)

        self.horizontalLayout_25.addWidget(self.amelioration_radiobtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.bathing_label = QLabel(self.groupBox_3)
        self.bathing_label.setObjectName(u"bathing_label")
        self.bathing_label.setFont(font)

        self.horizontalLayout_28.addWidget(self.bathing_label)

        self.bathing_lineEdit = QLineEdit(self.groupBox_3)
        self.bathing_lineEdit.setObjectName(u"bathing_lineEdit")
        self.bathing_lineEdit.setFont(font)

        self.horizontalLayout_28.addWidget(self.bathing_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.sweat_label = QLabel(self.groupBox_3)
        self.sweat_label.setObjectName(u"sweat_label")
        self.sweat_label.setFont(font)

        self.horizontalLayout_29.addWidget(self.sweat_label)

        self.sweat_lineEdit = QLineEdit(self.groupBox_3)
        self.sweat_lineEdit.setObjectName(u"sweat_lineEdit")
        self.sweat_lineEdit.setFont(font)

        self.horizontalLayout_29.addWidget(self.sweat_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.aleep_label = QLabel(self.groupBox_3)
        self.aleep_label.setObjectName(u"aleep_label")
        self.aleep_label.setFont(font)

        self.horizontalLayout_30.addWidget(self.aleep_label)

        self.sleep_lineEdit = QLineEdit(self.groupBox_3)
        self.sleep_lineEdit.setObjectName(u"sleep_lineEdit")
        self.sleep_lineEdit.setFont(font)

        self.horizontalLayout_30.addWidget(self.sleep_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.dreams_label = QLabel(self.groupBox_3)
        self.dreams_label.setObjectName(u"dreams_label")
        self.dreams_label.setFont(font)

        self.horizontalLayout_31.addWidget(self.dreams_label)

        self.dreams_lineEdit = QLineEdit(self.groupBox_3)
        self.dreams_lineEdit.setObjectName(u"dreams_lineEdit")
        self.dreams_lineEdit.setFont(font)

        self.horizontalLayout_31.addWidget(self.dreams_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.salivation_label = QLabel(self.groupBox_3)
        self.salivation_label.setObjectName(u"salivation_label")
        self.salivation_label.setFont(font)

        self.horizontalLayout_32.addWidget(self.salivation_label)

        self.salivation_lineEdit = QLineEdit(self.groupBox_3)
        self.salivation_lineEdit.setObjectName(u"salivation_lineEdit")
        self.salivation_lineEdit.setFont(font)

        self.horizontalLayout_32.addWidget(self.salivation_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.urine_label = QLabel(self.groupBox_3)
        self.urine_label.setObjectName(u"urine_label")
        self.urine_label.setFont(font)

        self.horizontalLayout_33.addWidget(self.urine_label)

        self.urine_lineEdit = QLineEdit(self.groupBox_3)
        self.urine_lineEdit.setObjectName(u"urine_lineEdit")
        self.urine_lineEdit.setFont(font)

        self.horizontalLayout_33.addWidget(self.urine_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.stool_label = QLabel(self.groupBox_3)
        self.stool_label.setObjectName(u"stool_label")
        self.stool_label.setFont(font)

        self.horizontalLayout_34.addWidget(self.stool_label)

        self.stool_lineEdit = QLineEdit(self.groupBox_3)
        self.stool_lineEdit.setObjectName(u"stool_lineEdit")
        self.stool_lineEdit.setFont(font)

        self.horizontalLayout_34.addWidget(self.stool_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.rectum_label = QLabel(self.groupBox_3)
        self.rectum_label.setObjectName(u"rectum_label")
        self.rectum_label.setFont(font)

        self.horizontalLayout_35.addWidget(self.rectum_label)

        self.rectum_lineEdit = QLineEdit(self.groupBox_3)
        self.rectum_lineEdit.setObjectName(u"rectum_lineEdit")
        self.rectum_lineEdit.setFont(font)

        self.horizontalLayout_35.addWidget(self.rectum_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.skin_label = QLabel(self.groupBox_3)
        self.skin_label.setObjectName(u"skin_label")
        self.skin_label.setFont(font)

        self.horizontalLayout_36.addWidget(self.skin_label)

        self.skin_lineEdit = QLineEdit(self.groupBox_3)
        self.skin_lineEdit.setObjectName(u"skin_lineEdit")
        self.skin_lineEdit.setFont(font)

        self.horizontalLayout_36.addWidget(self.skin_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_36)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.abuseDrugs_checkBox = QCheckBox(self.groupBox_3)
        self.abuseDrugs_checkBox.setObjectName(u"abuseDrugs_checkBox")
        self.abuseDrugs_checkBox.setFont(font)

        self.gridLayout.addWidget(self.abuseDrugs_checkBox, 2, 7, 1, 1)

        self.bloodLose_checkBox = QCheckBox(self.groupBox_3)
        self.bloodLose_checkBox.setObjectName(u"bloodLose_checkBox")
        self.bloodLose_checkBox.setFont(font)

        self.gridLayout.addWidget(self.bloodLose_checkBox, 2, 8, 1, 1)

        self.grief_checkBox = QCheckBox(self.groupBox_3)
        self.grief_checkBox.setObjectName(u"grief_checkBox")
        self.grief_checkBox.setFont(font)

        self.gridLayout.addWidget(self.grief_checkBox, 0, 11, 1, 1)

        self.anger_checkBox = QCheckBox(self.groupBox_3)
        self.anger_checkBox.setObjectName(u"anger_checkBox")
        self.anger_checkBox.setFont(font)

        self.gridLayout.addWidget(self.anger_checkBox, 0, 1, 1, 1)

        self.mortification_checkBox = QCheckBox(self.groupBox_3)
        self.mortification_checkBox.setObjectName(u"mortification_checkBox")
        self.mortification_checkBox.setFont(font)

        self.gridLayout.addWidget(self.mortification_checkBox, 2, 1, 1, 1)

        self.badnews_checkBox = QCheckBox(self.groupBox_3)
        self.badnews_checkBox.setObjectName(u"badnews_checkBox")
        self.badnews_checkBox.setFont(font)

        self.gridLayout.addWidget(self.badnews_checkBox, 2, 6, 1, 1)

        self.joy_checkBox = QCheckBox(self.groupBox_3)
        self.joy_checkBox.setObjectName(u"joy_checkBox")
        self.joy_checkBox.setFont(font)

        self.gridLayout.addWidget(self.joy_checkBox, 2, 12, 1, 1)

        self.love_checkBox = QCheckBox(self.groupBox_3)
        self.love_checkBox.setObjectName(u"love_checkBox")
        self.love_checkBox.setFont(font)

        self.gridLayout.addWidget(self.love_checkBox, 2, 11, 1, 1)

        self.excitement_checkBox = QCheckBox(self.groupBox_3)
        self.excitement_checkBox.setObjectName(u"excitement_checkBox")
        self.excitement_checkBox.setFont(font)

        self.gridLayout.addWidget(self.excitement_checkBox, 0, 7, 1, 1)

        self.aliments_label = QLabel(self.groupBox_3)
        self.aliments_label.setObjectName(u"aliments_label")
        self.aliments_label.setFont(font)

        self.gridLayout.addWidget(self.aliments_label, 0, 0, 1, 1)

        self.injury_checkBox = QCheckBox(self.groupBox_3)
        self.injury_checkBox.setObjectName(u"injury_checkBox")
        self.injury_checkBox.setFont(font)

        self.gridLayout.addWidget(self.injury_checkBox, 0, 4, 1, 1)

        self.fright_checkBox = QCheckBox(self.groupBox_3)
        self.fright_checkBox.setObjectName(u"fright_checkBox")
        self.fright_checkBox.setFont(font)

        self.gridLayout.addWidget(self.fright_checkBox, 0, 8, 1, 1)

        self.anticipation_checkBox = QCheckBox(self.groupBox_3)
        self.anticipation_checkBox.setObjectName(u"anticipation_checkBox")
        self.anticipation_checkBox.setFont(font)

        self.gridLayout.addWidget(self.anticipation_checkBox, 2, 4, 1, 1)

        self.emotions_checkBox = QCheckBox(self.groupBox_3)
        self.emotions_checkBox.setObjectName(u"emotions_checkBox")
        self.emotions_checkBox.setFont(font)

        self.gridLayout.addWidget(self.emotions_checkBox, 0, 6, 1, 1)

        self.disappointed_checkBox = QCheckBox(self.groupBox_3)
        self.disappointed_checkBox.setObjectName(u"disappointed_checkBox")
        self.disappointed_checkBox.setFont(font)

        self.gridLayout.addWidget(self.disappointed_checkBox, 0, 12, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.generalModalities_label = QLabel(self.groupBox_3)
        self.generalModalities_label.setObjectName(u"generalModalities_label")
        self.generalModalities_label.setFont(font)

        self.horizontalLayout_26.addWidget(self.generalModalities_label)

        self.generalModalities_lineEdit = QLineEdit(self.groupBox_3)
        self.generalModalities_lineEdit.setObjectName(u"generalModalities_lineEdit")
        self.generalModalities_lineEdit.setFont(font)

        self.horizontalLayout_26.addWidget(self.generalModalities_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.nailAnalysis_label = QLabel(self.groupBox_3)
        self.nailAnalysis_label.setObjectName(u"nailAnalysis_label")
        self.nailAnalysis_label.setFont(font)

        self.horizontalLayout_27.addWidget(self.nailAnalysis_label)

        self.nailAnalysis_lineEdit = QLineEdit(self.groupBox_3)
        self.nailAnalysis_lineEdit.setObjectName(u"nailAnalysis_lineEdit")
        self.nailAnalysis_lineEdit.setFont(font)

        self.horizontalLayout_27.addWidget(self.nailAnalysis_lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_27)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 15, 10, 15)
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_3)

        self.femaleOnly_label = QLabel(self.groupBox_4)
        self.femaleOnly_label.setObjectName(u"femaleOnly_label")
        font3 = QFont()
        font3.setPointSize(15)
        self.femaleOnly_label.setFont(font3)

        self.horizontalLayout_37.addWidget(self.femaleOnly_label)

        self.label_23 = QLabel(self.groupBox_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.horizontalLayout_37.addWidget(self.label_23)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_37)

        self.femaleOnly_textEdit = QTextEdit(self.groupBox_4)
        self.femaleOnly_textEdit.setObjectName(u"femaleOnly_textEdit")
        self.femaleOnly_textEdit.setFont(font)
        self.femaleOnly_textEdit.setTabChangesFocus(True)

        self.verticalLayout_8.addWidget(self.femaleOnly_textEdit)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.pregnancy_label = QLabel(self.groupBox_4)
        self.pregnancy_label.setObjectName(u"pregnancy_label")
        self.pregnancy_label.setFont(font)

        self.horizontalLayout_38.addWidget(self.pregnancy_label)

        self.pregnancy_lineEdit = QLineEdit(self.groupBox_4)
        self.pregnancy_lineEdit.setObjectName(u"pregnancy_lineEdit")
        self.pregnancy_lineEdit.setFont(font)

        self.horizontalLayout_38.addWidget(self.pregnancy_lineEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.obstetric_label = QLabel(self.groupBox_4)
        self.obstetric_label.setObjectName(u"obstetric_label")
        self.obstetric_label.setFont(font)

        self.horizontalLayout_39.addWidget(self.obstetric_label)

        self.marriedFor_label = QLabel(self.groupBox_4)
        self.marriedFor_label.setObjectName(u"marriedFor_label")
        self.marriedFor_label.setFont(font)

        self.horizontalLayout_39.addWidget(self.marriedFor_label)

        self.marriedFor_lineEdit = QLineEdit(self.groupBox_4)
        self.marriedFor_lineEdit.setObjectName(u"marriedFor_lineEdit")
        self.marriedFor_lineEdit.setFont(font)

        self.horizontalLayout_39.addWidget(self.marriedFor_lineEdit)

        self.gravida_label = QLabel(self.groupBox_4)
        self.gravida_label.setObjectName(u"gravida_label")
        self.gravida_label.setFont(font)

        self.horizontalLayout_39.addWidget(self.gravida_label)

        self.gravida_lineEdit = QLineEdit(self.groupBox_4)
        self.gravida_lineEdit.setObjectName(u"gravida_lineEdit")
        self.gravida_lineEdit.setFont(font)

        self.horizontalLayout_39.addWidget(self.gravida_lineEdit)

        self.abortion_label = QLabel(self.groupBox_4)
        self.abortion_label.setObjectName(u"abortion_label")
        self.abortion_label.setFont(font)

        self.horizontalLayout_39.addWidget(self.abortion_label)

        self.abortion_lineEdit = QLineEdit(self.groupBox_4)
        self.abortion_lineEdit.setObjectName(u"abortion_lineEdit")
        self.abortion_lineEdit.setFont(font)

        self.horizontalLayout_39.addWidget(self.abortion_lineEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_39)


        self.verticalLayout_9.addWidget(self.groupBox_4)


        self.verticalLayout_33.addLayout(self.verticalLayout_9)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(15)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, 40, -1, -1)
        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_16)

        self.header_label3 = QLabel(self.scrollAreaWidgetContents)
        self.header_label3.setObjectName(u"header_label3")
        self.header_label3.setFont(font1)

        self.horizontalLayout_100.addWidget(self.header_label3)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_17)


        self.verticalLayout_27.addLayout(self.horizontalLayout_100)

        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font)
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_26.setSpacing(8)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(10, 12, 10, 10)
        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.will_label = QLabel(self.groupBox_9)
        self.will_label.setObjectName(u"will_label")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(True)
        self.will_label.setFont(font4)

        self.horizontalLayout_101.addWidget(self.will_label)

        self.will2_label = QLabel(self.groupBox_9)
        self.will2_label.setObjectName(u"will2_label")
        self.will2_label.setFont(font)

        self.horizontalLayout_101.addWidget(self.will2_label)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_18)


        self.verticalLayout_26.addLayout(self.horizontalLayout_101)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.A_label = QLabel(self.groupBox_9)
        self.A_label.setObjectName(u"A_label")
        self.A_label.setFont(font)

        self.horizontalLayout_102.addWidget(self.A_label)

        self.A_lineEdit = QLineEdit(self.groupBox_9)
        self.A_lineEdit.setObjectName(u"A_lineEdit")
        self.A_lineEdit.setFont(font)

        self.horizontalLayout_102.addWidget(self.A_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_102)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.B_label = QLabel(self.groupBox_9)
        self.B_label.setObjectName(u"B_label")
        self.B_label.setFont(font)

        self.horizontalLayout_103.addWidget(self.B_label)

        self.B_lineEdit = QLineEdit(self.groupBox_9)
        self.B_lineEdit.setObjectName(u"B_lineEdit")
        self.B_lineEdit.setFont(font)

        self.horizontalLayout_103.addWidget(self.B_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_103)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.C_label = QLabel(self.groupBox_9)
        self.C_label.setObjectName(u"C_label")
        self.C_label.setFont(font)

        self.horizontalLayout_104.addWidget(self.C_label)

        self.C_lineEdit = QLineEdit(self.groupBox_9)
        self.C_lineEdit.setObjectName(u"C_lineEdit")
        self.C_lineEdit.setFont(font)

        self.horizontalLayout_104.addWidget(self.C_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_104)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.D_label = QLabel(self.groupBox_9)
        self.D_label.setObjectName(u"D_label")
        self.D_label.setFont(font)

        self.horizontalLayout_105.addWidget(self.D_label)

        self.D_lineEdit = QLineEdit(self.groupBox_9)
        self.D_lineEdit.setObjectName(u"D_lineEdit")
        self.D_lineEdit.setFont(font)

        self.horizontalLayout_105.addWidget(self.D_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_105)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.E_label = QLabel(self.groupBox_9)
        self.E_label.setObjectName(u"E_label")
        self.E_label.setFont(font)

        self.horizontalLayout_106.addWidget(self.E_label)

        self.E_lineEdit = QLineEdit(self.groupBox_9)
        self.E_lineEdit.setObjectName(u"E_lineEdit")
        self.E_lineEdit.setFont(font)

        self.horizontalLayout_106.addWidget(self.E_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_106)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.effectCompany_label = QLabel(self.groupBox_9)
        self.effectCompany_label.setObjectName(u"effectCompany_label")
        self.effectCompany_label.setFont(font)

        self.horizontalLayout_107.addWidget(self.effectCompany_label)

        self.effectCompany_lineEdit = QLineEdit(self.groupBox_9)
        self.effectCompany_lineEdit.setObjectName(u"effectCompany_lineEdit")
        self.effectCompany_lineEdit.setFont(font)

        self.horizontalLayout_107.addWidget(self.effectCompany_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_107)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.effectConsolation_label = QLabel(self.groupBox_9)
        self.effectConsolation_label.setObjectName(u"effectConsolation_label")
        self.effectConsolation_label.setFont(font)

        self.horizontalLayout_108.addWidget(self.effectConsolation_label)

        self.effectConsolation_lineEdit = QLineEdit(self.groupBox_9)
        self.effectConsolation_lineEdit.setObjectName(u"effectConsolation_lineEdit")
        self.effectConsolation_lineEdit.setFont(font)

        self.horizontalLayout_108.addWidget(self.effectConsolation_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_108)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.daSex_label = QLabel(self.groupBox_9)
        self.daSex_label.setObjectName(u"daSex_label")
        self.daSex_label.setFont(font)

        self.horizontalLayout_109.addWidget(self.daSex_label)

        self.daSex_lineEdit = QLineEdit(self.groupBox_9)
        self.daSex_lineEdit.setObjectName(u"daSex_lineEdit")
        self.daSex_lineEdit.setFont(font)

        self.horizontalLayout_109.addWidget(self.daSex_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_109)

        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.daSpecialsense_label = QLabel(self.groupBox_9)
        self.daSpecialsense_label.setObjectName(u"daSpecialsense_label")
        self.daSpecialsense_label.setFont(font)

        self.horizontalLayout_110.addWidget(self.daSpecialsense_label)

        self.daSpecialSense_lineEdit = QLineEdit(self.groupBox_9)
        self.daSpecialSense_lineEdit.setObjectName(u"daSpecialSense_lineEdit")
        self.daSpecialSense_lineEdit.setFont(font)

        self.horizontalLayout_110.addWidget(self.daSpecialSense_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_110)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.grief_label = QLabel(self.groupBox_9)
        self.grief_label.setObjectName(u"grief_label")
        self.grief_label.setFont(font)

        self.horizontalLayout_111.addWidget(self.grief_label)

        self.grief_lineEdit = QLineEdit(self.groupBox_9)
        self.grief_lineEdit.setObjectName(u"grief_lineEdit")
        self.grief_lineEdit.setFont(font)

        self.horizontalLayout_111.addWidget(self.grief_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_111)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.gesturesPostures_label = QLabel(self.groupBox_9)
        self.gesturesPostures_label.setObjectName(u"gesturesPostures_label")
        self.gesturesPostures_label.setFont(font)

        self.horizontalLayout_112.addWidget(self.gesturesPostures_label)

        self.gesturesPostures_lineEdit = QLineEdit(self.groupBox_9)
        self.gesturesPostures_lineEdit.setObjectName(u"gesturesPostures_lineEdit")
        self.gesturesPostures_lineEdit.setFont(font)

        self.horizontalLayout_112.addWidget(self.gesturesPostures_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_112)

        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(-1, -1, -1, 10)
        self.anxiety_label = QLabel(self.groupBox_9)
        self.anxiety_label.setObjectName(u"anxiety_label")
        self.anxiety_label.setFont(font)

        self.horizontalLayout_113.addWidget(self.anxiety_label)

        self.anxiety_lineEdit = QLineEdit(self.groupBox_9)
        self.anxiety_lineEdit.setObjectName(u"anxiety_lineEdit")
        self.anxiety_lineEdit.setFont(font)

        self.horizontalLayout_113.addWidget(self.anxiety_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_113)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.intellect_label = QLabel(self.groupBox_9)
        self.intellect_label.setObjectName(u"intellect_label")
        self.intellect_label.setFont(font4)

        self.horizontalLayout_114.addWidget(self.intellect_label)

        self.intellect_lineEdit = QLineEdit(self.groupBox_9)
        self.intellect_lineEdit.setObjectName(u"intellect_lineEdit")
        self.intellect_lineEdit.setFont(font)

        self.horizontalLayout_114.addWidget(self.intellect_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_114)

        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.memory_label = QLabel(self.groupBox_9)
        self.memory_label.setObjectName(u"memory_label")
        self.memory_label.setFont(font)

        self.horizontalLayout_115.addWidget(self.memory_label)

        self.memory_lineEdit = QLineEdit(self.groupBox_9)
        self.memory_lineEdit.setObjectName(u"memory_lineEdit")
        self.memory_lineEdit.setFont(font)

        self.horizontalLayout_115.addWidget(self.memory_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.anger_label = QLabel(self.groupBox_9)
        self.anger_label.setObjectName(u"anger_label")
        self.anger_label.setFont(font)

        self.horizontalLayout_116.addWidget(self.anger_label)

        self.anger_lineEdit = QLineEdit(self.groupBox_9)
        self.anger_lineEdit.setObjectName(u"anger_lineEdit")
        self.anger_lineEdit.setFont(font)

        self.horizontalLayout_116.addWidget(self.anger_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_116)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setSpacing(250)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")        
        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setSpacing(15)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.avarice_label = QLabel(self.groupBox_9)
        self.avarice_label.setObjectName(u"avarice_label")
        self.avarice_label.setFont(font)

        self.horizontalLayout_118.addWidget(self.avarice_label)

        self.yes_radioButton = QRadioButton(self.groupBox_9)
        self.yes_radioButton.setObjectName(u"yes_radioButton")
        self.yes_radioButton.setFont(font)

        self.horizontalLayout_118.addWidget(self.yes_radioButton)

        self.no_radioButton = QRadioButton(self.groupBox_9)
        self.no_radioButton.setObjectName(u"no_radioButton")
        self.no_radioButton.setFont(font)

        self.avarice_btn_group = QButtonGroup(self.groupBox_9)
        self.avarice_btn_group.setObjectName(u"avarice_btn_group")
        self.avarice_btn_group.addButton(self.yes_radioButton)
        self.avarice_btn_group.addButton(self.no_radioButton)

        self.horizontalLayout_118.addWidget(self.no_radioButton)

        self.horizontalLayout_117.addLayout(self.horizontalLayout_118)

        #self.widget2 = QWidget(self.groupBox_9)
        #self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setSpacing(15)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.religiouos_label = QLabel(self.groupBox_9)
        self.religiouos_label.setObjectName(u"religiouos_label")
        self.religiouos_label.setFont(font)
        self.religiouos_label.setIndent(3)

        self.horizontalLayout_119.addWidget(self.religiouos_label)

        self.yes2_radioButton = QRadioButton(self.groupBox_9)
        self.yes2_radioButton.setObjectName(u"yes2_radioButton")
        self.yes2_radioButton.setFont(font)

        self.horizontalLayout_119.addWidget(self.yes2_radioButton)

        self.no2_radioButton = QRadioButton(self.groupBox_9)
        self.no2_radioButton.setObjectName(u"no2_radioButton")
        self.no2_radioButton.setFont(font)

        self.religious_btn_group = QButtonGroup(self.groupBox_9)
        self.religious_btn_group.setObjectName(u"religious_btn_group")
        self.religious_btn_group.addButton(self.yes2_radioButton)
        self.religious_btn_group.addButton(self.no2_radioButton)

        self.horizontalLayout_119.addWidget(self.no2_radioButton)

        self.horizontalLayout_117.addLayout(self.horizontalLayout_119)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_117.addItem(self.horizontalSpacer_19)


        self.verticalLayout_26.addLayout(self.horizontalLayout_117)

        self.dominating_label = QLabel(self.groupBox_9)
        self.dominating_label.setObjectName(u"dominating_label")
        self.dominating_label.setFont(font4)

        self.verticalLayout_26.addWidget(self.dominating_label)

        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.laughing_label = QLabel(self.groupBox_9)
        self.laughing_label.setObjectName(u"laughing_label")
        self.laughing_label.setFont(font)

        self.horizontalLayout_120.addWidget(self.laughing_label)

        self.laughing_lineEdit = QLineEdit(self.groupBox_9)
        self.laughing_lineEdit.setObjectName(u"laughing_lineEdit")
        self.laughing_lineEdit.setFont(font)

        self.horizontalLayout_120.addWidget(self.laughing_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_120)

        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(-1, -1, -1, 10)
        self.selfConfidence_label = QLabel(self.groupBox_9)
        self.selfConfidence_label.setObjectName(u"selfConfidence_label")
        self.selfConfidence_label.setFont(font)

        self.horizontalLayout_121.addWidget(self.selfConfidence_label)

        self.selfConfidence_lineEdit = QLineEdit(self.groupBox_9)
        self.selfConfidence_lineEdit.setObjectName(u"selfConfidence_lineEdit")
        self.selfConfidence_lineEdit.setFont(font)

        self.horizontalLayout_121.addWidget(self.selfConfidence_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_121)

        self.sentimental_label = QLabel(self.groupBox_9)
        self.sentimental_label.setObjectName(u"sentimental_label")
        self.sentimental_label.setFont(font4)

        self.verticalLayout_26.addWidget(self.sentimental_label)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.sharing_label = QLabel(self.groupBox_9)
        self.sharing_label.setObjectName(u"sharing_label")
        self.sharing_label.setFont(font)

        self.horizontalLayout_122.addWidget(self.sharing_label)

        self.sharing_lineEdit = QLineEdit(self.groupBox_9)
        self.sharing_lineEdit.setObjectName(u"sharing_lineEdit")
        self.sharing_lineEdit.setFont(font)

        self.horizontalLayout_122.addWidget(self.sharing_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalLayout_123.setContentsMargins(-1, -1, -1, 10)
        self.shock_label = QLabel(self.groupBox_9)
        self.shock_label.setObjectName(u"shock_label")
        self.shock_label.setFont(font)

        self.horizontalLayout_123.addWidget(self.shock_label)

        self.shock_lineEdit = QLineEdit(self.groupBox_9)
        self.shock_lineEdit.setObjectName(u"shock_lineEdit")
        self.shock_lineEdit.setFont(font)

        self.horizontalLayout_123.addWidget(self.shock_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_123)

        self.sympathetic_label = QLabel(self.groupBox_9)
        self.sympathetic_label.setObjectName(u"sympathetic_label")
        self.sympathetic_label.setFont(font4)

        self.verticalLayout_26.addWidget(self.sympathetic_label)

        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.weeping_label = QLabel(self.groupBox_9)
        self.weeping_label.setObjectName(u"weeping_label")
        self.weeping_label.setFont(font)

        self.horizontalLayout_124.addWidget(self.weeping_label)

        self.weeping_lineEdit = QLineEdit(self.groupBox_9)
        self.weeping_lineEdit.setObjectName(u"weeping_lineEdit")
        self.weeping_lineEdit.setFont(font)

        self.horizontalLayout_124.addWidget(self.weeping_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_124)

        # self.widget1 = QWidget(self.groupBox_9)
        # self.widget1.setObjectName(u"widget1")
        # self.widget1.setFocusPolicy(Qt.NoFocus)
        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setSpacing(30)
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.work_label = QLabel(self.groupBox_9)
        self.work_label.setObjectName(u"work_label")
        self.work_label.setFont(font)
        self.work_label.setIndent(3)

        self.horizontalLayout_125.addWidget(self.work_label)

        self.slow_radioButton = QRadioButton(self.groupBox_9)
        self.slow_radioButton.setObjectName(u"slow_radioButton")
        self.slow_radioButton.setFont(font)

        self.horizontalLayout_125.addWidget(self.slow_radioButton)

        self.hurry_radioButton = QRadioButton(self.groupBox_9)
        self.hurry_radioButton.setObjectName(u"hurry_radioButton")
        self.hurry_radioButton.setFont(font)

        self.work_btn_group = QButtonGroup(self.groupBox_9)
        self.work_btn_group.setObjectName(u"work_btn_group")
        self.work_btn_group.addButton(self.slow_radioButton)
        self.work_btn_group.addButton(self.hurry_radioButton)
        
        self.horizontalLayout_125.addWidget(self.hurry_radioButton)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_125.addItem(self.horizontalSpacer_20)


        self.verticalLayout_26.addLayout(self.horizontalLayout_125)

        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.aggravation_label = QLabel(self.groupBox_9)
        self.aggravation_label.setObjectName(u"aggravation_label")
        self.aggravation_label.setFont(font)

        self.horizontalLayout_126.addWidget(self.aggravation_label)

        self.aggravation_lineEdit = QLineEdit(self.groupBox_9)
        self.aggravation_lineEdit.setObjectName(u"aggravation_lineEdit")
        self.aggravation_lineEdit.setFont(font)

        self.horizontalLayout_126.addWidget(self.aggravation_lineEdit)


        self.verticalLayout_26.addLayout(self.horizontalLayout_126)


        self.verticalLayout_27.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setFont(font)
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_28.setSpacing(8)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.pastHistory_label = QLabel(self.groupBox_10)
        self.pastHistory_label.setObjectName(u"pastHistory_label")
        font5 = QFont()
        font5.setPointSize(16)
        self.pastHistory_label.setFont(font5)

        self.verticalLayout_29.addWidget(self.pastHistory_label)

        self.pastHistory_textEdit = QTextEdit(self.groupBox_10)
        self.pastHistory_textEdit.setObjectName(u"pastHistory_textEdit")
        self.pastHistory_textEdit.setFont(font)
        self.pastHistory_textEdit.setTabChangesFocus(True)

        self.verticalLayout_29.addWidget(self.pastHistory_textEdit)


        self.verticalLayout_28.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.familyHistory_label = QLabel(self.groupBox_10)
        self.familyHistory_label.setObjectName(u"familyHistory_label")
        self.familyHistory_label.setFont(font5)

        self.verticalLayout_30.addWidget(self.familyHistory_label)

        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.fatherSide_label = QLabel(self.groupBox_10)
        self.fatherSide_label.setObjectName(u"fatherSide_label")
        self.fatherSide_label.setFont(font)

        self.horizontalLayout_127.addWidget(self.fatherSide_label)

        self.fatherSide_lineEdit = QLineEdit(self.groupBox_10)
        self.fatherSide_lineEdit.setObjectName(u"fatherSide_lineEdit")
        self.fatherSide_lineEdit.setFont(font)

        self.horizontalLayout_127.addWidget(self.fatherSide_lineEdit)


        self.verticalLayout_30.addLayout(self.horizontalLayout_127)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.motherSide_label = QLabel(self.groupBox_10)
        self.motherSide_label.setObjectName(u"motherSide_label")
        self.motherSide_label.setFont(font)

        self.horizontalLayout_128.addWidget(self.motherSide_label)

        self.motherSide_lineEdit = QLineEdit(self.groupBox_10)
        self.motherSide_lineEdit.setObjectName(u"motherSide_lineEdit")
        self.motherSide_lineEdit.setFont(font)

        self.horizontalLayout_128.addWidget(self.motherSide_lineEdit)


        self.verticalLayout_30.addLayout(self.horizontalLayout_128)


        self.verticalLayout_28.addLayout(self.verticalLayout_30)


        self.verticalLayout_27.addWidget(self.groupBox_10)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(10)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_129.addItem(self.horizontalSpacer_21)

        self.observation_lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.observation_lineEdit.setObjectName(u"observation_lineEdit")
        self.observation_lineEdit.setFont(font1)
        self.observation_lineEdit.setFocusPolicy(Qt.NoFocus)
        self.observation_lineEdit.setAlignment(Qt.AlignCenter)
        self.observation_lineEdit.setReadOnly(True)

        self.horizontalLayout_129.addWidget(self.observation_lineEdit)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_129.addItem(self.horizontalSpacer_22)


        self.verticalLayout_31.addLayout(self.horizontalLayout_129)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.physicalExamination_label = QLabel(self.scrollAreaWidgetContents)
        self.physicalExamination_label.setObjectName(u"physicalExamination_label")
        font6 = QFont()
        font6.setPointSize(14)
        self.physicalExamination_label.setFont(font6)

        self.verticalLayout_32.addWidget(self.physicalExamination_label)

        self.physicalExamination_textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.physicalExamination_textEdit.setObjectName(u"physicalExamination_textEdit")
        self.physicalExamination_textEdit.setFont(font)
        self.physicalExamination_textEdit.setTabChangesFocus(True)

        self.verticalLayout_32.addWidget(self.physicalExamination_textEdit)

        self.laboratoryInvestigation_label = QLabel(self.scrollAreaWidgetContents)
        self.laboratoryInvestigation_label.setObjectName(u"laboratoryInvestigation_label")
        self.laboratoryInvestigation_label.setFont(font6)

        self.verticalLayout_32.addWidget(self.laboratoryInvestigation_label)

        self.laboratoryInvestigation_textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.laboratoryInvestigation_textEdit.setObjectName(u"laboratoryInvestigation_textEdit")
        self.laboratoryInvestigation_textEdit.setFont(font)
        self.laboratoryInvestigation_textEdit.setTabChangesFocus(True)

        self.verticalLayout_32.addWidget(self.laboratoryInvestigation_textEdit)


        self.verticalLayout_31.addLayout(self.verticalLayout_32)


        self.verticalLayout_27.addLayout(self.verticalLayout_31)


        self.verticalLayout_33.addLayout(self.verticalLayout_27)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_130.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.id_label.setBuddy(self.id_lineEdit)
        self.name_label.setBuddy(self.name_lineEdit)
        self.date_label.setBuddy(self.dateEdit)
        self.age_label.setBuddy(self.age_lineEdit)
        self.job_label.setBuddy(self.job_comboBox)
        self.marriage_label.setBuddy(self.Marriage_comboBox)
        self.Religion_label.setBuddy(self.Religion_comboBox)
        self.Address_label.setBuddy(self.Address_lineEdit)
        self.contact_label.setBuddy(self.contact_lineEdit)
        self.illness_label.setBuddy(self.illness_textEdit)
        self.history_label.setBuddy(self.Past_illness_textEdit)
        self.thermal_label.setBuddy(self.thermal_lineEdit)
        self.thirst_label.setBuddy(self.thirst_lineEdit)
        self.tongue_label.setBuddy(self.tongue_lineEdit)
        self.appetite_label.setBuddy(self.appetite_lineEdit)
        self.craving_label.setBuddy(self.cravings_lineEdit)
        self.dislike_label.setBuddy(self.dislike_lineEdit)
        self.intolerance_label.setBuddy(self.intolerance_lineEdit)
        self.bathing_label.setBuddy(self.bathing_lineEdit)
        self.sweat_label.setBuddy(self.sweat_lineEdit)
        self.aleep_label.setBuddy(self.sleep_lineEdit)
        self.dreams_label.setBuddy(self.dreams_lineEdit)
        self.salivation_label.setBuddy(self.salivation_lineEdit)
        self.urine_label.setBuddy(self.urine_lineEdit)
        self.stool_label.setBuddy(self.stool_lineEdit)
        self.rectum_label.setBuddy(self.rectum_lineEdit)
        self.skin_label.setBuddy(self.skin_lineEdit)
        self.generalModalities_label.setBuddy(self.generalModalities_lineEdit)
        self.nailAnalysis_label.setBuddy(self.nailAnalysis_lineEdit)
        self.label_23.setBuddy(self.femaleOnly_textEdit)
        self.pregnancy_label.setBuddy(self.pregnancy_lineEdit)
        self.marriedFor_label.setBuddy(self.marriedFor_lineEdit)
        self.gravida_label.setBuddy(self.gravida_lineEdit)
        self.abortion_label.setBuddy(self.abortion_lineEdit)
        self.A_label.setBuddy(self.A_lineEdit)
        self.B_label.setBuddy(self.B_lineEdit)
        self.C_label.setBuddy(self.C_lineEdit)
        self.D_label.setBuddy(self.D_lineEdit)
        self.E_label.setBuddy(self.E_lineEdit)
        self.effectCompany_label.setBuddy(self.effectCompany_lineEdit)
        self.effectConsolation_label.setBuddy(self.effectConsolation_lineEdit)
        self.daSex_label.setBuddy(self.daSex_lineEdit)
        self.daSpecialsense_label.setBuddy(self.daSpecialSense_lineEdit)
        self.grief_label.setBuddy(self.grief_lineEdit)
        self.gesturesPostures_label.setBuddy(self.gesturesPostures_lineEdit)
        self.anxiety_label.setBuddy(self.anxiety_lineEdit)
        self.intellect_label.setBuddy(self.intellect_lineEdit)
        self.memory_label.setBuddy(self.memory_lineEdit)
        self.anger_label.setBuddy(self.anger_lineEdit)
        self.laughing_label.setBuddy(self.laughing_lineEdit)
        self.selfConfidence_label.setBuddy(self.selfConfidence_lineEdit)
        self.sharing_label.setBuddy(self.sharing_lineEdit)
        self.shock_label.setBuddy(self.shock_lineEdit)
        self.weeping_label.setBuddy(self.weeping_lineEdit)
        self.aggravation_label.setBuddy(self.aggravation_lineEdit)
        self.pastHistory_label.setBuddy(self.pastHistory_textEdit)
        self.fatherSide_label.setBuddy(self.fatherSide_lineEdit)
        self.motherSide_label.setBuddy(self.motherSide_lineEdit)
        self.physicalExamination_label.setBuddy(self.physicalExamination_textEdit)
        self.laboratoryInvestigation_label.setBuddy(self.laboratoryInvestigation_textEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scrollArea, self.name_lineEdit)
        QWidget.setTabOrder(self.name_lineEdit, self.male_radiobtn)
        QWidget.setTabOrder(self.male_radiobtn, self.female_radiobtn)
        QWidget.setTabOrder(self.female_radiobtn, self.age_lineEdit)
        QWidget.setTabOrder(self.age_lineEdit, self.job_comboBox)
        QWidget.setTabOrder(self.job_comboBox, self.Marriage_comboBox)
        QWidget.setTabOrder(self.Marriage_comboBox, self.Religion_comboBox)
        QWidget.setTabOrder(self.Religion_comboBox, self.Address_lineEdit)
        QWidget.setTabOrder(self.Address_lineEdit, self.contact_lineEdit)
        QWidget.setTabOrder(self.contact_lineEdit, self.illness_textEdit)
        QWidget.setTabOrder(self.illness_textEdit, self.Past_illness_textEdit)
        QWidget.setTabOrder(self.Past_illness_textEdit, self.thermal_lineEdit)
        QWidget.setTabOrder(self.thermal_lineEdit, self.thirst_lineEdit)
        QWidget.setTabOrder(self.thirst_lineEdit, self.tongue_lineEdit)
        QWidget.setTabOrder(self.tongue_lineEdit, self.appetite_lineEdit)
        QWidget.setTabOrder(self.appetite_lineEdit, self.cravings_lineEdit)
        QWidget.setTabOrder(self.cravings_lineEdit, self.dislike_lineEdit)
        QWidget.setTabOrder(self.dislike_lineEdit, self.intolerance_lineEdit)
        QWidget.setTabOrder(self.intolerance_lineEdit, self.aggravation_radiobtn)
        QWidget.setTabOrder(self.aggravation_radiobtn, self.amelioration_radiobtn)
        QWidget.setTabOrder(self.amelioration_radiobtn, self.bathing_lineEdit)
        QWidget.setTabOrder(self.bathing_lineEdit, self.sweat_lineEdit)
        QWidget.setTabOrder(self.sweat_lineEdit, self.sleep_lineEdit)
        QWidget.setTabOrder(self.sleep_lineEdit, self.dreams_lineEdit)
        QWidget.setTabOrder(self.dreams_lineEdit, self.salivation_lineEdit)
        QWidget.setTabOrder(self.salivation_lineEdit, self.urine_lineEdit)
        QWidget.setTabOrder(self.urine_lineEdit, self.stool_lineEdit)
        QWidget.setTabOrder(self.stool_lineEdit, self.rectum_lineEdit)
        QWidget.setTabOrder(self.rectum_lineEdit, self.skin_lineEdit)
        QWidget.setTabOrder(self.skin_lineEdit, self.anger_checkBox)
        QWidget.setTabOrder(self.anger_checkBox, self.injury_checkBox)
        QWidget.setTabOrder(self.injury_checkBox, self.emotions_checkBox)
        QWidget.setTabOrder(self.emotions_checkBox, self.excitement_checkBox)
        QWidget.setTabOrder(self.excitement_checkBox, self.fright_checkBox)
        QWidget.setTabOrder(self.fright_checkBox, self.grief_checkBox)
        QWidget.setTabOrder(self.grief_checkBox, self.disappointed_checkBox)
        QWidget.setTabOrder(self.disappointed_checkBox, self.mortification_checkBox)
        QWidget.setTabOrder(self.mortification_checkBox, self.anticipation_checkBox)
        QWidget.setTabOrder(self.anticipation_checkBox, self.badnews_checkBox)
        QWidget.setTabOrder(self.badnews_checkBox, self.abuseDrugs_checkBox)
        QWidget.setTabOrder(self.abuseDrugs_checkBox, self.bloodLose_checkBox)
        QWidget.setTabOrder(self.bloodLose_checkBox, self.love_checkBox)
        QWidget.setTabOrder(self.love_checkBox, self.joy_checkBox)
        QWidget.setTabOrder(self.joy_checkBox, self.generalModalities_lineEdit)
        QWidget.setTabOrder(self.generalModalities_lineEdit, self.nailAnalysis_lineEdit)
        QWidget.setTabOrder(self.nailAnalysis_lineEdit, self.femaleOnly_textEdit)
        QWidget.setTabOrder(self.femaleOnly_textEdit, self.pregnancy_lineEdit)
        QWidget.setTabOrder(self.pregnancy_lineEdit, self.marriedFor_lineEdit)
        QWidget.setTabOrder(self.marriedFor_lineEdit, self.gravida_lineEdit)
        QWidget.setTabOrder(self.gravida_lineEdit, self.abortion_lineEdit)
        QWidget.setTabOrder(self.abortion_lineEdit, self.A_lineEdit)
        QWidget.setTabOrder(self.A_lineEdit, self.B_lineEdit)
        QWidget.setTabOrder(self.B_lineEdit, self.C_lineEdit)
        QWidget.setTabOrder(self.C_lineEdit, self.D_lineEdit)
        QWidget.setTabOrder(self.D_lineEdit, self.E_lineEdit)
        QWidget.setTabOrder(self.E_lineEdit, self.effectCompany_lineEdit)
        QWidget.setTabOrder(self.effectCompany_lineEdit, self.effectConsolation_lineEdit)
        QWidget.setTabOrder(self.effectConsolation_lineEdit, self.daSex_lineEdit)
        QWidget.setTabOrder(self.daSex_lineEdit, self.daSpecialSense_lineEdit)
        QWidget.setTabOrder(self.daSpecialSense_lineEdit, self.grief_lineEdit)
        QWidget.setTabOrder(self.grief_lineEdit, self.gesturesPostures_lineEdit)
        QWidget.setTabOrder(self.gesturesPostures_lineEdit, self.anxiety_lineEdit)
        QWidget.setTabOrder(self.anxiety_lineEdit, self.intellect_lineEdit)
        QWidget.setTabOrder(self.intellect_lineEdit, self.memory_lineEdit)
        QWidget.setTabOrder(self.memory_lineEdit, self.anger_lineEdit)
        QWidget.setTabOrder(self.anger_lineEdit, self.yes_radioButton)
        QWidget.setTabOrder(self.yes_radioButton, self.no_radioButton)
        QWidget.setTabOrder(self.no_radioButton, self.yes2_radioButton)
        QWidget.setTabOrder(self.yes2_radioButton, self.no2_radioButton)
        QWidget.setTabOrder(self.no2_radioButton, self.laughing_lineEdit)
        QWidget.setTabOrder(self.laughing_lineEdit, self.selfConfidence_lineEdit)
        QWidget.setTabOrder(self.selfConfidence_lineEdit, self.sharing_lineEdit)
        QWidget.setTabOrder(self.sharing_lineEdit, self.shock_lineEdit)
        QWidget.setTabOrder(self.shock_lineEdit, self.weeping_lineEdit)
        QWidget.setTabOrder(self.weeping_lineEdit, self.slow_radioButton)
        QWidget.setTabOrder(self.slow_radioButton, self.hurry_radioButton)
        QWidget.setTabOrder(self.hurry_radioButton, self.aggravation_lineEdit)
        QWidget.setTabOrder(self.aggravation_lineEdit, self.pastHistory_textEdit)
        QWidget.setTabOrder(self.pastHistory_textEdit, self.fatherSide_lineEdit)
        QWidget.setTabOrder(self.fatherSide_lineEdit, self.motherSide_lineEdit)
        QWidget.setTabOrder(self.motherSide_lineEdit, self.physicalExamination_textEdit)
        QWidget.setTabOrder(self.physicalExamination_textEdit, self.laboratoryInvestigation_textEdit)
        QWidget.setTabOrder(self.laboratoryInvestigation_textEdit, self.observation_lineEdit)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionMaximize)
        self.menuSettings.addAction(self.actionFont_Size)
        self.menuSettings.addAction(self.actionFont_Family)
        self.menuSettings.addAction(self.actionFont_Color)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionBackground)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionPrescription.setText(QCoreApplication.translate("MainWindow", u"Prescription", None))
        self.actionInvestigation.setText(QCoreApplication.translate("MainWindow", u"Investigation", None))
        self.actionMinimize.setText(QCoreApplication.translate("MainWindow", u"Minimize", None))
        self.actionMaximize.setText(QCoreApplication.translate("MainWindow", u"Maximize", None))
        self.actionFont_Size.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.actionFont_Family.setText(QCoreApplication.translate("MainWindow", u"Font Family", None))
        self.actionFont_Color.setText(QCoreApplication.translate("MainWindow", u"Font Color", None))
        self.actionBackground.setText(QCoreApplication.translate("MainWindow", u"Background", None))
        self.header_label.setText(QCoreApplication.translate("MainWindow", u"GENERAL INFORMATION", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"Patient ID:", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Patient Name:", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.sex_label.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.male_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.female_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.age_label.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.job_label.setText(QCoreApplication.translate("MainWindow", u"Occupation:", None))
        self.job_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Student", None))
        self.job_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Teacher", None))
        self.job_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Farmer", None))
        self.job_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Businessman", None))
        self.job_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Worker", None))
        self.job_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Others", None))

        self.marriage_label.setText(QCoreApplication.translate("MainWindow", u"Marital Status:", None))
        self.Marriage_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Married", None))
        self.Marriage_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Unmarried", None))
        self.Marriage_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Divorced", None))
        self.Marriage_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Widow", None))

        self.Religion_label.setText(QCoreApplication.translate("MainWindow", u"Religion:", None))
        self.Religion_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Islam", None))
        self.Religion_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Hindu", None))
        self.Religion_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Christian", None))
        self.Religion_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Buddhism", None))
        self.Religion_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Others", None))

        self.Address_label.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.contact_label.setText(QCoreApplication.translate("MainWindow", u"Contact No:", None))
        self.illness_label.setText(QCoreApplication.translate("MainWindow", u"Patient's Complain (Detailed history of the present illness):", None))
        self.illness_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write Here ...", None))
        self.history_label.setText(QCoreApplication.translate("MainWindow", u"History of past illness (with treatment):", None))
        self.Past_illness_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write Here ...", None))
        self.header_label2.setText(QCoreApplication.translate("MainWindow", u"PHYSICAL SYMPTOMS", None))
        self.thermal_label.setText(QCoreApplication.translate("MainWindow", u"Thermal Reaction:", None))
        self.thirst_label.setText(QCoreApplication.translate("MainWindow", u"Thirst:", None))
        self.tongue_label.setText(QCoreApplication.translate("MainWindow", u"Tongue:", None))
        self.appetite_label.setText(QCoreApplication.translate("MainWindow", u"Appetite:", None))
        self.craving_label.setText(QCoreApplication.translate("MainWindow", u"Cravings or Liking of (Food & Drinks):", None))
        self.dislike_label.setText(QCoreApplication.translate("MainWindow", u"Aversion or Disliking (Food & Drinks):", None))
        self.intolerance_label.setText(QCoreApplication.translate("MainWindow", u"Food Allergies/ Intolarance/ Aggravation (Food & Drinks):", None))
        self.hunger_label.setText(QCoreApplication.translate("MainWindow", u"Hunger:", None))
        self.aggravation_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Aggravation", None))
        self.amelioration_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Amelioration", None))
        self.bathing_label.setText(QCoreApplication.translate("MainWindow", u"Bathing", None))
        self.sweat_label.setText(QCoreApplication.translate("MainWindow", u"Sweat/ Perspiration:", None))
        self.aleep_label.setText(QCoreApplication.translate("MainWindow", u"Sleep:", None))
        self.dreams_label.setText(QCoreApplication.translate("MainWindow", u"Dreams:", None))
        self.salivation_label.setText(QCoreApplication.translate("MainWindow", u"Salivation:", None))
        self.urine_label.setText(QCoreApplication.translate("MainWindow", u"Urine:", None))
        self.stool_label.setText(QCoreApplication.translate("MainWindow", u"Stool:", None))
        self.rectum_label.setText(QCoreApplication.translate("MainWindow", u"Rectum:", None))
        self.skin_label.setText(QCoreApplication.translate("MainWindow", u"Skin:", None))
        self.abuseDrugs_checkBox.setText(QCoreApplication.translate("MainWindow", u"Abuse Drugs", None))
        self.bloodLose_checkBox.setText(QCoreApplication.translate("MainWindow", u"Blood Lose", None))
        self.grief_checkBox.setText(QCoreApplication.translate("MainWindow", u"Grief", None))
        self.anger_checkBox.setText(QCoreApplication.translate("MainWindow", u"Anger", None))
        self.mortification_checkBox.setText(QCoreApplication.translate("MainWindow", u"Mortification", None))
        self.badnews_checkBox.setText(QCoreApplication.translate("MainWindow", u"Bad News", None))
        self.joy_checkBox.setText(QCoreApplication.translate("MainWindow", u"Joy", None))
        self.love_checkBox.setText(QCoreApplication.translate("MainWindow", u"Love", None))
        self.excitement_checkBox.setText(QCoreApplication.translate("MainWindow", u"Excitement", None))
        self.aliments_label.setText(QCoreApplication.translate("MainWindow", u"Aliments from:", None))
        self.injury_checkBox.setText(QCoreApplication.translate("MainWindow", u"Injury", None))
        self.fright_checkBox.setText(QCoreApplication.translate("MainWindow", u"fright", None))
        self.anticipation_checkBox.setText(QCoreApplication.translate("MainWindow", u"Anticipation", None))
        self.emotions_checkBox.setText(QCoreApplication.translate("MainWindow", u"Emotions", None))
        self.disappointed_checkBox.setText(QCoreApplication.translate("MainWindow", u"Disappointed", None))
        self.generalModalities_label.setText(QCoreApplication.translate("MainWindow", u"General Modalities:", None))
        self.nailAnalysis_label.setText(QCoreApplication.translate("MainWindow", u"Nail Analysis:", None))
        self.femaleOnly_label.setText(QCoreApplication.translate("MainWindow", u"For Female Only ", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"(Is sex desire Absent or Excessive or Others problem )", None))
        self.femaleOnly_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write detailed history ...", None))
        self.pregnancy_label.setText(QCoreApplication.translate("MainWindow", u"H/O Pregnancy:", None))
        self.obstetric_label.setText(QCoreApplication.translate("MainWindow", u"Obstetric History:", None))
        self.marriedFor_label.setText(QCoreApplication.translate("MainWindow", u"Married for", None))
        self.gravida_label.setText(QCoreApplication.translate("MainWindow", u"Gravida", None))
        self.abortion_label.setText(QCoreApplication.translate("MainWindow", u"Abortion", None))
        self.header_label3.setText(QCoreApplication.translate("MainWindow", u"MENTAL SYMPTOMS", None))
        self.will_label.setText(QCoreApplication.translate("MainWindow", u"Will:", None))
        self.will2_label.setText(QCoreApplication.translate("MainWindow", u"(It refers to that faculty of mind by which a person decides what to do)", None))
        self.A_label.setText(QCoreApplication.translate("MainWindow", u"A. Loves, hates & emotions:", None))
        self.B_label.setText(QCoreApplication.translate("MainWindow", u"B. Lasciviousness, revulsion to sex, sexual perversons:", None))
        self.C_label.setText(QCoreApplication.translate("MainWindow", u"C. Fears:", None))
        self.D_label.setText(QCoreApplication.translate("MainWindow", u"D. Temperament:", None))
        self.E_label.setText(QCoreApplication.translate("MainWindow", u"E. Nature & habits:", None))
        self.effectCompany_label.setText(QCoreApplication.translate("MainWindow", u"Effect of Company:", None))
        self.effectConsolation_label.setText(QCoreApplication.translate("MainWindow", u"Effect of Consolation:", None))
        self.daSex_label.setText(QCoreApplication.translate("MainWindow", u"D/A of sex:", None))
        self.daSpecialsense_label.setText(QCoreApplication.translate("MainWindow", u"D/A of special senses:", None))
        self.grief_label.setText(QCoreApplication.translate("MainWindow", u"Grief:", None))
        self.gesturesPostures_label.setText(QCoreApplication.translate("MainWindow", u"Various gestures & postures:", None))
        self.anxiety_label.setText(QCoreApplication.translate("MainWindow", u"Anxiety states:", None))
        self.intellect_label.setText(QCoreApplication.translate("MainWindow", u"Intellect/ Understanding:", None))
        self.memory_label.setText(QCoreApplication.translate("MainWindow", u"Memory:", None))
        self.anger_label.setText(QCoreApplication.translate("MainWindow", u"Anger:", None))
        self.avarice_label.setText(QCoreApplication.translate("MainWindow", u"Avarice:", None))
        self.yes_radioButton.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.no_radioButton.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.religiouos_label.setText(QCoreApplication.translate("MainWindow", u"Religious:", None))
        self.yes2_radioButton.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.no2_radioButton.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.dominating_label.setText(QCoreApplication.translate("MainWindow", u"Dominating:", None))
        self.laughing_label.setText(QCoreApplication.translate("MainWindow", u"Laughing:", None))
        self.selfConfidence_label.setText(QCoreApplication.translate("MainWindow", u"Self-confidence:", None))
        self.sentimental_label.setText(QCoreApplication.translate("MainWindow", u"Sentimental:", None))
        self.sharing_label.setText(QCoreApplication.translate("MainWindow", u"Sharing (His/her problem to others):", None))
        self.shock_label.setText(QCoreApplication.translate("MainWindow", u"Shock:", None))
        self.sympathetic_label.setText(QCoreApplication.translate("MainWindow", u"Sympathetic:", None))
        self.weeping_label.setText(QCoreApplication.translate("MainWindow", u"Weeping:", None))
        self.work_label.setText(QCoreApplication.translate("MainWindow", u"Work:", None))
        self.slow_radioButton.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.hurry_radioButton.setText(QCoreApplication.translate("MainWindow", u"Hurry", None))
        self.aggravation_label.setText(QCoreApplication.translate("MainWindow", u"Aggravation/ Amelioration:", None))
        self.pastHistory_label.setText(QCoreApplication.translate("MainWindow", u"Past History:", None))
        self.pastHistory_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write Here...", None))
        self.familyHistory_label.setText(QCoreApplication.translate("MainWindow", u"Family History:", None))
        self.fatherSide_label.setText(QCoreApplication.translate("MainWindow", u"Father Side:", None))
        self.motherSide_label.setText(QCoreApplication.translate("MainWindow", u"Mother Side:", None))
        self.observation_lineEdit.setText(QCoreApplication.translate("MainWindow", u"OBSERVATION & EXAMINATION", None))
        self.physicalExamination_label.setText(QCoreApplication.translate("MainWindow", u"Physical Examination:", None))
        self.physicalExamination_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write Here ...", None))
        self.laboratoryInvestigation_label.setText(QCoreApplication.translate("MainWindow", u"Laboratory Investigations:", None))
        self.laboratoryInvestigation_textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write Here ...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

