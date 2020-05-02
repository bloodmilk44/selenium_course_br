from selenium import webdriver
from selenium.webdriver.common.by import By
from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "group page").click()

    def open_group_page(self):
        if not (self.app.driver.current_url.endswith("/groups.php") and len(self.app.driver.find_elements(By.NAME, "new")) > 0):
            self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        self.open_group_page()
        # init group creation
        self.app.driver.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creation
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        # fill group form
        self.change_fiel_value("group_name", group.name)
        self.change_fiel_value("group_header", group.header)
        self.change_fiel_value("group_footer", group.footer)

    def change_fiel_value(self, field_name, text):
        if text is not None:
            self.app.driver.find_element(By.NAME, field_name).click()
            self.app.driver.find_element(By.NAME, field_name).send_keys(text)


    def delete_first_group(self):
        self.delete_group_by_index(0)


    def modify_first_group(self):
        self.modify_group_by_index(0)


    def delete_group_by_id(self, id):
        self.open_group_page()
        self.select_group_by_id(id)
        # submit delete
        self.app.driver.find_element(By.NAME, "delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_first_group(self):
        self.app.driver.find_element(By.NAME, "selected[]").click()


    def select_group_by_index(self, index):
        self.app.driver.find_elements(By.NAME, "selected[]")[index].click()

    def select_group_by_id(self, id):
        self.app.driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()


    def modify_group_by_index(self, index, new_group_data):
        self.open_group_page()
        self.select_group_by_index(index)
        # open modification form
        self.app.driver.find_element(By.NAME, "edit").click()
        # fill group form
        self.app.driver.find_element(By.NAME, "group_name").clear()
        self.fill_group_form(new_group_data)
        # submit modification
        self.app.driver.find_element(By.NAME, "update").click()
        self.return_to_group_page()
        self.group_cache = None


    def count(self):
        self.open_group_page()
        return len(self.app.driver.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            self.open_group_page()
            self.group_cache = []
            for element in self.app.driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


    def delete_group_by_index(self, index):
        self.open_group_page()
        self.select_group_by_index(index)
        # submit delete
        self.app.driver.find_element(By.NAME, "delete").click()
        self.return_to_group_page()
        self.group_cache = None

