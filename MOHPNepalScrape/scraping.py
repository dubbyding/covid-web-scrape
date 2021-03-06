from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from platform import system
import threading
from os import path
from time import sleep
from .firebaseDatabaseControl import firebase_database_initializing
from datetime import date


class covidScraping():
    def __init__(self):
        # Go to covid dashboard of Ministry of health Nepal
        self.url = "https://covid19.mohp.gov.np/"
        options = Options()
        options.headless = True   # keep this false in the case of debugging
        options.add_argument("--disable-blink-features=AutomationControlled")
        current_directory = path.dirname(path.realpath(__file__))
        chromedriver = path.join(current_directory, "chromedriver")
        if system() == "Windows":
            chromedriver = chromedriver + ".exe"
        self.driver = webdriver.Chrome(options=options, executable_path=chromedriver)
        self.driver.minimize_window()
        self.date_today = date.today().strftime("%Y/%m/%d")
        not_complete=True
        while(not_complete):
            try:
                self.driver.get(self.url)
                try:
                    # Delay the other working so that page can load
                    myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
                except:
                    pass
                not_complete=False
            except Exception as e:
                pass

    def get_district_data(self):
        list_empty_status = True
        counter = 0
        while list_empty_status:
            data_part = self.driver.find_elements_by_css_selector("div.ant-card-body div.ant-card-grid")
            list_of_cases = []
            if data_part:
                list_empty_status = False
            else:
                counter += 1
                print(counter)
                sleep(20)
            if counter == 10:
                return 0
        for district in data_part:
            district.find_elements_by_css_selector("span b")
            list_of_cases.append(district.text)
        for location_cases in list_of_cases:
            cases_list = location_cases.split("\n")
            location = cases_list[0]
            number_of_male = int(cases_list[2].split(":")[-1])
            number_of_female = int(cases_list[3].split(":")[-1])
            dict_of_cases = {}
            for variable in ["location", "number_of_male", "number_of_female"]:
                dict_of_cases[variable]=eval(variable)
            dict_of_cases["Date"] = self.date_today
            todb = firebase_database_initializing()
            todb.insertIntoByDistrict(dict_of_cases)
            del todb
    
    def getNewCases(self):
        data_part = self.driver.find_elements_by_css_selector("div.ant-card-body")
        new_cases_dict={}
        for new_cases in data_part:
            cases = new_cases.find_elements_by_css_selector("p")
            if cases[1].text == "New Cases":
                new_cases_dict["New_cases"]=int(cases[0].text)
                new_cases_dict["Date"] = self.date_today
                todb = firebase_database_initializing()
                todb.insertIntoNewCases(new_cases_dict)
                del todb
                break
            else:
                continue
    
    def getTotalCases(self):
        data_part = self.driver.find_elements_by_css_selector("div.ant-card-body")
        total_cases_dict={}
        for new_cases in data_part:
            cases = new_cases.find_elements_by_css_selector("p")
            if cases[1].text == "Total Cases":
                total_cases_dict["Total_cases"]=int(cases[0].text)
                total_cases_dict["Date"] = self.date_today
                todb = firebase_database_initializing()
                todb.insertIntoTotalCases(total_cases_dict)
                del todb
                break
            else:
                continue

    def getTotalDeaths(self):
        data_part = self.driver.find_elements_by_css_selector("div.ant-card-body")
        total_deaths_dict={}
        for new_cases in data_part:
            cases = new_cases.find_elements_by_css_selector("p")
            if cases[1].text == "Deaths":
                total_deaths_dict["Total_deaths"]=int(cases[0].text)
                total_deaths_dict["Date"] = self.date_today
                todb = firebase_database_initializing()
                todb.insertIntoTotalDeaths(total_deaths_dict)
                del todb
                break
            else:
                continue
    
    def getTotalRecovered(self):
        data_part = self.driver.find_elements_by_css_selector("div.ant-card-body")
        total_recovered_dict={}
        for new_cases in data_part:
            cases = new_cases.find_elements_by_css_selector("p")
            if cases[1].text == "Recovered":
                total_recovered_dict["Total_recovered"]=int(cases[0].text)
                total_recovered_dict["Date"] = self.date_today
                todb = firebase_database_initializing()
                todb.insertIntoTotalRecovered(total_recovered_dict)
                del todb
                break
            else:
                continue

    def refresh_page(self):
        print("Refreshing Page")
        sleep(20)
        not_complete=True
        while(not_complete):
            try:
                self.driver.get(self.url)
                try:
                    # Delay the other working so that page can load
                    myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
                except:
                    pass

                not_complete=False
            except Exception as e:
                pass
    
    def __del__(self):
        self.driver.close()

if __name__ == "__main__":
    execution_Status = True
    def executing():
        initializing = covidScraping()
        while execution_Status:
            # initializing.get_district_data()
            initializing.getNewCases()
            initializing.getTotalCases()
            initializing.getTotalDeaths()
            initializing.getTotalRecovered()
            initializing.refresh_page()
        del initializing

    def interrupt():
        global execution_Status
        while execution_Status:
            if input("You can type 's' to stop this execution anytime \n") == 's':
                print("Stopping After this Iteration")
                execution_Status = False
    t1 = threading.Thread(target=executing)
    t1.start()
    interrupt()
    t1.join()