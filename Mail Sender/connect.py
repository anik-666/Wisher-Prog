import smtplib
import creds as cr

em_var = cr.my_email
pass_var = cr.passwd

def sending(target ,message):   
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user = em_var , password = pass_var)
        connection.sendmail(from_addr= em_var, to_addrs= target, msg = message)
        