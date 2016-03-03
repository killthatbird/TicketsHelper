import requests
from bs4 import BeautifulSoup
from entity.university import university

university_list = []


def scrapy(startnum):
    req_url = 'http://yz.chsi.com.cn/sch/search.do?b211=1&start=' + str(startnum)
    html = requests.get(req_url).text
    soup = BeautifulSoup(html, 'html.parser')
    trs = str(soup.find('tbody'))
    tr_soup = BeautifulSoup(trs, 'html.parser')
    for each_tr in tr_soup.find_all('tr'):
        each_trs = each_tr.find_all('td')
        name = each_trs[0].text.strip()
        province = each_trs[1].text.strip()

        yxtx_spans = each_tr.find_all('span')
        b985 = yxtx_spans[0].text
        b211 = yxtx_spans[1].text

        university_ = university(name, b985, b211, province)
        university_list.append(university_)
        print(
            '学校 : ' + university_.name + '\t' + '省份 : ' + university_.province + '\t    ' + university_.b985 + '\t    ' + university_.b211)


def tocsv(list):
    csv_content = ''
    for each_item in list:
        csv_content += each_item.name + ', '
        csv_content += each_item.province + ', '
        csv_content += each_item.b985 + ', '
        csv_content += each_item.b211 + '\r\t'

    with open('d:/unversity.csv', 'wt') as f:
        f.write(csv_content)
        f.flush()
        f.close()


if __name__ == '__main__':
    start = 0
    while start <= 100:
        scrapy(start)
        start += 20
    tocsv(university_list)
