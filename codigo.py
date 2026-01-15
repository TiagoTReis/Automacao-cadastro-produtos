import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("tab",presses=4)
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey("ctrl", "l")
time.sleep(2)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=403, y=374)
time.sleep(0.2)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)

tabela = pd.read_csv("produtos.csv")
#print(tabela)

for linha in tabela.index:
    pyautogui.click(x=428, y=261)
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    time.sleep(0.3)

    pyautogui.press("tab")
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    time.sleep(0.3)

    pyautogui.press("tab")
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    time.sleep(0.3)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    time.sleep(0.3)

    pyautogui.press("tab")
    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)
    time.sleep(0.3)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    time.sleep(0.3)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha,"obs"])
    pyautogui.write(obs)
    time.sleep(0.3)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
    time.sleep(1)