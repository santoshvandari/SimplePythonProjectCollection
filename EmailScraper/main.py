import requests
import re
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

def get_emails(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", soup.text))
        return emails
    except:
        return set()

def get_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        for link in soup.find_all('a', href=True):
            links.add(link['href'])
        return links
    except:
        return set()
    
def get_emails_from_domain(url):
    domain_name = get_domain_name(url)
    if domain_name == '':
        print('Invalid URL')
        return
    emails = set()
    links = set()
    links.add(url)
    while len(links) > 0:
        link = links.pop()
        if get_domain_name(link) == domain_name:
            emails = emails.union(get_emails(link))
            links = links.union(get_links(link))
    return emails

if __name__ == '__main__':
    url = input('Enter the URL: ')
    if not url.startswith('http'):
        url = 'http://' + url
    if not re.match(r'https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', url):
        print('Invalid URL')
        sys.exit()
    emails = get_emails_from_domain(url)
    for email in emails:
        print(email)
    print('Total emails found:', len(emails))
