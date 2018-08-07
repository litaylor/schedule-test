# import re
# import mechanicalsoup
import datetime
now = datetime.datetime.now()

# from os import environ
from flask import Flask

# test_filename = str(now.year) + '-' + str(now.month) + '-' + str(now.day )+ '-' + str(now.hour) + '-' + str(now.minute) + '-test.txt'
#
# with open(test_filename, "w") as text_file:
#     text_file.write('test test test')

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()

# browser = mechanicalsoup.StatefulBrowser()
# browser.open('https://countyballotfiles.elections.myflorida.com/FVRSCountyBallotReports/AbsenteeEarlyVotingReports/PublicStats')
# links = browser.links(link_text=' Download File ')
# for link in links:
#     print(link)
#     link_name = str(link)
#     dl_name = (str(now.year) + '-' + str(now.month) + '-' + str(now.day )+ '-' + str(now.hour) + '-' + str(now.minute) + '-' + re.search('countyballotreportfiles/(.*).txt', link_name).group(1))
#     print(dl_name)
#     browser.download_link(link=link, file=(dl_name+'.txt'))
