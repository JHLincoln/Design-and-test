
from datetime import datetime, date, timedelta
#import dateutil
def age_checker(date_of_birth):
    current = date.today()
    #print (current)
    dob_int = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    #print (dob_int)
    difference = current - dob_int
    #print (difference)
    years_old = difference//365
    # print (years_old)
    #print (years_old.strftime("%d"))
    days = str(years_old).split()
    #print (days)
    age = days[0]
    if int(age) >= 16:
        return "Access granted."
    else:
        return "You are 3, you need to be 16 to access this."