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


upcoming_release()