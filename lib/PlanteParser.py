from lib import Plante

class PlanteParser():
    
    containerClass=''
    soup = None

    def ParseShopify(self, pPageCountMax=0):
        plantesList = []    
        
        for item in self.soup.find_all('li', attrs={'class': 'grid__item'}):

            plante= Plante.Plante()
            nomComplet = item.find(class_='h4 grid-view-item__title product-card__title').text
            
            nomDetail = nomComplet.split()
            plante.graines = (nomDetail[len(nomDetail)-1]=='Seeds')

            nomPrix =nomComplet.split('-')
            plante.nom = nomPrix[0].strip()
            plante.code=''.join(filter(str.isalpha, nomPrix[0].upper()))                
            if len(nomPrix)>1:
                plante.taille = nomPrix[1].strip()
                
            plante.prix=item.find(class_='price-item price-item--regular').text.strip()
            plante.prixSpecial=item.find(class_='price-item price-item--sale').text.strip()
                            
            plantesList.append(plante)

        return plantesList

    def __init__(self, pSoup, pClass):
        self.plantesHTML = pSoup.select(f'.{pClass}')
        self.soup=pSoup
        
        
        
