import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29202866"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "87b92238ec908026c7520486aca65a99")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://srcontant:MwRaopbXXqXnhRtD@cluster0.wxh4i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
