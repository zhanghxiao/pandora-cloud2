# -*- coding: utf-8 -*-

from os import getenv
# import os
from src.pandora_cloud.server import ChatBot

_port = getenv('PORT')
_proxy = getenv('PANDORA_PROXY')
_debug = getenv('PANDORA_DEBUG', 'false').lower() == 'true'
_local = getenv('PANDORA_LOGIN_LOCAL', 'false').lower() == 'true'
_listen = getenv('PANDORA_SERVER_LISTEN', 'true').lower() == 'true'
_server = getenv('PANDORA_SERVER', '0.0.0.0:{}'.format(_port) if _port else '0.0.0.0')
app = ChatBot(proxy=_proxy, debug=_debug, login_local=_local).run(_server, listen=_listen)


# from src.pandora_cloud.server import app

# if __name__=='__main__':
#     app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0')
