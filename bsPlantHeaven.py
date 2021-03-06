from bsBaseShopify import bsBaseShopify

class bsPlantHeaven(bsBaseShopify):

    URL = 'https://planthaventoronto.com/collections/shop-all-plants?page='
    CONTAINER_CLASS='grid__item grid__item--featured-collections small--one-half'
    LISTE_TYPE = 'li'
    LISTE_CLASS='grid__item'
    NOM_CLASS='h4 grid-view-item__title product-card__title'
    PRIX_CLASS='price-item price-item--regular'
    PRIX_SPECIAL_CLASS ='price-item price-item--sale'

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
    bs=bsPlantHeaven()
    bs.parsePlantes()
    for ann in bs.plantesList:
        print("")
        print(ann)