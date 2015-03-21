from selenium import webdriver
from selenium.webdriver.common.keys import Keys

baseURL = "http://www.mercadomineiro.com.br/pesquisa/gasolina-pesquisa-precos/"

browser = webdriver.Firefox()
# zipcode = "20010"

browser.get(baseURL)
# elem = browser.find_element_by_id("ctl00_Content_GBZS_txtZip").send_keys(zipcode)
# elem = browser.find_element_by_id("ctl00_Content_GBZS_btnSearch").click()

table = browser.find_element_by_id('tabelaPreco')

rows = table.find_elements_by_tag_name('tr')
print len(rows)

open all address with click :)
get all enderecos



outputfile = open('gasoline_prices.txt')

for element in rows:
    print type(element)
    print element.text



empresaEnderecos = browser.find_elements_by_id('empresaEndereco')
for endereco in empresaEnderecos:
	print endereco