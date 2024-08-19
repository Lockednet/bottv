from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Função que será chamada quando o comando /start for usado
async def start(update: Update, context):
    # Criação dos botões
    keyboard = [
        [InlineKeyboardButton("Baixar App", callback_data='baixar_app')],
        [InlineKeyboardButton("Tutorial", callback_data='tutorial')],
        [InlineKeyboardButton("Solicitar Teste", callback_data='solicitar_teste')]
    ]

    # Configuração dos botões em um layout
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Envia a mensagem com os botões
    await update.message.reply_text('Escolha uma das opções abaixo:', reply_markup=reply_markup)

# Função que lida com os cliques nos botões
async def button(update: Update, context):
    query = update.callback_query
    await query.answer()

    # Responde ao botão clicado
    if query.data == 'baixar_app':
        await query.edit_message_text(text="Você escolheu baixar o app.")
    elif query.data == 'tutorial':
        await query.edit_message_text(text="Você escolheu visualizar o tutorial.")
    elif query.data == 'solicitar_teste':
        await query.edit_message_text(text="Você escolheu solicitar um teste.")

async def main():
    # Substitua 'YOUR_TOKEN' pelo token do seu bot
    application = Application.builder().token("7220654524:AAFglI8oGgj7xEDtjd7rtbCXeSeh4V1DYBc").build()

    # Comando /start
    application.add_handler(CommandHandler("start", start))

    # Responde a interações com os botões
    application.add_handler(CallbackQueryHandler(button))

    # Inicia o bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
