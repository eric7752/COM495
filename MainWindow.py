from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        ####
        self.rounds = 150
        self.consumers = 100
        self.producers = 100
        self.is_delta = False
        self.delta = 0.1
        self.plots = []
        self.normal_dist = False
        self.ran = False
        ####
        Dialog.setObjectName("Dialog")
        Dialog.resize(445, 325)
        Dialog.setFixedWidth(445)
        Dialog.setFixedHeight(325)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(260, 10, 160, 200))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 100, 15))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 130, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 80, 120, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 110, 140, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 140, 120, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 170, 130, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 220, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(70, 30, 130, 22))
        self.horizontalSlider_2.setStyleSheet("")
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 75, 130, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(70, 120, 130, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")

        ####
        self.horizontalSlider_2.setMinimum(25)
        self.horizontalSlider_2.setMaximum(500)
        self.horizontalSlider_3.setMinimum(10)
        self.horizontalSlider_3.setMaximum(200)
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(200)
        ####

        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 32, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 75, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(70, 55, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(70, 100, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(70, 145, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(185, 55, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(185, 100, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(185, 145, 47, 13))
        self.label_11.setObjectName("label_11")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 180, 221, 105))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 30, 151, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 30, 16))
        self.label_4.setObjectName("label_4")

        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(60, 85, 47, 13))
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(175, 85, 47, 13))
        self.label_13.setObjectName("label_13")

        self.horizontalSlider_4 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(60, 60, 131, 22))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")

        #####
        self.horizontalSlider_4.setMinimum(0)
        self.horizontalSlider_4.setMaximum(100)
        ####

        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(120, 290, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 292, 101, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(260, 220, 161, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 290, 75, 23))
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.progressBar.raise_()
        self.pushButton.raise_()
        self.label_5.raise_()
        self.groupBox_4.raise_()
        self.pushButton_2.raise_()

        ####
        self.label_5.hide()
        self.progressBar.hide()
        ####

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(lambda: Dialog.close())
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(lambda: Dialog.close())

    def run(self):
        self.ran = True
        self.rounds = self.horizontalSlider_2.value()
        self.consumers = self.horizontalSlider.value()
        self.producers = self.horizontalSlider_3.value()
        self.delta = self.horizontalSlider_4.value() / 100
        self.is_delta = self.checkBox_7.isChecked()

        check_boxes = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5, self.checkBox_6]
        for i in range(len(check_boxes)):
            if check_boxes[i].isChecked():
                if i + 1 not in self.plots:
                    self.plots.append(i + 1)

        print(self.plots)

        if self.comboBox.currentText() == "Normal Distribution":
            self.normal_dist = True
        else:
            self.normal_dist = False

        self.label_5.show()
        self.progressBar.setValue(0)
        self.progressBar.show()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Economic Market Simulator"))
        self.groupBox.setTitle(_translate("Dialog", "Choose Plots to Display"))
        self.checkBox.setText(_translate("Dialog", "Summary Plot"))
        self.checkBox_2.setText(_translate("Dialog", "Initial Supply/Demand"))
        self.checkBox_3.setText(_translate("Dialog", "Final Supply/Demand"))
        self.checkBox_4.setText(_translate("Dialog", "Transaction Price Boxplot"))
        self.checkBox_5.setText(_translate("Dialog", "Surplus Plots"))
        self.checkBox_6.setText(_translate("Dialog", "Producer Revenue"))
        self.groupBox_2.setTitle(_translate("Dialog", "Options"))
        self.label.setText(_translate("Dialog", "Rounds"))
        self.label_2.setText(_translate("Dialog", "Consumers"))
        self.label_3.setText(_translate("Dialog", "Producers"))
        self.label_6.setText(_translate("Dialog", "25"))
        self.label_7.setText(_translate("Dialog", "10"))
        self.label_8.setText(_translate("Dialog", "10"))
        self.label_9.setText(_translate("Dialog", "500"))
        self.label_10.setText(_translate("Dialog", "200"))
        self.label_11.setText(_translate("Dialog", "200"))
        self.label_12.setText(_translate("Dialog", "0.0"))
        self.label_13.setText(_translate("Dialog", "1.0"))
        self.groupBox_3.setTitle(_translate("Dialog", "Delta Scaling"))
        self.checkBox_7.setText(_translate("Dialog", "Enable Delta Scaling"))
        self.label_4.setText(_translate("Dialog", "Delta"))
        self.pushButton.setText(_translate("Dialog", "Quit"))
        self.label_5.setText(_translate("Dialog", "Running Simulation:"))
        self.groupBox_4.setTitle(_translate("Dialog", "WTA/WTP Distribution"))
        self.comboBox.setItemText(0, _translate("Dialog", "Uniform Distribution"))
        self.comboBox.setItemText(1, _translate("Dialog", "Normal Distribution"))
        self.pushButton_2.setText(_translate("Dialog", "Run"))
