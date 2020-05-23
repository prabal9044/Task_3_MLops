import smtplib
a=" Welcome To E-mail Sender Tool "
print(a.center(100,'*'))
print()

sender_email=(str("akansh.agarwal23@gmail.com"))
password=(str("1973468521973"))
rec_email=(str("akansh.agarwal23@gmail.com"))
message= "The model is created successfully"

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()

server.login(sender_email,password)
print("LogIn Successfull")

server.sendmail(sender_email,rec_email,message)
print("Email has been sent successfully to "+rec_email)
