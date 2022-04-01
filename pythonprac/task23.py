'''
date and time module python

'''

import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)



date_object = datetime.date.today()
print(date_object)



print(dir(datetime))


from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)