import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import WebScrapeBackEnd as ws
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s : %(asctime)s : %(message)s')

fileHandler = logging.FileHandler('LogFile.log')
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 414)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setMouseTracking(False)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 541, 184))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.contentLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        self.contentLayout.setObjectName("contentLayout")
        self.industryLayout = QtWidgets.QVBoxLayout()
        self.industryLayout.setObjectName("industryLayout")
        self.industryInstruction = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.industryInstruction.sizePolicy().hasHeightForWidth())
        self.industryInstruction.setSizePolicy(sizePolicy)
        self.industryInstruction.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.industryInstruction.setObjectName("industryInstruction")
        self.industryLayout.addWidget(self.industryInstruction)
        self.industryOption = QtWidgets.QHBoxLayout()
        self.industryOption.setObjectName("industryOption")
        self.consumerRB = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.consumerRB.setObjectName("consumerRB")
        self.industryOption.addWidget(self.consumerRB)
        self.restaurantsRB = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.restaurantsRB.setObjectName("restaurantsRB")
        self.industryOption.addWidget(self.restaurantsRB)
        self.industrialRB = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.industrialRB.setObjectName("industrialRB")
        self.industryOption.addWidget(self.industrialRB)
        self.businessRB = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.businessRB.setObjectName("businessRB")
        self.industryOption.addWidget(self.businessRB)
        self.medicalRB = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.medicalRB.setObjectName("medicalRB")
        self.industryOption.addWidget(self.medicalRB)
        self.automotiveRB = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.automotiveRB.setObjectName("automotiveRB")
        self.industryOption.addWidget(self.automotiveRB)
        self.industryLayout.addLayout(self.industryOption)
        self.contentLayout.addLayout(self.industryLayout)
        self.categoryLayout = QtWidgets.QVBoxLayout()
        self.categoryLayout.setContentsMargins(-1, 20, -1, -1)
        self.categoryLayout.setObjectName("categoryLayout")
        self.categoryInstruction = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryInstruction.sizePolicy().hasHeightForWidth())
        self.categoryInstruction.setSizePolicy(sizePolicy)
        self.categoryInstruction.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.categoryInstruction.setObjectName("categoryInstruction")
        self.categoryLayout.addWidget(self.categoryInstruction)
        self.categoryOption = QtWidgets.QHBoxLayout()
        self.categoryOption.setObjectName("categoryOption")
        self.categoryMenu = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryMenu.sizePolicy().hasHeightForWidth())
        self.categoryMenu.setSizePolicy(sizePolicy)
        self.categoryMenu.setObjectName("categoryMenu")
        self.categoryMenu.addItem("")
        self.categoryOption.addWidget(self.categoryMenu)
        self.categoryLayout.addLayout(self.categoryOption)
        self.contentLayout.addLayout(self.categoryLayout)
        self.subCategoryLayout = QtWidgets.QVBoxLayout()
        self.subCategoryLayout.setContentsMargins(-1, 20, -1, -1)
        self.subCategoryLayout.setObjectName("subCategoryLayout")
        self.subCategoryInstruction = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subCategoryInstruction.sizePolicy().hasHeightForWidth())
        self.subCategoryInstruction.setSizePolicy(sizePolicy)
        self.subCategoryInstruction.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.subCategoryInstruction.setObjectName("subCategoryInstruction")
        self.subCategoryLayout.addWidget(self.subCategoryInstruction)
        self.subCategoryMenu = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subCategoryMenu.sizePolicy().hasHeightForWidth())
        self.subCategoryMenu.setSizePolicy(sizePolicy)
        self.subCategoryMenu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.subCategoryMenu.setObjectName("subCategoryMenu")
        self.subCategoryMenu.addItem("")
        self.subCategoryLayout.addWidget(self.subCategoryMenu)
        self.contentLayout.addLayout(self.subCategoryLayout)
        self.webScrapeButton = QtWidgets.QPushButton(self.centralwidget)
        self.webScrapeButton.setGeometry(QtCore.QRect(210, 340, 151, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webScrapeButton.sizePolicy().hasHeightForWidth())
        self.webScrapeButton.setSizePolicy(sizePolicy)
        self.webScrapeButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.webScrapeButton.setIconSize(QtCore.QSize(16, 16))
        self.webScrapeButton.setObjectName("webScrapeButton")
        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        self.messageLabel.setGeometry(QtCore.QRect(20, 240, 541, 81))
        self.messageLabel.setText("")
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setObjectName("messageLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.categoryMenu.setEnabled(False)
        self.subCategoryMenu.setEnabled(False)
        self.radioClick()
        self.categoryMenu.currentTextChanged.connect(self.categoryCheck)
        self.subCategoryMenu.currentTextChanged.connect(self.getSubCategoryName)
        self.webScrapeButton.clicked.connect(self.startScraping)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Street Directory Web Scraping Software"))
        self.industryInstruction.setText(_translate("MainWindow", "Please select one of the industries."))
        self.consumerRB.setText(_translate("MainWindow", "Consumer"))
        self.restaurantsRB.setText(_translate("MainWindow", "Restaurants"))
        self.industrialRB.setText(_translate("MainWindow", "Industrial"))
        self.businessRB.setText(_translate("MainWindow", "Business"))
        self.medicalRB.setText(_translate("MainWindow", "Medical"))
        self.automotiveRB.setText(_translate("MainWindow", "Automotive"))
        self.categoryInstruction.setText(_translate("MainWindow", "Please select one of the categories."))
        self.categoryMenu.setItemText(0, _translate("MainWindow", "Select a category"))
        self.subCategoryInstruction.setText(_translate("MainWindow", "Please select one of the sub-categories."))
        self.subCategoryMenu.setItemText(0, _translate("MainWindow", "Select a sub-category"))
        self.webScrapeButton.setText(_translate("MainWindow", "Web Scrape"))

    def showPopUP(self):
        self.messageBox = QMessageBox()
        self.messageBox.setWindowTitle("WebScraping Process Completed")
        self.messageBox.setText("WebScraping Process have completed.\n You may start a new process.")
        logger.info("WebScraping Process completed.")
        show = self.messageBox.exec_()

    def radioClick(self):
            self.consumerRB.clicked.connect(self.radioCheck)
            self.restaurantsRB.clicked.connect(self.radioCheck)
            self.industrialRB.clicked.connect(self.radioCheck)
            self.businessRB.clicked.connect(self.radioCheck)
            self.medicalRB.clicked.connect(self.radioCheck)
            self.automotiveRB.clicked.connect(self.radioCheck)

    def radioCheck(self):
        if self.consumerRB.isChecked():
            ws.setPage("Consumer")
            ws.isRestaurant = False
            ws.isMedical = False
            ws.isAutomotive = False
            ws.industryName = "Consumer"
            self.messageLabel.setText("You have selected Consumer Industry.\n Please select a category.")
            logger.info("Consumer industry selected.")
        elif self.restaurantsRB.isChecked():
            ws.setPage("Restaurants")
            ws.isRestaurant = True
            ws.isMedical = False
            ws.isAutomotive = False
            ws.industryName = "Restaurants"
            self.messageLabel.setText("You have selected Restaurant Industry.\n Please select a category.")
            logger.info("Restaurant industry selected.")
        elif self.industrialRB.isChecked():
            ws.setPage("Industrial")
            ws.isRestaurant = False
            ws.isMedical = False
            ws.isAutomotive = False
            ws.industryName = "Industrial"
            self.messageLabel.setText("You have selected Industrial Industry.\n Please select a category.")
            logger.info("Industrial industry selected.")
        elif self.businessRB.isChecked():
            ws.setPage("Business")
            ws.isRestaurant = False
            ws.isMedical = False
            ws.isAutomotive = False
            ws.industryName = "Business"
            self.messageLabel.setText("You have selected Business Industry.\n Please select a category.")
            logger.info("Business industry selected.")
        elif self.medicalRB.isChecked():
            ws.setPage("Medical")
            ws.isRestaurant = False
            ws.isMedical = True
            ws.isAutomotive = False
            ws.industryName = "Medical"
            self.messageLabel.setText("You have selected Medical Industry.\n Please select a category.")
            logger.info("Medical industry selected.")
        elif self.automotiveRB.isChecked():
            ws.setPage("Automotive")
            ws.isRestaurant = False
            ws.isMedical = False
            ws.isAutomotive = True
            ws.industryName = "Automotive"
            self.messageLabel.setText("You have selected Automotive Industry.\n Please select a category.")
            logger.info("Automotive industry selected.")

        ws.getLink()
        self.categoryMenu.clear()
        prohibitedCategory = ["Restaurants Menu"]
        for _ in range(ws.categoryCounter + 1):
            if ws.categoryList[_] not in prohibitedCategory:
                self.categoryMenu.addItem(ws.categoryList[_])
            else:
                pass
        self.categoryMenu.setEnabled(True)
        self.subCategoryMenu.setEnabled(False)

        logger.info("Category Menu generated. Ready for selection")

    def getCategoryText(self, text):
        self.messageLabel.setText(
            "You have selected the following category : " + str(text) + "\n Please select a sub-category.")


    def categoryCheck(self, value):
        self.subCategoryMenu.clear()
        self.subCategoryMenu.addItem("Select a sub-category")
        # if not ws.isRestaurant:
        ws.getSubCategory()
        prohibitedItems = ["",
                           "American Coffee",
                           "Local Coffee",
                           "American",
                           "Japanese",
                           "Sandwiches",
                           "Nose",
                           "Throat",
                           "Medical Equipment and Supplies",
                           "TCM and Family Medical",
                           "Alphabetical Search for",
                           "Buses",
                           "General Information"
                           ]

        if value in ws.catSubCatDictionary:
            valueList = ws.catSubCatDictionary[value].split(",")
            for _ in valueList:
                # for item in prohibitedItems:
                clearText = str([_]).replace("[", "").replace("'", "").replace("]", "").replace("\"", "").strip()
                if str(_.replace("[", "").replace("'", "").replace("]", "").replace("\"", "").strip()) not in prohibitedItems:
                    if clearText == "ENT Ear":
                        clearText = "ENT Ear,Nose,Throat"
                        self.subCategoryMenu.addItem(clearText)
                    else:
                        self.subCategoryMenu.addItem(clearText)

                # str([_]).replace("[", "").replace("'", "").replace("]", "").replace("\"", "").strip()
            self.subCategoryMenu.setEnabled(True)
            self.getCategoryText(self.categoryMenu.currentText())
            logger.info("Sub-Category Menu generated. Ready for selection")

    def getSubCategoryName(self):
        name = self.subCategoryMenu.currentText()
        ws.categoryName = self.categoryMenu.currentText()
        ws.subCategoryName = self.subCategoryMenu.currentText()
        if self.subCategoryMenu.currentIndex() > 0:
            self.messageLabel.setText(
                "You have selected the following sub-category : " + name + "\n You may begin the scraping process.")
            QtGui.QGuiApplication.processEvents()
        return str(name)

    def startScraping(self):
        try:
            ws.removePopUp()
        finally:

            time.sleep(1)
            ws.newFileName = self.getSubCategoryName()
            ws.scrapeSubCategory(self.getSubCategoryName())
            logger.info("Scraping Process completed.")
            self.showPopUP()
            self.messageLabel.setText("Scraping Process has completed.\n Thank you.")
            time.sleep(2)
            self.initialize()

    def initialize(self):
        self.consumerRB.setChecked(False)
        self.restaurantsRB.setChecked(False)
        self.industrialRB.setChecked(False)
        self.businessRB.setChecked(False)
        self.industrialRB.setChecked(False)
        self.automotiveRB.setChecked(False)
        ws.getBaseURL()
        self.categoryMenu.setCurrentIndex(0)
        self.subCategoryMenu.clear()
        self.subCategoryMenu.addItem("Select a sub-category")
        self.categoryMenu.setEnabled(False)
        self.subCategoryMenu.setEnabled(False)
        logger.info("Process has restarted. User may select new industry.")


# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    logger.info("Web Scraping software initialised.")
    ws.removePopUp()

    sys.exit(app.exec_())