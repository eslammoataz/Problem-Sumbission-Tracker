import requests
import datetime
from datetime import date
import time
import xlsxwriter
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ---------------------------------------------------------------------------------------------#
# for google sheet credentials
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Project Submission Tracker").sheet1

# Number of Submissions to go through
Number_Of_Submissions = '500'

# #----------------------------------------------------------------------------------------------#

# ESLAM
#
# First_Api = "https://codeforces.com/api/user.status?handle=okazakii&from=1&count=" + Number_Of_Submissions
# response = requests.get(First_Api)
# info = response.json()
#
# map_for_problems = {}
# for j in range(int(Number_Of_Submissions)):
#
#
#     second = info['result'][j]['creationTimeSeconds']
#     Date = time.strftime('%m/%d/%y', time.gmtime(second))
#     Day = int(Date[3] + Date[4])
#     month = int(Date[1])
#     ProblemStatus = info['result'][j]['verdict']
#     ProblemName = info['result'][j]['problem']['name']
#
#     if(month==2):
#         break
#     if (ProblemName in map_for_problems):
#         continue
#
#     # updating the desired cell of a certain day for User 1
#     if (ProblemStatus == 'OK' and month==3):
#         prevValue = int(sheet.cell(Day + 2, 3).value)
#         sheet.update_cell(Day + 2, 3, prevValue + 1)
#         map_for_problems[ProblemName]= 1

# #----------------------------------------------------------------------------------------------#

# AMIR
Second_Api = "https://codeforces.com/api/user.status?handle=itadorii&from=1&count=" + Number_Of_Submissions
response2 = requests.get(Second_Api)
info2 = response2.json()

# map to prevent multiple accepted submissions to be counted
map_for_problems2 = {}

for j in range(int(Number_Of_Submissions)):

    second2 = info2['result'][j]['creationTimeSeconds']
    Date2 = time.strftime('%m/%d/%y', time.gmtime(second2))
    Day2 = int(Date2[3] + Date2[4])
    month2 = int(Date2[1])
    ProblemStatus2 = info2['result'][j]['verdict']
    ProblemName2 = info2['result'][j]['problem']['name']
    if(month2==2):
        break

    # updating the desired cell of a certain day for User 1
    if(ProblemName2 in map_for_problems2):
        continue
    if (ProblemStatus2 == 'OK' and month2 == 3 ):
        prevValue = int(sheet.cell(Day2 + 2, 5).value)
        sheet.update_cell(Day2 + 2, 5, prevValue + 1)
        map_for_problems2[ProblemName2] = 1



# seconds = (datetime.datetime(2020,9,1,23,59,59) - datetime.datetime(1970,1,1)).total_seconds()
# response = time.strftime('%m/%d/%y %H:%M:%S' , time.gmtime(1647380763))
