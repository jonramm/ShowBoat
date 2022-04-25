# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'showboat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qwebengineview import QWebEngineView


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1067, 693)
        mainWindow.setStyleSheet(u"background-color: rgb(221, 255, 220);")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(10, 0, 1051, 641))
        self.homeTab = QWidget()
        self.homeTab.setObjectName(u"homeTab")
        self.bandPhotoLabel = QLabel(self.homeTab)
        self.bandPhotoLabel.setObjectName(u"bandPhotoLabel")
        self.bandPhotoLabel.setGeometry(QRect(50, 120, 423, 423))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bandPhotoLabel.sizePolicy().hasHeightForWidth())
        self.bandPhotoLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Britannic Bold")
        self.bandPhotoLabel.setFont(font)
        self.bandPhotoLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.bandPhotoLabel.setFrameShape(QFrame.StyledPanel)
        self.bandPhotoLabel.setFrameShadow(QFrame.Sunken)
        self.bandPhotoLabel.setLineWidth(3)
        self.bandPhotoLabel.setAlignment(Qt.AlignCenter)
        self.bandBioHeader = QLabel(self.homeTab)
        self.bandBioHeader.setObjectName(u"bandBioHeader")
        self.bandBioHeader.setGeometry(QRect(690, 240, 171, 41))
        font1 = QFont()
        font1.setFamily(u"Britannic Bold")
        font1.setPointSize(19)
        self.bandBioHeader.setFont(font1)
        self.bandBioHeader.setStyleSheet(u"color: rgb(198, 140, 41);\n"
"\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.bandBioHeader.setAlignment(Qt.AlignCenter)
        self.bandInfoNameLabel = QLabel(self.homeTab)
        self.bandInfoNameLabel.setObjectName(u"bandInfoNameLabel")
        self.bandInfoNameLabel.setGeometry(QRect(20, 560, 231, 41))
        font2 = QFont()
        font2.setFamily(u"Britannic Bold")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.bandInfoNameLabel.setFont(font2)
        self.bandInfoNameLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.bandInfoNameLabel.setFrameShape(QFrame.StyledPanel)
        self.bandInfoNameLabel.setFrameShadow(QFrame.Sunken)
        self.bandInfoNameLabel.setLineWidth(3)
        self.bandInfoNameLabel.setAlignment(Qt.AlignCenter)
        self.bandInfoWebsiteLabel = QLabel(self.homeTab)
        self.bandInfoWebsiteLabel.setObjectName(u"bandInfoWebsiteLabel")
        self.bandInfoWebsiteLabel.setGeometry(QRect(270, 560, 231, 41))
        self.bandInfoWebsiteLabel.setFont(font2)
        self.bandInfoWebsiteLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.bandInfoWebsiteLabel.setFrameShape(QFrame.StyledPanel)
        self.bandInfoWebsiteLabel.setFrameShadow(QFrame.Sunken)
        self.bandInfoWebsiteLabel.setLineWidth(3)
        self.bandInfoWebsiteLabel.setAlignment(Qt.AlignCenter)
        self.bandInfoWebsiteLabel.setOpenExternalLinks(True)
        self.searchBarContainer = QGroupBox(self.homeTab)
        self.searchBarContainer.setObjectName(u"searchBarContainer")
        self.searchBarContainer.setGeometry(QRect(520, 20, 501, 201))
        self.searchBarContainer.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.searchBarContainer.setAlignment(Qt.AlignCenter)
        self.searchButton = QPushButton(self.searchBarContainer)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(260, 130, 231, 51))
        font3 = QFont()
        font3.setFamily(u"Impact")
        font3.setPointSize(12)
        self.searchButton.setFont(font3)
        self.searchButton.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);")
        self.bandSearchLineEdit = QLineEdit(self.searchBarContainer)
        self.bandSearchLineEdit.setObjectName(u"bandSearchLineEdit")
        self.bandSearchLineEdit.setGeometry(QRect(12, 69, 481, 41))
        self.bandSearchLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.bandBioHeader_2 = QLabel(self.searchBarContainer)
        self.bandBioHeader_2.setObjectName(u"bandBioHeader_2")
        self.bandBioHeader_2.setGeometry(QRect(130, 10, 241, 41))
        font4 = QFont()
        font4.setFamily(u"Britannic Bold")
        font4.setPointSize(24)
        self.bandBioHeader_2.setFont(font4)
        self.bandBioHeader_2.setStyleSheet(u"color: rgb(198, 140, 41);\n"
"\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.bandBioHeader_2.setAlignment(Qt.AlignCenter)
        self.lastSearchButton = QPushButton(self.searchBarContainer)
        self.lastSearchButton.setObjectName(u"lastSearchButton")
        self.lastSearchButton.setGeometry(QRect(10, 130, 231, 51))
        self.lastSearchButton.setFont(font3)
        self.lastSearchButton.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);\n"
"")
        self.lastSearchButton.setCheckable(False)
        self.label = QLabel(self.homeTab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 471, 61))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Black")
        font5.setPointSize(36)
        font5.setBold(True)
        font5.setWeight(75)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: rgb(200, 47, 101);")
        self.label.setAlignment(Qt.AlignCenter)
        self.homeBioPlainTextEdit = QPlainTextEdit(self.homeTab)
        self.homeBioPlainTextEdit.setObjectName(u"homeBioPlainTextEdit")
        self.homeBioPlainTextEdit.setGeometry(QRect(520, 290, 501, 311))
        font6 = QFont()
        font6.setFamily(u"Tahoma")
        font6.setPointSize(10)
        self.homeBioPlainTextEdit.setFont(font6)
        self.homeBioPlainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 12px;")
        self.homeBioPlainTextEdit.setReadOnly(True)
        self.label_2 = QLabel(self.homeTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 451, 41))
        font7 = QFont()
        font7.setFamily(u"Tahoma")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"color: rgb(94, 94, 94);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        icon = QIcon()
        icon.addFile(u"../../../../Pictures/IconImages/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabs.addTab(self.homeTab, icon, "")
        self.tourDatesTab = QWidget()
        self.tourDatesTab.setObjectName(u"tourDatesTab")
        self.tourDatesScrollBar = QScrollBar(self.tourDatesTab)
        self.tourDatesScrollBar.setObjectName(u"tourDatesScrollBar")
        self.tourDatesScrollBar.setGeometry(QRect(995, 19, 31, 571))
        self.tourDatesScrollBar.setStyleSheet(u"background-color: rgb(202, 202, 202);")
        self.tourDatesScrollBar.setOrientation(Qt.Vertical)
        self.tourDatesDateLabel = QLabel(self.tourDatesTab)
        self.tourDatesDateLabel.setObjectName(u"tourDatesDateLabel")
        self.tourDatesDateLabel.setGeometry(QRect(50, 20, 81, 51))
        font8 = QFont()
        font8.setFamily(u"Britannic Bold")
        font8.setPointSize(20)
        self.tourDatesDateLabel.setFont(font8)
        self.tourDatesDateLabel.setStyleSheet(u"color: rgb(198, 140, 41);\n"
"\n"
"\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.tourDatesDateLabel.setAlignment(Qt.AlignCenter)
        self.tourDatesVenueLabel = QLabel(self.tourDatesTab)
        self.tourDatesVenueLabel.setObjectName(u"tourDatesVenueLabel")
        self.tourDatesVenueLabel.setGeometry(QRect(280, 20, 101, 51))
        self.tourDatesVenueLabel.setFont(font8)
        self.tourDatesVenueLabel.setStyleSheet(u"color: rgb(198, 140, 41);\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.tourDatesVenueLabel.setAlignment(Qt.AlignCenter)
        self.tourDatesCityLabel = QLabel(self.tourDatesTab)
        self.tourDatesCityLabel.setObjectName(u"tourDatesCityLabel")
        self.tourDatesCityLabel.setGeometry(QRect(540, 20, 141, 51))
        self.tourDatesCityLabel.setFont(font8)
        self.tourDatesCityLabel.setStyleSheet(u"color: rgb(198, 140, 41);\n"
"\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.tourDatesCityLabel.setAlignment(Qt.AlignCenter)
        self.tourDatesTicketInfoLabel = QLabel(self.tourDatesTab)
        self.tourDatesTicketInfoLabel.setObjectName(u"tourDatesTicketInfoLabel")
        self.tourDatesTicketInfoLabel.setGeometry(QRect(770, 20, 161, 51))
        self.tourDatesTicketInfoLabel.setFont(font8)
        self.tourDatesTicketInfoLabel.setStyleSheet(u"color: rgb(198, 140, 41);\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.tourDatesTicketInfoLabel.setAlignment(Qt.AlignCenter)
        self.tourDatesDateListLabel = QLabel(self.tourDatesTab)
        self.tourDatesDateListLabel.setObjectName(u"tourDatesDateListLabel")
        self.tourDatesDateListLabel.setGeometry(QRect(30, 90, 111, 501))
        font9 = QFont()
        font9.setFamily(u"Tahoma")
        font9.setBold(True)
        font9.setWeight(75)
        self.tourDatesDateListLabel.setFont(font9)
        self.tourDatesDateListLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"padding-top: 5px;")
        self.tourDatesDateListLabel.setFrameShape(QFrame.StyledPanel)
        self.tourDatesDateListLabel.setFrameShadow(QFrame.Sunken)
        self.tourDatesDateListLabel.setLineWidth(3)
        self.tourDatesDateListLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.tourDatesVenueListLabel = QLabel(self.tourDatesTab)
        self.tourDatesVenueListLabel.setObjectName(u"tourDatesVenueListLabel")
        self.tourDatesVenueListLabel.setGeometry(QRect(170, 90, 321, 501))
        self.tourDatesVenueListLabel.setFont(font9)
        self.tourDatesVenueListLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"padding-top: 5px;")
        self.tourDatesVenueListLabel.setFrameShape(QFrame.StyledPanel)
        self.tourDatesVenueListLabel.setFrameShadow(QFrame.Sunken)
        self.tourDatesVenueListLabel.setLineWidth(3)
        self.tourDatesVenueListLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.tourDatesCityListLabel = QLabel(self.tourDatesTab)
        self.tourDatesCityListLabel.setObjectName(u"tourDatesCityListLabel")
        self.tourDatesCityListLabel.setGeometry(QRect(520, 90, 191, 501))
        self.tourDatesCityListLabel.setFont(font9)
        self.tourDatesCityListLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"padding-top: 5px;")
        self.tourDatesCityListLabel.setFrameShape(QFrame.StyledPanel)
        self.tourDatesCityListLabel.setFrameShadow(QFrame.Sunken)
        self.tourDatesCityListLabel.setLineWidth(3)
        self.tourDatesCityListLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.ticketTextBrowser = QTextBrowser(self.tourDatesTab)
        self.ticketTextBrowser.setObjectName(u"ticketTextBrowser")
        self.ticketTextBrowser.setGeometry(QRect(740, 90, 221, 501))
        font10 = QFont()
        font10.setFamily(u"Tahoma")
        self.ticketTextBrowser.setFont(font10)
        self.ticketTextBrowser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"padding-top: 5px;")
        self.ticketTextBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.ticketTextBrowser.setOpenLinks(False)
        self.tabs.addTab(self.tourDatesTab, "")
        self.mapTab = QWidget()
        self.mapTab.setObjectName(u"mapTab")
        self.mapMapContainer = QWebEngineView(self.mapTab)
        self.mapMapContainer.setObjectName(u"mapMapContainer")
        self.mapMapContainer.setGeometry(QRect(20, 20, 1001, 501))
        self.mapMapContainer.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.mapMapHeaderLabel = QLabel(self.mapTab)
        self.mapMapHeaderLabel.setObjectName(u"mapMapHeaderLabel")
        self.mapMapHeaderLabel.setGeometry(QRect(10, 530, 1001, 71))
        font11 = QFont()
        font11.setFamily(u"Britannic Bold")
        font11.setPointSize(18)
        font11.setBold(False)
        font11.setWeight(50)
        self.mapMapHeaderLabel.setFont(font11)
        self.mapMapHeaderLabel.setStyleSheet(u"color: rgb(198, 140, 41);")
        self.mapMapHeaderLabel.setAlignment(Qt.AlignCenter)
        self.tabs.addTab(self.mapTab, "")
        self.videoTab = QWidget()
        self.videoTab.setObjectName(u"videoTab")
        self.video0 = QWebEngineView(self.videoTab)
        self.video0.setObjectName(u"video0")
        self.video0.setGeometry(QRect(30, 20, 461, 271))
        self.video0.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.video1 = QWebEngineView(self.videoTab)
        self.video1.setObjectName(u"video1")
        self.video1.setGeometry(QRect(550, 20, 461, 271))
        self.video1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.video2 = QWebEngineView(self.videoTab)
        self.video2.setObjectName(u"video2")
        self.video2.setGeometry(QRect(30, 320, 461, 271))
        self.video2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.videoSeeMoreButton = QPushButton(self.videoTab)
        self.videoSeeMoreButton.setObjectName(u"videoSeeMoreButton")
        self.videoSeeMoreButton.setGeometry(QRect(590, 390, 381, 91))
        font12 = QFont()
        font12.setPointSize(18)
        self.videoSeeMoreButton.setFont(font12)
        self.videoSeeMoreButton.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"color: rgb(200, 47, 101);")
        self.tabs.addTab(self.videoTab, "")
        self.infoTab = QWidget()
        self.infoTab.setObjectName(u"infoTab")
        self.infoInstructionsLabel = QLabel(self.infoTab)
        self.infoInstructionsLabel.setObjectName(u"infoInstructionsLabel")
        self.infoInstructionsLabel.setGeometry(QRect(170, 20, 191, 41))
        self.infoInstructionsLabel.setFont(font11)
        self.infoInstructionsLabel.setStyleSheet(u"color: rgb(198, 140, 41);\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.infoInstructionsLabel.setAlignment(Qt.AlignCenter)
        self.infoSupportLabel = QLabel(self.infoTab)
        self.infoSupportLabel.setObjectName(u"infoSupportLabel")
        self.infoSupportLabel.setGeometry(QRect(660, 20, 241, 41))
        self.infoSupportLabel.setFont(font11)
        self.infoSupportLabel.setStyleSheet(u"color: rgb(198, 140, 41);\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.infoSupportLabel.setAlignment(Qt.AlignCenter)
        self.infoTechLabel = QLabel(self.infoTab)
        self.infoTechLabel.setObjectName(u"infoTechLabel")
        self.infoTechLabel.setGeometry(QRect(160, 330, 221, 41))
        self.infoTechLabel.setFont(font11)
        self.infoTechLabel.setStyleSheet(u"color: rgb(198, 140, 41);\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.infoTechLabel.setAlignment(Qt.AlignCenter)
        self.infoCreatedLabel = QLabel(self.infoTab)
        self.infoCreatedLabel.setObjectName(u"infoCreatedLabel")
        self.infoCreatedLabel.setGeometry(QRect(700, 330, 161, 41))
        self.infoCreatedLabel.setFont(font11)
        self.infoCreatedLabel.setStyleSheet(u"color: rgb(198, 140, 41);\n"
"border-bottom: 3px solid rgb(198, 140, 41);")
        self.infoCreatedLabel.setAlignment(Qt.AlignCenter)
        self.infoInstructionsDisplayLabel = QLabel(self.infoTab)
        self.infoInstructionsDisplayLabel.setObjectName(u"infoInstructionsDisplayLabel")
        self.infoInstructionsDisplayLabel.setGeometry(QRect(30, 80, 481, 211))
        self.infoInstructionsDisplayLabel.setFont(font6)
        self.infoInstructionsDisplayLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoInstructionsDisplayLabel.setAlignment(Qt.AlignCenter)
        self.infoInstructionsDisplayLabel.setWordWrap(True)
        self.infoSupportDisplayLabel = QLabel(self.infoTab)
        self.infoSupportDisplayLabel.setObjectName(u"infoSupportDisplayLabel")
        self.infoSupportDisplayLabel.setGeometry(QRect(550, 80, 461, 211))
        self.infoSupportDisplayLabel.setFont(font6)
        self.infoSupportDisplayLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoSupportDisplayLabel.setAlignment(Qt.AlignCenter)
        self.infoSupportDisplayLabel.setWordWrap(True)
        self.infoSupportDisplayLabel.setOpenExternalLinks(True)
        self.infoTechDisplayLabel = QLabel(self.infoTab)
        self.infoTechDisplayLabel.setObjectName(u"infoTechDisplayLabel")
        self.infoTechDisplayLabel.setGeometry(QRect(30, 380, 481, 211))
        self.infoTechDisplayLabel.setFont(font6)
        self.infoTechDisplayLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoTechDisplayLabel.setAlignment(Qt.AlignCenter)
        self.infoTechDisplayLabel.setWordWrap(True)
        self.infoCreatedDisplayLabel = QLabel(self.infoTab)
        self.infoCreatedDisplayLabel.setObjectName(u"infoCreatedDisplayLabel")
        self.infoCreatedDisplayLabel.setGeometry(QRect(550, 380, 461, 211))
        self.infoCreatedDisplayLabel.setFont(font6)
        self.infoCreatedDisplayLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 10px;")
        self.infoCreatedDisplayLabel.setAlignment(Qt.AlignCenter)
        self.infoCreatedDisplayLabel.setWordWrap(True)
        self.tabs.addTab(self.infoTab, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1067, 23))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"ShowBoat", None))
#if QT_CONFIG(tooltip)
        self.bandPhotoLabel.setToolTip(QCoreApplication.translate("mainWindow", u"Artist photo will be displayed here", None))
#endif // QT_CONFIG(tooltip)
        self.bandPhotoLabel.setText("")
        self.bandBioHeader.setText(QCoreApplication.translate("mainWindow", u"Band Bio:", None))
        self.bandInfoNameLabel.setText("")
        self.bandInfoWebsiteLabel.setText("")
        self.searchBarContainer.setTitle("")
#if QT_CONFIG(tooltip)
        self.searchButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Search by artist name</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.searchButton.setText(QCoreApplication.translate("mainWindow", u"Find Shows", None))
        self.bandSearchLineEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Enter the name of an artist or band to find shows", None))
        self.bandBioHeader_2.setText(QCoreApplication.translate("mainWindow", u"Band Search", None))
#if QT_CONFIG(tooltip)
        self.lastSearchButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Click to execute last search</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lastSearchButton.setText(QCoreApplication.translate("mainWindow", u"Previous Search", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"ShowBoat", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Find out where your favorite bands are playing and get tickets, all with one click!", None))
        self.tabs.setTabText(self.tabs.indexOf(self.homeTab), QCoreApplication.translate("mainWindow", u"Home", None))
        self.tourDatesDateLabel.setText(QCoreApplication.translate("mainWindow", u"Date", None))
        self.tourDatesVenueLabel.setText(QCoreApplication.translate("mainWindow", u"Venue", None))
        self.tourDatesCityLabel.setText(QCoreApplication.translate("mainWindow", u"Location", None))
        self.tourDatesTicketInfoLabel.setText(QCoreApplication.translate("mainWindow", u"Ticket Info", None))
        self.tourDatesDateListLabel.setText("")
        self.tourDatesVenueListLabel.setText("")
        self.tourDatesCityListLabel.setText("")
        self.ticketTextBrowser.setHtml(QCoreApplication.translate("mainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.15094pt;\"><br /></p></body></html>", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tourDatesTab), QCoreApplication.translate("mainWindow", u"Shows", None))
        self.mapMapHeaderLabel.setText(QCoreApplication.translate("mainWindow", u"Click a marker on the map to see show details", None))
        self.tabs.setTabText(self.tabs.indexOf(self.mapTab), QCoreApplication.translate("mainWindow", u"Map", None))
#if QT_CONFIG(tooltip)
        self.videoSeeMoreButton.setToolTip(QCoreApplication.translate("mainWindow", u"Travel to artist YouTube page in browser", None))
#endif // QT_CONFIG(tooltip)
        self.videoSeeMoreButton.setText(QCoreApplication.translate("mainWindow", u"See More!", None))
        self.tabs.setTabText(self.tabs.indexOf(self.videoTab), QCoreApplication.translate("mainWindow", u"Video", None))
        self.infoInstructionsLabel.setText(QCoreApplication.translate("mainWindow", u"Instructions", None))
        self.infoSupportLabel.setText(QCoreApplication.translate("mainWindow", u"Support the Arts!", None))
        self.infoTechLabel.setText(QCoreApplication.translate("mainWindow", u"Technology Used", None))
        self.infoCreatedLabel.setText(QCoreApplication.translate("mainWindow", u"Created By", None))
        self.infoInstructionsDisplayLabel.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body>\n"
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
"</body></html>", None))
        self.infoSupportDisplayLabel.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body>\n"
"<p><strong>Click links below to support artists in need:</strong><br/><br/>\n"
"<a href='https://www.musicares.org/donations'>musicares.org</a><br>\n"
"<a href='https://www.sweetrelief.org/general-fund.html'>sweetrelief.org</a><br>\n"
"<a href='https://neworleansmusiciansclinic.org/get-involved/donate/'>neworleansmusiciansclinic.org</a>\n"
"</p></body></html>", None))
        self.infoTechDisplayLabel.setText(QCoreApplication.translate("mainWindow", u"<strong>\n"
"Python<br>\n"
"Flask<br>\n"
"PyQt5<br>\n"
"Qt Designer<br>\n"
"Folium map library<br>\n"
"</strong>", None))
        self.infoCreatedDisplayLabel.setText(QCoreApplication.translate("mainWindow", u"<strong>Jon Ramm</strong>\n"
"<p>\n"
"Musician turned programmer living in the high desert and eating burritos.\n"
"</p>\n"
"", None))
        self.tabs.setTabText(self.tabs.indexOf(self.infoTab), QCoreApplication.translate("mainWindow", u"Info", None))
    # retranslateUi

