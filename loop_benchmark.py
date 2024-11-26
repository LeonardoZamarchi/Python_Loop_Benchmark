#teste de eficiencia entre estruturas de loop utilizando operação quadrática
import timeit
import numpy as np

def using_for(arr):
    res = []
    for num in arr:
        res.append(num*num)
    return res

def using_while(arr):
    res = []
    i = 0
    while i < len(arr):
        res.append(arr[i] * arr[i])
        i += 1
    return res

def using_list_comprehention(arr):
    return [num * num for num in arr]

#construindo um list_comprehention
def using_list_map_lambda(arr):
    return list(map(lambda x : x * x, arr))

def using_square_numpy(np_arr):
    return np.square(np_arr)

arr = list(range(1,1_000_001))
np_arr = np.arange(1,1_000_001)

for_time = timeit.timeit("using_for(arr)", globals=globals(), number=1)
while_time = timeit.timeit("using_while(arr)", globals=globals(), number=1)
list_comprehention_time = timeit.timeit("using_list_comprehention(arr)", globals=globals(), number=1)
list_map_lambda_time = timeit.timeit("using_list_map_lambda(arr)", globals=globals(), number=1)
square_numpy_time = timeit.timeit("using_square_numpy(np_arr)", globals=globals(), number=1)

print(f'for_time: {for_time:.6f}')
print(f'while_time: {while_time:.6f}')
print(f'list_comprehention_time: {list_comprehention_time:.6f}')
print(f'list_map_lambda_time: {list_map_lambda_time:.6f}')
print(f'square_numpy_time: {square_numpy_time:.6f}')





import pytesseract
from pdf2image import convert_from_path
import re
import pandas as pd

# Configuração do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ajuste o caminho para o Tesseract

def pdf_to_images(pdf_path):
    """Converte PDF em uma lista de imagens"""
    images = convert_from_path(pdf_path)
    return images

def extract_text_from_images(images):
    """Extrai texto das imagens usando Tesseract"""
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image, lang='por')  # Ajustar idioma se necessário
    return text

def parse_information(text):
    """Processa o texto extraído e retorna as informações estruturadas"""
    data = {}

    # Exemplos de extrações usando regex
    data['Nome'] = re.search(r'Nome:\s*(.+)', text, re.IGNORECASE).group(1) if re.search(r'Nome:\s*(.+)', text, re.IGNORECASE) else None
    data['Endereço'] = re.search(r'Endereço:\s*(.+)', text, re.IGNORECASE).group(1) if re.search(r'Endereço:\s*(.+)', text, re.IGNORECASE) else None
    data['Idade'] = re.search(r'Idade:\s*(\d+)', text).group(1) if re.search(r'Idade:\s*(\d+)', text) else None
    bens = re.findall(r'Bem:\s*(.+)', text, re.IGNORECASE)
    valores = re.findall(r'Valor:\s*([\d.,]+)', text)

    data['Bens'] = [{'Bem': b, 'Valor': v} for b, v in zip(bens, valores)]

    return data

def save_to_csv(data, output_path='dados_extracao.csv'):
    """Salva os dados extraídos em um arquivo CSV"""
    bens_df = pd.DataFrame(data['Bens'])
    bens_df.to_csv(output_path, index=False)

# Main script
if __name__ == "__main__":
    pdf_path = "seu_documento.pdf"  # Substitua pelo caminho do seu PDF
    images = pdf_to_images(pdf_path)
    text = extract_text_from_images(images)
    extracted_data = parse_information(text)
    
    print("Informações Extraídas:")
    print(extracted_data)
    
    save_to_csv(extracted_data)
