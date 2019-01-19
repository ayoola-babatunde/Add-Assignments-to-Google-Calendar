import webbrowser

course = 'NS164'


#assignment names in order
assignments = ['Drug discovery and design challenge ',
        'Regenerative Medicine Challenge ',        
        'Genetic Testing and Engineering Challenge(LBA)'
        ]


#dates of release and submission in same order. [Week 5, Sunday = 51]
release = [17, 66, 116]
submission = [53, 101, 156]

import datetime as dt

#Sunday of week 1. First day of semester
day1 = dt.datetime(2019,1,13)

release1 = []; submission1 = []

big_list = [release, submission]; small_list = [release1, submission1]

for lists in big_list: 

    for x in lists: 
        a = str(x)[-1] #day of the week
        b = str(x)[:-1] #week of the semester
        
        no_of_days = 7*(int(b) - 1) + (int(a)) #days between day1 and x
        
        actual_date = day1 + dt.timedelta(days = no_of_days) #date of x
        
        actual_day = actual_date.day; actual_month = actual_date.month
    
        if len(str(actual_month)) == 1: 
            actual_month = '0' + str(actual_month) #changing 3 to 03, etc
        
        if len(str(actual_day)) == 1: 
            actual_day = '0' + str(actual_day) #changing 3 to 03, etc
        
        output = str(actual_month) + str(actual_day) #outputs date of x, e.g. Feb 3rd = 0203
    
        small_list[big_list.index(lists)].append(output)


#opens the link in google calendar 
for x in range(len(assignments)): 
    webbrowser.open('https://calendar.google.com/calendar/render?action=TEMPLATE&text='
          + course + ': ' + assignments[x] + '&dates=2019' + release1[x] + '/2019' + submission1[x])
    
