from scraping import covidScraping
import threading
execution_Status = True
def gettingDistrictData():
    initializing = covidScraping()
    while execution_Status:
        initializing.get_district_data()
        initializing.refresh_page()
    del initializing

def gettingOtherData():
    initializing = covidScraping()
    while execution_Status:
        initializing.getNewCases()
        initializing.refresh_page()
    del initializing

def interrupt():
    global execution_Status
    while execution_Status:
        if input("You can type 's' to stop this execution anytime \n") == 's':
            print("Stopping After this Iteration")
            execution_Status = False
t1 = threading.Thread(target=gettingDistrictData)
t2 = threading.Thread(target=gettingOtherData)
t1.start()
interrupt()