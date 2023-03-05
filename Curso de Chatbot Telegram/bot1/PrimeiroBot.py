#Garantir o acentuo nas palavras
#-- coding: utf-8 --

import telebot #importando a bliblioteca pyTelegramBotAPI
from telebot import types #Está selecionando a lib types que faz parte do telebot
API_TOKEN = '6006907759:AAHLmHb5l10L-WvhDEuK-1CXT4cml0kH6H0' #@botFather

bot = telebot.TeleBot(API_TOKEN) #telebot-sumário e TeleBot(comando) aplicando token

#Inicio

@bot.message_handler(commands=['start'])  #recebo mensagem /start  |  #mensagem digitada (usuário)
def send_welcome(message):
	cid = message.chat.id # pegar id da conversa
	msg = bot.reply_to(message, "Bem Vindo !!! \n Este é um bot criado por Leandro Ribeiro Paolucci.\n Em caso de dúvidas mande-nos um e-mail.\n Nosso id é " + str(cid)) #mensagem enviada para o usuário.

	bot.send_message(cid, "Caso você precisa de ajuda, use a função /ajuda.")
	
#Ajuda

@bot.message_handler(commands=['ajuda'])
def send_help(message):
	cid = message.chat.id 
	msg_help = bot.reply_to(message, "Você não se lembra das funções? Não tem problema eu vou te ajudar! \n Opção 1: /cadastro \n Opção 2: /categoria \n Opção 3: /contato")
	bot.send_message(cid, "Caso ainda encontre dificuldades, entre em contato pelo o e-mail: faleconosco@email.com.br")


@bot.message_handler(commands=['categoria'])
def send_category(message):
	cid = message.chat.id
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True) #crio o layout de opções, e digo para ele que só pode selecionar uma opção
	markup.add('Sapatos', 'Roupas', 'Botas', 'Tênis') #Opções que aparecerá para o nosso cliente
	msg_cat = bot.reply_to(message, "Escolha a categoria que você deseja para continuarmos.", reply_markup=markup) #qual das categorias ele deseja



bot.polling() #Escuta usuário






