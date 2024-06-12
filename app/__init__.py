from flask import Flask
from dotenv import load_dotenv 
import os
from OracleConnection import connect
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)
user = os.getenv('USER_FERRAMAX')
password = os.getenv('PASSWORD_FERRAMAX')
wallet_password = os.getenv('WALLET_PASSWORD')

connection = connect(user,password,wallet_password)

from .tools.routes import get_tools_route,get_tool_route,get_marcas_route 
from .transbank.routes import init_transaction,transaction_return
    