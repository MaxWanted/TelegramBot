import random
import urllib.request

s_about = '''Привет, меня зовут Марвин! Я телеграм-бот, написанный на языке программирования Python. 
Я создан, чтобы помочь моим друзьям.
Меня назвали в честь того самого робота из цикла романов "Автостопом по галактике", правда я 
не такой унылый, но как и мой прототип - разумнее тебя (но это не точно).
А если без шуток, то я очень люблю этих ребят:\n
<b>Максим Деркач</b> - разработчик 
@MaxWanted
<b>Евгения</b> - контент-мейкер 
@tg '''

s_help = '''Со мной очень просто общаться!\n
Используй клавиатуру внизу экрана для отправки мне ключевых слов и я выдам тебе соответствующую информацию. 
Кнопки сделаны для удобства, ты можешь просто отправить мне в чат ключевое слово из пунктов меню, например "Банкет". 
Чтобы показать или скрыть специальную клавиатуру нажми на соответствующую кнопку справа в поле ввода.
Еще я отзываюсь на своё имя в любом чате или не очень приятное слово "бот". 
Со временем я обрету больше навыков, а пока мой функционал ограничен.\n 
<i>Доступные команды:</i> 
/start - запуск бота и вызов меню
/help - помощь в общении с ботом
/about - информация о боте\n 
Удачи! '''

s_about_youg = '''Немного о виновниках торжества:\n 
<u> ... \n 
<u> ...\n
'''

# список слов на которые реагирует бот
S_bot_call = {'марвин', 'бот', 'бот?', 'бот!', 'marvin', 'bot', 'bot?', 'bot!'}