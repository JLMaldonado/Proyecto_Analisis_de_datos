import pandas as pd
import numpy as np
from datasets import load_dataset
import csv
import requests

def descargar_datos_y_guardar_como_csv(url, archivo_salida):
    
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(archivo_salida, 'w') as archivo:
                archivo.write(response.text)
            print("\n=============== Procesando información en bruto =======================================")
            
            print(f"Datos descargados y guardados como: ({archivo_salida})")
            print("\n======================================================")
        else:
            print(f"Error al descargar los datos. Código de estado: {response.status_code}")
    

# Llama a la función con la URL y el nombre del archivo de salida
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
nombre_archivo = "archivos_clinicos.csv"
descargar_datos_y_guardar_como_csv(url, nombre_archivo)