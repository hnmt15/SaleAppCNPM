# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
#
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:12345678@localhost/saledb?charset=utf8mb4"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#
# db = SQLAlchemy(app)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 3
db = SQLAlchemy(app)
