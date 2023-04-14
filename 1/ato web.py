from selenium import webdriver
import pandas as pd


tabela = pd.read_excel("commodities.xlsx")
print(tabela)

navegador = webdriver.Chrome()
navegador.get('https://google.com')

for linha in tabela.index:
    produto = tabela.loc[linha,'produto']

    print(produto)
    produto = produto.replace("ó","o").replace("ã","a").replace("á","a").replace("ç","c").replace("ú","u").replace("é","e")
    link = f'https://www.melhorcambio.com/{produto}-hoje'
    navegador.get(link)

    preço = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    preço = preço.replace(".","").replace(",",".")
    print(preço)
    tabela.loc[linha, "preço atual"] = float(preço)

tabela["comprar"] = tabela["preço atual"] < tabela["preço ideal"]

tabela.to_excel("commodities_atualizado.xlsx", index = False)

print(tabela)

#.click() -> clicar
#.send_keys("texto") -> escrever
#.get_attribute() -> pegar um valor
#.loc[] ->> localiza uma linha e coluna
#.repalce ->> troca alguma valor


