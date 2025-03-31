from selenium.webdriver import Chrome

URL = 'http://localhost:4200/'

class GeneralPage:
    def __init__(self,browser: Chrome,url):
        self.browser = browser
        self.url = url

    def open(self,x):
        self.browser.get(x)
        self.browser.maximize_window()

    def quit(self):
        self.browser.quit()

    def close(self):
        self.browser.close()

    def title(self):
        return self.browser.title

    def current_url(self):
        return self.current_url()

