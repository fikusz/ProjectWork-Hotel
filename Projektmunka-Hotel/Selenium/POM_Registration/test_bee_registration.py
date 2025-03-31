import time
import pytest
from Selenium.POM_Registration.page_main_registration import ReactFormPage
from Selenium.POM_general.data_converting_to_selenium import get_string_of_doom
from Selenium.POM_general.data_converting_to_selenium import get_automated_logins



import os
os.environ['DISPLAY'] = ':0'
old_display_var = os.environ['DISPLAY'] if 'DISPLAY' in os.environ else ':0'


URL = 'http://localhost:4200/'



data_first_name  = "Nagy"
data_last_name = "Balázs"
data_phone= "06704550735"
data_email = f"teszt{int(time.time())}@gmail.com"
data_zip_code = "1188"
data_city = "Budapest"
data_password = "aBC12345"
data_address = "Vezér utca 5."

browser_types = [ "firefox", "edge","chrome"]
# browser_types = ["chrome"]

@pytest.fixture(autouse=True)
def setup_page(request):
    browser = request.param
    request.instance.browser = browser
    request.instance.page = ReactFormPage(browser)
    request.instance.page.open(URL)
    yield
    # pass
    request.instance.page.close()

@pytest.mark.parametrize("setup_page", browser_types, indirect=True)
class TestTC:

    # register users
    def test_register_users(self,request):
        global wrong_input_type
        browser = self.browser
        registered_users = get_automated_logins()
        print()
        i = 0
        while i < (len(registered_users)*2):
            data_email = f"teszt{int(time.time())}@gmail.com"

            self.page.button_register().click()
            if (i == 0):
                self.page.browser.execute_script("window.scrollBy(0, 100);")

            self.page.input_firstname().clear()
            self.page.input_firstname().send_keys(registered_users["data_first_name"][i])

            self.page.input_lastname().clear()
            self.page.input_lastname().send_keys(registered_users["data_last_name"][i])

            self.page.input_phone().clear()
            self.page.input_phone().send_keys(registered_users["data_phone"][i])

            self.page.input_email().clear()
            self.page.input_email().send_keys(str(int(time.time())),registered_users["data_email"][i])

            self.page.input_password().clear()
            self.page.input_password().send_keys(registered_users["data_password"][i])

            self.page.input_zip_code().clear()
            self.page.input_zip_code().send_keys(registered_users["data_zip_code"][i])

            self.page.input_city().clear()
            self.page.input_city().send_keys(registered_users["data_city"][i])

            self.page.input_address().clear()
            self.page.input_address().send_keys(registered_users["data_address"][i])

            i += 1
            try:
                wrong_input_type = None
                wrong_input_type = self.page.text_wrong_input()
                assert wrong_input_type == None
            except AssertionError:
                print("⚠️ AssertionError: A ",browser," böngészőben, ", i+1, " sorban, ez nem volt jó: ", wrong_input_type.text)
                self.page.input_lastname().clear()
                continue

            self.page.dropbar_role().click()
            self.page.dropbar_beekeeper().click()


            self.page.button_submit().click()
        time.sleep(0.2)

    def test_stringtest(self):
        global current_string
        data_string_of_doom = get_string_of_doom()

        i = 0
        while i < (len(data_string_of_doom)):
            data_email = f"teszt{int(time.time())}@gmail.com"
            self.page.button_register().click()
            self.page.input_lastname().clear()

            if (i != 0):
                succesful_registration = self.page.input_firstname_check().get_attribute("value")
                try:
                    assert succesful_registration != "Nagy"
                except AssertionError:
                    print("⚠️ AssertionError:ebben a sorban:"
                          , i, "ezek nem voltak jók: ", data_string_of_doom[i - 1])
                    pass

            if (i == 0):
                self.page.browser.execute_script("window.scrollBy(0, 100);")

            self.page.input_firstname().clear()
            self.page.input_firstname().send_keys(data_first_name)

            try:
                self.page.input_lastname().send_keys(data_string_of_doom[i])
            except AssertionError:
                print("⚠️ AssertionError:ebben a sorban: "
                      , i, "ezek nem voltak jók: ", data_string_of_doom[i - 1], "got", repr(current_string))

            if (i != 0):
                current_string = self.page.input_lastname().get_attribute("value")
                try:
                    assert current_string == data_string_of_doom[i]
                except AssertionError:
                    print("⚠️ AssertionError:ebben a sorban: "
                          ,i,"ezek nem voltak jók: ",data_string_of_doom[i-1],"got",repr(current_string))
                    self.page.input_lastname().clear()
                    i += 1
                    continue

            self.page.input_phone().clear()
            self.page.input_phone().send_keys(data_phone)

            self.page.input_email().clear()
            self.page.input_email().send_keys(data_email)

            self.page.input_password().clear()
            self.page.input_password().send_keys(data_password)

            self.page.input_zip_code().clear()
            self.page.input_zip_code().send_keys(data_zip_code)

            self.page.input_city().clear()
            self.page.input_city().send_keys(data_city)

            self.page.input_address().clear()
            self.page.input_address().send_keys(data_address)

            self.page.dropbar_role().click()
            self.page.dropbar_beekeeper().click()

            self.page.button_submit().click()

            i += 1
            time.sleep(0.2)

