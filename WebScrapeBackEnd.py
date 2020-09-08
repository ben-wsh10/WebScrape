from datetime import date
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd
from bs4 import BeautifulSoup
import re
from datetime import datetime
import logging

# Logging information
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s : %(asctime)s : %(message)s')
fileHandler = logging.FileHandler('LogFile.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)



currentDateTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
popUpCounter = 0
categoryCounter = 0
categoryList = []
subCategoryCounter = 0
catSubCatDictionary = {}
scrappingDictionary = {}
nameLinkPair = {}
isRestaurant = False
isMedical = False
isAutomotive = False
newFileName = ""
industryName = ""
categoryName = ""
subCategoryName = ""
filename = "webscrape.csv"
fields = ['Company Name', 'Company Contact', 'Company Address', 'Sub-Category / Category', 'Industry']


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

directory = os.path.dirname(__file__)


try:
    PATH = r"C:\WebScrape\chromedriver.exe"
except:
    logger.exception("Unable to get chromedriver path")

driver = webdriver.Chrome(options=options, executable_path=PATH)
driver.get("https://www.streetdirectory.com/businessfinder/")

logger.info("Chromedriver found. Executing Chromedriver.exe")

def createCSV():
    try:
        with open(filename, 'w', encoding='utf-8') as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow(fields)
    except:
        logger.exception("Create CSV error.")

# Removes pop up that usually appears 5 times in a session
def removePopUp() :
    try:
        global popUpCounter
        while popUpCounter < 5 :
            try:
                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.ID, "popup_top_background"))
                ).click()
                driver.back()
                popUpCounter += 1
                logger.info("Removed Pop Up " + str(popUpCounter) + " times. If Pop Up counter reaches 5, Pop up will be permanently cleared.")
            except:
                popUpCounter = 6

    except:
        logger.exception("Pop up failure")


# Redirect to sub-category page and select List View
def scrapePreparation() :
    try:
        # find the "List by Companies" button
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.LINK_TEXT, "List by Companies"))
        )
        # select the "List View" link
        element.click()
    except:
        pass
    finally:
        # find the "List View" button
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.LINK_TEXT, "List View"))
        )
        # select the "List View" link
        element.click()
        logger.info("Selected List View. Ready for Scrape.")

# Scrape current URL
def scrape():
    try:
        global newFileName
        # find all general details within the html page
        companyNames = driver.find_elements_by_xpath("//*[@class='listing_company_name']") # General search for company names
        if len(companyNames) == 0: # Fine-tuning for some directory web pages to search for company names
            companyNames = driver.find_elements_by_class_name("listing_company_name")
        phoneIcons = driver.find_elements_by_xpath("//img[contains(@src,'https://x2.sdimgs.com/img/business_finder/tel-icon.png')]")
        companyAddresses = driver.find_elements_by_xpath("//*[@id='tr_address']")

        logger.info("General details retrieved for scraping.")

        # Count total number of directories per page
        countName = len(companyNames)
        countNumber = len(phoneIcons)
        countAddress = len(companyAddresses)
        counter = max(countName, countNumber, countAddress)
        subCatAndCatName = subCategoryName + " / " + categoryName

        # Extracting relevant details from xpath elements based on number of companies listed per page
        for _ in range(counter):
            # Scrape company name
            companyName = companyNames[_].text

            # Scrape company contact
            attributes = phoneIcons[_].get_attribute('onclick').split()
            # Fine-tuning search results
            if attributes[14] == "\'(65)" or attributes[14] == "\'65" or attributes[14] == "\'6" :
                getNumber = re.findall(r'\d+', attributes[15])
                for _ in getNumber:
                    if len(_) == 8:
                        companyNumber = re.findall(r'\d+', attributes[15])
                        companyNumber = " ".join(companyNumber)
                        companyNumber = companyNumber[:4] + " " + companyNumber[4:]
                    else:
                        companyNumber = (attributes[15] + " " + attributes[16]).replace("\'", "").replace(";", "").replace("-", " ")
            # Fine-tuning search results
            elif attributes[15] == "dcl_val.ga":
                if len(attributes[14]) == 11:
                    companyNumber = (attributes[13] + " " + attributes[14]).replace("\'", "").replace(";", "").replace("-", " ")
                    companyNumber = companyNumber[2:]
                else:
                    companyNumber = str("Nil")
            # General search for company results
            elif attributes[15] != "dcl_val.ga":
                companyNumber = re.findall(r'\d+', (attributes[14] + attributes[15]))
                companyNumber = " ".join(companyNumber)
                companyNumber = companyNumber[:4] + " " + companyNumber[4:]
            # No number listed
            else:
                companyNumber = str("Nil")

            # Scrape company address
            try:
                address = companyAddresses[_].text.replace("Address", "").replace(":", "").strip()
            except:
                address = "Nil"

            # Store company details in a list : Name, Contact, Physical Address, sub-category & category, Industry
            rows = [str([companyName])[2:-2], str([companyNumber])[2:-2], str([address])[2:-2], str(subCatAndCatName), str(industryName)]

            # Append company details into csv file
            with open(filename, 'a+', newline='', encoding='utf-8') as csvFile:
                write = csv.writer(csvFile)
                write.writerow(rows)
        logger.info("Scraping for current Page completed.")
    except :
        logger.exception("Scraping requires fine-tuning.")

# Navigate to the next page, if any
def navigateToNextPage():
    try:
        # current Page Number
        currentPageNumber = 1
        # base directory (without page number)
        baseURL = driver.current_url
        # Previous page, used to check if end of page has reached
        previousPage = baseURL + "All" + "/" + str(currentPageNumber) + "/"
        # Redirect to the next page, if any
        currentPageNumber += 1
        currentURL = baseURL + "All" + "/" + str(currentPageNumber) + "/"
        driver.get(currentURL)
        # check if web page is re-directed to next page. If end of page has reached, web page will be auto redirected to previous page
        while previousPage != driver.current_url :
            scrape()
            previousPage = baseURL + "All" + "/" + str(currentPageNumber) + "/"
            currentPageNumber += 1
            currentURL = baseURL + "All" + "/" + str(currentPageNumber) + "/"
            driver.get(currentURL)
    except:
        logger.exception("Navigating to next page error.")

# Get the Starting Page, for restarting purposes
def getBaseURL():
    try:
        driver.get("https://www.streetdirectory.com/businessfinder/")
        logger.info("Returned to starting page.")
    except :
        logger.exception("Return to starting page issue.")

# Direct to the respective industry Page
def setPage(industryName):
    try:
        global categoryCounter
        global categoryList

        try:
            element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.LINK_TEXT, industryName))
            )

            element.click()
            # Refresh category dropdown menu based on selected industry
            categoryCounter = 0
            categoryList = ["Select a category"]
            getCategory()
        except:
            driver.get("https://www.streetdirectory.com/businessfinder/")
            element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.LINK_TEXT, industryName))
            )
            element.click()
            # Refresh category dropdown menu based on selected industry
            categoryCounter = 0
            categoryList = ["Select a category"]
            getCategory()
    except :
        logger.exception("Re-direct to " + industryName + " error.")

# Populate a list of category based on selected industry
def getCategory():
    try:
        global categoryCounter
        global categoryList

        categoryNames = driver.find_elements_by_xpath("//*[@class='TextBold']")

        for _ in categoryNames:
            categoryCounter += 1
            categoryList.append(_.text)

    except:
        logger.exception("Get category list error.")


# Populate a list of sub-category based on selected category
def getSubCategory():
    try:
        global subCategoryCounter

        # Get current page html. Note: Ran into issues using selenium, hence, BeautifulSoup was used instead
        currentURL = driver.current_url
        currentPage = requests.get(currentURL).text
        soup = BeautifulSoup(currentPage, 'html.parser')

        # Retrieve Category names
        content = soup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['TextBold'])

        # Retrieve and store sub-category names into a dictionary
        for keys in content:
            # Different retrieval method was used for "Restaurant" Industry due to a layout difference compared to other industries
            if not isRestaurant:
                # Refresh sub-category list for each new category
                subCategoryValue = []

                values = keys.find_next('tr').find_next('td').find_next_siblings('td')
                for value in values:
                    value = value.find_next('tr').text
                    # Remove any empty sub-category names, if any
                    if value != "":
                        # Append list of sub-category names to respective category names as a key,value pair
                        subCategoryValue.append(value)
                        catSubCatDictionary[keys.text.strip()] = str(subCategoryValue).replace("\\n", "")
            else:
                # Refresh sub-category list for each new category
                subCategoryValue = []

                values = keys.find_next('tr').find_next('td').find_next_siblings('td')
                for value in values:
                    value = value.find_next('div').find_next('div').text.strip()
                    # Remove any empty sub-category names, if any
                    if value != "":
                        # Append list of sub-category names to respective category names as a key,value pair
                        subCategoryValue.append(value)
                        catSubCatDictionary[keys.text.strip()] = str(subCategoryValue).replace("\\n", "")
    except:
        logger.exception("Get sub-category list error.")

def formatCSV():
    try:
        # DateTime format
        currentDate = date.today().strftime('%d%b%Y')
        # Remove empty white rows
        df = pd.read_csv('webscrape.csv', engine='python', encoding='utf-8-sig')
        df.to_csv('webscrape.csv', index=False)
        # Rename file
        os.rename(r'webscrape.csv', newFileName + str(currentDate) + r'.csv')
    except:
        logger.exception("formatting csv error.")

# Entire scraping process
def scrapeProcess():
    scrapePreparation()
    scrape()
    navigateToNextPage()


# Retrieve required links to scrape, based on what sub-category user has chosen
def getLink():
    try:
        global scrappingDictionary
        global nameLinkPair
        # Get current page html. Note: Ran into issues using selenium, hence, BeautifulSoup was used instead
        currentURL = driver.current_url
        currentPage = requests.get(currentURL).text
        soup = BeautifulSoup(currentPage, 'html.parser')

        # Retrieve information about category and sub-category
        content = soup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['main_cat_mp'])
        # print(content)
        count = 0
        subCatLinks = []
        nameLinkPair = {}
        scrappingDictionary = {}

        for keys in content:
            if not isRestaurant and not isMedical and not isAutomotive :
                # Retrieve key (Name of all sub-category links)
                key = keys.find_next('a').text
            elif isRestaurant:
                key = keys.find_next('div').find_next('div').text
                key = key.strip()
            elif isMedical or isAutomotive:
                key = keys.find_next('td').text
            # Retrieve value (<a tags of all sub-category)
            value = keys.find_all('a')
            for _ in value:
                # List of all sub-category links
                if _.get('href') != "javascript:void(0)":
                    subCatLinks.append(_.get('href'))
                    # Store respective sub-category name and link as key,value pair
                    nameLinkPair[_.text] = _.get('href')
                    count += 1
            specificSubCatLinks = []
            for _ in range(count):
                # Retrieve and store all links required for scrapping, based on the respective sub-category name user has chosen
                if key in nameLinkPair:
                    specificSubCatLinks.append(subCatLinks[_])
                    nameLinkPair.pop(key)
                else:
                    specificSubCatLinks.append(subCatLinks[_])
                    # Stores all links to be scrapped, based on the respective sub-category name user has chosen
                    scrappingDictionary[key.strip()] = specificSubCatLinks

            count = 0
            subCatLinks = []
    except:
        logger.exception("Getting links error.")


def scrapeSubCategory(link):
    try:
        scrapeAllowed = True
        createCSV()
        scrapeList = scrappingDictionary[link]
        listCounter = len(scrapeList)
        # BlackListed URLs [Not able to scrape]
        prohibitedURL = ["https://www.streetdirectory.com/businessfinder/product_listing.php?q=real+estate&by=product",
                         "https://www.streetdirectory.com/businessfinder/",
                         "https://www.streetdirectory.com/restaurant/",
                         "https://www.streetdirectory.com/industrial/",
                         "https://www.streetdirectory.com/businessfinder/business/",
                         "https://www.streetdirectory.com/medical/",
                         "https://www.streetdirectory.com/automotive/",
                         "https://www.streetdirectory.com/yoshinoya",
                         "https://www.streetdirectory.com/Starbucks",
                         "https://www.streetdirectory.com/pizzahut",
                         "https://www.streetdirectory.com/canadian/",
                         "https://www.streetdirectory.com/ritepizza"
                         ]
        for _ in range(listCounter):
            # Fine-tuning url results
            if scrapeList[_] == "https://www.streetdirectory.com/businessfinder/company/7947/Japanese/":
                driver.get("https://www.streetdirectory.com/businessfinder/preview/4062/Japanese_Food/")
            # General url results
            else:
                driver.get(scrapeList[_])

            scrapeURL = str(driver.current_url)
            for url in prohibitedURL:
                if scrapeURL == url:
                    scrapeAllowed = False
                    break
            if scrapeAllowed:
                scrapeProcess()
            else:
                scrapeAllowed = True

        formatCSV()
    except:
        logger.exception("Check scraping for the particular link error.")