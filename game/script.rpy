# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define un = Character("предыстория")
define s = Character('Скала', color="#c8ffc8")
define l = Character('Эль Примо', color="#c8ffc8")
define j = Character('Жак Фреско', color="#c8ffc8")

define audio.musmistycal = 'music/crickets.mp3'
define audio.songHit = 'music/hit23.mp3'
define audio.select = 'music/cloth-heavy.wav'
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    play music musmistycal

    $ hp = 3

    un "Ты работал шпионом, тебя отправили в другую страну, чтобы раздобыть ценную информацию."

    un "Ты - программист под прекрытием."

    un "Ты работал в крупной компании."

    un "В один момент тебя стали очень сильно подозревать!"

    un "Когда ты возвращался домой с работы - тебя похитили."

    un "Тебя будут допрашивать! Постарайся не выдать себя! У тебя есть [hp] попытки!"

    scene podval 

    show scala

    s "Опа, проснулся!"

    s "Вы, весьма подозрительный чалодой маловек!"

    s "Мы вынуждены были похитить тебя, чтобы убедиться, что ты не какой-то там шпиён."

    s "Итак, первый вопрос!"

    s "Быстро мне ответил, какой основной язык программирования используется при разработке мобильных приложений под android!"

    menu:
        "Быстро мне ответил, какой основной язык программирования используется при разработке мобильных приложений под android!"

        "Java":
            jump correctOne
        "Python":
            jump vrongOne
        "C#": 
            jump vrongOne
        "Pascal":
            jump vrongOne

    return

label vrongOne:

    play sound select

    s "Ай, ай, ай! Это неправильный ответ!"

    s "Ты очень сильно подбил моё доверие к тебе!"

    $hp = hp - 1

    "Неизвестный голос" "У тебя осталось [hp] попытки"

    jump qestionTwo

    return

label correctOne:

    play sound select

    s "Хмм, правильно!"

    s "Я удивлён!"

    s "Если ты это знаешь, то ты действительно Синьёр-разработчик!"

    jump qestionTwo

    return

label qestionTwo:

    s "Следующий вопрос!"

    s "Скажи мне, сколько существует разновидностей мобильный приложений!"

    menu:
        "Скажи мне, сколько существует разновидностей мобильный приложений!"

        "1":
            jump vrongTwo
        "2":
            jump vrongTwo
        "3":
            jump correctTwo
        "4":
            jump vrongTwo

    play sound select

    return 

label vrongTwo:

    s "Ай, ай, ай! Это неправильный ответ!"

    s "Ты очень сильно подбил моё доверие к тебе!"
    
    s "Правильный ответ - 3."

    $hp = hp - 1

    "Неизвестный голос" "У тебя осталось [hp] попытки(а)"

    jump qestionThree

    return

label correctTwo:

    s "Молодец! Я в тебе и не сомневался!"

    jump qestionThree

    return

label qestionThree:

    s "Если ты назовёшь, хотя бы одно из трёх приложений, то тогда, у меня больше не будет к тебе вопросов!"

    menu:
        "Если ты назовёшь, хотя бы одно из трёх приложений, то тогда, у меня больше не будет к тебе вопросов!"

        "Гибридное":
            jump correctThree
        "Нативное":
            jump correctThree
        "Игровое":
            jump vrongThree
        "Промо-приложение":
            jump vrongThree

    play sound select

    return 

label vrongThree:

    s "Ай, ай, ай! Это неправильный ответ!"

    s "Ты очень сильно подбил моё доверие к тебе!"

    $hp = hp - 1

    "Неизвестный голос" "У тебя осталось [hp] попытки(а)"

    if hp == 0:
        jump bedEnd

    jump glavaTwo

    return

label bedEnd:

    hide elprimo

    show scala

    s "Что ж, я был лучшего мнения о тебе!"

    s "Прощай!"

    play sound songHit

    scene bg

    hide scala

    hide jack

    "Вы прошли игру, на плохую концовку!"

    return 

label correctThree:

    s "Молодец! Я в тебе и не сомневался!"

    s "У меня больше нет к тебе вопросов!"

    s "Но!"

    s "У одного человека, всё же есть для тебя ещё вопросы!"

    jump glavaTwo

    return

label glavaTwo:

    hide scala

    show elprimo

    l "Привет, я слышал как ты отвечал на вопросы скалы."

    l "Ты неплохо справлялся!"

    l "Может ты и действительно не ШПИЁЁЁН!"

    l "Но, перед вердиктом, я хочу задать тебе пару вопросов..."

    l "И так, первый вопрос!"

    l "В каком году началась история Android?"

    menu:
        "В каком году началась история Android?"

        "2002":
            jump vrongFoure
        "2003":
            jump correctFoure
        "2004":
            jump vrongFoure
        "2005":
            jump vrongFoure

    play sound select

    return

label vrongFoure:

    l "Как можно не знать ответа, на такой элементарный вопрос?"

    $hp = hp - 1

    "Неизвестный голос" "У тебя осталось [hp] попытки(а)"

    if hp == 0:
        jump bedEnd
    
    jump glavaTwoTwo

    return 

label correctFoure:

    l "Молодец!"

    l "Правильно!"

    jump glavaTwoTwo

    return

label glavaTwoTwo:

    show elprimo

    l "Последний вопрос!"

    l "Этот вопрос решит всё!"

    l "Перечисли мне больше всего плюсов при разработке мобильных веб-приложений?"

    menu:
        "Какие есть плюсы при разработке мобильных веб-приложений?"

        "Кросплатформенность, не требует установки, скорость разработки":
            jump correctFive
        "Лучшее позиционирование в магазине, максимальное использование возможностей":
            jump vrongFive
        "Не требует установки, Дешёвая разработка":
            jump vrongFive

    play sound select

    return

label vrongFive:

    l "Как можно не знать ответа, на такой элементарный вопрос?"

    $hp = hp - 1

    "Неизвестный голос" "У тебя осталось [hp] попытки(а)"

    if hp == 0:
        jump bedEnd
    
    jump final

    return 

label correctFive:

    l "Молодец!"

    l "Правильно!"

    jump final

    return

label final:

    hide elprimo

    show scala

    s "Ты ответил на все наши вопросы!"

    s "Этого достаточно, чтобы мы прекратили подозревать тебя!"

    s "Ты свободен!"

    hide scala

    scene goodend

    "Вы прошли игру! На хорошую концовку!"

    if hp == 3:
        jump secret

    return

label secret:

    scene bg

    show jack

    j "Ты прошёл игру без единой ошибки!"

    j "Ты открыл секретную концовку!"

    j "Но, здесь ничего не будет..."

    j "Кроме одного вопроса..."

    j "Сколько?"

    j "А точнее, какую оценку вы поставите этой игре?"

    menu:
        "Какую оценку вы поставите этой игре?"

        "3":
            jump ansvOne
        "4":
            jump ansvTwo
        "5":
            jump ansvThree

    return 

label ansvOne:

    "Брух"

    return

label ansvTwo:

    "Круто, спасибо! :D"

    return

label ansvThree:

    "Спасибо за 5! :D"

    return