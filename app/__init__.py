from flask import Flask
from dotenv import load_dotenv 
import os
from OracleConnection import connect

load_dotenv()

app = Flask(__name__)

user = os.getenv('USER_FERRAMAX')
password = os.getenv('PASSWORD_FERRAMAX')
wallet_password = os.getenv('WALLET_PASSWORD')


connection = connect(user,password,wallet_password)

from .tools.routes import get_tools_route,get_tool_route,get_marcas_route #create_tool_route
