import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("26162072", 12345))
      API_HASH = os.environ.get("ba25181c01b50d945748801b6c8b6ecc")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Stylish_Star2")
