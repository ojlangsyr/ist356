import datetime

def parsedate_mdy(text:str) -> datetime:
    return datetime.datetime.strptime(text,"%m/%d/%Y")

def format_date_ymd(date: datetime) ->str:
    return date.strftime("%Y-%m-%d")

date = "12/30/1999"
date_dt=parsedate_mdy(date)
date_str=format_date_ymd(date_dt)
print(date,date_str)