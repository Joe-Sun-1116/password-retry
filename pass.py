ans = 'a123456'
times = 3
while times > 0:
	paswd = input('請輸入密碼 : ')
	times-=1
	if paswd == ans:
		print('登入成功')
		break
	else:
		print('密碼錯誤，還有',times,'次機會')