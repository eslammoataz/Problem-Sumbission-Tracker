import requests
import datetime
import time
import xlsxwriter
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#---------------------------------------------------------------------------------------------
# for google sheet credentials
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds =  ServiceAccountCredentials.from_json_keyfile_name("creds.json" ,scope)
client = gspread.authorize(creds)
sheet  = client.open("Project Submission Tracker").sheet1

# Print data will print sheet's data
# data = sheet.get_all_records()
#you can use "Sheet.row_values() ,sheet.col_values() , sheet.cell(1,3).value" to print

#---------------------------------------------------------------------------------------------






#Number of Submissions Need to Print

Number_Of_Submissions = int(input("Enter a Value: \n"))
Number_Of_Submissions_string = Number_Of_Submissions.__str__()
url = "https://codeforces.com/api/user.status?handle=okazakii&from=1&count=" + Number_Of_Submissions_string

response = requests.get(url)
info = response.json()






# print('Problem Name: ', info['result'][j]['problem']['name'])

PrevDate = 0
pos = 2
for j in range(Number_Of_Submissions):
    # Getting Seconds from API
    second = info['result'][j]['creationTimeSeconds']
    # Converting Seconds into Date
    Date = time.strftime('%m/%d/%y', time.gmtime(second))


    if (Date != PrevDate):
        insert = [ '-------------------', '-------------------', '--------------------']
        sheet.insert_row(insert , pos)
        pos+=1
        insert=[Date]
        sheet.insert_row(insert,pos+1)
        pos+=1
        PrevDate = Date

    ProblemName = info['result'][j]['problem']['name']
    ProblemStatus = info['result'][j]['verdict']
    insert = [' ',ProblemName ,ProblemStatus ]
    sheet.insert_row(insert, pos)




# seconds = (datetime.datetime(2020,9,1,23,59,59) - datetime.datetime(1970,1,1)).total_seconds()
# response = time.strftime('%m/%d/%y %H:%M:%S' , time.gmtime(1647380763))
# creating an excel sheet
# outworkbook = xlsxwriter.Workbook("out.xlsx")
# outsheet = outworkbook.add_worksheet()