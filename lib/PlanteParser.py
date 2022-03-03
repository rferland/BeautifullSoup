from datetime import datetime
from lib import Plante

class PlanteParser():
    
    containerClass=''
    soup = None
    listeType=''
    listeClass=''
    nomClass= ''
    prixClass =''
    prixSpecialClass = ''
    url=''

    def ParseShopify(self, siteName = '', pPageCountMax=0):
        plantesList = []    
        
        for item in self.soup.find_all(self.listeType, attrs={f'class': {self.listeClass}}):

            plante= Plante.Plante()
            plante.url=self.url
            plante.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.nomComplet = item.find(class_= self.nomClass).getText()            

            nomPrix =self.nomComplet.split('-')
            plante.nom = nomPrix[0].strip()
            plante.code=''.join(filter(str.isalpha, nomPrix[0].upper()))                
            if len(nomPrix)>1:
                plante.detail = nomPrix[1].strip()
                
            prix= plante.prix=item.find(class_=self.prixClass)
            if(prix):
                plante.prix = self.parseRegularPrice(prix.getText())
                plante.prixSpecial=self.parseSpecialPrice(prix.getText())

            if(self.prixSpecialClass != '' and item.find(class_=self.prixSpecialClass) ):
                plante.prixSpecial=item.find(class_=self.prixSpecialClass).getText().strip()
                            
            plantesList.append(plante.__dict__)
        
        print()
        print(f"{self.url} Total: {len(plantesList)}")

        return plantesList

    def parseRegularPrice(self, pPrixTexte):
        Texte = pPrixTexte.replace("$","").replace("CAD","").replace("\n"," ").split()
        if("Regular" in Texte):
            return Texte[2]
        if len(Texte)>0:
            return Texte[0]
        return None

    def parseSpecialPrice(self, pPrixTexte):
        Texte = pPrixTexte.replace("$","").replace("\n"," ").split()
        if("Sale" in Texte):
            return Texte[5]
        return None

    def __init__(self, pSoup, pClass, pUrl):
        self.url=pUrl
        self.plantesHTML = pSoup.select(f".{pClass}")
        self.soup=pSoup
        
        
        
