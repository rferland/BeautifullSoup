from bsBaseShopify import bsBaseShopify

class bsPlantHeaven(bsBaseShopify):

    def __init__(self):
        super().__init__('https://planthaventoronto.com/collections/shop-all-plants?page=')

if __name__ == '__main__':
    bs=bsPlantHeaven()
    bs.parsePlantes()
    for ann in bs.plantesList:
        print("")
        print(ann)