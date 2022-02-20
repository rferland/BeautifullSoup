import bsBaseShopify


class bsMissBoon(bsBaseShopify.bsBaseShopify):  
    
    liste=[]

    def parsePlantes(self):
        super().initParser('https://missboon.ca/collections/plantes')
        self.liste += super().parsePlantes()


if __name__ == '__main__':
    bs=bsMissBoon()
    bs.parsePlantes()
    for ann in bs.plantesList:
        # print(ann.code)
        print(str(ann))