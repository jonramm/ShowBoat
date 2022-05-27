# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\jrgbo\Documents\repos\ShowBoat\dist\showboat\showboat.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1067, 692)
        mainWindow.setStyleSheet("background-color: rgb(221, 255, 220);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(10, 0, 1051, 641))
        self.tabs.setObjectName("tabs")
        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setObjectName("homeTab")
        self.bandPhotoLabel = QtWidgets.QLabel(self.homeTab)
        self.bandPhotoLabel.setGeometry(QtCore.QRect(50, 120, 423, 423))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bandPhotoLabel.sizePolicy().hasHeightForWidth())
        self.bandPhotoLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        self.bandPhotoLabel.setFont(font)
        self.bandPhotoLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.bandPhotoLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bandPhotoLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bandPhotoLabel.setLineWidth(3)
        self.bandPhotoLabel.setText("")
        self.bandPhotoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bandPhotoLabel.setObjectName("bandPhotoLabel")
        self.bandBioHeader = QtWidgets.QLabel(self.homeTab)
        self.bandBioHeader.setGeometry(QtCore.QRect(690, 240, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(19)
        self.bandBioHeader.setFont(font)
        self.bandBioHeader.setStyleSheet("color: rgb(198, 140, 41);\n"
"\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.bandBioHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.bandBioHeader.setObjectName("bandBioHeader")
        self.bandInfoNameLabel = QtWidgets.QLabel(self.homeTab)
        self.bandInfoNameLabel.setGeometry(QtCore.QRect(20, 560, 231, 41))
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
        self.bandInfoWebsiteLabel = QtWidgets.QLabel(self.homeTab)
        self.bandInfoWebsiteLabel.setGeometry(QtCore.QRect(270, 560, 231, 41))
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
        self.searchBarContainer = QtWidgets.QGroupBox(self.homeTab)
        self.searchBarContainer.setGeometry(QtCore.QRect(520, 20, 501, 201))
        self.searchBarContainer.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.searchBarContainer.setTitle("")
        self.searchBarContainer.setAlignment(QtCore.Qt.AlignCenter)
        self.searchBarContainer.setObjectName("searchBarContainer")
        self.searchButton = QtWidgets.QPushButton(self.searchBarContainer)
        self.searchButton.setGeometry(QtCore.QRect(260, 130, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);")
        self.searchButton.setObjectName("searchButton")
        self.bandSearchLineEdit = QtWidgets.QLineEdit(self.searchBarContainer)
        self.bandSearchLineEdit.setGeometry(QtCore.QRect(12, 69, 481, 41))
        self.bandSearchLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bandSearchLineEdit.setObjectName("bandSearchLineEdit")
        self.bandBioHeader_2 = QtWidgets.QLabel(self.searchBarContainer)
        self.bandBioHeader_2.setGeometry(QtCore.QRect(130, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(24)
        self.bandBioHeader_2.setFont(font)
        self.bandBioHeader_2.setStyleSheet("color: rgb(198, 140, 41);\n"
"\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.bandBioHeader_2.setAlignment(QtCore.Qt.AlignCenter)
        self.bandBioHeader_2.setObjectName("bandBioHeader_2")
        self.lastSearchButton = QtWidgets.QPushButton(self.searchBarContainer)
        self.lastSearchButton.setGeometry(QtCore.QRect(10, 130, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.lastSearchButton.setFont(font)
        self.lastSearchButton.setStyleSheet("background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);\n"
"")
        self.lastSearchButton.setCheckable(False)
        self.lastSearchButton.setObjectName("lastSearchButton")
        self.label = QtWidgets.QLabel(self.homeTab)
        self.label.setGeometry(QtCore.QRect(30, 20, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(200, 47, 101);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.homeBioPlainTextEdit = QtWidgets.QPlainTextEdit(self.homeTab)
        self.homeBioPlainTextEdit.setGeometry(QtCore.QRect(520, 290, 501, 311))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.homeBioPlainTextEdit.setFont(font)
        self.homeBioPlainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 12px;")
        self.homeBioPlainTextEdit.setReadOnly(True)
        self.homeBioPlainTextEdit.setObjectName("homeBioPlainTextEdit")
        self.label_2 = QtWidgets.QLabel(self.homeTab)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 451, 41))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\jrgbo\\Documents\\repos\\ShowBoat\\dist\\showboat\\../../../../Pictures/IconImages/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs.addTab(self.homeTab, icon, "")
        self.tourDatesTab = QtWidgets.QWidget()
        self.tourDatesTab.setObjectName("tourDatesTab")
        self.showsTableWidget = QtWidgets.QTableWidget(self.tourDatesTab)
        self.showsTableWidget.setGeometry(QtCore.QRect(0, 50, 1041, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showsTableWidget.sizePolicy().hasHeightForWidth())
        self.showsTableWidget.setSizePolicy(sizePolicy)
        self.showsTableWidget.setMaximumSize(QtCore.QSize(1041, 561))
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
        self.showsHeaderLabel = QtWidgets.QLabel(self.tourDatesTab)
        self.showsHeaderLabel.setGeometry(QtCore.QRect(20, 10, 1001, 31))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(18)
        self.showsHeaderLabel.setFont(font)
        self.showsHeaderLabel.setStyleSheet("color: rgb(198, 140, 41);")
        self.showsHeaderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.showsHeaderLabel.setObjectName("showsHeaderLabel")
        self.label_3 = QtWidgets.QLabel(self.tourDatesTab)
        self.label_3.setGeometry(QtCore.QRect(430, 570, 141, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\Users\\jrgbo\\Documents\\repos\\ShowBoat\\dist\\showboat\\../../../../Downloads/attribution-assets/attribution-assets/powered-by-sk/powered-by-songkick-pink.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabs.addTab(self.tourDatesTab, "")
        self.mapTab = QtWidgets.QWidget()
        self.mapTab.setObjectName("mapTab")
        self.mapMapContainer = QtWebEngineWidgets.QWebEngineView(self.mapTab)
        self.mapMapContainer.setGeometry(QtCore.QRect(20, 20, 1001, 501))
        self.mapMapContainer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.mapMapContainer.setObjectName("mapMapContainer")
        self.mapMapHeaderLabel = QtWidgets.QLabel(self.mapTab)
        self.mapMapHeaderLabel.setGeometry(QtCore.QRect(10, 530, 1001, 71))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.mapMapHeaderLabel.setFont(font)
        self.mapMapHeaderLabel.setStyleSheet("color: rgb(198, 140, 41);")
        self.mapMapHeaderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mapMapHeaderLabel.setObjectName("mapMapHeaderLabel")
        self.tabs.addTab(self.mapTab, "")
        self.videoTab = QtWidgets.QWidget()
        self.videoTab.setObjectName("videoTab")
        self.video0 = QtWebEngineWidgets.QWebEngineView(self.videoTab)
        self.video0.setGeometry(QtCore.QRect(30, 20, 461, 271))
        self.video0.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.video0.setObjectName("video0")
        self.video1 = QtWebEngineWidgets.QWebEngineView(self.videoTab)
        self.video1.setGeometry(QtCore.QRect(550, 20, 461, 271))
        self.video1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.video1.setObjectName("video1")
        self.video2 = QtWebEngineWidgets.QWebEngineView(self.videoTab)
        self.video2.setGeometry(QtCore.QRect(30, 320, 461, 271))
        self.video2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.video2.setObjectName("video2")
        self.videoSeeMoreButton = QtWidgets.QPushButton(self.videoTab)
        self.videoSeeMoreButton.setGeometry(QtCore.QRect(590, 490, 381, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.videoSeeMoreButton.setFont(font)
        self.videoSeeMoreButton.setStyleSheet("background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);")
        self.videoSeeMoreButton.setObjectName("videoSeeMoreButton")
        self.radioButtonPopular = QtWidgets.QRadioButton(self.videoTab)
        self.radioButtonPopular.setEnabled(True)
        self.radioButtonPopular.setGeometry(QtCore.QRect(610, 410, 131, 18))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonPopular.setFont(font)
        self.radioButtonPopular.setChecked(True)
        self.radioButtonPopular.setObjectName("radioButtonPopular")
        self.radioButtonNewest = QtWidgets.QRadioButton(self.videoTab)
        self.radioButtonNewest.setGeometry(QtCore.QRect(760, 410, 90, 18))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonNewest.setFont(font)
        self.radioButtonNewest.setObjectName("radioButtonNewest")
        self.radioButtonOldest = QtWidgets.QRadioButton(self.videoTab)
        self.radioButtonOldest.setGeometry(QtCore.QRect(870, 410, 90, 18))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonOldest.setFont(font)
        self.radioButtonOldest.setObjectName("radioButtonOldest")
        self.label_4 = QtWidgets.QLabel(self.videoTab)
        self.label_4.setGeometry(QtCore.QRect(553, 340, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(198, 140, 41);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.tabs.addTab(self.videoTab, "")
        self.infoTab = QtWidgets.QWidget()
        self.infoTab.setObjectName("infoTab")
        self.infoInstructionsLabel = QtWidgets.QLabel(self.infoTab)
        self.infoInstructionsLabel.setGeometry(QtCore.QRect(170, 20, 191, 41))
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
        self.infoSupportLabel = QtWidgets.QLabel(self.infoTab)
        self.infoSupportLabel.setGeometry(QtCore.QRect(660, 20, 241, 41))
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
        self.infoTechLabel = QtWidgets.QLabel(self.infoTab)
        self.infoTechLabel.setGeometry(QtCore.QRect(160, 330, 221, 41))
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
        self.infoCreatedLabel = QtWidgets.QLabel(self.infoTab)
        self.infoCreatedLabel.setGeometry(QtCore.QRect(700, 330, 161, 41))
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
        self.infoInstructionsDisplayLabel = QtWidgets.QLabel(self.infoTab)
        self.infoInstructionsDisplayLabel.setGeometry(QtCore.QRect(30, 80, 481, 211))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.infoInstructionsDisplayLabel.setFont(font)
        self.infoInstructionsDisplayLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoInstructionsDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoInstructionsDisplayLabel.setWordWrap(True)
        self.infoInstructionsDisplayLabel.setObjectName("infoInstructionsDisplayLabel")
        self.infoSupportDisplayLabel = QtWidgets.QLabel(self.infoTab)
        self.infoSupportDisplayLabel.setGeometry(QtCore.QRect(550, 80, 461, 211))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.infoSupportDisplayLabel.setFont(font)
        self.infoSupportDisplayLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoSupportDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoSupportDisplayLabel.setWordWrap(True)
        self.infoSupportDisplayLabel.setOpenExternalLinks(True)
        self.infoSupportDisplayLabel.setObjectName("infoSupportDisplayLabel")
        self.infoTechDisplayLabel = QtWidgets.QLabel(self.infoTab)
        self.infoTechDisplayLabel.setGeometry(QtCore.QRect(30, 380, 481, 211))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.infoTechDisplayLabel.setFont(font)
        self.infoTechDisplayLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoTechDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoTechDisplayLabel.setWordWrap(True)
        self.infoTechDisplayLabel.setObjectName("infoTechDisplayLabel")
        self.infoCreatedDisplayLabel = QtWidgets.QLabel(self.infoTab)
        self.infoCreatedDisplayLabel.setGeometry(QtCore.QRect(550, 380, 461, 211))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.infoCreatedDisplayLabel.setFont(font)
        self.infoCreatedDisplayLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoCreatedDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoCreatedDisplayLabel.setWordWrap(True)
        self.infoCreatedDisplayLabel.setObjectName("infoCreatedDisplayLabel")
        self.tabs.addTab(self.infoTab, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 23))
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
        self.bandPhotoLabel.setToolTip(_translate("mainWindow", "Artist photo will be displayed here"))
        self.bandBioHeader.setText(_translate("mainWindow", "Artist Bio:"))
        self.searchButton.setToolTip(_translate("mainWindow", "<html><head/><body><p>Search by artist name</p></body></html>"))
        self.searchButton.setText(_translate("mainWindow", "Find Shows"))
        self.bandSearchLineEdit.setPlaceholderText(_translate("mainWindow", "Enter the name of an artist or band to find shows"))
        self.bandBioHeader_2.setText(_translate("mainWindow", "Artist Search"))
        self.lastSearchButton.setToolTip(_translate("mainWindow", "<html><head/><body><p>Click to execute last search</p></body></html>"))
        self.lastSearchButton.setText(_translate("mainWindow", "Previous Search"))
        self.label.setText(_translate("mainWindow", "ShowBoat"))
        self.label_2.setText(_translate("mainWindow", "Find out where your favorite bands are playing and get tickets, all with one click!"))
        self.tabs.setTabText(self.tabs.indexOf(self.homeTab), _translate("mainWindow", "Home"))
        item = self.showsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Date"))
        item = self.showsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "Venue"))
        item = self.showsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "City"))
        item = self.showsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Tickets"))
        self.showsHeaderLabel.setText(_translate("mainWindow", "Double click venue or tickets cell to view information in your browser"))
        self.tabs.setTabText(self.tabs.indexOf(self.tourDatesTab), _translate("mainWindow", "Shows"))
        self.mapMapHeaderLabel.setText(_translate("mainWindow", "Click a marker on the map to see show details"))
        self.tabs.setTabText(self.tabs.indexOf(self.mapTab), _translate("mainWindow", "Map"))
        self.videoSeeMoreButton.setToolTip(_translate("mainWindow", "Travel to artist YouTube page in browser"))
        self.videoSeeMoreButton.setText(_translate("mainWindow", "See More!"))
        self.radioButtonPopular.setText(_translate("mainWindow", "Most Popular"))
        self.radioButtonNewest.setText(_translate("mainWindow", "Newest"))
        self.radioButtonOldest.setText(_translate("mainWindow", "Oldest"))
        self.label_4.setText(_translate("mainWindow", "Display videos that are:"))
        self.tabs.setTabText(self.tabs.indexOf(self.videoTab), _translate("mainWindow", "Video"))
        self.infoInstructionsLabel.setText(_translate("mainWindow", "Instructions"))
        self.infoSupportLabel.setText(_translate("mainWindow", "Support the Arts!"))
        self.infoTechLabel.setText(_translate("mainWindow", "Technology Used"))
        self.infoCreatedLabel.setText(_translate("mainWindow", "Created By"))
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
        self.infoSupportDisplayLabel.setText(_translate("mainWindow", "<html><head/><body>\n"
"<p><strong>Click links below to support artists in need:</strong><br/><br/>\n"
"<a href=\'https://www.musicares.org/donations\'>musicares.org</a><br>\n"
"<a href=\'https://www.sweetrelief.org/general-fund.html\'>sweetrelief.org</a><br>\n"
"<a href=\'https://neworleansmusiciansclinic.org/get-involved/donate/\'>neworleansmusiciansclinic.org</a>\n"
"</p></body></html>"))
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
        self.infoCreatedDisplayLabel.setText(_translate("mainWindow", "<strong>Jon Ramm</strong>\n"
"<p>\n"
"Musician turned programmer living in the high desert and eating burritos.\n"
"</p>\n"
""))
        self.tabs.setTabText(self.tabs.indexOf(self.infoTab), _translate("mainWindow", "Info"))
from PyQt5 import QtWebEngineWidgets
