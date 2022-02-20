
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
        super().initParser(self.URL, 
        self.CONTAINER_CLASS, 
        self.LISTE_TYPE,
        self.LISTE_CLASS,
        self.NOM_CLASS,
        self.PRIX_CLASS,
        self.PRIX_SPECIAL_CLASS)

        return super().parsePlantes()

   
if __name__ == '__main__':
    bs=bsYouGrowGlencoco()
    bs.parsePlantes()
    for ann in bs.plantesList:
        # print(ann.code)
        print(str(ann))