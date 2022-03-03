import bsBaseShopify


class bsAroidsShop(bsBaseShopify.bsBaseShopify):  
    
    URL = ''
    CONTAINER_CLASS='grid-uniform grid-link__container'
    LISTE_TYPE = 'div'
    LISTE_CLASS='grid__item wide--one-fifth large--one-quarter medium-down--one-half'
    NOM_CLASS='grid-link__title'
    PRIX_CLASS='grid-link__meta'
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
    
    bs=bsAroidsShop("https://aroidsshop.com/en/collections/all")
    return bs.parsePlantes()
    

if __name__ == '__main__':
    bsBaseShopify.main()