# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:33:49 2020

@author: 呂兆凱
"""

def CoronavirusTopic():
    """ 程式碼開始 """
    '''
    爬蟲
    '''
    import urllib.request as req
        
    url="https://www.bbc.com/zhongwen/trad/51222586"
    request=req.Request(url, headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    '''
    解析爬下來的文字
        * 依序抓到 左上角三張大圖 -> 右邊的視頻音頻 -> 下面的科學常識 -> 下面的更多報道 -> 下面的新聞回顧 -> 視頻音頻(重複的) -> 深度分析
            * 問題發現: 2020/4/4 20:52 的時候 
                * print(len(titles), len(links), len(images), len(times)) => 422 422 431 421
            * 問題分析:
                * 問題一: 深度分析的標題跟連結跟時間抓不到，也因為排序跟抓到的順序一樣，因此最後幾個圖片要放棄掉，也就是長度跟title長度一樣即可
                * 問題二: 第一張大圖沒有時間，所以要補上第一張大圖的時間(用現在的時間代替)
    '''
    import bs4
    from datetime import datetime
    root=bs4.BeautifulSoup(data, "html.parser")

    titles=root.find_all("span", class_="title-link__title-text") 
    links=root.find_all("a", class_="title-link")
    images=root.find_all("div", class_="js-delayed-image-load")
    times=root.find_all("div", class_="date date--v2")

    images = images[:len(titles)] # 最後幾個圖片要放棄掉
    times.insert(0, int(datetime.timestamp(datetime.now()))) # 補上第一張大圖的時間(用現在的時間代替)
    '''
    讀取data.json
    若無此檔案，則建立空的dict
    '''
    import pathlib, os, json
    curPath=str(pathlib.Path(__file__).parent.absolute())
    dict={}
    if os.path.exists(curPath + "/src/data.json"):
        with open(curPath + '/src/data.json', 'r') as f:
            dict = json.load(f)

    '''
    把不重複的資訊放進dict內
        * dict = {標題: [圖片位置，新聞網址，對應的圖片連結, 抓取時間]}
    
    下載還未載過的圖片
    '''
    from datetime import datetime
    import requests
    j, count = len(dict), 1
    for i, (title, link, image, time) in enumerate(zip(titles, links, images, times)):
        titles[i] = title.string

        # 每個feature
        title = titles[i]
        link = "https://www.bbc.com"+link['href']
        image = image['data-src']
        time = int(time['data-seconds']) if i != 0 else int(datetime.timestamp(datetime.now()))

        # 如果沒在dict裡面，新增進去dict，並下載圖片
        if dict.get(title, 0) == 0:
            dict[title]=[curPath + '/picture/' + str(j) + '.png', link, image, time]
            request = requests.get(image)
            f = open(dict[title][0], 'wb')
            f.write(request.content)
            f.close()
            print("Picture ", count, "downloaded !")
            count += 1
            j += 1

    '''
    把已經不存在的title從dict和檔案中刪除
    '''
    # 這是範例，假設多了一個不再titles裡面的檔案
    # dict["example"] = [curPath + '/picture/' + "example.txt"] # for test, 在picture資料夾內新增一個example.txt
    titles = set(titles) # 去除重複的titles
    to_delete_title = titles ^ dict.keys() # return set(不存在的titles)
    for tmp in to_delete_title:
        os.remove(dict[tmp][0])
        print("Delete ", dict[tmp][0], "!")
        del dict[tmp]
        print("Delete Title in data.json = ", tmp, "!")

    '''
    把dict存成data.json
    '''
    with open(curPath + '/src/data.json', 'w') as outfile:
        json.dump(dict, outfile)
    
if __name__ == "__main__":
    import json
    CoronavirusTopic()
    

    
