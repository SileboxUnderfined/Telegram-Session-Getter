from pyrogram import Client
from configparser import ConfigParser

config: ConfigParser = ConfigParser()
config.read('config.ini')
info = config['Info']

session_name: str = input('Введите название для файла: ')
app: Client = Client(name=session_name,api_id=info['api_id'],api_hash=info['api_hash'])
app.start()
app.stop()
print(f'Сессия сохранена в {session_name}.session')