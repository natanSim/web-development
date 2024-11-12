from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return ('Welcome to our website!,'
            'You can find here the best collections in the world')


@app.route('/price')
def get_price():
    return 'This collection is discounted for 24 hours today - instead of 200$, you pay 150$  '


@app.route('/news')
def news():
    return ('You can read news about our collection here '
            '(When a new collections arrives, and more)')


@app.route('/about')
def about():
    return 'You can read here about of our company'


@app.route('/collection')
def collection():
    return 'You can find our collections here '

# news
# about
# collection


app.run()