from bs4 import BeautifulSoup
import os
from selenium import webdriver

from pymet import collection
from pymet.utils import constants


paintings = collection.MetPaintings()
works = paintings.get_works_by_artist('gogh')

path = os.path.join(constants.Urls.MET_ROOT, str(works[1].object_id))

driver8 = webdriver.Chrome('/Users/Andrew/wip/webdrivers/chromedriver')
driver8.set_window_size(1440, 900)
driver8.get(path)
image = driver8.find_element_by_id('artwork__image')

print(image)
