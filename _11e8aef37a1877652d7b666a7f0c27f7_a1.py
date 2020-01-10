def seconds_difference(time_1, time_2):
    solving = time_2 - time_1
    return solving

def hours_difference(time_1, time_2):
    return (time_2 - time_1)/60/60

def to_float_hours(hours, minutes, seconds):
    min_seconds = minutes * 60
    hr_seconds = hours * 3600
    time = seconds + min_seconds + hr_seconds
    solving = time / 3600
    return solving

def to_24_hour_clock(hours):
    return hours % 24
     
### Write your get_hours function definition here:
def get_hours(seconds):
    hours = seconds // 3600
    solving = to_24_hour_clock(hours)
    return solving

### Write your get_minutes function definition here:
def get_minutes(seconds):
    minutes = seconds // 60
    solving = minutes % 60
    return solving

### Write your get_seconds function definition here:
def get_seconds(seconds):
    seconds_aft = seconds % (3600 * 24)
    solving = seconds_aft % 60
    return solving

def time_to_utc(utc_offset, time):
    uts_t = time - utc_offset
    solving = to_24_hour_clock(uts_t)
    return solving
   
def time_from_utc(utc_offset, time):
    timezone = time + utc_offset
    solving = to_24_hour_clock(timezone)
    return solving



