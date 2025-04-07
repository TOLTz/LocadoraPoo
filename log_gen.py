from datetime import datetime
import os


def log(object):
    
    folder = 'log'
    file = os.path.join(folder, 'log.txt')
    os.makedirs(folder, exist_ok=True)
    try:
        # Tenta criar o arquivo se não existir
        with open(file, 'x', encoding='utf-8') as f:
            f.write(f"Log do codigo\n")
            f.write(f"\n{datetime.now()}\nAdicionado: {object} \n \n")
    except FileExistsError:

        with open(file, 'a', encoding='utf-8') as f:
            f.write(f"\n{datetime.now()}\nAdicionado: {object} \n \n")  
