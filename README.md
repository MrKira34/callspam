# Call Spammer (DEAD)
Спамер звонков<br>
Только для России!<br>
Связь со мной в <a href="https://t-do.ru/FSystem88">Telegram</a> или <a href="https://vk.com/fsys88">Вконтакте</a><br>
Новости об обновлениях в <a href="https://t-do.ru/spymer">Telegram</a><br>
<b>Обязательно подпишитесь на канал в телеграме, так как именно там я пишу когда надо обновиться, чтобы сервисов было больше!</b><br><br>
# Донатерная
<b>Кому не жалко копейку на развитие проекта:</b><br>
http://FSystem88.ru/donate
<br>
https://paypal.me/FSystem88
<br><br>
# Как уставновить?
Только на андроид. Тупо следуйте инструкции...<br>
Скачать <a href="https://play.google.com/store/apps/details?id=com.termux&hl=ru">Termux из GooglePlay</a> и открыть его.<br>
<code>apt update</code> //<i>Проверим на наличие обновлений</i><br>
<code>apt upgrade</code> //<i>Обновим предложенные пакеты</i><br>
<code>apt install git</code> //<i>Установим Git для копирования программ с гитхаба</i><br>
<code>git clone https://github.com/FSystem88/callspam</code> //<i>Скачаем Спамер с гитхаба</i><br>
<code>sh callspam/install.sh</code> //<i>Установим Спамер в Termux'e</i><br>
<code>callspam phone --text '[текст с жалобой]'</code> //<i>Запустим Спамер с телефоном жертвы</i><br>
<br>
<b>Пример:</b><br>
<code>callspam 89991234455 --text 'Развод и распил имущества'</code><br><br>
Будут вопросы - контакты выше.<br>
<b>Приятного пользования!</b>
<br><br>
# Как обновить?
<br>
Прописываем <code>callspam-update</code>
<br>или<br>
Открываем Термух и прописываем следующее:<br>
<code>rm -rf callspam</code> //удаляем папку с прогой
<br>
<code>git clone https://github.com/FSystem88/callspam</code> скачаем обновленную версию с гитхаба
<br>
<code>sh callspam/install.sh</code> (обновим конфигурацию).
<br>
<b>Готово! Можете дальше использовать мой спамер.</b>
