with open('./log/test_time-log.txt') as f:
    time = 0
    for i in f:
        if i.startswith('time'): time+= float(i.split()[-1])
    print time
    print time/3600