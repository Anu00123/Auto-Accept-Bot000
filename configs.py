from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:AdDfgFRFVVfDEhdhyjjvjjftSEW")
    FSUB = getenv("FSUB", "SDBotz")
    CHANNEL_ID = int(getenv("CHANNEL_ID, "-1001722623591"))
    CHID = int(getenv("CHID", "-1000112234"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://ab:a@cluster0.xuftvdk.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
