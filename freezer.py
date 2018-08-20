from flask_frozen import Freezer
from app import app, Market

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

@freezer.register_generator
def market():
    for market in Market.query.all():
        yield { 'FMID': market.FMID }

if __name__ == '__main__':
    freezer.freeze()