from demo.models import Routes
from splinter import Browser

if __name__ == "__main__":
    browser = Browser('chrome', headless=True)
    browser.visit("https://angkot.web.id/#/")
    locations = browser.find_by_css(".number")

    for location in locations:
        location.click()
        print("Currently on origin {} and destination {} ".format(browser.find_by_css(".origin").text,
                                                                  browser.find_by_css(".destination").text))
        Routes.objects.create(origin=browser.find_by_css(".origin").text,
                              destination=browser.find_by_css(".destination").text,
                              routes=browser.find_by_css(".route").text)
