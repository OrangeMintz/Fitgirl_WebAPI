from bs4 import BeautifulSoup
import requests

html_content = requests.get('https://fitgirl-repacks.site').text
soup = BeautifulSoup(html_content,'html.parser')

@staticmethod
def upcoming_release():
    entry_div = soup.find('div', class_='entry-content')
    title = entry_div.find('h3')
    upcoming = title.find_all('span')
    
    result = []

    for titles in upcoming:
        title_text = titles.get_text(strip=True).replace('⇢','')
        result.append({"title": title_text})
        
        json_result = {"status": "success",
                       "upcoming_releases": result
                       }
        
    print(json_result)
    return json_result

def new_release():
    entry_title = soup.find_all('h1', class_='entry-title')
    
    results = []
    
    for newRelease in entry_title:
        title_text = newRelease.get_text(strip=True)
        a_tag = newRelease.find('a', href=True)
        link = a_tag['href']
        results.append({'title': title_text, 
                        'link': link})
        
    json_result ={
        "status":"success",
        "new_releases": results
    }
    print(json_result)
    
# upcoming_release()
new_release()