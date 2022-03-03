class Plante():
    site=''
    nom=''
    nomcomplet = ''
    date=''
    code =''
    detail=''
    prix=''
    prixSpecial=''
    photos= []
    url = ''
    def __str__(self):
        attrs = vars(self)
        return '[{' +', '.join("%s: %s" % item for item in attrs.items())+'}]'