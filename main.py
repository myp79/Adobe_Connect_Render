import requests


def download(url: str):
    reg = requests.get(url)
    with open('./test.zip', 'wb') as file:
        file.write(reg.content)


if __name__ == '__main__':
    url = input('URL:\n')
    download(url)
