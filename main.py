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
    entry_header = soup.find_all('header', class_='entry-header')
    
    results = []
    
    for header in entry_header:
        title_tag = header.find('h1', class_='entry-title')
        if not title_tag:
            continue
        
        title_text = title_tag.get_text(strip=True)
        
        if 'Upcoming Repacks' in title_text:
            continue
        
        a_tag = title_tag.find('a', href=True)
        link = a_tag['href'] if a_tag else None
        
        time_tag = header.find('time', class_='entry-date')
        date = time_tag['datetime'] if time_tag else None
        
        results.append({
            'title': title_text,
            'link': link,
            'date': date
        })
        
    json_result ={
        "status":"success",
        "new_releases": results
    }
    print(json_result)
    
upcoming_release()
new_release()