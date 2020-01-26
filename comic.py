import hashlib
import requests
from bs4 import BeautifulSoup

from sys import stdout
import urllib.request

if __name__ == "__main__":    
    
    page_num = 2

    for page_index in range(1, page_num + 1):
        
        target = "https://www.wnacg.com/albums-index-page-" + str(page_index) +".html"
        print(target)
        req = requests.get(url=target)

        bs = BeautifulSoup(req.text)

        divs = bs.find_all(attrs={"class":"pic_box"})

        for div in divs:

            print(div.a["title"])
            name = div.a["title"]

            hash = hashlib.md5(name.encode(encoding='utf-8')).hexdigest()
            downStr = "http://d4.wnacg.download/down/0934/" + hash +".zip"
            # downStr = "http://d4.wnacg.download/down/0934/65657befb4fd4d9fec0a6c21f42042ed.zip"
            print(downStr)

            # down_file =  urllib.request.urlopen(downStr)
            down_file = requests.get(downStr)
            
            if down_file.status_code == 200:
                file_size = int(down_file.headers.get('Content-Length'))
                print(file_size)
                i = 0
                with open(name + ".zip", 'wb') as file:
                    # while i < file_size:
                        for chunk in down_file.iter_content(1024):
                        # if data is None or len(data) <= 0:
                        #     break
                            file.write(chunk)
                        # file.write(data)
                        # i+= 1024
            
            
 
        
                




    