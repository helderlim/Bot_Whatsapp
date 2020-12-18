#importar as bibliotecas 
from selenium import webdriver 
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#navegar até o whatsapp web 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(8)
#definir contato e qual mensagem sera enviada 
contatos = ['Jean']
mensagem = 'OLA eu sou atendente virtual da Salomao Fiat e vim te dizer que voce é um viado'
#bsucar contatos 
def buscar_contato(contatos):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def ler_mensagem(mensagem):
    campo_envio = driver.find_elements_by_xpath('//')

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(5)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    ler_mensagem(mensagem)
#campo de mensagem privada 'copyable-text selectable-text'
#enviar mensagens para o contato /grupo 
#laço de repetição se for bom dia manda opção se for 1 mande itanhaem se for 4 mande link de vendas e 
#assim vai indo.