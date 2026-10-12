import telebot
from telebot import types

TOKEN = open("token.txt").read().strip()
bot = telebot.TeleBot(TOKEN)

NEGOCIO = "Tienda Don Pepe"

def teclado():
    k = types.ReplyKeyboardMarkup(resize_keyboard=True)
    k.row("/productos", "/ofertas")
    k.row("/domicilio", "/horarios")
    k.row("/ubicacion", "/contacto")
    return k

@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, f"¡Hola! Bienvenido a {NEGOCIO} 🛒\nElige una opción:", reply_markup=teclado())

@bot.message_handler(commands=["productos"])
def productos(m):
    bot.reply_to(m, "🥖 Pan y panadería\n🥛 Lácteos y huevos\n🍎 Frutas y verduras\n🥩 Carnes y embutidos\n🧴 Limpieza e higiene\n🥤 Bebidas y snacks")

@bot.message_handler(commands=["ofertas"])
def ofertas(m):
    bot.reply_to(m, "🔥 Ofertas de la semana:\n- Huevos (docena): 2 USD\n- Leche (litro): 1 USD\n- Arroz (kg): 1.20 USD")

@bot.message_handler(commands=["domicilio"])
def domicilio(m):
    bot.reply_to(m, "🛵 Enviamos a domicilio en el barrio.\nPedido mínimo: 10 USD. Envío: 1 USD.\nHaz tu pedido por WhatsApp con tu lista y dirección.")

@bot.message_handler(commands=["horarios"])
def horarios(m):
    bot.reply_to(m, "Lunes a sábado: 9:00 a 23:00\nDomingos: 9:00 a 22:00")

@bot.message_handler(commands=["ubicacion"])
def ubicacion(m):
    bot.reply_to(m, "📍 Calle Principal 123, junto a la plaza")

@bot.message_handler(commands=["contacto"])
def contacto(m):
    bot.reply_to(m, "📞 WhatsApp: +00 000 000 000")

@bot.message_handler(func=lambda m: True)
def otros(m):
    bot.reply_to(m, "No entendí 😅 Usa los botones de abajo.", reply_markup=teclado())

bot.infinity_polling()
