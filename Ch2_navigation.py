import requests
from bs4 import BeautifulSoup

def main():
    resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/table/table.html')
    soup =BeautifulSoup(resp.text,'html.parser')#解析html檔案
    
    #計算課程均價
    #取得所有課程價錢: (一)使用index
    prices = []
    rows = soup.find('table','table').tbody.find_all('tr')
    for row in rows:
        price = row.find_all('td')[2].text
        #在第index =2的攔位
        prices.append(int(price))
    print(sum(prices)/len(prices))
        
    #(二)使用parent(<td>)的previous_sibling

if __name__ == "__main__":
    main()
