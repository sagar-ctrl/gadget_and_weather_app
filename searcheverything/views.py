from urllib.parse import quote_plus

import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from bs4 import *
from django.views.generic import DetailView
from pandocfilters import Null

from searcheverything.models import ALLPRODUCT

BASE_URL='https://www.gadgetbytenepal.com/?s={}'
#all_prod=[]
def indexes(req):
    all_prod=[]
    search= req.POST.get('search',"")

    finalurl=BASE_URL.format(quote_plus(search))


    response=requests.get(finalurl)
    data=response.text
    # print(data)
    soup=BeautifulSoup(data,features='html.parser')
    gadget_div=soup.find_all('div',{'class':'td-module-thumb'})
    # gadget_inner_div=gadget_div.find_all('div',{'class':'td-module-thumb'})
    for gadgets in gadget_div:
        link=gadgets.find('a',{'rel':'bookmark'})
        image=link.find('img').get('srcset')
        title=link.get('title')
        gadget_link=link.get('href')
        # if ALLPRODUCT.gadget_link == gadget_link:
        #     pass
        # else:
        #     ALLPRODUCT.objects.create(gadget_link=gadget_link,image=image,title=title)

        if ALLPRODUCT.objects.filter(gadget_link=gadget_link):
            pass
        else:
            ALLPRODUCT.objects.create(gadget_link=gadget_link, image=image, title=title)
        prod=ALLPRODUCT.objects.filter(gadget_link=gadget_link)
        for product in prod:
            id = product.id
            images=product.image
            titles=product.title
            links=product.gadget_link
            all_prod.append([images, titles, links,id])


        #all_prod.append([image,title,gadget_link])


        # link_set.append(link)







    return render(req,'searcheverything/index.html',{'allprod':all_prod})


# class ProductDetail(DetailView):
#     model = ALLPRODUCT

def detailView(req,pk):
    product=ALLPRODUCT.objects.get(id=pk)
    link=product.gadget_link
    print(link)
    response=requests.get(link)
    page_content=[]
    imagearr=[]

    data=response.text

    # print(data)
    soup=BeautifulSoup(data,features='html.parser')
    gadget_div=soup.find_all('div',{'class':'td-post-content'})
    for images in gadget_div:
        # image = images.find('a').find('img').get('srcset')
        try:
            imageset = images.find('a').find('img').get('srcset')

            # for picitem in imageset:
            #     print(picitem)
            #     # image=picitem.get('src')
            #     # print(image)
            #     # imagearr.append(image)

        except:
            # image = images.find('a').find('img').get('src')
            pass
    for paragraph in gadget_div:
        p=paragraph.find('p').text
        # h2=paragraph.find('h2').find('strong').text
        h2=paragraph.find('h2')
        try:
            h2=h2.find('strong').text
        except:
            h2=''


        # print(p)
        # print(h2)



        page_content.append([p,h2])


    print(page_content)



    return render(req,'searcheverything/gadgetview.html',{'page':page_content,'image':imageset})

