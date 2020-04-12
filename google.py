import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox(executable_path="/Users/ricascross/Desktop/projects/google_search/geckodriver")



def google_search():
    arg = str(sys.argv[2])
    input_search_bar = browser.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input")
    input_search_bar.send_keys(arg, Keys.ENTER)
    

def google_image():
    arg = str(sys.argv[2])
    images = browser.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[1]/div[2]/a")
    images.click()
    input_image_search = browser.find_element_by_xpath("/html/body/div/div[3]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
    input_image_search.send_keys(arg, Keys.ENTER)



if __name__ == "__main__":
    browser.maximize_window()

    browser.get('https://www.google.pt')

    if(sys.argv[1] == '-s'): google_search()
    elif(sys.argv[1] == '-i'): google_image()

    time.sleep(120)
    browser.quit()

    
