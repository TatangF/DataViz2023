#importation des bibnliotheque 
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd


app = FastAPI()

class RgaBasqueItem(BaseModel):
    echelle : str
    categorie:str
    Types:str
    annee:int
    valeur:float
    sau_tot_ha:float
    sau_moy_ha:float
    sau_ha:float
    ugb:float
    etp:float
    age_5:float
    tetes:float
    bio:float
    surface:float
    irrigation:float
    nombre_exploitation_bio:float
    surface_bio:float
    otefdd_coef17:float
    code_insee:int
    commune:str 
    Geo_Shape:str 
    geo_point_2d:str
    latitude:float 
    longitude:float 

with open('C:/Users/Férol/Documents/DataViz/modele_rf_ful.pickle', "rb") as f:
    model=pickle.load(f)


@app.post('/')
async def production_ragEndpoint(item:RgaBasqueItem):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    rga_futur = model.predict(df)
    return {"La prediction de la production agricole standard est ":float(rga_futur)}
