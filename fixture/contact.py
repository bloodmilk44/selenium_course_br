from model.contact import Contact
from selenium.webdriver.common.by import By
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def change_field_value(self, field_name, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).send_keys(text)

    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            self.app.open_home_page()
            self.contact_cache = []
            for row in self.app.driver.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                firstname = cells[1].text
                lastname = cells[2].text
                id2 = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id2,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        self.app.open_home_page()
        row = self.app.driver.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        self.app.open_home_page()
        row = self.app.driver.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        firstname = self.app.driver.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = self.app.driver.find_element(By.NAME, "lastname").get_attribute("value")
        id = self.app.driver.find_element(By.NAME, "id").get_attribute("value")
        homephone = self.app.driver.find_element(By.NAME, "home").get_attribute("value")
        workphone = self.app.driver.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = self.app.driver.find_element(By.NAME, "mobile").get_attribute("value")
        secondaryphone = self.app.driver.find_element(By.NAME, "phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)


    def get_contact_from_view_page(self, index):
        self.open_contact_view_by_index(index)
        text = self.app.driver.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)