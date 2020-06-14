import imapclient
conn = imapclient.IMAPClient("imap.gmail.com", ssl = True)
conn.login('bui.binh.k56@gmail.com','01649518551')
conn.select_folder ('INBOX', readonly =True)


import datetime

UIDs = conn.search(['SINCE', datetime.date(2020, 6, 10)])
print(UIDs)

rawMessage = conn.fetch([26295], ['BODY[]', 'FLAGS'])

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[26295][b'BODY[]'])
message.get_subject()
print(message.get_subject())

print('Who send email to you')
message.get_address('from')
print(message.get_address('from'))

print("Who will be recive your email")
message.get_address('to')
print(message.get_address('to'))


message.text_part
print(message.text_part)
message.html_part == None
print(message.html_part == None)
message.text_part.get_payload().decode('UTF-8')
print(message.text_part.get_payload().decode('UTF-8'))


#filte email
conn.select_folder('INBOX', readonly = False)


