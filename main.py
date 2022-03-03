from bs4 import BeautifulSoup
from click import style
import requests
import sys
from rich.console import Console
from rich.progress import track
from rich.table import Table
import time
# https://news.ycombinator.com/newest
# https://news.ycombinator.com/front
# https://news.ycombinator.com/newcomments
# https://news.ycombinator.com/show
# https://news.ycombinator.com/jobs

#-new, -front, -newcomments, -show, -jobs
#print(sys.argv)

BASE_URL = 'https://news.ycombinator.com'
raw_text = requests.get(BASE_URL).text

# bs = BeautifulSoup(raw_text, 'lxml')

# data = bs.find_all('a', {'class': 'titlelink'})

# for item in data:
#     print(f'{item.text} \n[{item.get("href")}]', end='\n\n')

def fetch_info(url):
    console = Console()
    console.print('Fetching...\n', style="bold green")
    response = requests.get(url, stream=True)

    raw_text  = response.text
    bs = BeautifulSoup(raw_text, 'lxml')
    data = bs.find_all('a', {'class': 'titlelink'})
    for item in data:
        text = item.text
        link = item.get('href')

        if link.lower().startswith('item'):
            link = f'{BASE_URL}/{link}'
        console.print(text, style="bold", justify="left")
        console.print(link, style='italic white', justify="left")
        print('\n')
def help():
    table = Table(title="Help")
    console = Console()
    table.add_column("Flags", justify="left", style="green")
    table.add_column("Description", justify="left", style="white")
    table.add_row("-new", "Show the newest posts")
    table.add_row("-past", "Show the front page")
    table.add_row("-show", "Show the show page")
    table.add_row("-jobs", "Show the jobs page")
    table.add_row("-help", "Show this help")
    #table.add_row("-exit", "Exit the program")
    console.print(table)

    # print('Usage: ')
    # print('-new: Newest posts')
    # print('-past: Past posts')
    # #print('-comments: New comments')
    # print('-show: Show posts')
    # print('-jobs: Jobs')
    # print('-help: Help')
if len(sys.argv) == 1:
    fetch_info(BASE_URL)
elif len(sys.argv) == 2 and sys.argv[1] == '-new':
    fetch_info(f'{BASE_URL}/newest')
elif len(sys.argv) == 2 and sys.argv[1] == '-past':
    fetch_info(f'{BASE_URL}/front')
# elif len(sys.argv) == 2 and sys.argv[1] == '-comments':
#     fetch_info(f'{BASE_URL}/newcomments')
elif len(sys.argv) == 2 and sys.argv[1] == '-show':
    fetch_info(f'{BASE_URL}/show')
elif len(sys.argv) == 2 and sys.argv[1] == '-jobs':
    fetch_info(f'{BASE_URL}/jobs')
elif len(sys.argv)==2 and sys.argv[1] == '-help':
    help()
else:
    help()

#https://news.ycombinator.com/item?id=30539080