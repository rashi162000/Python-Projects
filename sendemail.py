import smtplib as s 
#smtplib is an inbuilt library in python, No need to install it.

ob=s.SMTP('smtp.gmail.com',587) 
#ob is a variable= s is the SMTP library, mail address, port number
ob.starttls()
ob.login("rashishrivastava16@gmail.com","uvojojqpbsfrnerj")
subject="Email Sending Functionality using Python"
body="This is a mail to check the SMTP mail transfer!"
message ="Subject:{}\n\n{}".format(subject,body)
listofaddress=["shivadantare@gmail.com ","rashishrivastava16@gmail.com","shrutigoyal1201@gmail.com","shrutipui@gmail.com"]
ob.sendmail("rashishrivastava16@gmail.com",listofaddress,message)
print("Mail sent successfully!")
ob.quit()