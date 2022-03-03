import json

import numpy as np
import bsAyasTropicalPlants
import bsAroidsShop
import bsMissboon
import bsNsTropicals
import bsPlantHeaven
import bsTropicouture
import bsYouGrowGlencoco
import pandas as pd 


ListeFinale=bsPlantHeaven.main()
ListeFinale.extend(bsTropicouture.main())
ListeFinale.extend(bsAyasTropicalPlants.main())
ListeFinale.extend(bsAroidsShop.main())
ListeFinale.extend(bsMissboon.main())
ListeFinale.extend(bsNsTropicals.main())
ListeFinale.extend(bsYouGrowGlencoco.main())

df = pd.DataFrame(ListeFinale)

print(df)
df.to_excel("plantes.xlsx", encoding='utf-8')
