import requests
import datetime
import time
import xlsxwriter

# Number of Submissions Need to Print

Number_Of_Submissions = int(input("Enter a Value: \n"))
Number_Of_Submissions_string = Number_Of_Submissions.__str__()
url = "https://codeforces.com/api/user.status?handle=okazakii&from=1&count=" + Number_Of_Submissions_string

response = requests.get(url)
info = response.json()

# creating an excel sheet

outworkbook = xlsxwriter.Workbook("out.xlsx")
outsheet = outworkbook.add_worksheet()

# writing columns
outsheet.write('A1', 'Date')
outsheet.write('B1', 'Problem Name')
outsheet.write('C1', 'Status')

# # print('Problem Name: ', info['result'][j]['problem']['name'])


PrevDate = 0

for j in range(Number_Of_Submissions):

    # Getting Seconds from API
    second = info['result'][j]['creationTimeSeconds']
    # Converting Seconds into Date
    Date = time.strftime('%m/%d/%y', time.gmtime(second))


    if (Date != PrevDate):
        outsheet.write(j + 2, 1, '-------------------')
        outsheet.write(j + 2, 2, '-------------------')
        outsheet.write(j + 2, 0, '-------------------')
        cell_for_Date = 'A' + (j + 3).__str__()
        j += 3
        outsheet.write(cell_for_Date, Date)
        PrevDate = Date


    # printing Problem Name in col B
    outsheet.write(j + 2, 1, info['result'][j]['problem']['name'])
    # printing Problem Name in col C
    outsheet.write(j + 2, 2, info['result'][j]['verdict'])

outworkbook.close()

# seconds = (datetime.datetime(2020,9,1,23,59,59) - datetime.datetime(1970,1,1)).total_seconds()
# response = time.strftime('%m/%d/%y %H:%M:%S' , time.gmtime(1647380763))
