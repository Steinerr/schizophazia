import re
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    urls = [f'https://pesen-net.livejournal.com/?skip={i*10}' for i in range(5)]

    texts = []
    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            all_texts = soup.find_all('p', {'class': None})
            mono_text = ' '.join((p.text for p in all_texts))
            cleaned_text = ' '.join(re.findall(r'[а-яА-ЯёЁ]+', mono_text))
            cleaned_text = cleaned_text.lower()
            texts.append(cleaned_text)
    text = ' '.join(texts)

