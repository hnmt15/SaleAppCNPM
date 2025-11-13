
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin%40123@localhost/saledb?charset=utf8mb4"
#tren truong la root:root@localhost
#o nha la root:admin%40123@localhost
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 3
db = SQLAlchemy(app)
