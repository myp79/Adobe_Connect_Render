import requests


def download(url: str, filename: str) -> None:
    reg = requests.get(url)
    with open('./%s.zip' % filename, 'wb') as file:
        file.write(reg.content)


def url_format(url: str) -> str:
    q_index = url.find('?')
    url = url[:q_index]+'output/filename.zip?download=zip&'+url[q_index+1:]
    return url


if __name__ == '__main__':
    url = input('URL:\n')
    name = input('Filenames:\n')
    url = url_format(url)
    download(url, name)
