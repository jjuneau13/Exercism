from datetime import datetime, timedelta, date

def add(moment):
    days = 1e9//(3600*24)
    seconds = 1e9 % (3600 * 24)
    return moment + timedelta(days = days, seconds = seconds)