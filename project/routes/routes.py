from flask import Blueprint, render_template, redirect, url_for, abort, request, jsonify, flash
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

from extensions import extensions
# from sqlalchemy import desc, asc, func
# from sqlalchemy import and_, or_
# from flask_socketio import SocketIO, emit
# from datetime import datetime

db = extensions.db
# db.create_all()
# db.session.commit()
home = Blueprint('home', __name__, template_folder='templates')

socketio = extensions.socketio


@home.route('/')
def home_view():
    return render_template('home.html')


@home.route('/competition_site')
def competition_site():
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    driver.get("https://www.flashscorekz.com/basketball/")

    driver.implicitly_wait(10)
    # жмем на кнопку принять куки.
    try:
        driver.find_element("id", 'onetrust-accept-btn-handler').click()
    except Exception as e:
        print("accept_all_button exception ", e)
    tabs = driver.find_elements("xpath", "//div[@class='filters__text filters__text--default']")
    for tab in tabs:
        tab_name = tab.text
        if tab_name.lower() == "завершенные":
            tab.click()


    driver.implicitly_wait(10)

    table_type_1 = "//div[@class='event__match event__match--twoLine']"
    for match_table in driver.find_elements("xpath", table_type_1):
        id = match_table.get_attribute("id")
        home_team_xpath_txt = "// *[ @ id = '" + id + "']/div[@class='event__participant event__participant--home fontExtraBold']"
        home_team_final_score_xpath_txt = "// *[ @ id = '" + id + "']/div[@class='event__score event__score--home']"

        away_team_xpath_txt = "// *[ @ id = '" + id + "']/div[@class='event__participant event__participant--away']"
        away_team_final_score_xpath_txt = "// *[ @ id = '" + id + "']/div[@class='event__score event__score--away']"

        try:
            home_team = driver.find_element("xpath", home_team_xpath_txt).text
            home_team_final_score = driver.find_element("xpath", home_team_final_score_xpath_txt).text
            away_team = driver.find_element("xpath", away_team_xpath_txt).text
            away_team_final_score = driver.find_element("xpath", away_team_final_score_xpath_txt).text

            print(home_team, home_team_final_score, away_team, away_team_final_score)
        except:
            pass




    return "test"
