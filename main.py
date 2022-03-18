import requests
import datetime
from datetime import date
import time
import xlsxwriter
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#---------------------------------------------------------------------------------------------#
# for google sheet credentials
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds =  ServiceAccountCredentials.from_json_keyfile_name("creds.json" ,scope)
client = gspread.authorize(creds)
sheet  = client.open("Project Submission Tracker").sheet1
sheet_Id = '1aM8pUZxpP-5yxuSRYaaQRK7H_qxtL_62Va4MGkHr7ps'

# reseting all values in the sheet
for i in range(2,32):
    sheet.update_cell(i ,3,0)
#---------------------------------------------------------------------------------------------#

#Number of Submissions to go through
Number_Of_Submissions = '700'
url = "https://codeforces.com/api/user.status?handle=okazakii&from=1&count=" + Number_Of_Submissions
response = requests.get(url)
info = response.json()
#---------------------------------------------------------------------------------------------#

#looping in the list and counting Number Of Solved Problem each day
for j in range(int(Number_Of_Submissions)):

    # Getting Seconds from API
    second = info['result'][j]['creationTimeSeconds']

    # Converting Seconds into Date
    Date = time.strftime('%m/%d/%y', time.gmtime(second))

    #Variables to check the correct Day and Month
    Day = int(Date[3]+Date[4])
    month = int(Date[1])
    ProblemStatus = info['result'][j]['verdict']

    #updating the desired cell of a certain day
    if (ProblemStatus == 'OK' and month==3):
        prevValue =int(sheet.cell(Day+1 ,3).value)
        sheet.update_cell(Day+1 ,3 , prevValue+1)
        PrevDate = Date


# seconds = (datetime.datetime(2020,9,1,23,59,59) - datetime.datetime(1970,1,1)).total_seconds()
# response = time.strftime('%m/%d/%y %H:%M:%S' , time.gmtime(1647380763))
