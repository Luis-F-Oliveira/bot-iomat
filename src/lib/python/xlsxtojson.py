import json
from tkinter import filedialog
import pandas as pd
from unidecode import unidecode

def XlsxToJson():
    try:
        filename = filedialog.askopenfilename(
            initialdir="/", 
            title="Selecione um arquivo", 
            filetypes=(
                ("Arquivos Excel", "*.xlsx"), 
                ("Todos os arquivos", "*.*")
            )
        )

        df = pd.read_excel(filename)
        
        df = df.apply(lambda x: x.map(lambda y: unidecode(str(y).lower())))

        data = df.to_json(orient='records', force_ascii=False)

        formatted_data = json.loads(data)
        formatted_json = json.dumps(formatted_data, indent=4)

        with open('json/servers.json', 'w', encoding='utf-8') as f:
            f.write(formatted_json)

        return True
    except Exception as e:
        print("Ocorreu um erro durante a conversão do arquivo:", e)
        return False