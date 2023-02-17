import requests

def converter():
    init_currency = input('Что переводим? ')
    target_currency = input('Во что переводим? ')

    while True:
        try:
            amount = float(input('Сколько переводим?: '))
        except:
            print('Таки сколько?')
            continue
        if not amount > 0:
            print('Слишком мало чтобы переводить -)')
            continue
        else:
            break

    url = (
            "https://api.apilayer.com/exchangerates_data/convert?to=" + target_currency + '&from='
            + init_currency + '&amount=' + str(amount))

    payload = {}
    headers = {
        'apikey': 'JRSaCL6cG9mvxBxapPpW4EpLvVZP2mkh'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code

    if status_code != 200:
        print('Збоит... Попробуй позже')
        quit()

    result = response.json()
    print('Получилось ' + str(result['result']) + " " + str(target_currency))


if __name__ == '__main__':
    converter()

