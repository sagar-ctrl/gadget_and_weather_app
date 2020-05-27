from urllib.parse import quote_plus

from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
from django.views.generic import DetailView

from coronameter.models import weather

BASE_URL='https://www.timeanddate.com/weather/?query={}'
def index(req):
    weathers=[]
    search=req.POST.get('fsearch',"kathmandu")
    if search=='':
        search='kathmandu'
    city=BASE_URL.format(quote_plus(search))
    # print(city)
    response=requests.get(city)

    data=response.text

    # print(data)
    soup=BeautifulSoup(data,features='html.parser')
    # tdiv=soup.find('div',{'class':'tb-scroll'})
    # print(tdiv)
    rows=[]
    # table=soup.find_all('table',{'class':'zebra fw tb-theme'})
    # tbody=table.find('thead')
    # print(tbody)
    # tbody=soup.find_all('div',{'class':'my-city__items'})
    tbody=soup.find('table',{'class':"zebra fw tb-theme"})
    # trs=tbody.find_all('tr')
    # for tr in trs:
    #     row=tr.find('td')
    #     if row is None:
    #         pass
    #     else:
    #         rows.append(row)
    # # print(rows)
    # for city_row in rows:
    #     link=city_row.find('a').text
    #
    #
    #     print(link)
    trs=tbody.find_all('tr')
    for tr in trs:
        checking=tr.find('td') or tr.find('td',{'class':'r'})
        if checking is None:
            pass
        else:
            city_name=checking.find('a').text
            city_link="https://www.timeanddate.com"+checking.find('a').get('href')
            time=tr.find("td",{'class':'r'}).text
            class_R=tr.find_all('td',{'class':'r'})

            for images in class_R:
                image_checking=images.find('img')

                if image_checking is None:
                    pass
                else:
                    image=image_checking.get("src")

            temp=tr.find('td',{'class':'rbi'}).text
            if weather.objects.filter(city_link=city_link):
                pass
                # weathers.append([weather.city_name,weather.time,weather.temp,weather.image,weather.city_link,])



            else:
                weather.objects.create(city_name=city_name,city_link=city_link,time=time,image=image,temp=temp)
            # print(temp)
            # print(image)
            # print(time)
            # print(city_name)
            # print((city_link))
            # weathers.append([city_name,time,temp,image,city_link])

            # print(weather)
            for weath in weather.objects.all():
                if weath.city_link == city_link:
                    weathers.append([weath.city_name, weath.time, weath.temp, weath.image, weath.city_link,weath.id])












    # print(tdiv)

    return render(req,'coronameter/index.html',{'weather':weathers})


def city_detail(req,pk):
    link=weather.objects.get(pk=pk).city_link
    response=requests.get(link)
    data=response.text
    soup=BeautifulSoup(data,features='html.parser')
    now_div=soup.find('section',{'class':'bk-wt','id':'bk-focus'})
    detail_1=now_div.find('div',{'class':'three columns','id':'qlook'})
    # print(detail_1)
    # print(now_div)
    image=detail_1.find('img',{'class':'mtt','id':'cur-weather'}).get('src')
    temp=detail_1.find('div',{'class':'h2'}).text
    climates = detail_1.find_all('p')
    climate=climates[0].text
    feelslike=climates[1].text

    # print(link)
    #print(image)
    # print(climate)
    detail_2=now_div.find('div',{'class':'five columns'}).find_all('p')
    try:
        map = now_div.find('div', {'class': 'four columns'}).find('div').find('img').get('src')
    except:
        map='http://c.tadst.com/gfx/citymap/in-10.png?9'
    print(map)

    return render(req,'coronameter/city_detail.html',{'feels':feelslike,'image':image,'temp':temp,'climate':climate,'detail':detail_2,'location':detail_2[0].text,'curr_time':detail_2[1].text,'latest':detail_2[2].text,'visibility':detail_2[3].text,'pressure':detail_2[4].text,'humidity':detail_2[5].text,'dew_point':detail_2[6].text,'map':map})

