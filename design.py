# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.flashCardPage = QtWidgets.QTabWidget(self.centralwidget)
        self.flashCardPage.setObjectName("flashCardPage")
        self.dashTab = QtWidgets.QWidget()
        self.dashTab.setObjectName("dashTab")
        self.scheduleVLayout = QtWidgets.QVBoxLayout(self.dashTab)
        self.scheduleVLayout.setObjectName("scheduleVLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.dashTab)
        self.stackedWidget.setObjectName("stackedWidget")
        self.dashPage = QtWidgets.QWidget()
        self.dashPage.setObjectName("dashPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dashPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scheduleLabel = QtWidgets.QLabel(self.dashPage)
        self.scheduleLabel.setObjectName("scheduleLabel")
        self.verticalLayout_2.addWidget(self.scheduleLabel)
        self.dayChooserHLayout = QtWidgets.QHBoxLayout()
        self.dayChooserHLayout.setObjectName("dayChooserHLayout")
        self.monB = QtWidgets.QPushButton(self.dashPage)
        self.monB.setObjectName("monB")
        self.dayChooserHLayout.addWidget(self.monB)
        self.tueB = QtWidgets.QPushButton(self.dashPage)
        self.tueB.setObjectName("tueB")
        self.dayChooserHLayout.addWidget(self.tueB)
        self.wedB = QtWidgets.QPushButton(self.dashPage)
        self.wedB.setObjectName("wedB")
        self.dayChooserHLayout.addWidget(self.wedB)
        self.thuB = QtWidgets.QPushButton(self.dashPage)
        self.thuB.setObjectName("thuB")
        self.dayChooserHLayout.addWidget(self.thuB)
        self.friB = QtWidgets.QPushButton(self.dashPage)
        self.friB.setObjectName("friB")
        self.dayChooserHLayout.addWidget(self.friB)
        self.satB = QtWidgets.QPushButton(self.dashPage)
        self.satB.setObjectName("satB")
        self.dayChooserHLayout.addWidget(self.satB)
        self.sunB = QtWidgets.QPushButton(self.dashPage)
        self.sunB.setObjectName("sunB")
        self.dayChooserHLayout.addWidget(self.sunB)
        self.verticalLayout_2.addLayout(self.dayChooserHLayout)
        self.addCoursesB = QtWidgets.QPushButton(self.dashPage)
        self.addCoursesB.setObjectName("addCoursesB")
        self.verticalLayout_2.addWidget(self.addCoursesB)
        self.stackedWidget.addWidget(self.dashPage)
        self.generationPage = QtWidgets.QWidget()
        self.generationPage.setObjectName("generationPage")
        self.genPageVLayout = QtWidgets.QVBoxLayout(self.generationPage)
        self.genPageVLayout.setObjectName("genPageVLayout")
        self.generatorVLayout = QtWidgets.QVBoxLayout()
        self.generatorVLayout.setObjectName("generatorVLayout")
        self.courseResultScrollArea = QtWidgets.QScrollArea(self.generationPage)
        self.courseResultScrollArea.setWidgetResizable(True)
        self.courseResultScrollArea.setObjectName("courseResultScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.courseResultScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.generatorVLayout.addWidget(self.courseResultScrollArea)
        self.genPageVLayout.addLayout(self.generatorVLayout)
        self.courseSearchHLayout = QtWidgets.QHBoxLayout()
        self.courseSearchHLayout.setObjectName("courseSearchHLayout")
        self.courseSearch = QtWidgets.QLineEdit(self.generationPage)
        self.courseSearch.setObjectName("courseSearch")
        self.courseSearchHLayout.addWidget(self.courseSearch)
        self.searchButton = QtWidgets.QPushButton(self.generationPage)
        self.searchButton.setObjectName("searchButton")
        self.courseSearchHLayout.addWidget(self.searchButton)
        self.genPageVLayout.addLayout(self.courseSearchHLayout)
        self.scheduleEditB = QtWidgets.QPushButton(self.generationPage)
        self.scheduleEditB.setObjectName("scheduleEditB")
        self.genPageVLayout.addWidget(self.scheduleEditB)
        self.dashboardB = QtWidgets.QPushButton(self.generationPage)
        self.dashboardB.setObjectName("dashboardB")
        self.genPageVLayout.addWidget(self.dashboardB)
        self.stackedWidget.addWidget(self.generationPage)
        self.scheduleVLayout.addWidget(self.stackedWidget)
        self.flashCardPage.addTab(self.dashTab, "")
        self.calTab = QtWidgets.QWidget()
        self.calTab.setObjectName("calTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.calTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.calTab)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_6.addWidget(self.calendarWidget)
        self.scrollArea = QtWidgets.QScrollArea(self.calTab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 98, 35))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.todoCalendarLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.todoCalendarLabel.setObjectName("todoCalendarLabel")
        self.verticalLayout_5.addWidget(self.todoCalendarLabel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.calEditB = QtWidgets.QPushButton(self.calTab)
        self.calEditB.setObjectName("calEditB")
        self.verticalLayout_6.addWidget(self.calEditB)
        self.flashCardPage.addTab(self.calTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cardLabel = QtWidgets.QLabel(self.tab)
        self.cardLabel.setObjectName("cardLabel")
        self.verticalLayout_3.addWidget(self.cardLabel)
        self.navigationHLayout = QtWidgets.QHBoxLayout()
        self.navigationHLayout.setObjectName("navigationHLayout")
        self.leftCardB = QtWidgets.QPushButton(self.tab)
        self.leftCardB.setObjectName("leftCardB")
        self.navigationHLayout.addWidget(self.leftCardB)
        self.flipCardB = QtWidgets.QPushButton(self.tab)
        self.flipCardB.setObjectName("flipCardB")
        self.navigationHLayout.addWidget(self.flipCardB)
        self.shuffleDeckB = QtWidgets.QPushButton(self.tab)
        self.shuffleDeckB.setObjectName("shuffleDeckB")
        self.navigationHLayout.addWidget(self.shuffleDeckB)
        self.rightCardB = QtWidgets.QPushButton(self.tab)
        self.rightCardB.setObjectName("rightCardB")
        self.navigationHLayout.addWidget(self.rightCardB)
        self.verticalLayout_3.addLayout(self.navigationHLayout)
        self.flashCardEditB = QtWidgets.QPushButton(self.tab)
        self.flashCardEditB.setObjectName("flashCardEditB")
        self.verticalLayout_3.addWidget(self.flashCardEditB)
        self.flashCardPage.addTab(self.tab, "")
        self.integralCalcPage = QtWidgets.QWidget()
        self.integralCalcPage.setObjectName("integralCalcPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.integralCalcPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.basicFormLabel = QtWidgets.QLabel(self.integralCalcPage)
        self.basicFormLabel.setObjectName("basicFormLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.basicFormLabel)
        self.basicFormComboBox = QtWidgets.QComboBox(self.integralCalcPage)
        self.basicFormComboBox.setObjectName("basicFormComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.basicFormComboBox)
        self.coefficientLabel = QtWidgets.QLabel(self.integralCalcPage)
        self.coefficientLabel.setObjectName("coefficientLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.coefficientLabel)
        self.integralLineEdit = QtWidgets.QLineEdit(self.integralCalcPage)
        self.integralLineEdit.setObjectName("integralLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.integralLineEdit)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.calcB = QtWidgets.QPushButton(self.integralCalcPage)
        self.calcB.setObjectName("calcB")
        self.verticalLayout_4.addWidget(self.calcB)
        self.answerLabel = QtWidgets.QLabel(self.integralCalcPage)
        self.answerLabel.setText("")
        self.answerLabel.setObjectName("answerLabel")
        self.verticalLayout_4.addWidget(self.answerLabel)
        self.flashCardPage.addTab(self.integralCalcPage, "")
        self.verticalLayout.addWidget(self.flashCardPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.flashCardPage.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scheduleLabel.setText(_translate("MainWindow", "TextLabel"))
        self.monB.setText(_translate("MainWindow", "Monday"))
        self.tueB.setText(_translate("MainWindow", "Tuesday"))
        self.wedB.setText(_translate("MainWindow", "Wednesday"))
        self.thuB.setText(_translate("MainWindow", "Thursday"))
        self.friB.setText(_translate("MainWindow", "Friday"))
        self.satB.setText(_translate("MainWindow", "Saturday"))
        self.sunB.setText(_translate("MainWindow", "Sunday"))
        self.addCoursesB.setText(_translate("MainWindow", "Go to Add Courses"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.scheduleEditB.setText(_translate("MainWindow", "Edit Schedule"))
        self.dashboardB.setText(_translate("MainWindow", "Return to Dashboard"))
        self.flashCardPage.setTabText(self.flashCardPage.indexOf(self.dashTab), _translate("MainWindow", "Dashboard"))
        self.todoCalendarLabel.setText(_translate("MainWindow", "TODO:"))
        self.calEditB.setText(_translate("MainWindow", "Edit Calendar TODO"))
        self.flashCardPage.setTabText(self.flashCardPage.indexOf(self.calTab), _translate("MainWindow", "Calendar"))
        self.cardLabel.setText(_translate("MainWindow", "TextLabel"))
        self.leftCardB.setText(_translate("MainWindow", "←"))
        self.flipCardB.setText(_translate("MainWindow", "Flip Card"))
        self.shuffleDeckB.setText(_translate("MainWindow", "Shuffle Deck"))
        self.rightCardB.setText(_translate("MainWindow", "→"))
        self.flashCardEditB.setText(_translate("MainWindow", "Edit Flash Card Deck"))
        self.flashCardPage.setTabText(self.flashCardPage.indexOf(self.tab), _translate("MainWindow", "Flash Cards"))
        self.basicFormLabel.setText(_translate("MainWindow", "Please Choose a Basic Form: "))
        self.coefficientLabel.setText(_translate("MainWindow", "Type down the coefficient of x:"))
        self.calcB.setText(_translate("MainWindow", "Calculate Integral"))
        self.flashCardPage.setTabText(self.flashCardPage.indexOf(self.integralCalcPage), _translate("MainWindow", "Integral Calculator"))
