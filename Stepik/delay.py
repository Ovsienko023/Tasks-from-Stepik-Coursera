def delay_1():
    from datetime import timedelta, date, datetime

    timer_stop = datetime.utcnow() + timedelta(seconds=3)
    while True:
        if datetime.utcnow() > timer_stop:
            break
    return 1