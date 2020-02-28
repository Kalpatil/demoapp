from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1366, 768))
display.start()
browser = webdriver.Firefox()
browser.get('http://13.235.69.192:8081/')
print browser.title
browser.quit()

display.stop()
