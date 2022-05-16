from django.core.management import CommandError, BaseCommand
import random
import threading
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import randint
from textwrap import wrap
from selenium.common.exceptions import TimeoutException
import chromedriver_autoinstaller

from firstapp.models import Data

chromedriver_autoinstaller.install()


class Command(BaseCommand):
    help = 'Scape data from wikipedia'

    def handle(self, *args, **options):
        driver = webdriver.Chrome()
       
        Data.objects.all().delete()
        i = 0
        while i <= 10:
            try:
                driver.get('https://en.wikipedia.org/wiki/Special:Random')
                driver.set_window_size(1853, 1053)
                heading = driver.find_element(By.ID, "firstHeading").text
                description = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]').text
                img_url = driver.find_element(By.CSS_SELECTOR, ".infobox-image img").get_attribute("src")

                Data.objects.create(heading=heading, description=description, imgUrl=img_url)
                i =  i+1
            except:
                pass


