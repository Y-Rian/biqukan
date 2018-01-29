'''
@Author  : Y-Rian
@Time    : 2018/1/29 11:45
'''
import requests
from bs4 import BeautifulSoup
base_url='http://www.biqukan.com/'
url='http://www.biqukan.com/1_1408/'    #飞剑问道
header={
    'User-Agnet':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}
def get_nover_list():
    pass
def get_chapter_list(url):
    response=requests.get(url,headers=header)
    response.encoding='gbk'
    html=response.text
    soup=BeautifulSoup(html,'lxml')
    book_name=soup.find('meta',attrs={'property':'og:novel:book_name'})['content']
    author=soup.find('meta',attrs={'property':'og:novel:author'})['content']
    # print(author)
    # print(book_name)
    div_tags=soup.find_all('div',class_='listmain')
    tags_soup=BeautifulSoup(str(div_tags[0]),'lxml')
    a_tags=tags_soup.find_all('a')[13:]
    url_list=[]
    for each in a_tags:
        chapter_url=each['href']
        chapter_name=each.get_text()
        new_url=base_url+chapter_url
        url_list.append(new_url)
        # print(chapter_name,new_url)
        # break
    return url_list
    # print(a_tags)
    # print(tags_soup)
    # print(div_tags)
def save_chapter_text(url):
    response=requests.get(url,headers=header)
    # response.encoding='gbk'
    html=response.text
    soup=BeautifulSoup(html,'lxml')
    chapter_name=soup.find('h1').string
    # print(chapter_name)
    div_tags=soup.find_all('div',class_='showtxt')
    content=div_tags[0].text.replace('\xa0*8','\n\n')
    # content = div_tags[0].text
    text=chapter_name+content
    # print(content)
    # print(type(content))
    # print(type(chapter_name))
    # print(chapter_name)
    # print(text)
    try:

        file_name='飞剑问道//%s.txt' %chapter_name
        # file_name='飞剑问道//飞剑问道.txt'
        with open(file_name,'w',encoding='utf-8') as f :
            f.write(content)
        print('{}写入完成'.format(chapter_name))

    except:
        print('---------------------------------')


urls_list=get_chapter_list(url)
for url in urls_list:
    d=save_chapter_text(url)
# test_url='http://www.biqukan.com/1_1408/16067401.html'
# test_url='http://www.biqukan.com/1_1408/16061982.html'
# save_chapter_text(test_url)
