from bs4 import BeautifulSoup
import requests
from os import system
from sys import exit
import time
from requests.exceptions import ConnectionError
import csv
import os
import os.path

class Annonce():
    id=''
    motsCle = ''
    titre=''
    categorie=''
    prix=''
    description=''
    region=''
    parueDepuis =''
    dateParution=''
    vendue=False 
    photos = []
    def __init__(self):
         pass

    def __str__(self):
        attrs = vars(self)
        return ', '.join("%s: %s" % item for item in attrs.items())





class bsLespac():
    url='https://lespac.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    annonces=[]
    def __init__(self):
         pass
    def parseAnnonces(self, pMotsCle):        
            self.annoncesHTML = self.soup.select('.detailedView ')
            for annonceItem in self.annoncesHTML:           
                    ann=Annonce()
                    ann.motsCle = pMotsCle
                    ann.id="LP_" +annonceItem.get('data-listing-id')
                    ann.description=' '.join(annonceItem.find(class_='description').text.split())
                    #Vendu en34 jours
                    
                    ann.parueDepuis=' '.join(annonceItem.find(class_='since').text.split())
                    ann.vendue = ann.parueDepuis.split()[0]=='Vendu'
                    ann.titre=annonceItem.find(class_='title').get('title')
                    ann.categorie= annonceItem.get('data-listing-category-code')
                    ann.prix= annonceItem.get('data-listing-price')                    
                    
                    ann.region=annonceItem.get('data-listing-region-code')
                    
                    self.annonces.append(ann)
                    
    def Search(self, pMotsCle, pNbPasges=1):        
        for i in range(pNbPasges):
            self.searchstringurl = f"https://www.lespac.com/charlesbourg/{'-'.join(pMotsCle.split())}_g15161k{i+1}R1.jsa?ncc=dx0"
            response = requests.get(self.searchstringurl,headers=self.headers    )
            self.soup = BeautifulSoup(response.text,'html.parser')
            self.parseAnnonces(pMotsCle)

def main():
    bs=bsLespac()
    bs.Search('fujinon or fujifilm',12)
    for item in bs.annonces:
        print(item)
        print("")

if __name__ == '__main__':
    bsLespac.main()