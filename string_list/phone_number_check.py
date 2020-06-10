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
		print("Wrong len")
		return False
	
	if x[0] != '0':
		print(x[0])
		print("Wrong the first character")
		return False

	if x[1:3].isdecimal() == False:
		print("Wrong 2")
		return False
	if x[3] != '-':
		print("Wrong 3")
		return False
	if x[3:6].isdecimal() == False:
		print("Wrong 4")
		return False
	if x[6] != '-':
		print("Wrong 5")
		return False
	if x[7:12].isdecimal() == False:
		print("Wrong 2=6")
		return False
	return True

print(phone_number_check("034-951-8551"))

