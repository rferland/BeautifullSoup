import bsBaseShopify


class bsNsTropical(bsBaseShopify.bsBaseShopify):  
    
    URL = 'https://NsTropical.ca/collections/plantes'
    CONTAINER_CLASS='grid collection-grid grid--uniform grid--no-gutters'
    LISTE_TYPE = 'div'
    LISTE_CLASS='product-item grid__item small--one-half medium-up--one-quarter'
    NOM_CLASS='product-item__title'
    PRIX_CLASS='product-item__price-wrapper'
    PRIX_SPECIAL_CLASS =''

    def parsePlantes(self):
        super().initParser(self.URL, 
        self.CONTAINER_CLASS, 
        self.LISTE_TYPE,
        self.LISTE_CLASS,
        self.NOM_CLASS,
        self.PRIX_CLASS,
        self.PRIX_SPECIAL_CLASS)

        return super().parsePlantes()
    
    def __init__(self, pUrl):
        self.URL=pUrl


if __name__ == '__main__':
    liste = []
    bs=bsNsTropical("https://nstropicals.com/collections/anthuriums")
    liste = bs.parsePlantes()
    bs=bsNsTropical("https://nstropicals.com/collections/monstera")
    liste += bs.parsePlantes()
    bs=bsNsTropical("https://nstropicals.com/collections/philodendrons")
    liste += bs.parsePlantes()
    for ann in liste:
        # print(ann.code)
        print(str(ann))