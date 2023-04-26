from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello world"


# Endpoint 1: Get average exchange rate for a given date and currency code
@app.route('/api/exchange_rate/<table>/<code>/<date>', methods=['GET'])
def get_exchange_rate(table, code, date):
    url = f'http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/'
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][0]['mid']
    return  render_template('exchange.html', rate=rate)

# Endpoint 2: Get max and min average value for a given currency and number of last quotations
@app.route('/api/average_value/<table>/<code>/last/<num>', methods=['GET'])
def get_average_value(table, code, num):

    url = f'http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/last/{num}/'
    response = requests.get(url)
    data = response.json()
    rates = [float(rate['mid']) for rate in data['rates']]
    max_rate = max(rates)
    min_rate = min(rates)
    return render_template('min_max.html', min=min_rate, max=max_rate, currency = code, num=num )
    # return jsonify({'max_rate': max_rate, 'min_rate': min_rate})

# Endpoint 3: Get major difference between buy and ask rate for a given currency and number of last quotations
@app.route('/api/buy_sell_difference/c/<code>/last/<num>/', methods=['GET'])
def get_buy_sell_difference(code, num):

    url = f'http://api.nbp.pl/api/exchangerates/rates/c/{code}/last/{num}/'
    response = requests.get(url)
    data = response.json()
    buy_rates = [float(rate['bid']) for rate in data['rates']]
    sell_rates = [float(rate['ask']) for rate in data['rates']]
    difference = max([abs(buy_rates[i] - sell_rates[i]) for i in range(len(buy_rates))])
    return render_template('Diff.html', diff=difference, currency = code, num=num )

if __name__ == '__main__':
    app.run(debug=True)
