<!-- TABLE OF CONTENTS -->
<details>
  <summary>Оглавление</summary>
  <ol>
    <li>
      <a href="#о-проекте">О проекте</a>
      <ul>
        <li><a href="#библиотеки">Библиотеки</a></li>
      </ul>
    </li>
    <li><a href="#как-начать-использовать">Как начать использовать</a></li>
    <li><a href="#применение">Применение</a></li>
    <li><a href="#контакты">Контакты</a></li>
    <li><a href="#лицензия">Лицензия</a></li>
    <li><a href="#благодарности">Благодарности</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## О проекте

![Логотип](https://github.com/caffreyfizz/e-school-Unik/raw/main/images/logo.png)

В настоящще время во многих учебных учреждениях плохо организовано общение между учениками и преподавателями. Например, учитель русского языка принимает сообщения в WhatsApp, учитель информатики на Gmail, а учитель математики только в Telegram. Данная система, построенная на двух чат ботах, решает эту проблему, позволяя организовать безопасное и быстрое взаимодействие преподавателей и учеников.

Вот почему:
* Регистрация учеников и учителей сопровождается обязательным вводом паролей.
* Под каждый класс создается отдельная категория, права доступа на которую имеют только учитель и ученики этого класса (за некоторыми исключениями и др.)
* Личные кабинеты у каждого пользователя.
* Возможность добавлять информацию для учеников в свои личные кабинеты (доступно только учителям, руководству и директору)
* Смена пароля учителей, всех учеников, каждого класса в частности.

Конечно, человеческий фактор никто не упускает из виду. Распространение паролей среди учеников, намеренная нагрузка на бота с целью замедлить его скорость работы и прочее.
#### Над всеми недочетами идет работа, и пока я вам представлю первую версию — Электронная школа Unick 1.0.

Используйте `README.md` для ознакомления с проектом.


## Библиотеки

Здесь представлены все библиотеки, которыми я пользовался при создании проекта.

* <img src="https://github.com/caffreyfizz/e-school-Unik/raw/main/images/bf.png" width="120">
* <img src="https://github.com/caffreyfizz/e-school-Unik/raw/main/images/discordpylogo.png" width="100">
* <img src="https://github.com/caffreyfizz/e-school-Unik/raw/main/images/aiogramlogo.png" width="100">


<!-- GETTING STARTED -->
## Как начать использовать

Проект работает на основе чат ботов, запущенных на внешних серверах независимо от пользователя. Следовательно вам не требуется установка библиотек через терминал / командную строку.

#### **Настройка ботов на сервере**

Требования к серверу на данный момент:

* Операционная система Windows Vista и выше, macOS, Linux
* Наличие PyCharm и языка Python не ниже 3.8
* Предустановленные библиотеки `discord.py`, `bs4`, `aiogram`, `asyncio`, `logging`, `requests`
  
  ```sh
  pip install discord.py
  ```
  
  ```sh
  pip install bs4
  ```
  
  ```sh
  pip install aiogram
  ```
  
  ```sh
  pip install asyncio
  ```
  
  ```sh
  pip install logging
  ```
  
  ```sh
  pip install requests
  ```

После чего создаете файл с расширением `.py` и вставьте туда программный код. Чтобы запустить проект пропишите в терминал следующую команду, указав вместо filename имя вашего файла:

  ```sh
  python filename.py
  ```

В терминале вы должны увидеть следующие сообщения:
<img src="https://github.com/caffreyfizz/e-school-Unik/raw/main/images/start_server.png" width="800">

#### **Настройка ботов для использования**

Требования к устройству на данный момент:

* Устройство с ОС Windows 7 и выше, masOS 10.13 и выше, IOS 11.0 и выше, Android 6 и выше
* Браузер Google Chrome, Firefox 80+, Opera, Microsoft Edge 17+ (включая Chromium Edge 79+), Safari 11+
* Приложение Discord последней версии (желательно установить, но можно использовать браузерную версию)
* Аккаунт в Discord


<!-- USAGE EXAMPLES -->
## Применение

  Директор - владелец сервера сообщества школы. Роль выдает сам себе вручную.  
  Руководство - пользователь, зарегистрированный как учитель. Роль "Руководство" выдается вручную директором. Роль учителя не снимать с пользователя!  
  Ученик - пользователь, зарегистрированный как ученик. Не требует ручной выдачи ролей.  

```mermaid
graph LR;
    Учитель-->+учитель-->+учепароль-->+добавить_информацию-->+удалить_информацию;
    Руководство-->+учитель-->+учепароль-->+добавить_информацию-->+удалить_информацию;
    Руководство-->+учипароль-->+пароли_ученик;
    Директор-->+стопрегученики-->+стопрегучители-->+добавить_информацию-->+удалить_информацию-->+учипароль-->+пароли_ученик-->+старт_сервера
      
```

## **Функция `on_ready()`**

  Смотреть в файле `Discord_bot.py`. Строка 40-46
  
Аргументы:
* Нет
  
  Получает ID сервера и объявляет объект. В дальнейшем пригодится для выдачи ролей, изменнении ников, создании каналов и прочее.


## **Функция `pelikan(ctx, cl)`**

Смотреть в файле `Discord_bot.py`. Строка 49-87

Аргументы:
* Класс

  Функция парсит информацию с сайта [Пеликан](https://369.pelikan.online/) и выводит информацию о трансляциях уроков этого класса.

  ```sh
  +пеликан 9г
  ```
  
  *В любой канал. Доступна всем пользователям.*


## **Функция `telegram(ctx, *args)`**

  Смотреть в файле `Discord_bot.py`. Строка 90-105

Аргументы:
* ID

  ID может быть представлен как цифры: `123456` или сообщением `Ваш ID: 123456…`.  
  Функция записывает данные в словарь `telegram_id` в виде: ID пользователя в Discord - ключ, ID пользователя в Telegram - значение.  
  Возможность получать уведомления в telegram о смене пароля в вашем классе.

    ```sh
    +телеграм 1234567
    ```
    или
     ```sh
    +телеграм Ваш ID: 1234567
    ```
  *В личные сообщения с ботом. Доступна всем пользователям.*
  

## **Функция `telegram_delete(ctx)`**

  Смотреть в файле `Discord_bot.py`. Строка 108-117
  
Аргументы:
* Нет

  Функция удаляет информацию о пользователе из словаря `telegram_id`. Бот больше не будет уведомлять вас в telegram о смене пароля.

  ```sh
  +удалить_телеграм
  ```
  
  *В личные сообщения с ботом. Доступна всем пользователям.*


## **Функция `teacher(ctx, teachers_password, name, surname, cl, password)`**

  Смотреть в файле `Discord_bot.py`. Строка 120-172

Аргументы:
* Пароль учителя
* Имя
* Отчество
* Класс
* Пароль для учеников (придумать)

  Регистрирует пользователя на сервере как учитель и готовит пространство для регистрации учеников этого класса.  
  Создает категорию: *класс*  
  Создает роли: Ученик *класс*, Учитель *класс*  
  Создает каналы в категории: общение, учительская, новости класса  
  Добавляет роль класса в переменную `classes`  
  Изменяет ник пользователю на имя, отчество.

  ```sh
  +учитель 123 Имя Фамилия 9а 321
  ```
  
  *В личные сообщения с ботом. Доступна всем пользователям.*


## **Функция `student(ctx, name, surname, cl, password)`**

  Смотреть в файле `Discord_bot.py`. Строка 175-196

Аргументы:
* Имя
* Фамилия
* Класс
* Пароль для учеников

  Регистрирует пользователя на сервере как ученика.  
  Создает личный кабинет ученика в категории его класса и выдает ему роли, для доступа к чатам класса (Ученик, Ученик класс).

  ```sh
  +ученик Имя Фамилия 9а 321
  ```
  
  *В личные сообщения с ботом. Доступна всем пользователям.*
  

## **Функция `new_info(ctx, inf, *text)`**

  Смотреть в файле `Discord_bot.py`. Строка 199-225

Аргументы:
* Категория
* Информация (произвольный текст)

  Заполнение личного кабинета учителя. Функция добавляет в словарь `new_teacher` информацию в раздел с учителем.  
  Категории: консультации, расписание, доп занятия, важная информация.

  ```sh
  +добавить_информацию расписание сегодня два урока
  ```
  *В любой канал. Доступна директору, руководству, учителю.*
  

## **Функция `info(ctx, name, surname, inf)`**

  Смотреть в файле `Discord_bot.py`. Строка 228-237

Аргументы:
* Имя учителя
* Отчество учителя
* Категория

  Получение информации из личного кабинета указанного учителя.  
  Категории: консультации, расписание, доп занятия, важная информация.

  ```sh
  +информация имя отчество расписание
  ```
  *В любой канал. Доступна всем пользователям.*
  

## **Функция `commands(ctx)`**

  Смотреть в файле `Discord_bot.py`. Строка 240-269
  
Аргументы:
* Нет

   Выводит подсказку по командам в зависимости от прав доступа пользователя.

  ```sh
  +команды
  ```
  *В любой канал. Доступна всем пользователям.*
  

## **Функция `del_info(ctx, inf, index)`**

  Смотреть в файле `Discord_bot.py`. Строка 272-283

Аргументы:
* Категория
* Индекс

  Удаление информации из личного кабинета учителя.
  Категории: консультации, расписание, доп занятия, важная информация.
  Индекс, под которым находится информация в данной категории (начиная с 1)

  ```sh
  +удалить_информацию расписание 3
  ```
  *В любой канал. Доступна директору, руководству, учителю.*
  

## **Функция `new_students_password(ctx, cl, password)`**

  Смотреть в файле `Discord_bot.py`. Строка 286-315

Аргументы:
* Класс
* Пароль

  Меняет пароль для регистрации учеников в указанном классе. Закрепляет сообщение с паролем в учительской этого класса.  
  Ученики уведомляются об этом в Telegram.

  ```sh
  +учепароль 9г 12345
  ```
  *В любой канал. Доступна руководству и учителю.*
  

## **Функция `new_teachers_password(ctx, password)`**

  Смотреть в файле `Discord_bot.py`. Строка 318-345

Аргументы:
* Пароль для учителей

  Меняет пароль для регистрации учителей. Закрепляет сообщение с паролем в общем канале для учителей.  
  Учителя уведомляются об этом в Telegram.

  ```sh
  +учипароль 12345
  ```
  *В любой канал. Доступна директору и руководству.*
  

## **Функция `start(ctx, name, surname, password)`**

  Смотреть в файле `Discord_bot.py`. Строка 348-458

Аргументы:
* Имя
* Отчество
* Пароль для учителей

  Функция подготавливает пространство сервера для регистрации пользователей.  
  Создаются категории: 
    Общий раздел:
      * Общение лицея (текстовый)
      * Частые вопросы (текстовый)
      * Главный холл (голосовой)
    Чат сотрудников:
      * Директор (текстовый)
      * Чат руководства (текстовый)
      * Чат учителей (текстовый)
      * Общее собрание (голосовой)
      * Общение учителей (голосовой)
      * Общение руководства (голосовой)
  
  Отдельное внимание хочу уделить текстовому каналу `Логи команд`.  
  Доступ к этому каналу имеет только директор и руководство. В нем хранятся все данные об использовании команд на сервере. Под каждую команду создана своя форма. В ней указвается пользователь, время, канал, в некоторых случаях удачно или неудачно (при регистрации) и прочая полезная информация.  
  Этот канал облегчает учет пользователей и их ролей, позволяет следить за безопасностью и использованием команд на сервере.

  ```sh
  +старт_сервера Имя Отчество 
  ```
  *В любой канал. Доступна директору.*


## **Функция `new_passwords_for_students(ctx)`**

  Смотреть в файле `Discord_bot.py`. Строка 461-485
  
Аргументы:
* Нет

  Меняет пароль для регистрации учеников во всех классах. Закрепляет сообщение с паролем в учительской каждого класса.  
  Ученики уведомляются об этом в Telegram.

  ```sh
  +пароли_ученик
  ```
  *В любой канал. Доступна директору и руководству.*
  

## **Функция `stop_reg_teacher(ctx)`**

  Смотреть в файле `Discord_bot.py`. Строка 488-516
  
Аргументы:
* Нет

  Останавливает регистрацию учителей. Функция меняет пароль для регистрации учителей на случайно сгенерированный. При этом новый пароль не объявляется никому.  
  Учители уведомляются об этом в Telegram.

  ```sh
  +стопрегучители
  ```
  *В любой канал. Доступна директору.*
  

## **Функция `stop_reg_students(ctx)`**

  Смотреть в файле `Discord_bot.py`. Строка 519-552
  
Аргументы:
* Нет

   Останавливает регистрацию учеников. Функция меняет пароль для регистрации учеников в каждом классе на случайно сгенерированный. При этом новый пароль не объявляется никому.  
   Ученики уведомляются об этом в Telegram.

  ```sh
  +стопрегученики
  ```
  *В любой канал. Доступна директору.*
  

## **Функция `on_member_join(member)`**

  Смотреть в файле `Discord_bot.py`. Строка 555-579
  
Аргументы:
* Нет

  Системная (не вызывается вручную). Отправляет приветственное сообщение новым пользователям.
  

## **Функция `check_users(ctx)`**

  Смотреть в файле `Discord_bot.py`. Строка 582-594
  
Аргументы:
* Нет

  Удаляет из базы данных информацию о пользователях, не находящихся на сервере.  
  Так называемая "чистка".

  ```sh
  +проверка_пользователей
  ```
  *В любой канал. Доступна директору и руководству.*


## **Функция `get_id`**

  Смотреть в файле `Discord_bot.py`. Строка 597-600
  
Аргументы:
* Нет

  Команда прописывается Telegram боту. Вы получаете свой ID, он пригодится для регистрации своего аккаунта Telegram в Discord сообществе школы.  
  Если ваш Telegram зарегестрирован при помощи команд `+телеграм ID`, то бот будет уведомлять вас о смене паролей в вашем классе.  

   [Telegram бот](https://t.me/Ynik_bot)


<!-- CONTACT -->
## Контакты

[ВК](https://vk.com/id437234179)

[Почта](nikitayusko2007@gmail.com)

[Ссылка на проект](https://github.com/caffreyfizz/e-school-Unik)


<!-- LICENSE -->
## Лицензия

Распространяется по лицензии MIT. См `LICENSE` дополнительная информация.


<!-- ACKNOWLEDGMENTS -->
## Благодарность

  В первую очередь, хочу выразить слова благодарности [@DMGolD](https://t.me/DMGolD) за моральную поддержку на протяжении всего времени реализации проекта.  

Также отдельно выделю ресурсы, которые помогли мне в разработке.

* [Документация discord.py](https://discordpy.readthedocs.io/en/stable/)
* [Документация asyncio](https://docs.python.org/3/library/asyncio.html)
* [Документация aiogram](https://docs.aiogram.dev/ru/latest/index.html)
* [Stack Overflow](https://stackoverflow.com/)
* [Habr](https://habr.com/ru/all/)


<p align="right">(<a href="#о-проекте">В начало</a>)</p>
