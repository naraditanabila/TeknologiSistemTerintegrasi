import requests
from bs4 import BeautifulSoup
from flask import Flask, request
from flask_restful import Resource, Api


def make_soup(url):
    #Membuat request
    r = requests.get(url)
    #Hasil response
    response = r.content
    soupdata = BeautifulSoup(response, 'html.parser')
    return soupdata

app = Flask(__name__)
api = Api(app)


class Show(Resource):
    def get(self,limit,page):
        soup = make_soup(url = 'https://www.grobmart.com/Buku?limit='+str(limit)+'&page='+str(page))
        name = soup.find_all('div',attrs={'class':'name'})
        description = soup.find_all('div',attrs={'class':'description'})
        price = soup.find_all('span',attrs={'class':'price-new'})
        buku={}
        for x in range(0, len(name)):
            buku[x+1]={'Nama': name[x].text.strip(),'Deskripsi': description[x].text.strip(),'Harga': price[x].text.strip()}
        return buku
    
api.add_resource(Show,'/show/limit=<int:limit>&page=<int:page>')

if __name__== '__main__':
    app.run(debug=True)