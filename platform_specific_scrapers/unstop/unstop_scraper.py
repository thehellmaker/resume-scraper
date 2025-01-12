from selenium_utils.selenium_helper import driver
from llm.openai_helper import client
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
from pathlib import Path
import os

def open_unstop_manage_candidates_page(driver, job_link):
    driver.get(job_link)    
    sleep(15)

def open_each_candidate_and_download_resume(driver, name_web_element, name):
    os.makedirs("resumes", exist_ok=True)
    resume_file_path = Path(f"resumes/{name}.pdf")
    my_file = Path(resume_file_path)
    if my_file.is_file():
        return
    name_web_element.click()
    driver.implicitly_wait(10)
    profile_link = driver.find_element(By.XPATH, "//a[.//span[text()='Profile']]")
    profile_link.click()
    driver.implicitly_wait(10)
    resume_link_element = driver.find_element(By.LINK_TEXT, "download file from here")
    resume_link = resume_link_element.get_attribute("href")
    urllib.request.urlretrieve(resume_link, resume_file_path)
    back_button = driver.find_element(By.XPATH, "//span[.//em[text()='keyboard_backspace']]")
    back_button.click()

def download_resumes_for_all_candidates_on_page(driver):
    table = driver.find_elements(By.TAG_NAME, "table");
    tr_list=table[0].find_elements(By.TAG_NAME, "tr")
    for tr in tr_list:
        try:
            td_list = tr.find_elements(By.TAG_NAME, "td")
            if(len(td_list) < 3):
                continue
            
            name_web_element = td_list[2]
            print("=============================================")
            print(name_web_element.text)
            print("=============================================")
            name = name_web_element.text.replace("\\", "").replace("/", "").replace("\n", "_").replace("visibility_off_", "").replace(" ", "_").replace(",", "")
            print("Name", name)
            open_each_candidate_and_download_resume(driver, name_web_element, name)
        except Exception as e:
            print(e)

def scrape_unstop_resumes(job_link):
    open_unstop_manage_candidates_page(driver, job_link)
    while True:
        try:
            download_resumes_for_all_candidates_on_page(driver)
            sleep(2)
            next_button = driver.find_element(By.CLASS_NAME, "right-arrow")
            if "disabled" in next_button.get_attribute("class").split(" "):
                break
            next_button.click()
            sleep(2)
        except Exception as e:
            print(e)
    driver.quit()