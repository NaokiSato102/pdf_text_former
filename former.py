'''f = open('input.txt','r',encoding='UTF-8')
text = f.read()
f.close()
formated_text = text
formated_text = formated_text.replace('\n',' ')
formated_text = formated_text.replace('.','.\n')

f = open('output.txt','w',encoding='UTF-8')
f.write(formated_text)
f.close()'''

import pyperclip as clip
import time


text = ''
pre_text = ''
while 1:
	f = open('input.txt','r',encoding='UTF-8')
	text = f.read()
	f.close()

	if pre_text != text:
		pre_text = text
		text = text.replace('\n',' ')
		text = text.replace('.','.\n')
	
		print('内容を整形しました！')
		clip.copy(text)
	
	time.sleep(1)
	
	
