# import re
# import mechanicalsoup
import datetime
now = datetime.datetime.now()

test_filename = str(now.year) + '-' + str(now.month) + '-' + str(now.day )+ '-' + str(now.hour) + '-' + str(now.minute) + '-test.txt'

with open(test_filename, "w") as text_file:
    text_file.write('test test test')

# browser = mechanicalsoup.StatefulBrowser()
# browser.open('https://countyballotfiles.elections.myflorida.com/FVRSCountyBallotReports/AbsenteeEarlyVotingReports/PublicStats')
# links = browser.links(link_text=' Download File ')
# for link in links:
#     print(link)
#     link_name = str(link)
#     dl_name = (str(now.year) + '-' + str(now.month) + '-' + str(now.day )+ '-' + str(now.hour) + '-' + str(now.minute) + '-' + re.search('countyballotreportfiles/(.*).txt', link_name).group(1))
#     print(dl_name)
#     browser.download_link(link=link, file=(dl_name+'.txt'))
