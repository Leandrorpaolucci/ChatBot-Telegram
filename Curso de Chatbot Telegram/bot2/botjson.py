#-- coding: utf-8 --

import telebot #biblioteca do bot
import json #valores em json
import urllib # tratar urls
import urllib.request
#-----------------------------------

API_TOKEN = '6006907759:AAHLmHb5l10L-WvhDEuK-1CXT4cml0kH6H0' #@botFather

bot = telebot.TeleBot(API_TOKEN) #telebot-sumário e TeleBot(comando) aplicando token

@bot.message_handler(commands=['cep'])

def send_cep(message):
	# responde o comando /cep com uma mensagem/ação.
	msg = bot.reply_to(message, """Digite o cep que deseja consultar:
""")
	#Pegar o ID da conversa.
	cid = message.chat.id 
	
	#Armazena a informação digitada e joga para o proximo passo (mensagem digitada -> proximo passo)
	bot.register_next_step_handler(msg, send_cep_step)
	
def send_cep_step(message):
	cid = message.chat.id #pegar o id da conversa
	mensagem_cep = message.text #mensagem digitada
	mensagem_cep = mensagem_cep.replace("-", "").replace(".", "")
	if len(mensagem_cep) == 8:
		try:
			url = "https://viacep.com.br/ws/" + mensagem_cep + "/json/"
			response = urllib.request.urlopen(url) # abrir a url que nós colocamos json
			data = json.loads(response.read()) # carregar o json e ler os valores do json
			cep = data['cep'] # escolhendo valores do json
			cep = cep.replace("-", "")
			logradouro =  data['logradouro']
			bairro = data['bairro']
			localidade = data['localidade']
			uf = data['uf']
			bot.send_message(cid, "CEP: " + cep + "\nLogradouro: " + logradouro + "\nBairro: " + bairro + "\nLocalidade: " + localidade + "\nUF: " + uf)
			bot.reply_to(message, "Consulta CEP realizada com sucesso!\nCaso queira consultar novamente acesse: /cep\nCaso deseja retornar para o menu, acesse o /menu")
		except Exception as e:
			bot.reply_to(message, f"{mensagem_cep} incorreto!Tente novamente.\nDeseja consultar novamente? clique aqui: /cep")
			print(e)
		
	
bot.polling()

