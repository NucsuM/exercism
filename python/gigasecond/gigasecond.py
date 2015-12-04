from datetime import timedelta

def add_gigasecond(startDate):
    return startDate + timedelta(seconds=(10**9))
