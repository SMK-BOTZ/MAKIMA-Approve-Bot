from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28243586"))
    API_HASH = getenv("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
    BOT_TOKEN = getenv("BOT_TOKEN", "6812106698:AAGtDaint6SnowdD8tvgIEktg6Q-hzzhg50")
    FSUB = getenv("FSUB", "SMK_NETWORK_0")
    CHID = int(getenv("CHID", "-1002092889672"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://jyotimaurya891824:AQOW8F91e1FhF7Ty@cluster0.m5988ba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
