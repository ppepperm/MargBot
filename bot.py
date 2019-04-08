import requests
import datetime
import time
#Установка адреса бота
url = 'https://api.telegram.org/bot801959812:AAFO7z60M95zAKxSvB0mjfekqbc4tqgoLHA/'
#Get-запрос на обновление информации к боту. Результат – строка json. Метод .json позволяет развернуть ее в массив
def getUpdatesJson(request):
    settings = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=settings)
    return response.json()
#Поиск последнего сообщения из массива чата с пользователем Telegram.
def lastUpdate(dataEnd):
    res = dataEnd['result']
    totalUpdates = len(res) - 1
    return res[totalUpdates]
#Получение идентификатора чата Telegram
def getChatID(update):
    chatID = update['message']['chat']['id']
    return chatID
#получения текста последнего сообщения
def getText(update):
    text= update['message']['text']
    return text;

#отправка запроса sendMessage боту
def sendResp(chat, value):
    settings = {'chat_id': chat, 'text': value}
    resp = requests.post(url + 'sendMessage', data=settings)
    return resp
#Главная функция
def main():
    chatID = getChatID(lastUpdate(getUpdatesJson(url)))
    updateID = lastUpdate(getUpdatesJson(url))['update_id']
#Бесконечный цикл, который отправляет запросы боту на получение обновлений
    while True:
#Если обновление есть, отправляем сообщение
        if updateID == lastUpdate(getUpdatesJson(url))['update_id']:
            text=getText(lastUpdate(getUpdatesJson(url)))
            mani=''
            for k in text:
                if k.isdigit():
                    mani+=k

            mani=int(mani)

            if text=='Кинь мем':
                sendResp(getChatID(lastUpdate(getUpdatesJson(url))), 'Иди нахуй, заебал. Сначала деньги мне плати бля!')
            elif 'руб'in text:
                if mani<100:
                    sendResp(getChatID(lastUpdate(getUpdatesJson(url))), 'Хуле тут так мало? Мне жрать не на что, дебил ты ебучий!')
                else:
                    sendResp(getChatID(lastUpdate(getUpdatesJson(url))), 'Спасибо за донат Анон! Но мемов пока всё равно нет')
            else:
                sendResp(getChatID(lastUpdate(getUpdatesJson(url))), 'Ты чё дебил?\nПисать научись сначала, дегрот!')
            updateID += 1
            time.sleep(1)
#Запуск главной функции
if __name__ == '__main__':
    main()
