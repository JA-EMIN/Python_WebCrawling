import requests
from bs4 import BeautifulSoup

class Conversaion:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def get_subjects():
    subjects = []
    req = requests.get("https://basicenglishspeaking.com/daily-english-conversation-topics/")
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.findAll('div', {"class": "thrv_wrapper thrv_text_element"})
    for div in divs:
        links = div.findAll('a')
        for link in links:
            subject = link.text
            subjects.append(subject)
    return subjects

subjects = get_subjects()

print(subjects)