import telebot

import requests

from bs4 import BeautifulSoup

from decouple import config

from keyboards.inline import inline_keyboard as in_key

bot = telebot.TeleBot(config("TOKEN"))

BASE_URL = 'https://www.eldorado.ru/c/smartfony/'


def get_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers)
    return response.text


def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup


title = {}
images = {}
price = {}


@bot.message_handler(commands=['start', ])
def welcome(message):
    chat_id = message.chat.id
    html = get_url(BASE_URL)
    soup = get_soup(html)
    info = soup.find('div', class_="ListingContent_listingContentWrapper__37KSE").find('ul',
                                                                                       class_='GridInner_list___8u79').find_all(
        'li', class_='ListingProductCardList_productCardListingWrapper__3-o9i')
    count = 0
    while count < 16:
        for i, a in enumerate(info, len(title) + 1):
            title[i] = a.find('div', class_="ListingProductCardList_productCardListingTitle__1eVYx").text
            images[i] = a.find('div', class_="ListingProductCardList_productCardListingSection__2OGZd").find('a',
                                                                                                             class_='ListingProductCardList_productCardListingImageContainer__FqE33').find(
                'img').get('src')
            price[i] = a.find('div',
                              class_="PriceBlock_buyBoxPriceBlock__dpI5A PriceBlock_buyBoxPriceBlockStyledAvailable__1XDmA").find(
                'span', class_='PriceBlock_buyBoxPrice__3QGyj PriceBlock_buyBoxPriceStyled__29J_G').text
            count += 1

            if count >= 16:
                break
        if count >= 16:
            break
    # name_title = ''
    # for i in range(1, len(title)+1):
    #     name_title += f'{i}:{title[i]}\n '
    bot.send_message(chat_id, 'here we go!', reply_markup=in_key)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    chat_id = c.message.chat.id
    for i in range(1, len(title) + 1):
        if str(i) == c.data:
            bot.send_message(chat_id, title[i], )
            bot.send_message(chat_id, images[i])
            bot.send_message(chat_id, price[i])


bot.polling(none_stop=True)
