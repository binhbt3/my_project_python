import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()

# TO login to your gmail you need seeting your gmail account: "Less secure app access": ON
conn.login('bui.binh.k56@gmail.com','01649518551')

conn.sendmail('bui.binh.k56@gmail.com', 'tranvanhong.181093@gmail.com', 'Subject: Hello Van Hong, This email was sent from python program\n\n Dear Van Hong,\nI hope you are well. Now I can send an email from python programmer. I am discovering new things about python in here :)). Have a nice weekend! ')
{}


conn.quit()
  
