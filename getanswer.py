import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service


from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

class Fetcher:
    def __init__(self, url):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        service = Service("./chrome/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 5)
        self.url = url

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "gsfi")
            ))
        except:
            print("Loading")
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        answer = soup.find_all(class_="hgKElc")

        if not answer:
            answer = soup.find_all(class_="uJm78b")

        if not answer:
            answer = "I don't Know sorry!"
        self.driver.quit()
        return answer[0].get_text()


