from gettext import install
import os

import pip
leitura = r"C:\Users\ge380\OneDrive\Documentos\Projects\leitura"; 
for nome_arquivo in os.lista(leitura):
   caminho_arquivo = os.path.join(leitura,nome_arquivo);
   if nome_arquivo.endswith(".txt"):
    with open(caminho_arquivo, "r", encoding = "utf-8") as f:
      conteudo_txt= f.read();
      print(conteudo_txt);
   elif nome_arquivo.endswith(".json"):
     import json
     with open(caminho_arquivo, "r", encoding="utf-8") as f:
       dados_json = json.load(f);
       print(dados_json)
       