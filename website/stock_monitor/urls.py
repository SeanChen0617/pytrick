from django.urls import path
from . import views

urlpatterns = [
	path('', views.StockList, name='stocklist'),
	#path('<int:stock_code>/', views.detail, name='detail'),
]