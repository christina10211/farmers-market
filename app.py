from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import render_template



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///markets.db'
db = SQLAlchemy(app)

class Market(db.Model):
  __tablename__ = 'markets'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  FMID = db.Column(db.String, primary_key=True)

@app.route("/")
def hello():
  markets = Market.query.all()
  return render_template("list.html", markets = markets)


@app.route("/markets/")
def markets():
  markets = Market.query.all()
  return render_template("list.html", markets = markets)
  

@app.route("/markets/<FMID>/")
def market(FMID):
  market = Market.query.filter_by(FMID=FMID).first()
  return render_template("show.html", market=market)



if __name__ == "__main__":
  app.run(debug=True)