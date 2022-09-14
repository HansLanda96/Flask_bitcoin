from application import app
from flask import render_template
from webargs import fields
from webargs.flaskparser import use_kwargs
from .utils import get_rate, currency_input
from werkzeug.exceptions import NotFound


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rates')
@use_kwargs(
    {
        'currency': fields.Str(required=True)
    },
    location="query"
)
def rate_input(currency: str):
    rate = currency_input(currency)
    if rate is None:
        raise NotFound
    return render_template('currency/rates.html', rate=rate)


@app.route('/currency_list')
def currency_list():
    return render_template('currency/currency_list.html', data=get_rate())


@app.route('/currency_list/detail/<string:currency>')
def detail(currency: str):
    data = currency_input(currency)
    if data is None:
        raise NotFound
    return render_template('currency/currency_detail.html', currency=data)
