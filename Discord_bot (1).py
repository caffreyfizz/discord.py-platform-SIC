import discord
from discord.ext import commands

from bs4 import BeautifulSoup
import random
import asyncio
import requests
from datetime import datetime

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor


API_TOKEN = "5939181352:AAGoG3q5-vYX37Ns0TNNDmvgLGZ8AETcJ4I"  # token Telegram bot
logging.basicConfig(level=logging.INFO)
tele_bot = Bot(token=API_TOKEN)  # Telegram bot
storage = MemoryStorage()
dp = Dispatcher(tele_bot, storage=storage)  # commands telegram

loop = asyncio.get_event_loop()  # a separate thread to run two bots


intents = discord.Intents.all()  # setting the standard permissions to the discord bot
intents.message_content = True  # give the discord bot permission to read the contents of the message
bot = commands.Bot(command_prefix='+', intents=intents)  # задаем префикс и права для бота

# website for parsing information
url = requests.get('https://369.pelikan.online/?start=24.09.2022&finish=24.09.2022&all=on&status=pnd&status=run&status=fin')
soup = BeautifulSoup(url.text, 'lxml')
text = soup.find_all('div', class_='truncate')

classes = {}  # class roles and their roles for students
new_teacher = {}  # teachers' personal account
telegram_id = {}  # list of users registered in telegram
passwords = {}  # class passwords
easy_passwords = [123456, 123456789, 12345678, 12345, 1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 123123, 1234567, 1234567890, 666666, 7777777, 555555, 123, 000000]
teacher_passwords = []  # password for teachers


@bot.event
async def on_ready():

    """Gets the server ID."""

    global guild
    guild = bot.get_guild(1015693536055787670)


@bot.command(aliases=['пеликан'])
async def pelikan(ctx, cl):

    """Displays lessons from the site https://369.pelikan.online to the user."""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")
    embed = discord.Embed(title='Пеликан', colour=discord.Colour.from_rgb(106, 192, 245))
    embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
    embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
    embed.add_field(name=f"📝  Канал", value=str(ctx.message.channel).title(), inline=False)
    embed.set_footer(text="Лог команды Пеликан | Лицей №369", icon_url=ctx.author.avatar)
    await logs.send("**Пеликан**", embed=embed)

    all_lessons = []  # список для хранения всех уроков
    list_of_one_lesson = []  # список для накопелния информации об одном уроке и внесение этой информации партией в
    # список all_info
    for string_on_html_code in range(0, len(text), 1):  # цикл по каждой строке кода страницы
        string = ' '.join(list(filter(
            lambda info: info != '' and info not in ['face', 'alarm', 'people', 'videocam'],
            # фильтрация списочного выражения, для получения только нужной информации и преобразование информации в
            # строку
            [info_string.strip() for info_string in text[string_on_html_code].text.split(
                '\n')])))  # списочное выражение для получения информации по уроку в одну строку
        # это информация вида 1-ая строка: Имя, 2-ая строка: Время, 3-я строка: Класс, 4-ая строка: Кабинет
        if string_on_html_code <= 3 or string_on_html_code % 4 != 0:  # если это строки, в которой все еще идет
            # информация об одном и том же уроке, то мы ее сохраняем в переменную list_of_one_lesson
            list_of_one_lesson.append(string)
        elif string_on_html_code % 4 == 0:  # если мы считали строку, кратную 4, то в этой строке хранится информация
            # о новом уроке
            all_lessons.append(
                list_of_one_lesson)  # тогда мы добавляем в список со всеми уроками, информацию, накопленную в
            # переменной list_of_one_lesson о старом уроке
            list_of_one_lesson = [
                string]  # оставляем в переменной list_of_one_lesson только информацию о только что считанном уроке
    all_lessons.append(list_of_one_lesson)  # в конце цикла добавляем в all_info информацию о последнем считанном уроке
    printed_lesson = False
    # вывод уроков пользователю
    for lesson in all_lessons:
        if " ".join(list(cl.lower())) == lesson[2].lower():
            await ctx.channel.send(
                f'{lesson[0]}\n{lesson[1]}\n{lesson[2]}\n{lesson[3]}\nhttps://369.pelikan.online/?start=24.09.2022'
                f'&finish=24.09.2022&all=on&status=pnd&status=run&status=fin')
            printed_lesson = True  # если мы вывели какой-то урок, значит он был в списке all_info, значит мы меняем
            # flag на True
    if printed_lesson == False:  # если flag так и остался False, то есть никакой урок не был выведен, то бот
        # сообщает об этом пользователю
        await ctx.channel.send('В пеликане нет записей и запланированных трансляций об этих уроках')


@bot.command(aliases=['телеграм'])
@commands.dm_only()
async def telegram(ctx, *args):

    date = datetime.now()

    logs = discord.utils.get(guild.channels, name="логи-команд")
    embed = discord.Embed(title='Телеграм', colour=discord.Colour.from_rgb(106, 192, 245))
    embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
    embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
    embed.add_field(name=f"📝  Канал:", value="Личные сообщения с ботом", inline=False)
    embed.set_footer(text="Лог команды Телеграм | Лицей №369", icon_url=ctx.author.avatar)
    await logs.send("**Телеграм**", embed=embed)

    if ctx.channel.type != discord.ChannelType.private:
        return
    if ctx.author.id in telegram_id:
        await ctx.channel.send("Вы итак уже в моей базе данных")
        return
    if type(args) is tuple:
        user_id = int(" ".join(list(args)).split()[-1])
        telegram_id[ctx.author.id] = user_id
    else:
        telegram_id[ctx.author.id] = int(str(args))
    await ctx.channel.send("Теперь я буду уведомлять вас в личные сообщения Telegram о смене пароля для регистрации")
    await ctx.channel.send("Найти меня вы можете здесь: https://t.me/Ynik_bot")
    print(telegram_id)


@bot.command(aliases=['удалить_телеграм'])
@commands.dm_only()
async def telegram_delete(ctx):

    date = datetime.now()

    logs = discord.utils.get(guild.channels, name="логи-команд")
    embed = discord.Embed(title='Удалить_телеграм', colour=discord.Colour.from_rgb(106, 192, 245))
    embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
    embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
    embed.add_field(name=f"📝  Канал:", value="Личные сообщения с ботом", inline=False)
    embed.set_footer(text="Лог команды Удалить_телеграм | Лицей №369", icon_url=ctx.author.avatar)
    await logs.send("**Удалить телеграм**", embed=embed)

    if ctx.channel.type != discord.ChannelType.private:
        return
    if ctx.author.id in telegram_id:
        telegram_id.pop(telegram_id[ctx.author.id])
        await ctx.channel.send("Больше не буду беспокоить вас в telegram")
    else:
        await ctx.channel.send("Не могу найти вас в базе данных")


@bot.command(aliases=['учитель'])
@commands.dm_only()
async def teacher(ctx, teachers_password, name, surname, cl, password):

    """Регистрация на сервере как учитель. Смена ника, выдача ролей, создание категории и каналов, генерация пароля и пр."""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")

    if ctx.channel.type != discord.ChannelType.private:
        return
    if teachers_password != teacher_passwords[0]:
        await ctx.channel.send("Неверный пароль!")

        embed = discord.Embed(title='Учитель', colour=discord.Colour.from_rgb(178, 34, 34))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.name, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value="Личные сообщения с ботом", inline=False)
        embed.add_field(name=f"❌  Состояние:", value="Неудачно. Неверный пароль.", inline=False)
        embed.set_footer(text="Лог команды Учитель | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Учитель (неудачно)**", embed=embed)

        return
    if (password.isdigit() and int(password) in easy_passwords) or password in passwords.values():
        await ctx.channel.send("Придумайте новый пароль и повторите попытку.")

        embed = discord.Embed(title='Учитель', colour=discord.Colour.from_rgb(178, 34, 34))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.name, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value="Личные сообщения с ботом", inline=False)
        embed.add_field(name=f"❌  Состояние:", value="Неудачно. Повторяющийся или слишком простой пароль для учеников.", inline=False)
        embed.set_footer(text="Лог команды Учитель | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Учитель (неудачно)**", embed=embed)

        return

    await ctx.channel.send("Вы зарегистрировались как учитель!")
    teach = discord.utils.get(guild.roles, name='Учитель')
    passwords[cl] = password
    perms = discord.Permissions(manage_roles=True, ban_members=True,
                                kick_members=True)  # приватные права для роли учителей
    global role_s
    role_s = await guild.create_role(name=f'Ученик {cl.lower()}')  # создание роли ученика этого класса
    classes[cl.lower()] = role_s  # добавляем роль ученика в словарь класс: id роли класса
    global role_t
    role_t = await guild.create_role(name=f'Учитель {cl.lower()}', permissions=perms)  # создаем роль учителя

    await guild.get_member(ctx.author.id).edit(nick=f"{name.title()} {surname.title()}")  # смена ника пользователю

    embed = discord.Embed(title='Учитель', colour=discord.Colour.from_rgb(50, 205, 50))
    embed.add_field(name=f"🧑  Пользователь:", value=f"{name} {surname}", inline=False)
    embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
    embed.add_field(name=f"📝  Канал:", value="Личные сообщения с ботом", inline=False)
    embed.add_field(name=f"✅  Состояние:", value="Удачно", inline=False)
    embed.add_field(name=f"Класс:", value=cl, inline=False)
    embed.add_field(name=f"Пароль для учеников:", value=password, inline=False)
    embed.set_footer(text="Лог команды Учитель | Лицей №369", icon_url=ctx.author.avatar)
    await logs.send("**Учитель**", embed=embed)

    overwrites = {  # словарь с правами для категории
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        role_s: discord.PermissionOverwrite(read_messages=True),
        role_t: discord.PermissionOverwrite(read_messages=True)}

    overwrites_for_teacher = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                              # словарь с правами для учительской
                              role_t: discord.PermissionOverwrite(read_messages=True),
                              role_s: discord.PermissionOverwrite(read_messages=False)}
    overwrites_for_news = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                           # словарь с правами для учительской
                           role_t: discord.PermissionOverwrite(read_messages=True),
                           teach: discord.PermissionOverwrite(read_messages=True),
                           role_s: discord.PermissionOverwrite(read_messages=True)}
    # создание всех каналов
    global category
    category = await guild.create_category(name=f'{cl.lower()} класс', overwrites=overwrites)
    await guild.create_voice_channel(name='Общение', category=category)
    room_for_teacher = await guild.create_text_channel(name=f'учительская {cl}', category=category,
                                                       overwrites=overwrites_for_teacher)
    await guild.create_text_channel(name='новости класса', category=category, overwrites=overwrites_for_news)
    new_teacher[f'{name.lower()} {surname.lower()}'] = {'консультации': [], 'расписание': [], 'доп_занятия': [],
                                                        'важная_информация': []}  # создание личного кабинета учителя
    await guild.get_member(ctx.author.id).add_roles(role_t, teach)
    message_with_password_for_students = await room_for_teacher.send(f"Пароль для учеников: {password}")
    await message_with_password_for_students.pin()


@bot.command(aliases=['ученик'])
@commands.dm_only()
async def students(ctx, name, surname, cl, password):

    """Регистрация пользователя на сервере как ученик. Смена ника, выдача ролей и пр."""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")

    if passwords[cl] != password:
        await ctx.channel.send(f"Неверный пароль!")

        embed = discord.Embed(title='Ученик', colour=discord.Colour.from_rgb(178, 34, 34))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.name, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value="Личные сообщения с ботом", inline=False)
        embed.add_field(name=f"❌  Состояние:", value="Неудачно. Неверный пароль.", inline=False)
        embed.set_footer(text="Лог команды Ученик | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Ученик**", embed=embed)

        return
    await ctx.channel.send("Вы зарегистрировались как ученик!")
    overwrites = {  # права для личного кабинета ученика
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(guild.roles, name=f"Учитель {cl.lower()}"): discord.PermissionOverwrite(read_messages=True)}

    student_role = discord.utils.get(guild.roles, name="Ученик")
    student_category = discord.utils.get(guild.categories, name=f"{cl.lower()} класс")
    await guild.get_member(ctx.author.id).add_roles(classes[cl])  # добавление ролей ученику
    await guild.get_member(ctx.author.id).add_roles(student_role)
    await guild.create_text_channel(name=f'{name} {surname}', category=student_category,
                                    overwrites=overwrites)  # создание личного кабинета ученика
    await guild.get_member(ctx.author.id).edit(nick=f"{name.title()} {surname.title()}")  # смена ника ученика

    embed = discord.Embed(title='Ученик', colour=discord.Colour.from_rgb(50, 205, 50))
    embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
    embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
    embed.add_field(name=f"📝  Канал:", value="Личные сообщения с ботом", inline=False)
    embed.add_field(name=f"✅  Состояние:", value="Удачно", inline=False)
    embed.set_footer(text="Лог команды Ученик | Лицей №369", icon_url=ctx.author.avatar)
    await logs.send("**Ученик**", embed=embed)


@bot.command(aliases=['добавить_информацию'])
async def new_info(ctx, inf, *text):

    """Добавление информации в личный кабинет учителя"""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")

    # проверка пользователя на наличие роли учителя
    if len(ctx.author.roles) >= 2 and ("Учитель" in ctx.author.roles[1].name or "Директор" in ctx.author.roles[1].name or ("Руководство" in ctx.author.roles[1].name and "Учитель" in ctx.author.roles[2].name)):
        name, surname = ctx.author.nick.split()
        if f'{name.lower()} {surname.lower()}' in new_teacher.keys():  # проверка на наличие личного кабинета этого
            # учителя
            new_teacher[f'{name.lower()} {surname.lower()}'][inf.lower()].append(text)  # добавление информации
            await ctx.channel.send('Информация успешно добавлена!\n'
                                   'Вот вся информация, которая хранится в вашем кабинете:')
            for key, value in new_teacher[
                f'{name.lower()} {surname.lower()}'].items():  # цикл для получения информации из личного кабинета
                # учителя
                if value == []:  # ключ - категория (консультации, расписание....), значение - список. Если
                    # информации там нет, то ничего не выводит
                    continue
                else:
                    await ctx.channel.send(f'**{key.title()}**:')  # вывод информации, которая только что была добавлена
                    for information in value:
                        await ctx.channel.send(f"{' '.join(information)}")

            embed = discord.Embed(title='Добавить информацию', colour=discord.Colour.from_rgb(50, 205, 50))
            embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
            embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
            embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
            embed.add_field(name=f"✅  Состояние:", value="Удачно", inline=False)
            embed.set_footer(text="Лог команды Добавить_информацию | Лицей №369", icon_url=ctx.author.avatar)
            await logs.send("**Добавить информацию**", embed=embed)

        else:
            await ctx.channel.send('Увы, но я не знаю такого учителя')  # если указанный учитель не зарегистрирован

            embed = discord.Embed(title='Добавить информацию', colour=discord.Colour.from_rgb(178, 34, 34))
            embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
            embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
            embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
            embed.add_field(name=f"❌  Состояние:", value="Неудачно. Не найден учитель.", inline=False)
            embed.set_footer(text="Лог команды Добавить_информацию | Лицей №369", icon_url=ctx.author.avatar)
            await logs.send("**Добавить информацию**", embed=embed)
    else:
        await ctx.channel.send('Ты не можешь использовать такую команду')  # если ученик написал эту команду

        embed = discord.Embed(title='Добавить информацию', colour=discord.Colour.from_rgb(178, 34, 34))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"❌  Состояние:", value="Неудачно. Команда недоступна для пользователя.", inline=False)
        embed.set_footer(text="Лог команды Добавить_информацию | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Добавить информацию**", embed=embed)


@bot.command(aliases=['информация'])
async def info(ctx, name, surname, inf):

    """Вывод информации пользователю из личного кабинета учителя"""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")
    embed = discord.Embed(title='Информация', colour=discord.Colour.from_rgb(106, 192, 245))
    embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
    embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
    embed.add_field(name=f"📝  Канал:", value=str(ctx.message.channel).title(), inline=False)
    embed.add_field(name=f"Учитель:", value=f"{name} {surname}", inline=False)
    embed.set_footer(text="Лог команды Информация | Лицей №369", icon_url=ctx.author.avatar)
    await logs.send("**Информация**", embed=embed)

    if len(new_teacher[f'{name.lower()} {surname.lower()}'][inf.lower()]) != 0:
        for info in new_teacher[f'{name.lower()} {surname.lower()}'][inf.lower()]:  # получение
            await ctx.channel.send(' '.join(info))  # вывод
    else:
        await ctx.channel.send("В этом разделе информации нет")


@bot.command(aliases=['команды'])
async def commands(ctx):

    """Подсказка по всем командам, доступным пользователю на сервере"""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")

    embed = discord.Embed(title='Команды', colour=discord.Colour.from_rgb(106, 192, 245))
    embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
    embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
    embed.add_field(name=f"📝  Канал:", value=str(ctx.message.channel).title(), inline=False)
    embed.set_footer(text="Лог команды Команды | Лицей №369", icon_url=ctx.author.avatar)
    await logs.send("**Команды**", embed=embed)

    if 'Ученик' in ctx.author.roles[1].name:  # если ты ученик
        await ctx.channel.send(
            f'Привет, дорогой(-ая) {f"<@{ctx.author.id}>"}!\nЯ вижу, что ты забыл на что я способен. '
            f'Так давай я тебе напомню!\nК каждой команде обязательно используй **префикс "+"**\n'
            f'**пеликан** *класс* - показывает тебе все текущие или будущие уроки твоего класса в Пеликане\n'
            f'**ученик** *имя, фамилия, класс, пароль* - регистрирует тебя на этом сервере\n'
            f'Обрати внимание, что писать команду "+ученик" ты должен в личные сообщения боту\n '
            f'**информация** *имя учителя, отчество учителя, *на выбор(консультации, расписание, доп_занятия, '
            f'важная_информация)* - показывает тебе информацию, оставленную учителем\n')
    elif 'Учитель' in ctx.author.roles[1].name:  # если ты учитель
        await ctx.channel.send(
            f'Здравствуй, уважаемый(-ая) {f"<@{ctx.author.id}>"}!\nЯ вижу, что ты забыл на что я способен. '
            f'Так давай я тебе напомню!\nК каждой команде обязательно используй **префикс "+"**\n'
            f'**учитель** *пароль учителя, имя, отчество, класс, пароль для учеников* - регистрирует тебя как учителя\n'
            f'**пеликан** *класс* - показывает тебе все текущие или будущие уроки класса в Пеликане\n'
            f'**информация** *имя учителя, отчество учителя, на выбор(консультации, расписание, доп_занятия, '
            f'важная_информация)* - показывает тебе информацию, оставленную учителем\n '
            f'**добавить_информацию** *на выбор(консультации, расписание, доп._занятия, важная_информация), сама информация*'
            f' - добавляет в базу данных информацию, которую ученики с легкостью смогут сами посмотреть\n'
            f'**удалить_информацию** *на выбор(консультации, расписание, доп._занятия, важная_информация) номер* - '
            f'удаляет информацию, опубликованную под номером, указанным вами\n'
            f'**учепароль** *новый пароль* - меняет пароль для регистрации учеников в вашем классе')
    else:
        await ctx.channel.send(f'Эта команда доступна только участникам с ролью "Ученик" или "Учитель".\n'
                               f'Увидеть доступные вам команды вы можете в своих личных каналах')


@bot.command(aliases=['удалить_информацию'])
async def del_info(ctx, inf, index):

    """Удаляет информацию из личного кабинета учителя."""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")

    name, surname = ctx.author.nick.split()
    if len(ctx.author.roles) >= 2 and ("Учитель" in ctx.author.roles[1].name or "Директор" in ctx.author.roles[1].name or ("Руководство" in ctx.author.roles[1].name and "Учитель" in ctx.author.roles[2].name)):
        del new_teacher[f'{name.lower()} {surname.lower()}'][inf.lower()][
            int(index) - 1]  # получение информации с указанным индексом и ее удаление
        await ctx.channel.send('Информация успешно удалена!')

        embed = discord.Embed(title='Удалить информацию', colour=discord.Colour.from_rgb(50, 205, 50))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"✅  Состояние:", value="Удачно", inline=False)
        embed.set_footer(text="Лог команды Удалить_информацию | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Удалить информацию**", embed=embed)

    else:
        await ctx.channel.send("Ты не можешь использовать такую команду")

        embed = discord.Embed(title='Удалить информацию', colour=discord.Colour.from_rgb(178, 34, 34))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"❌  Состояние:", value="Неудачно. Команда недоступна для пользователя.", inline=False)
        embed.set_footer(text="Лог команды Удалить_информацию | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Удалить информацию**", embed=embed)


@bot.command(aliases=['учепароль'])
async def new_students_password(ctx, cl, password):

    """Меняет пароль для одного класса"""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")

    await ctx.message.delete()

    role = discord.utils.get(guild.roles, name=f"Ученик {cl}")
    members = role.members

    if (password.isdigit() and int(password) in easy_passwords) or password in passwords.values():
        await ctx.channel.send("Придумайте новый пароль и повторите попытку.")

        embed = discord.Embed(title='Учепароль', colour=discord.Colour.from_rgb(178, 34, 34))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"❌  Состояние:", value="Неудачно. Повторяющийся или слишком простой пароль.", inline=False)
        embed.set_footer(text="Лог команды Учепароль | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Учепароль**", embed=embed)

        return

    if len(ctx.author.roles) >= 2 and ("Учитель" in ctx.author.roles[1].name or ("Руководство" in ctx.author.roles[1].name and "Учитель" in ctx.author.roles[2].name)):

        embed = discord.Embed(title='Учепароль', colour=discord.Colour.from_rgb(50, 205, 50))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"✅  Состояние:", value="Удачно.", inline=False)
        embed.add_field(name=f"Класс:", value=cl, inline=False)
        embed.add_field(name=f"Новый пароль для учеников:", value=password, inline=False)
        embed.set_footer(text="Лог команды Учепароль | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Учепароль**", embed=embed)

        for user in members:
            if user.id in telegram_id:
                await tele_bot.send_message(telegram_id[user.id], f"Новый пароль для регистрации учеников: {password}")

        passwords[cl] = password
        channel = discord.utils.get(guild.channels, name=f"учительская-{cl}")
        pins = await ctx.channel.pins()

        for pin in pins:
            if "пароль для учеников" in pin.content.lower() or "регистрация учеников остановлена" in pin.content.lower():
                await pin.delete()
                new_pin = await channel.send(f"Новый пароль для учеников: {password}")
                await new_pin.pin()
                return


@bot.command(aliases=['учипароль'])
async def new_teachers_password(ctx, password):

    """Меняет пароль для учителей"""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")

    await ctx.message.delete()

    role = discord.utils.get(guild.roles, name="Учитель")
    members = role.members

    if len(ctx.author.roles) >= 2 and ("Директор" in ctx.author.roles[1].name or "Руководство" in ctx.author.roles[1].name):

        embed = discord.Embed(title='Учипароль', colour=discord.Colour.from_rgb(50, 205, 50))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"✅  Состояние:", value="Удачно.", inline=False)
        embed.add_field(name=f"Новый пароль для учителей:", value=password, inline=False)
        embed.set_footer(text="Лог команды Учипароль | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Учипароль**", embed=embed)

        for user in members:
            if user.id in telegram_id:
                await tele_bot.send_message(telegram_id[user.id], f"Новый пароль для регистрации учителей: {password}")

        teacher_passwords.clear()
        teacher_passwords.append(password)
        channel = discord.utils.get(ctx.guild.channels, name=f"чат-учителей")
        channel_with_teachers_password = discord.utils.get(guild.channels, name="чат-учителей")
        pins = await channel_with_teachers_password.pins()

        for pin in pins:
            if "пароль для учителей" in pin.content.lower() or "регистрация учителей остановлена" in pin.content.lower():
                await pin.delete()
                new_pin = await channel.send(f"Новый пароль для учителей: {password}")
                await new_pin.pin()
                return
    else:

        embed = discord.Embed(title='Учипароль', colour=discord.Colour.from_rgb(178, 34, 34))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"❌  Состояние:", value="Неудачно. Команда недоступна для пользователя.", inline=False)
        embed.set_footer(text="Лог команды Учипароль | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Учипароль**", embed=embed)


@bot.command(aliases=['старт_сервера'])
async def start(ctx, name, surname, password):

    """Создает роли, категории, каналы и прочее, необходимые для начала регистрации пользователей"""

    await ctx.message.delete()
    overwrites_for_everyone = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Ученик"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Учитель"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Руководство"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Директор"): discord.PermissionOverwrite(read_messages=True)}

    overwrites_for_logs = {guild.default_role: discord.PermissionOverwrite(read_messages=False),
                           discord.utils.get(ctx.guild.roles, name="Руководство"): discord.PermissionOverwrite(read_messages=True),
                           discord.utils.get(ctx.guild.roles, name="Директор"): discord.PermissionOverwrite(read_messages=True)}

    overwrites_for_management = {guild.default_role: discord.PermissionOverwrite(read_messages=False)}

    overwrites_for_management_t = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Учитель"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Руководство"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Директор"): discord.PermissionOverwrite(read_messages=True)}

    overwrites_for_management_m = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Руководство"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Директор"): discord.PermissionOverwrite(read_messages=True)}

    overwrites_for_director = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Директор"): discord.PermissionOverwrite(read_messages=True)}

    overwrites_for_questions = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Ученик"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Учитель"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Руководство"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Директор"): discord.PermissionOverwrite(read_messages=True)}

    if len(ctx.author.roles) >= 2 and "Директор" in ctx.author.roles[1].name:
        new_teacher[f'{name.lower()} {surname.lower()}'] = {'консультации': [], 'расписание': [], 'доп_занятия': [],
                                                            'важная_информация': []}

        teacher_passwords.clear()
        teacher_passwords.append(password)

        await guild.create_text_channel(name="Логи команд", overwrites=overwrites_for_logs)

        category_for_everyone = await guild.create_category(name=f'Общий раздел', overwrites=overwrites_for_everyone)
        await guild.create_voice_channel(name='Главный холл', category=category_for_everyone)
        await guild.create_text_channel(name="Общение лицея", category=category_for_everyone)

        category_for_management = await guild.create_category(name=f'Чат сотрудников',
                                                              overwrites=overwrites_for_management)
        room_for_teacher = await guild.create_text_channel(name='чат учителей', category=category_for_management,
                                                           overwrites=overwrites_for_management_t)
        voice_room_for_teachers = await guild.create_voice_channel(name='Общение учителей',
                                                                   category=category_for_management, overwrites=overwrites_for_management_t)
        voice_room_for_management = await guild.create_voice_channel(name='Общение руководства', category=category_for_management, overwrites=overwrites_for_management_m)
        voice_room_for_personal = await guild.create_voice_channel(name='Общее собрание',
                                                                   category=category_for_management, overwrites=overwrites_for_management_t)
        room_for_management = await guild.create_text_channel(name='чат руководства', category=category_for_management,
                                                              overwrites=overwrites_for_management_m)
        room_for_director = await guild.create_text_channel(name="директор", overwrites=overwrites_for_director, category=category_for_management)
        room_for_questions = await guild.create_text_channel(name="Частые вопросы", overwrites=overwrites_for_questions, category=category_for_everyone)
        message_with_teachers_passwords = await room_for_teacher.send(f'Пароль для учителей: {password}')
        await message_with_teachers_passwords.pin()
        message_for_questions = await room_for_questions.send(f"**Итак, здравствуй! Давай начнем с правилами использования команд**\n"
                                                              f"\t1. Чтобы узнать доступные тебе команды - напиши +команды в любой чат или посмотри закрепленные сообщения в новостях твоего класса.\n"
                                                              f"\t2. При прописывании команды аргументы указываются строго через пробел, без запятых и прочих символов. Например: +ученик Имя Фамилия класс пароль.\n"
                                                              f"\t3. Много ли команд я знаю? - Конечно, но большинство из них предназначены для сотрудников. Со временем будут новые команды и для учеников.\n"
                                                              f"\t4. Может ли посторонний зарегистрироваться как учитель? - Сомневаюсь, пароли учителей регулярно меняются и состав учителей отслеживается.\n"
                                                              f"\t5. Могу ли я пригласить друга на сервер? - Нет, этот сервер предназначен только для учеников и сотрудников Лицея №369.\n"
                                                              f"Соблюдайте нормы общения на сервере. Избегайте спама, оскорблений, попыток обойти алгоритмы бота и уважайте друг друга.")
        await message_for_questions.pin()
        message_with_commands_for_teacher = await room_for_teacher.send(f'**учитель** *пароль учителя, имя, отчество, класс, пароль для учеников* - регистрирует тебя как учителя\n'
                                                                        f'**пеликан** *класс* - показывает тебе все текущие или будущие уроки класса в Пеликане\n'
                                                                        f'**информация** *имя учителя, отчество учителя, на выбор(консультации, расписание, доп_занятия, '
                                                                        f'важная_информация)* - показывает тебе информацию, оставленную учителем\n '
                                                                        f'**добавить_информацию** *на выбор(консультации, расписание, доп._занятия, важная_информация), сама информация*'
                                                                        f' - добавляет в базу данных информацию, которую ученики с легкостью смогут сами посмотреть\n'
                                                                        f'**удалить_информацию** *на выбор(консультации, расписание, доп._занятия, важная_информация) номер* - '
                                                                        f'удаляет информацию, опубликованную под номером, указанным вами\n'
                                                                        f'**учепароль** *новый пароль* - меняет пароль для регистрации учеников в вашем классе')
        await message_with_commands_for_teacher.pin()
        message_with_commands_for_management = await room_for_management.send(f'**учитель** *пароль учителя, имя, отчество, класс, пароль для учеников* - регистрирует тебя как учителя\n'
                                                                              f'**пеликан** *класс* - показывает тебе все текущие или будущие уроки класса в Пеликане\n'
                                                                              f'**информация** *имя учителя, отчество учителя, на выбор(консультации, расписание, доп_занятия, '
                                                                              f'важная_информация)* - показывает тебе информацию, оставленную учителем\n '
                                                                              f'**добавить_информацию** *на выбор(консультации, расписание, доп._занятия, важная_информация), сама информация*'
                                                                              f' - добавляет в базу данных информацию, которую ученики с легкостью смогут сами посмотреть\n'
                                                                              f'ТОЛЬКО если вы зарегистрированы как учитель\n'
                                                                              f'**удалить_информацию** *на выбор(консультации, расписание, доп._занятия, важная_информация) номер* - '
                                                                              f'удаляет информацию, опубликованную под номером, указанным вами\n'
                                                                              f'ТОЛЬКО если вы зарегистрированы как учитель\n'
                                                                              f'**учепароль** *новый пароль* - меняет пароль для регистрации учеников в вашем классе\n'
                                                                              f'ТОЛЬКО если вы зарегистрированы как учитель\n'
                                                                              f'**удалить_учителя** *Имя, Отчество, класс* - удаляет учителя\n'
                                                                              f'**пароли_ученик** - меняет пароли всем классам\n')
        await message_with_commands_for_management.pin()
        message_with_commands_for_director = await room_for_director.send(f'**пеликан** *класс* - показывает тебе все текущие или будущие уроки класса в Пеликане\n'
                                                                          f'**добавить_информацию** *на выбор(консультации, расписание, доп._занятия, важная_информация), сама информация*'
                                                                          f' - добавляет в базу данных информацию, которую ученики с легкостью смогут сами посмотреть\n'
                                                                          f'**удалить_информацию** *на выбор(консультации, расписание, доп._занятия, важная_информация) номер* - '
                                                                          f'удаляет информацию, опубликованную под номером, указанным вами\n'
                                                                          f'**удалить_учителя** *Имя, Отчество, класс* - удаляет учителя\n'
                                                                          f'**пароли_ученик** - меняет пароли всем классам\n'
                                                                          f'**стопрегучители** - останавливает регистрацию учителей\n'
                                                                          f'**стопрегученики** - останавливает регистрацию учеников')
        await message_with_commands_for_director.pin()

        for user in telegram_id.values():
            await tele_bot.send_message(user, f'Сервер "Лицей №369" начал свою работу!\n'
                                              f'Ученики, вы можете начинать регистрироваться сразу после ваших учителей.'
                                              f'Учителя, постарайтесь завершить регистрацию в ближайшее время и сообщить ученикам пароль.')

        date = datetime.now()
        logs = discord.utils.get(guild.channels, name="логи-команд")

        embed = discord.Embed(title='Старт', colour=discord.Colour.from_rgb(50, 205, 50))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=str(ctx.message.channel).title(), inline=False)
        embed.add_field(name=f"Пароль для учителей:", value=password, inline=False)
        embed.set_footer(text="Лог команды Старт_сервера | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Старт сервера**", embed=embed)


@bot.command(aliases=["пароли_ученик"])
async def new_passwords_for_students(ctx):

    """Меняет пароли всех классов"""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")
    role = discord.utils.get(guild.roles, name="Ученик")
    members = role.members

    for user in members:
        if user.id in telegram_id:
            await tele_bot.send_message(telegram_id[user.id], f"Пароль класса был изменен.")

    if len(ctx.author.roles) >= 2 and ("Директор" in ctx.author.roles[1].name or "Руководство" in ctx.author.roles[1].name):
        new_passwords = list(range(3154, 10987))
        random.shuffle(new_passwords)
        random.shuffle(new_passwords)

        embed = discord.Embed(title='Пароли ученик', colour=discord.Colour.from_rgb(50, 205, 50))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=str(ctx.message.channel).title(), inline=False)
        embed.set_footer(text="Лог команды Пароли_ученик | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Пароли ученик**", embed=embed)

        for key, value in passwords.items():
            new_password = random.choice(new_passwords)
            del new_passwords[new_passwords.index(new_password)]
            passwords[key] = new_password
            channel = discord.utils.get(ctx.guild.channels, name=f"учительская-{key}")
            pins = await channel.pins()

            for pin in pins:
                if "пароль для учеников" in pin.content.lower() or "Регистрация учеников остановлена" in pin.content:
                    await pin.delete()
                    new_pin = await channel.send(f"*Новый пароль для учеников:* **{new_password}**")
                    await new_pin.pin()
                    break
    else:

        embed = discord.Embed(title='Пароли ученик', colour=discord.Colour.from_rgb(178, 34, 34))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=str(ctx.message.channel).title(), inline=False)
        embed.add_field(name=f"❌  Состояние:", value="Неудачно.", inline=False)
        embed.set_footer(text="Лог команды Пароли_ученик | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Пароли ученик (неудачно)**", embed=embed)

        return


@bot.command(aliases=["стопрегучители"])
async def stop_reg_teacher(ctx):

    """Останавливает регистрацию учителей"""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")

    role = discord.utils.get(guild.roles, name="Учитель")
    members = role.members

    if len(ctx.author.roles) >= 2 and "Директор" in ctx.author.roles[1].name:

        embed = discord.Embed(title='Стопрегучители', colour=discord.Colour.from_rgb(50, 205, 50))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"✅  Состояние:", value="Удачно.", inline=False)
        embed.set_footer(text="Лог команды Стопрегучители | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Стопрегучители**", embed=embed)

        for user in members:
            if user.id in telegram_id:
                await tele_bot.send_message(telegram_id[user.id], f"Регистрация учителей остановлена.")

        teacher_passwords.clear()
        teacher_passwords.append(random.randint(576351675361, 9018309183981731535))
        channel = discord.utils.get(ctx.guild.channels, name="чат-руководства")
        channel_for_teachers = discord.utils.get(ctx.guild.channels, name="чат-учителей")
        pins = await channel_for_teachers.pins()

        for pin in pins:
            if "пароль для учителей" in pin.content.lower():
                await pin.delete()
                await channel.send(f"Регистрация учителей остановлена.\nДля возобновления регистрации воспользуйтесь функцией **учипароль**")
                new_pin = await channel_for_teachers.send("Регистрация учителей остановлена")
                await new_pin.pin()
                return
    else:

        embed = discord.Embed(title='Стопрегучители', colour=discord.Colour.from_rgb(178, 34, 34))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"❌  Состояние:", value="Неудачно. Команда недоступна для пользователя.", inline=False)
        embed.set_footer(text="Лог команды Стопрегучители | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Стопрегучители**", embed=embed)

        return


@bot.command(aliases=["стопрегученики"])
async def stop_reg_students(ctx):

    """Останавливает регистрацию учеников."""

    date = datetime.now()
    logs = discord.utils.get(guild.channels, name="логи-команд")

    if len(ctx.author.roles) >= 2 and "Директор" in ctx.author.roles[1].name:

        embed = discord.Embed(title='Стопрегученики', colour=discord.Colour.from_rgb(50, 205, 50))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"✅  Состояние:", value="Удачно.", inline=False)
        embed.set_footer(text="Лог команды Стопрегученики | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Стопрегученики**", embed=embed)

        role = discord.utils.get(guild.roles, name="Ученик")
        members = role.members
        for user in members:
            if user.id in telegram_id:
                await tele_bot.send_message(telegram_id[user.id], f"Регистрация учеников остановлена.")

        new_passwords = list(range(189999889989999, 189999890000000))

        for key, value in passwords.items():
            password = random.choice(new_passwords)
            del new_passwords[new_passwords.index(password)]
            passwords[key] = password
            channel_for_student = discord.utils.get(guild.channels, name=f"учительская-{key}")
            pins = await channel_for_student.pins()

            for pin in pins:
                if "пароль для учеников" in pin.content.lower():
                    await pin.delete()
                    new_pin = await channel_for_student.send(f"Регистрация учеников остановлена.")
                    await new_pin.pin()
                    break

        channel = discord.utils.get(ctx.guild.channels, name="чат-руководства")

        await channel.send(f"Регистрация учеников остановлена.\nДля возобновления регистрации воспользуйтесь функцией **пароли_ученик**")
    else:

        embed = discord.Embed(title='Стопрегученики', colour=discord.Colour.from_rgb(178, 34, 34))
        embed.add_field(name=f"🧑  Пользователь:", value=ctx.author.nick, inline=False)
        embed.add_field(name=f"🕑  Время:", value=f"{datetime.strftime(date, '%d.%m.%Y | %H:%M')}", inline=False)
        embed.add_field(name=f"📝  Канал:", value=ctx.message.channel, inline=False)
        embed.add_field(name=f"❌  Состояние:", value="Неудачно. Команда недоступна для пользователя.", inline=False)
        embed.set_footer(text="Лог команды Стопрегученики | Лицей №369", icon_url=ctx.author.avatar)
        await logs.send("**Стопрегученики**", embed=embed)

        return


@bot.event
async def on_member_join(member):

    """Приветственные слова"""

    await member.send(f"""Здравствуй!
Ты присоединился на общий discord-сервер Лицея №369
Сперва предлагаю тебе посетить нашего telegram бота: https://t.me/Ynik_bot
Он будет тебя уведомлять о смене паролей для регистрации, мероприятиях, интересных новостях и прочее
Перейди на страницу бота, получи ID и пропиши команду +телеграм *твой id*
**Примечание:** Вставлять ID можно в любом виде. Как с текстом 'Ваш ID...', так и просто цифры.

Для регистрации **как ученик** пропиши команду **+ученик** мне в личные сообщения
Не забудь указать имя, фамилию, класс, пароль
Пароль можешь получить у классного руководителя или администрации лицея
Пример команды: +ученик Иван Иванов 1е 1234

Для регистрации **как учитель** пропиши команду **+учитель** мне в личные сообщения
**ВНИМАНИЕ!** регистрация как учитель со стороны ученика наказывается!
Для регистрации укажите пароль учителя, имя, отчество, класс, пароль для учеников
Пароль класса сохранится в вашей личной учительской, а пароль учителя можете получить у администрации лицея
Пример команды: +учитель 1234 Елена Анатольевна 9д 4321

**ВАЖНО!** Просьба использовать все команды в личном кабинете, дабы не засорять общие чаты
И помни, я всегда могу подсказать команды! Просто пропиши **+команды** в любой канал сервера""")


@bot.command(aliasses=["проверка_пользователей"])
async def check_users(ctx):
    if "Директор" in ctx.author.roles[1] or "Руководство" in ctx.author.roles[1]:
        for user in new_teacher.keys():
            try:
                user_id = discord.utils.get(guild.members, name=user)
            except:
                new_teacher.pop(user)
        for user in telegram_id:
            try:
                discord.utils.get(guild.members, id=user)
            except:
                telegram_id.pop(user)


@dp.message_handler(commands=['start'])
async def get_id(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id}")
    await message.answer(f"Можете отправить Discord боту как и цифры, так и полностью сообщение с ID")


loop.create_task(bot.start('MTAxNTI4NDY3ODY4MjQ4ODg3Mg.GNTFVI.pip-PXUk0i2j8QQqE2kg4Nidx959JU4OC-epFg'))
loop.create_task(executor.start_polling(dp, skip_updates=True))
try:
    loop.run_forever()
finally:
    loop.stop()
