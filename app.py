import pyautogui
from time import sleep

# # Passos manuais para realizar este processo? 
# 1 - Clicar e digitar meu usuario
pyautogui.click(984,538, duration=0.5)
pyautogui.write('Renato')
# 2 - Clicar e digitar minha senha
pyautogui.click(976,568, duration=0.5)
pyautogui.write('123456')
# 3 - CLicar em entrar
pyautogui.click(867,599, duration=0.5)
# 4 - Extrar cada produto
with open('produtos.txt', 'r') as file:
    for line in file:
        product = line.split(',')[0]
        quantity = line.split(',')[1]
        price = line.split(',')[2]
        # 	1 - clicar e digitar produto
        pyautogui.click(720,525, duration=0.5)
        pyautogui.write(product)
        # 	2 - clicar e digitar quantidade
        pyautogui.click(704,559, duration=0.5)
        pyautogui.write(quantity)
        # 	3 - clicar e digitar o preço
        pyautogui.click(684,578, duration=0.5)
        pyautogui.write(price)
        # 	4 - clicar em registrar
        pyautogui.click(589,738, duration=0.5)
        sleep(1)

