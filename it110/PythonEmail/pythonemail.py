###############################################################
# Python Email sending project for IT110
# Using PythonEmail Sending Module
# Contains both Plain text version and HTML version
# Composed by siyao.fu@umb.edu 11/03/2016
###############################################################

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# step 1 Configure the Sending Module

print("composing!")
print("Welcome to Your name's email system!")
you = input("Please input recipient's address:\n")
# me == sender's email address. Please refer to the final part
# you == recipient's email address 'name@abc.com'
me = "YourEmail"   # change this to your email address
#psw = input(print("Please input your password!\n"))  # skip the authentication part

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "My Python Email"
msg['From'] = 'Your Name"
msg['To'] = you

print 'Email Module Configuration ===========> done!'
# step 2 Compose the email body
# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"

html = """\
<html>
  <head></head>
  <body><h1> Hello</h1>
    <div>
    <h1>Map</h1>
    <a href="https://www.google.com/maps/place/Umass+boston/"><img src="http://maps.googleapis.com/maps/api/staticmap?center=Umass+boston&zoom=12&scale=2&size=300x250&maptype=roadmap&format=png&visual_refresh=true" alt="Google Map of Umass boston"></a>
    </div>
    <h1>Picture</h1>
    <p> <img src="">

    <div> <table border="1">
<tr>
<td>My My HTML Table</td>
<td>Is very simple</td>
</tr>
<tr>
<td>Random Column</td>
<td>Tables are fun</td>
</tr>
</table></div>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

print 'Email composing ===========> done!'

# step 3 Shoot
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

# Gmail server is recommanded here. If you use other email service, try to find the smtp information

mail.ehlo()  # Please Google the difference between HELO and EHLO
mail.starttls()  # take an existing insecure connection and upgrade it to a secure connection using SSL/TLS

# this will be your email login information
mail.login('username', 'password')
mail.sendmail(me, you, msg.as_string())
print 'Email sending ===========> done!'
mail.quit()
