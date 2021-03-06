from bs4 import BeautifulSoup
import requests
import os.path
from lib import PlanteParser 

class bsBaseShopify():
    nbPagesTotal = "1"
    plantesList=[]
    containerClass=''
    listeType=''
    listeClass=''
    nomClass=''
    prixClass=''
    prixSpecialClass=''

    def parsePlantes(self):        
        for i in range(int(self.nbPagesTotal)):
            parser=PlanteParser.PlanteParser(self.soup, self.containerClass)
            parser.listeType=self.listeType
            parser.listeClass= self.listeClass
            parser.nomClass = self.nomClass
            parser.prixClass= self.prixClass
            parser.prixSpecialClass = self.prixSpecialClass

            self.plantesList += parser.ParseShopify( )     
        return self.plantesList

    """ 
    Sert pour les sites Shopify qui ont différentes pages pour différents types de plantes  
    """
    def initParser(self, pUrl, pContainerClass,pListeType, 
                    pListeClass,pNomClass, pPrixClass, pPrixSpecialClass ):
        
        # L'élément qui contient les items à lister
        self.containerClass=pContainerClass

        #Les items à lister
        self.listeClass = pListeClass
        self.listeType = pListeType
        self.nomClass = pNomClass
        self.prixClass = pPrixClass
        self.prixSpecialClass = pPrixSpecialClass

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
        response = requests.get(pUrl,headers=headers    )
        self.soup = BeautifulSoup(response.text,'html.parser')    

        # La pagination    
        liPage = self.soup.find('li', attrs={'class': 'pagination__text'})
        if(liPage):
            pageNotext= liPage.text
            self.nbPagesTotal = pageNotext.split()[len(pageNotext.split())-1]

    def __init__(self, *args):        
        if (len(args) > 0):
            self.initParser(args[0], args[1])
