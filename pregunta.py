"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime


def clean_data():
    
    def normalizar_fecha(fecha):
        try:
            # Intenta analizar la fecha en diferentes formatos
            formatos = ['%Y/%m/%d', '%d/%m/%Y', '%y/%m/%d', '%d/%m/%y']
            for formato in formatos:
                try:
                    fecha_obj = datetime.strptime(fecha, formato)
                    return fecha_obj.strftime('%d/%m/%Y')
                except ValueError:
                    pass  # Formato no coincide
            raise ValueError('Formato de fecha no reconocido')
        except ValueError as e:
            print(f"Error: {e}")
            return None
    
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    
    df = df.drop(["ind"], axis=1)
    
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(normalizar_fecha)
    
    df = df.dropna()
    df = df.drop_duplicates()
    
    # df = df.applymap(lambda x: x.lower().strip() if isinstance(x, str) else x)
    
    df['sexo'] = df['sexo'].apply(lambda x: x.lower().strip())
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].apply(lambda x: x.lower())
    df['idea_negocio'] = df['idea_negocio'].apply(lambda x: x.lower().replace("_"," ").replace("-"," ").strip())
    # df['idea_negocio'] = df['idea_negocio'].apply(lambda x: x.strip())
    df['barrio'] = df['barrio'].apply(lambda x: x.lower().replace("_","-").replace("-"," "))
    # df['barrio'] = df['barrio'].apply(lambda x: x.strip())
    
    df['línea_credito'] = df['línea_credito'].apply(lambda x: x.lower().replace("-"," ").replace("_"," ").strip())
    
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: float(x.replace("$ ","").replace(",","").replace(" ","").strip()))
    
    df = df.drop_duplicates()
    df = df.dropna()
    # df = df.loc[df['monto_del_credito'] >= 100000]
        
    # print(df)
    # print(df.sexo.value_counts())
    # print(df.tipo_de_emprendimiento.value_counts())
    # print(df.idea_negocio.value_counts())
    # print(df.barrio.value_counts())
    # print(df.estrato.value_counts())
    # print(df.comuna_ciudadano.value_counts())
    # print(df.fecha_de_beneficio.value_counts())
    # print(df.monto_del_credito.value_counts())
    # print(df.línea_credito.value_counts())

    # df.barrio.value_counts().reset_index().to_csv('df_idea.csv', index=False)
    
    # print(df)

    return df

