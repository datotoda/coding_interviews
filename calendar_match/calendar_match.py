"""
sample input:
[['9:00', '10:30'], ['12:30', '13:30'], ['16:00', '18:00']]
['9:00', '20:00']
[['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
['10:00', '18:30']
30
sample output:
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
"""


def get_time_in_minute(time_str):
    time_str_list = time_str.split(':')
    return (int(time_str_list[0]) * 60) + int(time_str_list[1])


def get_free_time_list(calendar_list, limit):
    free_time_list = [['00:00', '24:00']]
    limit_start_time_in_sec = get_time_in_minute(limit[0])
    limit_end_time_in_sec = get_time_in_minute(limit[1])
    for time_period in calendar_list:
        free_time_list[-1:] = [free_time_list[-1][0], time_period[0]], [time_period[1], free_time_list[-1][1]]

    for i, free_time_period in enumerate(free_time_list):
        if limit_start_time_in_sec >= get_time_in_minute(free_time_period[1]):
            free_time_list[i] = None
            continue
        if limit_start_time_in_sec > get_time_in_minute(free_time_period[0]):
            free_time_list[i] = [limit[0], free_time_period[1]]
            break
        else:
            break
    free_time_list = [ftp for ftp in free_time_list if ftp]

    for i, free_time_period in reversed(list(enumerate(free_time_list))):
        if limit_end_time_in_sec <= get_time_in_minute(free_time_period[0]):
            free_time_list[i] = None
            continue
        if limit_end_time_in_sec < get_time_in_minute(free_time_period[1]):
            free_time_list[i] = [free_time_period[0], limit[1]]
            break
        else:
            break
    free_time_list = [ftp for ftp in free_time_list if ftp]
    free_time_list = [ftp for ftp in free_time_list if ftp[0] != ftp[1]]

    return free_time_list


def get_unioned_list(time_list_1, time_list_2):
    if len(time_list_1) > len(time_list_2):
        time_list_1, time_list_2 = time_list_2, time_list_1
    unioned_list = []

    for time_period_1 in time_list_1:
        time_period_2_list = []
        for time_period_2 in time_list_2:
            if get_time_in_minute(time_period_1[0]) >= get_time_in_minute(time_period_2[1]):
                continue
            if get_time_in_minute(time_period_1[1]) <= get_time_in_minute(time_period_2[0]):
                break
            time_period_2_list.append(time_period_2)

        for time_period_2 in time_period_2_list:
            temp_time = ['', '']
            if get_time_in_minute(time_period_1[0]) > get_time_in_minute(time_period_2[0]):
                temp_time[0] = time_period_1[0]
            else:
                temp_time[0] = time_period_2[0]
            if get_time_in_minute(time_period_1[1]) < get_time_in_minute(time_period_2[1]):
                temp_time[1] = time_period_1[1]
            else:
                temp_time[1] = time_period_2[1]
            unioned_list.append(temp_time)

    return unioned_list


def get_final_list(time_list, duration):
    for i, time_period in enumerate(time_list):
        if get_time_in_minute(time_period[1]) - get_time_in_minute(time_period[0]) < duration:
            time_list[i] = None

    time_list = [ftp for ftp in time_list if ftp]

    return time_list


def free_time(person_1_calendar, person_1_limit, person_2_calendar, person_2_limit, duration):
    person_1_free_time_list = get_free_time_list(person_1_calendar, person_1_limit)
    person_2_free_time_list = get_free_time_list(person_2_calendar, person_2_limit)

    unioned_free_time_list = get_unioned_list(person_1_free_time_list, person_2_free_time_list)

    matched_free_time_with_duration = get_final_list(unioned_free_time_list, duration)

    return matched_free_time_with_duration


al = free_time(person_1_calendar=[['9:00', '10:30'], ['12:00', '13:30'], ['16:00', '18:00']],
               person_1_limit=['9:00', '20:00'],
               person_2_calendar=[['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']],
               person_2_limit=['10:00', '18:30'],
               duration=30)

print(al)
print(al == [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']])

# 1 hour
