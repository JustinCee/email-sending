# importing the smtp module
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'calvertjustin1996@gmail.com'
receiver_email_id = ['beardedbigfoot19@gmail.com', "abdullah.isaacs@gmail.com", "jeandreross@gmail.com", "jessenterblanche@gmail.com"]
password = input("Enter senders email password")
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent
message = "Greetings Everybody\n"
message = message + "I hope you guys are enjoying python"
# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)
# terminating the session
s.quit()
