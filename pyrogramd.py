from pyrogram import Client, filters

bot_token = "6736117252:AAGqsg1Qu1WUFiSObDA1f3_ymq_-RCk_0Xg"

api_id = 29551577
api_hash = "d09fb1a2667ade3fbd78a6586d6d945e"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()
