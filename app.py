import re
import mechanicalsoup
import datetime
now = datetime.datetime.now()
# print str(now.year, str(now.month, str(now.day, str(now.hour, str(now.minute, str(now.second

# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     browser = mechanicalsoup.StatefulBrowser()
#     browser.open('https://countyballotfiles.elections.myflorida.com/FVRSCountyBallotReports/AbsenteeEarlyVotingReports/PublicStats')
#     links = browser.links(link_text=' Download File ')
#     for link in links:
#         print(link)
#         link_name = str(link)
#         dl_name = (str(now.year) + '-' + str(now.month) + '-' + str(now.day )+ '-' + str(now.hour) + '-' + str(now.minute) + '-' + re.search('countyballotreportfiles/(.*).txt', link_name).group(1))
#
#         browser.download_link(link=link, file=(dl_name+'.txt'))
#     return ('Downloaded: ' + str(links))

browser = mechanicalsoup.StatefulBrowser()
browser.open('https://countyballotfiles.elections.myflorida.com/FVRSCountyBallotReports/AbsenteeEarlyVotingReports/PublicStats')
links = browser.links(link_text=' Download File ')
for link in links:
    print(link)
    link_name = str(link)
    dl_name = (str(now.year) + '-' + str(now.month) + '-' + str(now.day )+ '-' + str(now.hour) + '-' + str(now.minute) + '-' + re.search('countyballotreportfiles/(.*).txt', link_name).group(1))

    browser.download_link(link=link, file=(dl_name+'.txt'))
