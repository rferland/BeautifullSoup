import bsBaseShopify


class bsMissBoon(bsBaseShopify.bsBaseShopify):  
    
    CONTAINER_CLASS='collection-cascade'
    LISTE_TYPE = 'div'
    LISTE_CLASS='item'
    NOM_CLASS='color--primary-text m0 mt2 font-size--sm line-height--4 wd--font-size--m wd--line-height--4'
    PRIX_CLASS='color--primary-meta m0 font-size--sm line-height--4 wd--font-size--m wd--line-height--4'
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
    liste = []
    bs=bsMissBoon("https://missboon.ca/collections/plantes")
    liste = bs.parsePlantes()
    bs=bsMissBoon("https://missboon.ca/collections/plantes-locales")
    liste += bs.parsePlantes()
    bs=bsMissBoon("https://missboon.ca/collections/plantes-tendance")
    liste += bs.parsePlantes()
    
    return liste

if __name__ == '__main__':
    bsMissBoon.main()
    