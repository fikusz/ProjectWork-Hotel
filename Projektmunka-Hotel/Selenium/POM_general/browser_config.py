from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def get_driver(browser_name):
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("dom.webdriver.enabled", False)  # Example preference
        browser = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument('--disable-search-engine-choice-screen')
        browser = webdriver.Edge(options=options)

    # options.add_argument('window-position=2000,0')
    # options.add_argument("--lang=en")
    # options.add_argument("--lang=hu")
    browser.maximize_window()
    return browser


