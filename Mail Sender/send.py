import wisher as w

target_id = input("Please eneter reciepent mail id\n")
subject = input("Enter subject\n")
body = input("Enter body of the mail\n")
var = int(input("Enter 1\n"))


w.send(var, target_id, subject, body)

    

