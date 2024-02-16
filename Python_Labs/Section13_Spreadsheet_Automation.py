import gspread 
from oauth2client.service_account import ServiceAccountCredentials 
from pprint import pprint

#Define the scope and credentials 

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive'] 

creds = ServiceAccountCredentials.from_json_keyfile_name('<ADD YOUR JSON KEY LOCATION>', scope) 

# Authenticate with Google Sheets API
client = gspread.authorize(creds)  


#Open the target google sheet 
sheet = client.open('spreadsheet1').sheet1 
values = sheet.get_all_values()

#print all values from the selected google sheet as is 

pprint(values)


