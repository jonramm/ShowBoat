# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\jrgbo\Documents\repos\ShowBoat\showboat.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1223, 809)
        mainWindow.setStyleSheet("background-color: rgb(221, 255, 220);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setMovable(False)
        self.tabs.setObjectName("tabs")
        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setObjectName("homeTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.homeTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.homeTab)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(200, 47, 101);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.homeTab)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(94, 94, 94);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.bandPhotoLabel = QtWidgets.QLabel(self.homeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bandPhotoLabel.sizePolicy().hasHeightForWidth())
        self.bandPhotoLabel.setSizePolicy(sizePolicy)
        self.bandPhotoLabel.setMinimumSize(QtCore.QSize(423, 423))
        self.bandPhotoLabel.setMaximumSize(QtCore.QSize(460, 460))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        self.bandPhotoLabel.setFont(font)
        self.bandPhotoLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;\n"
"\n"
"margin-left: .5em;\n"
"margin-right: .5em;\n"
"")
        self.bandPhotoLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bandPhotoLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bandPhotoLabel.setLineWidth(3)
        self.bandPhotoLabel.setText("")
        self.bandPhotoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bandPhotoLabel.setObjectName("bandPhotoLabel")
        self.horizontalLayout_3.addWidget(self.bandPhotoLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bandInfoNameLabel = QtWidgets.QLabel(self.homeTab)
        self.bandInfoNameLabel.setMinimumSize(QtCore.QSize(0, 40))
        self.bandInfoNameLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bandInfoNameLabel.setFont(font)
        self.bandInfoNameLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.bandInfoNameLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bandInfoNameLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bandInfoNameLabel.setLineWidth(3)
        self.bandInfoNameLabel.setText("")
        self.bandInfoNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bandInfoNameLabel.setObjectName("bandInfoNameLabel")
        self.horizontalLayout_2.addWidget(self.bandInfoNameLabel)
        self.bandInfoWebsiteLabel = QtWidgets.QLabel(self.homeTab)
        self.bandInfoWebsiteLabel.setMinimumSize(QtCore.QSize(0, 40))
        self.bandInfoWebsiteLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bandInfoWebsiteLabel.setFont(font)
        self.bandInfoWebsiteLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.bandInfoWebsiteLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bandInfoWebsiteLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bandInfoWebsiteLabel.setLineWidth(3)
        self.bandInfoWebsiteLabel.setText("")
        self.bandInfoWebsiteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bandInfoWebsiteLabel.setOpenExternalLinks(True)
        self.bandInfoWebsiteLabel.setObjectName("bandInfoWebsiteLabel")
        self.horizontalLayout_2.addWidget(self.bandInfoWebsiteLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.bandBioHeader_2 = QtWidgets.QLabel(self.homeTab)
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(36)
        self.bandBioHeader_2.setFont(font)
        self.bandBioHeader_2.setStyleSheet("color: rgb(198, 140, 41);\n"
"\n"
"border-bottom: 3px solid rgb(198, 140, 41);\n"
"\n"
"margin-left: 5em;\n"
"margin-right: 5em;\n"
"\n"
"font-size: 2em;\n"
"")
        self.bandBioHeader_2.setAlignment(QtCore.Qt.AlignCenter)
        self.bandBioHeader_2.setObjectName("bandBioHeader_2")
        self.horizontalLayout_4.addWidget(self.bandBioHeader_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bandSearchLineEdit = QtWidgets.QLineEdit(self.homeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bandSearchLineEdit.sizePolicy().hasHeightForWidth())
        self.bandSearchLineEdit.setSizePolicy(sizePolicy)
        self.bandSearchLineEdit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bandSearchLineEdit.setFont(font)
        self.bandSearchLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"margin-top: .5em;\n"
"margin-bottom: .5em;\n"
"margin-left: 2em;\n"
"margin-right: 2em;")
        self.bandSearchLineEdit.setObjectName("bandSearchLineEdit")
        self.horizontalLayout_5.addWidget(self.bandSearchLineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lastSearchButton = QtWidgets.QPushButton(self.homeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastSearchButton.sizePolicy().hasHeightForWidth())
        self.lastSearchButton.setSizePolicy(sizePolicy)
        self.lastSearchButton.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.lastSearchButton.setFont(font)
        self.lastSearchButton.setStyleSheet("background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);\n"
"margin-top: 1em;\n"
"\n"
"")
        self.lastSearchButton.setCheckable(False)
        self.lastSearchButton.setObjectName("lastSearchButton")
        self.horizontalLayout_6.addWidget(self.lastSearchButton)
        self.searchButton = QtWidgets.QPushButton(self.homeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);\n"
"margin-top: 1em;\n"
"")
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_6.addWidget(self.searchButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.bandBioHeader = QtWidgets.QLabel(self.homeTab)
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(20)
        self.bandBioHeader.setFont(font)
        self.bandBioHeader.setStyleSheet("color: rgb(198, 140, 41);\n"
"\n"
"border-bottom: 3px solid rgb(198, 140, 41);\n"
"\n"
"margin-left: 5em;\n"
"margin-right: 5em;")
        self.bandBioHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.bandBioHeader.setObjectName("bandBioHeader")
        self.horizontalLayout_7.addWidget(self.bandBioHeader)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.homeBioPlainTextEdit = QtWidgets.QPlainTextEdit(self.homeTab)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.homeBioPlainTextEdit.setFont(font)
        self.homeBioPlainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"margin-top: .5em;\n"
"margin-bottom: .5em;")
        self.homeBioPlainTextEdit.setReadOnly(True)
        self.homeBioPlainTextEdit.setObjectName("homeBioPlainTextEdit")
        self.verticalLayout_3.addWidget(self.homeBioPlainTextEdit)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\jrgbo\\Documents\\repos\\ShowBoat\\../../../../Pictures/IconImages/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs.addTab(self.homeTab, icon, "")
        self.tourDatesTab = QtWidgets.QWidget()
        self.tourDatesTab.setObjectName("tourDatesTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tourDatesTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.showsHeaderLabel = QtWidgets.QLabel(self.tourDatesTab)
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(18)
        self.showsHeaderLabel.setFont(font)
        self.showsHeaderLabel.setStyleSheet("color: rgb(198, 140, 41);")
        self.showsHeaderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.showsHeaderLabel.setObjectName("showsHeaderLabel")
        self.horizontalLayout_10.addWidget(self.showsHeaderLabel)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.showsTableWidget = QtWidgets.QTableWidget(self.tourDatesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showsTableWidget.sizePolicy().hasHeightForWidth())
        self.showsTableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.showsTableWidget.setFont(font)
        self.showsTableWidget.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.showsTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.showsTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.showsTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.showsTableWidget.setObjectName("showsTableWidget")
        self.showsTableWidget.setColumnCount(4)
        self.showsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.showsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.showsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.showsTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.showsTableWidget.setHorizontalHeaderItem(3, item)
        self.showsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.showsTableWidget)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.artistTourLabel = QtWidgets.QLabel(self.tourDatesTab)
        self.artistTourLabel.setMinimumSize(QtCore.QSize(800, 0))
        self.artistTourLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.artistTourLabel.setFont(font)
        self.artistTourLabel.setStyleSheet("")
        self.artistTourLabel.setText("")
        self.artistTourLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.artistTourLabel.setObjectName("artistTourLabel")
        self.horizontalLayout_9.addWidget(self.artistTourLabel)
        spacerItem8 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.label_3 = QtWidgets.QLabel(self.tourDatesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(180, 80))
        self.label_3.setMaximumSize(QtCore.QSize(180, 80))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\Users\\jrgbo\\Documents\\repos\\ShowBoat\\powered-by-songkick-pink.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        spacerItem9 = QtWidgets.QSpacerItem(60, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.tabs.addTab(self.tourDatesTab, "")
        self.mapTab = QtWidgets.QWidget()
        self.mapTab.setObjectName("mapTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.mapTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.mapMapHeaderLabel = QtWidgets.QLabel(self.mapTab)
        self.mapMapHeaderLabel.setMaximumSize(QtCore.QSize(16777215, 74))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.mapMapHeaderLabel.setFont(font)
        self.mapMapHeaderLabel.setStyleSheet("color: rgb(198, 140, 41);")
        self.mapMapHeaderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mapMapHeaderLabel.setObjectName("mapMapHeaderLabel")
        self.verticalLayout_7.addWidget(self.mapMapHeaderLabel)
        self.mapMapContainer = QtWebEngineWidgets.QWebEngineView(self.mapTab)
        self.mapMapContainer.setMinimumSize(QtCore.QSize(0, 590))
        self.mapMapContainer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.mapMapContainer.setObjectName("mapMapContainer")
        self.verticalLayout_7.addWidget(self.mapMapContainer)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.mapMapHeaderLabel_2 = QtWidgets.QLabel(self.mapTab)
        self.mapMapHeaderLabel_2.setMinimumSize(QtCore.QSize(0, 60))
        self.mapMapHeaderLabel_2.setMaximumSize(QtCore.QSize(16777215, 74))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.mapMapHeaderLabel_2.setFont(font)
        self.mapMapHeaderLabel_2.setStyleSheet("color: rgb(198, 140, 41);")
        self.mapMapHeaderLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.mapMapHeaderLabel_2.setObjectName("mapMapHeaderLabel_2")
        self.horizontalLayout_11.addWidget(self.mapMapHeaderLabel_2)
        self.citySearchButton = QtWidgets.QPushButton(self.mapTab)
        self.citySearchButton.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.citySearchButton.setFont(font)
        self.citySearchButton.setStyleSheet("background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);")
        self.citySearchButton.setObjectName("citySearchButton")
        self.horizontalLayout_11.addWidget(self.citySearchButton)
        self.citySearchInput = QtWidgets.QLineEdit(self.mapTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.citySearchInput.sizePolicy().hasHeightForWidth())
        self.citySearchInput.setSizePolicy(sizePolicy)
        self.citySearchInput.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.citySearchInput.setFont(font)
        self.citySearchInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.citySearchInput.setObjectName("citySearchInput")
        self.horizontalLayout_11.addWidget(self.citySearchInput)
        self.clearCityButton = QtWidgets.QPushButton(self.mapTab)
        self.clearCityButton.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.clearCityButton.setFont(font)
        self.clearCityButton.setStyleSheet("background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);")
        self.clearCityButton.setObjectName("clearCityButton")
        self.horizontalLayout_11.addWidget(self.clearCityButton)
        self.miles50Radio = QtWidgets.QRadioButton(self.mapTab)
        self.miles50Radio.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(10)
        self.miles50Radio.setFont(font)
        self.miles50Radio.setChecked(True)
        self.miles50Radio.setObjectName("miles50Radio")
        self.horizontalLayout_11.addWidget(self.miles50Radio)
        self.miles100Radio = QtWidgets.QRadioButton(self.mapTab)
        self.miles100Radio.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(10)
        self.miles100Radio.setFont(font)
        self.miles100Radio.setObjectName("miles100Radio")
        self.horizontalLayout_11.addWidget(self.miles100Radio)
        self.miles250Radio = QtWidgets.QRadioButton(self.mapTab)
        self.miles250Radio.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(10)
        self.miles250Radio.setFont(font)
        self.miles250Radio.setObjectName("miles250Radio")
        self.horizontalLayout_11.addWidget(self.miles250Radio)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.gridLayout_5.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.tabs.addTab(self.mapTab, "")
        self.videoTab = QtWidgets.QWidget()
        self.videoTab.setObjectName("videoTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.videoTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.setSpacing(40)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.video2 = QtWebEngineWidgets.QWebEngineView(self.videoTab)
        self.video2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.video2.setObjectName("video2")
        self.gridLayout_4.addWidget(self.video2, 1, 0, 1, 1)
        self.video0 = QtWebEngineWidgets.QWebEngineView(self.videoTab)
        self.video0.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.video0.setObjectName("video0")
        self.gridLayout_4.addWidget(self.video0, 0, 0, 1, 1)
        self.video1 = QtWebEngineWidgets.QWebEngineView(self.videoTab)
        self.video1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.video1.setObjectName("video1")
        self.gridLayout_4.addWidget(self.video1, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.videoTab)
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(198, 140, 41);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonPopular = QtWidgets.QRadioButton(self.videoTab)
        self.radioButtonPopular.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonPopular.setFont(font)
        self.radioButtonPopular.setChecked(True)
        self.radioButtonPopular.setObjectName("radioButtonPopular")
        self.horizontalLayout.addWidget(self.radioButtonPopular)
        self.radioButtonNewest = QtWidgets.QRadioButton(self.videoTab)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonNewest.setFont(font)
        self.radioButtonNewest.setObjectName("radioButtonNewest")
        self.horizontalLayout.addWidget(self.radioButtonNewest)
        self.radioButtonOldest = QtWidgets.QRadioButton(self.videoTab)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonOldest.setFont(font)
        self.radioButtonOldest.setObjectName("radioButtonOldest")
        self.horizontalLayout.addWidget(self.radioButtonOldest)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.videoSeeMoreButton = QtWidgets.QPushButton(self.videoTab)
        self.videoSeeMoreButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.videoSeeMoreButton.setFont(font)
        self.videoSeeMoreButton.setStyleSheet("background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);\n"
"\n"
"padding: 2em;")
        self.videoSeeMoreButton.setObjectName("videoSeeMoreButton")
        self.verticalLayout.addWidget(self.videoSeeMoreButton)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabs.addTab(self.videoTab, "")
        self.infoTab = QtWidgets.QWidget()
        self.infoTab.setObjectName("infoTab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.infoTab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(10, -1, 10, -1)
        self.gridLayout_8.setSpacing(40)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.splitter_8 = QtWidgets.QSplitter(self.infoTab)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.infoSupportLabel = QtWidgets.QLabel(self.splitter_8)
        self.infoSupportLabel.setMinimumSize(QtCore.QSize(0, 60))
        self.infoSupportLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.infoSupportLabel.setFont(font)
        self.infoSupportLabel.setStyleSheet("color: rgb(198, 140, 41);\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.infoSupportLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoSupportLabel.setObjectName("infoSupportLabel")
        self.infoSupportDisplayLabel = QtWidgets.QLabel(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.infoSupportDisplayLabel.setFont(font)
        self.infoSupportDisplayLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoSupportDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoSupportDisplayLabel.setWordWrap(True)
        self.infoSupportDisplayLabel.setOpenExternalLinks(True)
        self.infoSupportDisplayLabel.setObjectName("infoSupportDisplayLabel")
        self.gridLayout_8.addWidget(self.splitter_8, 0, 1, 1, 1)
        self.splitter_7 = QtWidgets.QSplitter(self.infoTab)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.infoTechLabel = QtWidgets.QLabel(self.splitter_7)
        self.infoTechLabel.setMinimumSize(QtCore.QSize(0, 60))
        self.infoTechLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.infoTechLabel.setFont(font)
        self.infoTechLabel.setStyleSheet("color: rgb(198, 140, 41);\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.infoTechLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoTechLabel.setObjectName("infoTechLabel")
        self.infoTechDisplayLabel = QtWidgets.QLabel(self.splitter_7)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.infoTechDisplayLabel.setFont(font)
        self.infoTechDisplayLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoTechDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoTechDisplayLabel.setWordWrap(True)
        self.infoTechDisplayLabel.setObjectName("infoTechDisplayLabel")
        self.gridLayout_8.addWidget(self.splitter_7, 1, 0, 1, 1)
        self.splitter_6 = QtWidgets.QSplitter(self.infoTab)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.infoInstructionsLabel = QtWidgets.QLabel(self.splitter_6)
        self.infoInstructionsLabel.setMinimumSize(QtCore.QSize(0, 60))
        self.infoInstructionsLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.infoInstructionsLabel.setFont(font)
        self.infoInstructionsLabel.setStyleSheet("color: rgb(198, 140, 41);\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.infoInstructionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoInstructionsLabel.setObjectName("infoInstructionsLabel")
        self.infoInstructionsDisplayLabel = QtWidgets.QLabel(self.splitter_6)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.infoInstructionsDisplayLabel.setFont(font)
        self.infoInstructionsDisplayLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoInstructionsDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoInstructionsDisplayLabel.setWordWrap(True)
        self.infoInstructionsDisplayLabel.setObjectName("infoInstructionsDisplayLabel")
        self.gridLayout_8.addWidget(self.splitter_6, 0, 0, 1, 1)
        self.splitter_9 = QtWidgets.QSplitter(self.infoTab)
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.infoCreatedLabel = QtWidgets.QLabel(self.splitter_9)
        self.infoCreatedLabel.setMinimumSize(QtCore.QSize(0, 60))
        self.infoCreatedLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.infoCreatedLabel.setFont(font)
        self.infoCreatedLabel.setStyleSheet("color: rgb(198, 140, 41);\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.infoCreatedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoCreatedLabel.setObjectName("infoCreatedLabel")
        self.infoCreatedDisplayLabel = QtWidgets.QLabel(self.splitter_9)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.infoCreatedDisplayLabel.setFont(font)
        self.infoCreatedDisplayLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoCreatedDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoCreatedDisplayLabel.setWordWrap(True)
        self.infoCreatedDisplayLabel.setObjectName("infoCreatedDisplayLabel")
        self.gridLayout_8.addWidget(self.splitter_9, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabs.addTab(self.infoTab, "")
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1223, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "ShowBoat"))
        self.label.setText(_translate("mainWindow", "ShowBoat"))
        self.label_2.setText(_translate("mainWindow", "Find out where your favorite bands are playing and get tickets, all with one click!"))
        self.bandPhotoLabel.setToolTip(_translate("mainWindow", "Artist photo will be displayed here"))
        self.bandBioHeader_2.setText(_translate("mainWindow", "Artist Search"))
        self.bandSearchLineEdit.setPlaceholderText(_translate("mainWindow", "Enter the name of an artist or band to find shows"))
        self.lastSearchButton.setToolTip(_translate("mainWindow", "<html><head/><body><p>Click to execute last search</p></body></html>"))
        self.lastSearchButton.setText(_translate("mainWindow", "Previous Search"))
        self.searchButton.setToolTip(_translate("mainWindow", "<html><head/><body><p>Search by artist name</p></body></html>"))
        self.searchButton.setText(_translate("mainWindow", "Find Shows"))
        self.bandBioHeader.setText(_translate("mainWindow", "Artist Bio:"))
        self.tabs.setTabText(self.tabs.indexOf(self.homeTab), _translate("mainWindow", "Home"))
        self.showsHeaderLabel.setText(_translate("mainWindow", "Double click venue or tickets cell to view information in your browser"))
        item = self.showsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Date"))
        item = self.showsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Venue"))
        item = self.showsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "City"))
        item = self.showsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Tickets"))
        self.tabs.setTabText(self.tabs.indexOf(self.tourDatesTab), _translate("mainWindow", "Shows"))
        self.mapMapHeaderLabel.setText(_translate("mainWindow", "Click a marker on the map to see show details"))
        self.mapMapHeaderLabel_2.setText(_translate("mainWindow", "Search by proximity to city"))
        self.citySearchButton.setText(_translate("mainWindow", "Search"))
        self.citySearchInput.setPlaceholderText(_translate("mainWindow", "Enter city or address..."))
        self.clearCityButton.setText(_translate("mainWindow", "Clear City"))
        self.miles50Radio.setText(_translate("mainWindow", "50 miles"))
        self.miles100Radio.setText(_translate("mainWindow", "100 miles"))
        self.miles250Radio.setText(_translate("mainWindow", "250 miles"))
        self.tabs.setTabText(self.tabs.indexOf(self.mapTab), _translate("mainWindow", "Map"))
        self.label_4.setText(_translate("mainWindow", "Display videos that are:"))
        self.radioButtonPopular.setText(_translate("mainWindow", "Most Popular"))
        self.radioButtonNewest.setText(_translate("mainWindow", "Newest"))
        self.radioButtonOldest.setText(_translate("mainWindow", "Oldest"))
        self.videoSeeMoreButton.setToolTip(_translate("mainWindow", "Travel to artist YouTube page in browser"))
        self.videoSeeMoreButton.setText(_translate("mainWindow", "See More!"))
        self.tabs.setTabText(self.tabs.indexOf(self.videoTab), _translate("mainWindow", "Video"))
        self.infoSupportLabel.setText(_translate("mainWindow", "Support the Arts!"))
        self.infoSupportDisplayLabel.setText(_translate("mainWindow", "<html><head/><body>\n"
"<p><strong>Click links below to support artists in need:</strong><br/><br/>\n"
"<a href=\'https://www.musicares.org/donations\'>musicares.org</a><br>\n"
"<a href=\'https://www.sweetrelief.org/general-fund.html\'>sweetrelief.org</a><br>\n"
"<a href=\'https://neworleansmusiciansclinic.org/get-involved/donate/\'>neworleansmusiciansclinic.org</a>\n"
"</p></body></html>"))
        self.infoTechLabel.setText(_translate("mainWindow", "Technology Used"))
        self.infoTechDisplayLabel.setText(_translate("mainWindow", "<strong>\n"
"Python<br>\n"
"Flask<br>\n"
"PyQt5<br>\n"
"Qt Designer<br>\n"
"Folium map library<br>\n"
"Band data: The AudioDB<br>\n"
"Show data: SongKick\n"
"</strong>\n"
""))
        self.infoInstructionsLabel.setText(_translate("mainWindow", "Instructions"))
        self.infoInstructionsDisplayLabel.setText(_translate("mainWindow", "<html><head/><body>\n"
"<p>\n"
"<strong>Home:</strong><br>\n"
"Search by artist to display shows <br/>\n"
"<strong>Shows:</strong><br>\n"
"View shows and click link for ticket info<br>\n"
"<strong>Map:</strong><br>\n"
"Explore shows on interactive map, click marker for info<br>\n"
"<strong>Video:</strong><br>\n"
"View artist music videos<br/>\n"
"</p>\n"
"</body></html>"))
        self.infoCreatedLabel.setText(_translate("mainWindow", "Created By"))
        self.infoCreatedDisplayLabel.setText(_translate("mainWindow", "<strong>Jon Ramm</strong>\n"
"<p>\n"
"Musician turned programmer living in the high desert and eating burritos.\n"
"</p>\n"
""))
        self.tabs.setTabText(self.tabs.indexOf(self.infoTab), _translate("mainWindow", "Info"))
from PyQt5 import QtWebEngineWidgets
