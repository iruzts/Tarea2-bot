import os
import telebot

bot = telebot.TeleBot('1876928307:AAGflQfNmpErCfpaYhsnHB-lEChTEMME6lI') #anadimos el token

@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def saludo(mensaje):
    bot.reply_to(mensaje, "Hola, Estoy a tu disposicion")
    print("Mandaron saludo")

@bot.message_handler(commands=['dolar']) 
def dolar(mensaje):
    bot.reply_to(mensaje, "La tasa de cambio del dolar es de 23.81 lempira hondureño")
    print("Mandaron dolar")

@bot.message_handler(commands=['euro'])
def euro(mensaje):
    bot.reply_to(mensaje, "La tasa de cambio del euto es de 28.11 lempira hondureño")
    print("Mandaron euro")

@bot.message_handler(commands=['oro'])
def oro(mensaje):
    bot.reply_to(mensaje,   "El precion de la onza de Oro es L 43,111.62 en $1,812.35")
    print("Mandaron oro")


@bot.message_handler(commands=['cafe'])
def direccion(mensaje):
    bot.reply_to(mensaje, "El precio del cafe L 3,597.88")
    print("Mandaron cafe")

bot.polling()