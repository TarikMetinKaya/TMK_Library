from datetime import datetime
from datetime import timedelta

def twoStringDateLength(start_date,end_date,is_end_date_include=True):
    """
    Usage:
    twoStringDateLength("2021-09-20","2021-09-21",False)
    OUTPUT: 1


    twoStringDateLength("2021-09-20","2021-09-21",True)
    OUTPUT: 2

    twoStringDateLength("2021-05-21","2021-05-15",False)
    OUTPUT: -6


    :param start_date: Must be like "%Y-%m-%d" string
    :param end_date: Must be like "%Y-%m-%d" string
    :param is_end_date_include: If it is True add last day to length
    :return:
    """

    start_date = datetime.strptime(start_date,"%Y-%m-%d")
    end_date = datetime.strptime(end_date,"%Y-%m-%d")
    delta = end_date - start_date
    if is_end_date_include:
        return delta.days+1
    else:
        return delta.days

def divide_date_range(start_date,end_date,divide_per_day):
    length=twoStringDateLength(start_date,end_date,True)
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    mod_minus=(length%divide_per_day)-1
    if mod_minus < 0:
        mod_minus=0
    normal_count=int(length/divide_per_day)
    start_dates_list=[]
    end_dates_list=[]
    temp_date=start_date
    start_dates_list.append(temp_date.strftime("%Y-%m-%d"))
    for i in range(0,normal_count):
        temp_date=temp_date + timedelta(days=divide_per_day-1)
        end_dates_list.append(temp_date.strftime("%Y-%m-%d"))
        temp_date=temp_date + timedelta(days=1)

        start_dates_list.append(temp_date.strftime("%Y-%m-%d"))
    temp_date=temp_date + timedelta(days=mod_minus)
    end_dates_list.append(temp_date.strftime("%Y-%m-%d"))
    return start_dates_list,end_dates_list
