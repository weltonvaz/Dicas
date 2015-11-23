import datetime
import time

def diffdates(d1, d2):
    #Date format: %Y-%m-%d %H:%M:%S
    return (time.mktime(time.strptime(d2,"%Y-%m-%d %H:%M:%S")) -
               time.mktime(time.strptime(d1, "%Y-%m-%d %H:%M:%S")))

d1 = datetime.datetime(2015, 8, 5, 8, 12, 23, 113827)
d2 = datetime.datetime(2015, 8, 9, 8, 13, 23, 113827)
diff = diffdates(d1, d2)
