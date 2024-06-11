import requests

#creating a function to find vaccine by pincode and date
def find_vaccines(pincode, date):
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pincode+"&date="+date
    r = requests.get(url = URL, )
    if r.status_code==200:
        response = r.json()['centers']
        counter = 0
        for each in response:
            for session in each['sessions']:
                if session['available_capacity_dose1'] and session['min_age_limit']==45:
                    print(each['name'], session['date'], session['min_age_limit'])
                    counter = 1
        if counter == 0:
            print("No vaccine found")

pincode = input("Enter pin code: ")
date = input("Enter the date in the format DD-MM-YYYY: ")
find_vaccines(pincode, date) 