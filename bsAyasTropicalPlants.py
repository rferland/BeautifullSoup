import bsBaseShopify


class bsAyasTropicalPlants(bsBaseShopify.bsBaseShopify):  
    
    CONTAINER_CLASS='collectionProductsContainer-inner' #Le container de la liste des plantes
    LISTE_TYPE = 'li' #L'élément de l'annonce
    LISTE_CLASS='tm-secondpro' # La classe css de l'annonce
    NOM_CLASS='title' # le nom de la plante
    PRIX_CLASS='price' # Le prix de la plante
    PRIX_SPECIAL_CLASS =''

    def parsePlantes(self):
        super().initParser(
        self.CONTAINER_CLASS, 
        self.LISTE_TYPE,
        self.LISTE_CLASS,
        self.NOM_CLASS,
        self.PRIX_CLASS,
        self.PRIX_SPECIAL_CLASS)

        return super().parsePlantes(self.URL)
    
    def __init__(self, pUrl):
        self.URL=pUrl

def main():    
    sites=[
        "https://www.ayastropicalplants.com/en/monstera/",
        "https://www.ayastropicalplants.com/en/syngonium/",
        "https://www.ayastropicalplants.com/en/philodendron/",
        "https://www.ayastropicalplants.com/en/anthurium/",
        "https://www.ayastropicalplants.com/en/hoya/",
        "https://www.ayastropicalplants.com/en/epipremnum/",
        "https://www.ayastropicalplants.com/en/alocasia/",
        "https://www.ayastropicalplants.com/en/scindpasus/"        
    ]
    for url in sites:
        liste = []
        bs=bsAyasTropicalPlants(url)
        liste = bs.parsePlantes()   
        
    return liste

if __name__ == '__main__':
    bsAyasTropicalPlants.main()