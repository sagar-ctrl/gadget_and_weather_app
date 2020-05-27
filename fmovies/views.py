from urllib.parse import quote_plus

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# from requests.compat import quote_plus



# Create your views here.
BASE_URL='https://yomovies.to/?s={}'
def index(req):
    allprod=[]


    search=req.POST.get('fsearch',"")
    final_url=BASE_URL.format(quote_plus(search))
    print(final_url)
    response=requests.get(final_url)
    data=response.text
    soup=BeautifulSoup(data,features="html.parser")
    #print(final_url)

    #post_titles=soup.find_all('img',{'class':'lazy thumb mli-thumb'})
    #for post in post_titles:
      #  print(post.get('data-original'))
    post_titles=soup.find_all('a',{'class':'ml-mask jt'})
    for post in post_titles:
        link=post.get('href')
        title=post.get('oldtitle')
        image=post.find('img').get('data-original')
        allprod.append([link,title,image])
    params={'allprod':allprod,'name':search}







    return render(req, 'fmovies/index.html',params)



