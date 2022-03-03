
import bsBaseShopify


class bsYouGrowGlencoco(bsBaseShopify.bsBaseShopify):  

    URL = 'https://yougrowglencoco.com/'
    CONTAINER_CLASS='collection-cascade'
    LISTE_TYPE = 'li'
    LISTE_CLASS='grid__item'
    NOM_CLASS='h4 grid-view-item__title product-card__title'
    PRIX_CLASS='price-item--regular'
    PRIX_SPECIAL_CLASS ='price-item--sale'

    def parsePlantes(self):
        super().initParser(
        self.CONTAINER_CLASS, 
        self.LISTE_TYPE,
        self.LISTE_CLASS,
        self.NOM_CLASS,
        self.PRIX_CLASS,
        self.PRIX_SPECIAL_CLASS)

        return super().parsePlantes(self.URL)

   
def main():
    bs=bsYouGrowGlencoco()
    return bs.parsePlantes()
   

if __name__ == '__main__':
    bsYouGrowGlencoco.main()