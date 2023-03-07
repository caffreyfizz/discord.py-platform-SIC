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
    <li>
      <a href="#как-начать-использовать">Как начать использовать</a>
    </li>
    <li><a href="#применение">Применение</a></li>
    <li><a href="#контакты">Контакты</a></li>
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


### Библиотеки

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

Скоро заполню :)


<!-- CONTACT -->
## Контакты

[ВК](https://vk.com/id437234179)

[Почта](nikitayusko2007@gmail.com)

Ссылка на проект: [https://github.com/caffreyfizz/e-school-Unik](https://github.com/caffreyfizz/e-school-Unik)


<!-- ACKNOWLEDGMENTS -->
## Благодарность

Хотелось бы отдельно выделить ресурсы, которые помогли мне в реализации этого проекта.

* [Документация discord.py](https://discordpy.readthedocs.io/en/stable/)
* [Документация asyncio](https://docs.python.org/3/library/asyncio.html)
* [Документация aiogram](https://docs.aiogram.dev/ru/latest/index.html)
* [Stack Overflow](https://stackoverflow.com/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
