# Link = https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Programando horário para rodar seu código: https://www.youtube.com/watch?v=SxEjHAlCqmo

# Passo a Passo do Projeto

# Passo 1 -Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# BIBLIOTECAS EM PYTHON , (pyautogui = RPA) 
# pip install pyautogui
import pyautogui
import time
# clicar ->  pyautogui.click
# escrver -> pyautogui.write
# aperta uma tecla -> pyautogui.press
# atalhos -> pyautogui.hotkey("ctrl", "c")
# rolar a página -> pyautogui.scroll

pyautogui.PAUSE = 0.5 # PAUSE SÓ RODA NOS COMANDOS DO pyautogui espera 1 segundo para executar cada comando

# aperta a tecla do windows 
pyautogui.press("win")
# digita o nome do programa (google)
pyautogui.write("google")
# aperta enter
pyautogui.press("enter")
# digitar o link
link = "dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# apertar enter
pyautogui.press("enter")
# espera 2 segundos
time.sleep(2)


# Passo 2 - Fazer Longin
pyautogui.click(x=608, y=512)
# digitar o email
pyautogui.write("cadastroproduto@gmail.com")
# passar para o campo de senha
pyautogui.press("tab")
# digitar a senha
pyautogui.write("produto")
# ir para o botão de logar
pyautogui.click(x=932, y=708)
time.sleep(2)

# passo 3 - Importar base de dados
# pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)
# PANDAS USA [] PARA TRABALHAR COM DADOS

for linha in tabela.index:
    # passo 4 - Cadastrar um produto
    pyautogui.click(x=634, y=369)
    # codigo
    codigo = tabela.loc[linha , "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # marca
    marca = tabela.loc[linha , "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # tipo
    tipo = tabela.loc[linha , "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    # categoria
    categoria = tabela.loc[linha , "categoria"]
    pyautogui.write(str(categoria)) # str(1)
    pyautogui.press("tab")
    # preco
    preco = tabela.loc[linha , "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    # custo
    custo = tabela.loc[linha , "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # obs  
    obs = tabela.loc[linha , "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
        pyautogui.press("tab")

    # enviar o produto
    pyautogui.press("enter")

    pyautogui.scroll(5000)
    # passo 5 - Repetir até acabar a base de dados
