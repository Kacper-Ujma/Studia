from datetime import timedelta
 
t0 = timedelta(hours=6,minutes=52,seconds=0)
t1 = timedelta(minutes = 1.5*6,seconds = 1.5*15)
t2 = timedelta(minutes=4.8*4,seconds=4.8*12)
t3 = timedelta(minutes=1*6,seconds=1*15)
tk = t0+t1+t2+t3
print("skonczy biegac o",tk)
