from selenium import webdriver
from getpass import getpass
import time
import os
from datetime import date

#check advanced python scheduler at https://apscheduler.readthedocs.io/en/stable/userguide.html

#Or can run it with Windows task Scheduler
#Tutorial:-> https://www.youtube.com/watch?v=n2Cr_YRQk7o
#Create task
#Actions:-> Program/ script: put the location of python.exe file
        #-> Add arguments: script name of script you wanna run "script.py"
        #Start in: location of script you wanna run
#Trigger: set the time
#Disadvantage of Windows task scheduler: PC must be on

#This one is done by the first scheduler

#How to use Heroku
#sign up
#install heroku on your device and restart cmd so that heroku can be added to path
#create new app
#Follow instructions on deploy tab as indicated below...
#First create requirements.txt file with all things that were installed with pip
#Next create a Procfile and add the command that you would use to run your script with
#Then go to your command prompt (locally) and type
#--heroku login or heroku login -i
#--heroku git:clone -a respublica-bot (where respublica-bot is your heroku app name )
#--git add .
#--git commit -am "make it better"
#--git push heroku master

#On Heroku, go to settings...
#Add Buildpack
#select Python
#Add Buildpack
#type in: 'https://github.com/heroku/heroku-buildpack-google-chrome'
#Add Buildpack
#type in: 'https://github.com/heroku/heroku-buildpack-chromedriver'
#Then scroll to reveal Config Vars
#KEY = 'CHROMEDRIVER_PATH'; VALUE = '/app/.chromedriver/bin/chromedriver'
#KEY = 'GOOGLE_CHROME_BIN'; VALUE = '/app/.apt/usr/bin/google-chrome';

####article = 'https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/'
####different video: = 'https://www.youtube.com/watch?v=rfdNIOYGYVI'

#Run script via heroku:-> 'heroku run python clock.py to check that it works'

#Schedule it to run automatically by going to resources and on the line under
        #change dyno type, select pencil icon and toggle button to on and confirm


###firefox buildpack:-> 'https://pyronlaboratory.github.io/heroku-integrated-firefox-geckodriver/'

username = "nyoroerick12@gmail.com"
password = "Nyoro1012"



def respublica_bot():

#----------Use below part locally (If you have no server)-------------------------------------------------------

    # PATH = "C:\\Program Files (x86)\\chromedriver.exe"
    # driver = webdriver.Chrome(PATH)#webdriver for this driver is located at path

#----------Use above part locally (If you have no server)-------------------------------------------------------
# 
# 
# ########################################################################################################################    

#----------Use below part on Heroku-------------------------------------------------------    

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        
#----------Use above part on Heroku-------------------------------------------------------


###########################################################################################################################
    driver.get("https://sm.respublica.co.za/login/")

    username_id = driver.find_element_by_id("login")
    username_id.send_keys(username)
    password_id = driver.find_element_by_id("password")
    password_id.send_keys(password)


    login_button = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/div[3]/input')
    login_button.submit()

    my_Covid = driver.find_element_by_xpath('//*[@id="sidebar"]/div/div/ul/li[17]/a')
    my_Covid.click()


    # print(driver.page_source)

    

        #fever
    driver.find_element_by_css_selector("input[type='radio'][name='13'][value='No']").click()
    time.sleep(3)
    #

    #sore throat
    driver.find_element_by_css_selector("input[type='radio'][name='14'][value='No']").click()
    time.sleep(5)

    #dry cough
    driver.find_element_by_css_selector("input[type='radio'][name='15'][value='No']").click()
    time.sleep(1)

    #body aches
    driver.find_element_by_css_selector("input[type='radio'][name='16'][value='No']").click()
    time.sleep(5)

    #fatigue
    driver.find_element_by_css_selector("input[type='radio'][name='17'][value='No']").click()
    time.sleep(2)

    #red eyes
    driver.find_element_by_css_selector("input[type='radio'][name='18'][value='No']").click()
    time.sleep(3)

    #difficulty breathing
    driver.find_element_by_css_selector("input[type='radio'][name='19'][value='No']").click()
    time.sleep(5)

    #headache
    driver.find_element_by_css_selector("input[type='radio'][name='20'][value='No']").click()
    time.sleep(1)

    #vomiting
    driver.find_element_by_css_selector("input[type='radio'][name='21'][value='No']").click()
    time.sleep(2)

    #any covid symptoms
    driver.find_element_by_css_selector("input[type='radio'][name='77'][value='No']").click()
    time.sleep(4)

    #chills
    driver.find_element_by_css_selector("input[type='radio'][name='78'][value='No']").click()
    time.sleep(1)

    #smell or taste
    driver.find_element_by_css_selector("input[type='radio'][name='79'][value='No']").click()
    time.sleep(6)

    #diarrhoea
    driver.find_element_by_css_selector("input[type='radio'][name='80'][value='No']").click()
    time.sleep(1)

    #dizzyness
    driver.find_element_by_css_selector("input[type='radio'][name='81'][value='No']").click()
    time.sleep(2)

    #contact with a person that is testing for covid
    driver.find_element_by_css_selector("input[type='radio'][name='22'][value='No']").click()
    time.sleep(6)
    #contact with a person that has tested positive
    driver.find_element_by_css_selector("input[type='radio'][name='23'][value='No']").click()
    time.sleep(15)




    submit_response = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/form/div[21]/input')
    submit_response.submit()



#     driver.implicitly_wait(10)


    #Check radio buttons status (whether selected or not)
    # status = driver.find_element_by_id().is_selected()  #true-> button is selected, false->not selected
    # if(status):
    #     driver.find_element_by_id().click
#     driver.close()



# respublica_bot()
# driver.implicitly_wait(10)