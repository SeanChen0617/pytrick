from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Stocks
from django.views import generic
import twstock, time

# Create your views here.
def StockList(request):
	monitored_stocks = Stocks.objects.all()[:10]
	result = []

	for _ in monitored_stocks:
		monitored_stocks_with_price = {}

		stock = twstock.realtime.get(_.stock_code)
		
		monitored_stocks_with_price['stock_name'] = stock['info']['name']
		monitored_stocks_with_price['stock_code'] = stock['info']['code']
		monitored_stocks_with_price['stock_open_price'] = stock['realtime']['open']
		monitored_stocks_with_price['stock_latest_price'] = stock['realtime']['latest_trade_price']
		monitored_stocks_with_price['percentage'] = round((float(stock['realtime']['latest_trade_price']) - float(stock['realtime']['open']))/float(stock['realtime']['open'])*100, 3)

		stock = twstock.Stock(_.stock_code)

		monitored_stocks_with_price['stock_price'] = ', '.join(map(str,stock.high[-5:]))

		result.append(monitored_stocks_with_price)

		time.sleep(3)

	context = {
		'result': result,
	}
	return render(request, 'stocks/index.html', context)
