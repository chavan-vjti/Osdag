# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_preferences1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ShearDesignPreferences(object):
    def setupUi(self, ShearDesignPreferences):
        ShearDesignPreferences.setObjectName(_fromUtf8("ShearDesignPreferences"))
        ShearDesignPreferences.resize(822, 462)
        self.gridLayout_5 = QtGui.QGridLayout(ShearDesignPreferences)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.btn_save = QtGui.QPushButton(ShearDesignPreferences)
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.gridLayout_2.addWidget(self.btn_save, 0, 2, 1, 1)
        self.btn_defaults = QtGui.QPushButton(ShearDesignPreferences)
        self.btn_defaults.setObjectName(_fromUtf8("btn_defaults"))
        self.gridLayout_2.addWidget(self.btn_defaults, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 4, 1, 1)
        self.btn_close = QtGui.QPushButton(ShearDesignPreferences)
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.gridLayout_2.addWidget(self.btn_close, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(ShearDesignPreferences)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 5)
        self.line_4 = QtGui.QFrame(self.tab)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 1, 5, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.combo_boltHoleType = QtGui.QComboBox(self.tab)
        self.combo_boltHoleType.setFocusPolicy(QtCore.Qt.TabFocus)
        self.combo_boltHoleType.setObjectName(_fromUtf8("combo_boltHoleType"))
        self.combo_boltHoleType.addItem(_fromUtf8(""))
        self.combo_boltHoleType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.combo_boltHoleType, 2, 2, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setMinimumSize(QtCore.QSize(210, 320))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 2, 5, 5, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.txt_boltHoleClearance = QtGui.QLineEdit(self.tab)
        self.txt_boltHoleClearance.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_boltHoleClearance.setObjectName(_fromUtf8("txt_boltHoleClearance"))
        self.gridLayout.addWidget(self.txt_boltHoleClearance, 3, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)
        self.txt_boltFu = QtGui.QLineEdit(self.tab)
        self.txt_boltFu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_boltFu.setObjectName(_fromUtf8("txt_boltFu"))
        self.gridLayout.addWidget(self.txt_boltFu, 5, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 5, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 201, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 1, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_16 = QtGui.QLabel(self.tab_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_6.addWidget(self.label_16, 0, 0, 1, 1)
        self.line_8 = QtGui.QFrame(self.tab_2)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout_6.addWidget(self.line_8, 1, 0, 1, 3)
        self.label_22 = QtGui.QLabel(self.tab_2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_6.addWidget(self.label_22, 2, 0, 1, 1)
        self.combo_weldType = QtGui.QComboBox(self.tab_2)
        self.combo_weldType.setObjectName(_fromUtf8("combo_weldType"))
        self.combo_weldType.addItem(_fromUtf8(""))
        self.combo_weldType.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.combo_weldType, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(211, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 2, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_7.addWidget(self.label_17, 0, 0, 1, 1)
        self.line_5 = QtGui.QFrame(self.tab_2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_7.addWidget(self.line_5, 1, 0, 1, 1)
        self.textBrowser_weldDescription = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser_weldDescription.setMinimumSize(QtCore.QSize(210, 320))
        self.textBrowser_weldDescription.setObjectName(_fromUtf8("textBrowser_weldDescription"))
        self.gridLayout_7.addWidget(self.textBrowser_weldDescription, 2, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 1, 2, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 288, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_38 = QtGui.QLabel(self.tab_5)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_9.addWidget(self.label_38, 0, 0, 1, 1)
        self.line_11 = QtGui.QFrame(self.tab_5)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.gridLayout_9.addWidget(self.line_11, 1, 0, 1, 4)
        self.label_39 = QtGui.QLabel(self.tab_5)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_9.addWidget(self.label_39, 2, 0, 1, 1)
        self.combo_detailingEdgeType = QtGui.QComboBox(self.tab_5)
        self.combo_detailingEdgeType.setObjectName(_fromUtf8("combo_detailingEdgeType"))
        self.combo_detailingEdgeType.addItem(_fromUtf8(""))
        self.combo_detailingEdgeType.addItem(_fromUtf8(""))
        self.gridLayout_9.addWidget(self.combo_detailingEdgeType, 2, 1, 1, 2)
        self.label_29 = QtGui.QLabel(self.tab_5)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_9.addWidget(self.label_29, 3, 0, 1, 1)
        self.txt_detailingGap = QtGui.QLineEdit(self.tab_5)
        self.txt_detailingGap.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_detailingGap.setObjectName(_fromUtf8("txt_detailingGap"))
        self.gridLayout_9.addWidget(self.txt_detailingGap, 3, 1, 1, 1)
        self.label_36 = QtGui.QLabel(self.tab_5)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_9.addWidget(self.label_36, 3, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem5, 3, 3, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.line_6 = QtGui.QFrame(self.tab_5)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout_10.addWidget(self.line_6, 1, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.tab_5)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_10.addWidget(self.label_18, 0, 0, 1, 1)
        self.textBrowser_detailingDescription = QtGui.QTextBrowser(self.tab_5)
        self.textBrowser_detailingDescription.setMinimumSize(QtCore.QSize(210, 0))
        self.textBrowser_detailingDescription.setObjectName(_fromUtf8("textBrowser_detailingDescription"))
        self.gridLayout_10.addWidget(self.textBrowser_detailingDescription, 2, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 1, 2, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 255, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem6, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(ShearDesignPreferences)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.btn_close, QtCore.SIGNAL(_fromUtf8("clicked()")), ShearDesignPreferences.close)
        QtCore.QMetaObject.connectSlotsByName(ShearDesignPreferences)

    def retranslateUi(self, ShearDesignPreferences):
        ShearDesignPreferences.setWindowTitle(_translate("ShearDesignPreferences", "Dialog", None))
        self.btn_save.setText(_translate("ShearDesignPreferences", "Save", None))
        self.btn_defaults.setText(_translate("ShearDesignPreferences", "Defaults", None))
        self.btn_close.setText(_translate("ShearDesignPreferences", "Close", None))
        self.label_5.setText(_translate("ShearDesignPreferences", "Inputs", None))
        self.label_3.setText(_translate("ShearDesignPreferences", "Description", None))
        self.label.setText(_translate("ShearDesignPreferences", "Bolt hole type", None))
        self.combo_boltHoleType.setItemText(0, _translate("ShearDesignPreferences", "Standard", None))
        self.combo_boltHoleType.setItemText(1, _translate("ShearDesignPreferences", "Over-sized", None))
        self.textBrowser.setHtml(_translate("ShearDesignPreferences", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">IS 4000: 1992 - Annex C recommended slip factors:</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p>\n"
"<table border=\"0\" style=\" border-color:#a3a3a3; border-style:solid; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"0\">\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">Treatment of surface</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\';\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">Slip factor </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">Surface not treated</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">0.2</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">Surface blasted with shot or grit </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">with any loose rust removed, no pitting</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">0.5</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">and hot-dip galvanized</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">0.1</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">and spray-metallized with zinc (thickness 50-70 micro-m</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">0.25</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">and painted with ethyl-zinc silicate coat (thickness 30-80  micro-m)</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">0.30</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">and painted with alkali-zinc silicate coat (thickness 60-80  micro-m</span></p></td>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">0.30</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">and spray metallized with aluminium (thickness &gt; 50  micro-m)</span></p></td>\n"
"<td style=\" vertical-align:top; padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">0.5</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"> </span></p></td></tr></table></body></html>", None))
        self.label_2.setText(_translate("ShearDesignPreferences", "Bolt hole clearance", None))
        self.txt_boltHoleClearance.setText(_translate("ShearDesignPreferences", "2", None))
        self.label_9.setText(_translate("ShearDesignPreferences", "mm", None))
        self.label_4.setText(_translate("ShearDesignPreferences", "Material grade overwrite", None))
        self.label_8.setText(_translate("ShearDesignPreferences", "Fu", None))
        self.txt_boltFu.setText(_translate("ShearDesignPreferences", "800", None))
        self.label_11.setText(_translate("ShearDesignPreferences", "MPa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ShearDesignPreferences", "Bolt", None))
        self.label_16.setText(_translate("ShearDesignPreferences", "Inputs", None))
        self.label_22.setText(_translate("ShearDesignPreferences", "Type of weld", None))
        self.combo_weldType.setItemText(0, _translate("ShearDesignPreferences", "Shop weld", None))
        self.combo_weldType.setItemText(1, _translate("ShearDesignPreferences", "Field weld", None))
        self.label_17.setText(_translate("ShearDesignPreferences", "Description", None))
        self.textBrowser_weldDescription.setHtml(_translate("ShearDesignPreferences", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Shop weld takes a material safety factor of 1.25</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Field weld takes a material safety factor of 1.5</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ShearDesignPreferences", "Weld", None))
        self.label_38.setText(_translate("ShearDesignPreferences", "Inputs", None))
        self.label_39.setText(_translate("ShearDesignPreferences", "Type of edges", None))
        self.combo_detailingEdgeType.setItemText(0, _translate("ShearDesignPreferences", "a - Sheared or hand flame cut", None))
        self.combo_detailingEdgeType.setItemText(1, _translate("ShearDesignPreferences", "b - Rolled, machine-flame cut, sawn and planed", None))
        self.label_29.setText(_translate("ShearDesignPreferences", "Gap between beam & support", None))
        self.txt_detailingGap.setText(_translate("ShearDesignPreferences", "10", None))
        self.label_36.setText(_translate("ShearDesignPreferences", "mm", None))
        self.label_18.setText(_translate("ShearDesignPreferences", "Description", None))
        self.textBrowser_detailingDescription.setHtml(_translate("ShearDesignPreferences", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt; vertical-align:middle;\">The minimum edge and end distances from the centre of any hole to the nearest edge of a plate shall not be less than </span><span style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:600; vertical-align:middle;\">1.7 </span><span style=\" font-family:\'Calibri\'; font-size:10pt; vertical-align:middle;\">times the hole diameter in case of [</span><span style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:600; vertical-align:middle;\">a - sheared or hand flame cut edges</span><span style=\" font-family:\'Calibri\'; font-size:10pt; vertical-align:middle;\">] and </span><span style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:600; vertical-align:middle;\">1.5 </span><span style=\" font-family:\'Calibri\'; font-size:10pt; vertical-align:middle;\">times the hole diameter in case of [</span><span style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:600; vertical-align:middle;\">b - Rolled, machine-flame cut, sawn and planed edges</span><span style=\" font-family:\'Calibri\'; font-size:10pt; vertical-align:middle;\">] (IS 800 - Cl. 10.2.4.2)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri\'; font-size:10pt; vertical-align:middle;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10pt;\">This gap should include the tolerance value of 5 mm. So if the assumed clearance is 5 mm, then the gap should be = 10 mm ( = 5 mm {clearance} + 5 mm {tolerance} )</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("ShearDesignPreferences", "Detailing", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("ShearDesignPreferences", "Design", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ShearDesignPreferences = QtGui.QDialog()
    ui = Ui_ShearDesignPreferences()
    ui.setupUi(ShearDesignPreferences)
    ShearDesignPreferences.show()
    sys.exit(app.exec_())
