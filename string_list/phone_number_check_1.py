""""
Kiem tra xem 1 so co phai la so dien thoai hay khong?
034-951-8551
- co 12 ki tu
- ki tu dau la 0
- Ki tu thu 3 la -
- 3 ki tu tiep theo la so
- ki tu thu 7 la -
- 4 ki tu sau la so


"""
def phone_number_check(x):
    check = False
    if len(x) != 12:
        #print("Wrong len")
        return False
    
    if x[0] != '0':
        #print(x[0])
        #print("Wrong the first character")
        return False

    if x[1:3].isdecimal() == False:
        #print("Wrong 2")
        return False
    if x[3] != '-':
        #print("Wrong 3")
        return False
    if x[4:7].isdecimal() == False:
        #print("Wrong 4")
        return False
    if x[7] != '-':
        #print("Wrong 5")
        return False
    if x[8:12].isdecimal() == False:
        #print("Wrong 2=6")
        return False
    return True

print(phone_number_check("034-951-8551"))

#
print("Check number in a text!")
#message = "Call me 034-951-8551 if you arrive. Or call my roomate 034-981-0123"
message = "Call me  if you arrive. Or call my roomate "

count = 0
for i in range(len(message)):
    if message[i].isdecimal():
        if phone_number_check(message[i:i+12]) == True:
            print(message[i:i+12])
            count +=1
if count == 0:
        print("No phone number in the text")
















