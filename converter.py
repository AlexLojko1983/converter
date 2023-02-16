import requests


def convert():
    init_currency = input('')
    target_currency = input('')

    while True:
        try:
            amount = float(input(''))
        except:
            print('')
            continue
        if not amount > 0:
            print('')
            continue
        else:
            break
    url = ('' + target_currency + '&from=' + init_currency + '&amount=' + str(amount))

    payload = {}
    headers = {'API_KEY': ''}
    response = requests.request('GET', url, headers= headers, data=payload)
    status_code =response.status_code

    if status_code != 200:
        print('')
        quit()

    result = response.json()
    print('' + str(result['result']))

if __name__ == '__main__'
    convert()
