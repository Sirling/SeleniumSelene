
from selene.api import *
from selene.browser import set_driver, driver
from selenium import webdriver

from SeleniumPart.selene_part.components.top_menu import top_menu


def setup():
    set_driver(webdriver.Chrome())


def teardown():
    driver().quit()


class TestSilpoSelene:

    def test_selene(self):
        top_menu.s('.search').click()
        s(".side-menu-search").should(be.visible)

        s(".side-menu-search input").set_value("вода").press_enter()
        s(".search-form__result span").should(have.text("10 результатів за запитом"))

        search_list = ss(".search-results li")
        for item in search_list:
            item.should(have.text("вода"))

