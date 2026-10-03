from telegram.ext import Updater, CommandHandler, MessageHandler, filters

import leerAPI


sportracker = "<numero_de_telefono>:<API_de_Telegran_acociada_al_telefono"
opciones = "\n\n/ultimaCarrera\n/proximaCarrera\n/verClasificacionPilotos\n/verClasificacionConstructores"


def helpCommandStart(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = leerAPI.helpCommandStart()
    )

help_handler = CommandHandler('help', helpCommandStart)
command_handler = CommandHandler('command', helpCommandStart)
start_handler = CommandHandler('start', helpCommandStart)


def last(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = leerAPI.lastRace() + opciones,
        parse_mode="Markdown"
    )


last_handler = CommandHandler('ultimaCarrera', last)


def next(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = leerAPI.nextRace() + opciones,
        parse_mode="Markdown"
    )


next_handler = CommandHandler('proximaCarrera', next)


def drivers(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = leerAPI.driversQualy() + opciones,
        parse_mode="Markdown"
    )

drivers_handler = CommandHandler('verClasificacionPilotos', drivers)


def constructors(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = leerAPI.constructorsQualy() + opciones,
        parse_mode="Markdown"
    )



constructors_handler = CommandHandler('verClasificacionConstructores', constructors)




if __name__ == "__main__":
    updater = Updater(token = sportracker)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(last_handler)
    dispatcher.add_handler(next_handler)
    dispatcher.add_handler(drivers_handler)
    dispatcher.add_handler(constructors_handler)

    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(command_handler)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

    updater.idle()