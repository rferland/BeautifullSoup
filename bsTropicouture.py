import bsBaseShopify


class bsTropicouture(bsBaseShopify.bsBaseShopify):  
    
    CONTAINER_CLASS='grid__wrap-inner' #Le container de la liste des plantes
    LISTE_TYPE = 'div' #L'élément de l'annonce
    LISTE_CLASS='grid-product' # La classe css de l'annonce
    NOM_CLASS='grid-product__title' # le nom de la plante
    PRIX_CLASS='grid-product__price-value ec-price-item' # Le prix de la plante
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
        "https://tropicoutureplants.com/products/JUST-IN-c113321555",
        "https://tropicoutureplants.com/products/SALE-c110269219",
        "https://tropicoutureplants.com/products/ANTHURIUMS-c109135864",
        "https://tropicoutureplants.com/products/HOYAS-c109471293",
        "https://tropicoutureplants.com/products/MONSTERAS-c109471292",
        "https://tropicoutureplants.com/products/OTHER-PLANTS-c109467283",
        "https://tropicoutureplants.com/products/PHILODENDRONS-c109131884",
        "https://tropicoutureplants.com/products/SCINDAPSUS-c109466790"        
    ]
    liste = []
    for url in sites:
        
        bs=bsTropicouture(url)
        liste += bs.parsePlantes()   
        
    return liste

if __name__ == '__main__':
    bsTropicouture.main()
    
    