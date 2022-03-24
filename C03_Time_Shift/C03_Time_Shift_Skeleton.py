### OBJECTIVE ###
"""
In the future, BEST will have gone interstellar and change it name to Board of Every Student of Technology!
Every year, the hackathon organisation will take place on another planet and the date and time in UTC+0 gets send by
laser to Earth. However, interference can cause the data to get scrambled. The data you receive is in the following
format: "Seconds:Year:Day:Hour:Minute:Month".
Your first task is to reformat that to a normal "Weekday, Month Day, Year at Hour:Minute:Second" representation as you
can see in the first line of example output at the bottom.
Secondly, a list of participating locations on Earth is sent over and for each location the offset (positive or negative)
from UTC time is included as well. Print for every location at what date and time it will happen on earth in chronological
order in the same normal representation as task 1.
Lastly, return how many days and Hours:Minutes:Seconds are remaining for the Earthlings until the time of the event
counting from today 21:00 hours.
"""

### INPUT - DO NOT TOUCH ###
from datetime import datetime
from datetime import timedelta

inputTime = eval(input())
locations = eval(input())
### END INPUT ###


def time_shift(timeToShift):
    # TODO
    pass


### OUTPUT - DO NOT TOUCH ###
time_shift(inputTime)
### END OUTPUT ###


### EXAMPLE INPUT - YOU MAY COPY THIS INTO YOUR TERMINAL ###
# "30:2121:1:21:15:12"
# [("Brussels", 1), ("London", 0)]

### EXAMPLE OUTPUT ###
# Monday, December 01, 2121 at 21:15:30
# London: Monday, December 01, 2121 at 21:15:30
# Brussels: Monday, December 01, 2121 at 22:15:30
# 36524 days, 0:15:30