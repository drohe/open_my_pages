from selenium import webdriver


pages = [
#insert your URLs here as strings ('') separating them with a comma
]
browser = webdriver.Chrome(r'c:/python/chromedriver/chromedriver.exe') # YOU WILL NEED TO INPUT THE PATH TO YOUR CHROMEDRIVER EXECUTABLE FILE IN THE FIRST ARGUMENT. WINDOWS OS MAY REQUIRE USING r BEFORE THE QUOTES AND PUTTING THE ACTUAL .EXE FILE IN THE PATH

### END CHROME DRIVER SETUP



for page in pages:
  browser.get(page)
