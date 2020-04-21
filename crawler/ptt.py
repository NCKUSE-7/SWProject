import os
import re
import sys
import json
import requests
import codecs
from bs4 import BeautifulSoup
from six import u

def parse_articles( start, end, board, path='.', timeout=3):
            filename = 'output.json'
            filename = os.path.join(path, filename)
            store(filename, u'', 'w')
            for i in range(end-start+1):
                index = start + i
                resp = requests.get(
                    url = PTT_URL + '/bbs/' + board + '/index' + str(index) + '.html',
                    cookies={'over18': '1'}, verify=True , timeout=timeout
                )
                if resp.status_code != 200:
                    print('invalid url:', resp.url)
                    continue
                soup = BeautifulSoup(resp.text, 'html.parser')
                divs = soup.find_all("div", "r-ent")
                for div in divs:
                    try:
                        href = div.find('a')['href']
                        link = PTT_URL + href
                        article_id = re.sub('\.html', '', href.split('/')[-1])
                        if div == divs[-1] and i == end-start:  # last div of last page
                            store(filename, parse(link, article_id, board), 'a')
                        else:
                            store(filename, parse(link, article_id, board) + ',\n', 'a')
                    except:
                        pass
            store(filename, u']}', 'a')
            return filename

def parse_article( article_id, board, path='.'):
    link = PTT_URL + '/bbs/' + board + '/' + article_id + '.html'
    filename = board + '-' + article_id + '.json'
    filename = os.path.join(path, filename)
    store(filename, parse(link, article_id, board), 'w')
    return filename


def parse(link, article_id, board, timeout=3):
    print('Processing article:', article_id)
    resp = requests.get(url=link, cookies={'over18': '1'}, verify=True, timeout=timeout)
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_content = soup.find(id="main-content")
    metas = main_content.select('div.article-metaline')
    author = ''
    title = ''
    date = ''
    if metas:
        author = metas[0].select('span.article-meta-value')[0].string if metas[0].select('span.article-meta-value')[0] else author
        title = metas[1].select('span.article-meta-value')[0].string if metas[1].select('span.article-meta-value')[0] else title
        date = metas[2].select('span.article-meta-value')[0].string if metas[2].select('span.article-meta-value')[0] else date

        # remove meta nodes
        for meta in metas:
            meta.extract()
        for meta in main_content.select('div.article-metaline-right'):
            meta.extract()

        # remove and keep push nodes
    pushes = main_content.find_all('div', class_='push')
    for push in pushes:
        push.extract()
    filtered = [ v for v in main_content.stripped_strings if v[0] not in [u'※', u'◆'] and v[:2] not in [u'--'] ]
    expr = re.compile(u(r'[^\u4e00-\u9fa5\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\s\w:/-_.?~%()]'))
    for i in range(len(filtered)):
        filtered[i] = re.sub(expr, '', filtered[i])

    filtered = [_f for _f in filtered if _f]  # remove empty strings
    filtered = [x for x in filtered if article_id not in x]  # remove last line containing the url of the article
    content = ' '.join(filtered)
    content = re.sub(r'(\s)+', ' ', content)

    p, b, n = 0, 0, 0
    i = 0

    while (push in pushes) and (i <= 3):
        if not push.find('span', 'push-tag'):
            continue
        push_tag = push.find('span', 'push-tag').string.strip(' \t\n\r')
           
        if push_tag == u'推':
            p += 1
        elif push_tag == u'噓':
            b += 1
        else:
            n += 1
        i += 1

    # json data
    data = {
        'url': link,
        'article_title': title,
        'author': author,
        'push': p, 
        'boo': b, 
        'content': content,
        'date': date
    }
    return json.dumps(data, sort_keys=True, ensure_ascii=False)

def store(filename, data, mode):
    with codecs.open(filename, mode, encoding='utf-8') as f:
        f.write(data)

def getLastPage(board, timeout=3):
    content = requests.get(
        url= 'https://www.ptt.cc/bbs/' + board + '/index.html',
        cookies={'over18': '1'}, timeout=timeout
    ).content.decode('utf-8')
    first_page = re.search(r'href="/bbs/' + board + '/index(\d+).html">&lsaquo;', content)
    if first_page is None:
        return 1
    return int(first_page.group(1)) + 1


#---------- 執行方法 ---------------------------------

# 輸入要輸入的參數
PTT_URL = 'https://www.ptt.cc'
board = 'nCov2019'
#預設為爬最新的前兩頁
start = 0
end = 1
if __name__ == "main":
    #執行function
    parse_articles(start, end, board)