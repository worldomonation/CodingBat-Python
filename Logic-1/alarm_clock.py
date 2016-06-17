# Tested 2016-06-14 23:41

def alarm_clock(day, vacation):
    weekend = [0, 6]
    if vacation:
        return 'off' if day in weekend else '10:00'
    return '10:00' if day in weekend else '7:00'
