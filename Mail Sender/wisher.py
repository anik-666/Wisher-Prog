import connect as c
import datetime as dt
import pandas as p
import random as ran

add_quote = r"E:\WORK\STUDY MATERIAL\PYTHON\Projects\Mail Sender\contents\quotes.txt"
with open(add_quote) as quote_file:
    all_quotes = quote_file.readlines()
    quote = ran.choice(all_quotes)
    #print(quote)


today_date = dt.datetime.now()
#print(today_date)
today_tuple = (today_date.month, today_date.day)
#print(today_tuple)
csv_file = r"E:\WORK\STUDY MATERIAL\PYTHON\Projects\Mail Sender\contents\birthday.csv"
data = p.read_csv(csv_file)
birthday_dict = { (data_row["month"], data_row["day"]):
                     data_row for( _, data_row) in data.iterrows()}
#print(birthday_dict)


def send(var, tgt, sub, bod):

    if ((var == 1) and (today_tuple in birthday_dict)):
        message = f'Subject: {sub}\n\n{bod}\n"Happy Birthday"\n{quote}'
        c.sending(tgt, message)
        print("Wished Birthday")
               
    elif(var == 1):
        message= f'Subject: {sub}\n\n{bod}\n{quote}'
        c.sending(tgt, message)
        print("Sent")
    else:
        print("Not sent")
    
    