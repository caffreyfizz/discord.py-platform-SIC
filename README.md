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
    <li><a href="#usage">Применение</a></li>
    <li><a href="#contact">Контакты</a></li>
    <li><a href="#acknowledgments">Благодарности</a></li>
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

* Операционная система Windows, macOS, Linux
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


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
