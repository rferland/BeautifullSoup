
import bsBaseShopify


class bsYouGrowGlencoco(bsBaseShopify.bsBaseShopify):  
    

    def __init__(self):
        super().__init__('https://yougrowglencoco.com/','grid__item grid__item--featured-collections small--one-half')
    





if __name__ == '__main__':
    bs=bsYouGrowGlencoco()
    bs.parsePlantes('')
    for ann in bs.plantesList:
        # print(ann.code)
        print(str(ann))