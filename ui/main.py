# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(834, 688)
        MainWindow.setMinimumSize(QtCore.QSize(834, 688))
        MainWindow.setMaximumSize(QtCore.QSize(834, 688))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 60, 391, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_solo_rank = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_solo_rank.setObjectName("label_solo_rank")
        self.gridLayout.addWidget(self.label_solo_rank, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_uuid = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_uuid.setObjectName("label_uuid")
        self.gridLayout.addWidget(self.label_uuid, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_id = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_id.setObjectName("label_id")
        self.gridLayout.addWidget(self.label_id, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_flex_rank = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_flex_rank.setObjectName("label_flex_rank")
        self.gridLayout.addWidget(self.label_flex_rank, 3, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(500, 600, 304, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_status = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.horizontalLayout.addWidget(self.label_status)
        self.label_icon = QtWidgets.QLabel(self.centralwidget)
        self.label_icon.setGeometry(QtCore.QRect(590, 40, 200, 200))
        self.label_icon.setText("")
        self.label_icon.setObjectName("label_icon")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_solo_rank.setText(_translate("MainWindow", "-"))
        self.label_3.setText(_translate("MainWindow", "单双排:"))
        self.label_uuid.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "用户名:"))
        self.label_id.setText(_translate("MainWindow", "-"))
        self.label_2.setText(_translate("MainWindow", "puuid:"))
        self.label_5.setText(_translate("MainWindow", "灵活组排:"))
        self.label_flex_rank.setText(_translate("MainWindow", "-"))
        self.label_4.setText(_translate("MainWindow", "当前状态："))
        self.label_status.setText(_translate("MainWindow", "未检测到客户端！"))
