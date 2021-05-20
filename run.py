from MOHPNepalScrape.scraping import covidScraping
import threading
execution_Status = True
def gettingDistrictData():
    initializing = covidScraping()
    while execution_Status:
        initializing.get_district_data()
        if execution_Status:
            initializing.refresh_page()
    del initializing
    print("End of getting district datas")

def gettingOtherData():
    initializing = covidScraping()
    while execution_Status:
        initializing.getNewCases()
        initializing.getTotalCases()
        initializing.getTotalDeaths()
        initializing.getTotalRecovered()
        if execution_Status:
            initializing.refresh_page()
    del initializing
    print("End of getting Other datas")

def interrupt():
    global execution_Status
    while execution_Status:
        if input("You can type 's' to stop this execution anytime \n") == 's':
            print("Stopping After this Iteration")
            execution_Status = False
t1 = threading.Thread(target=gettingDistrictData)
t2 = threading.Thread(target=gettingOtherData)
t1.start()
t2.start()
interrupt()
t1.join()
t2.join()