from django.urls import path

from . import views

urlpatterns = [
	path('', views.ListView.as_view(), name='list'),
	path('<int:topic_id>/', views.detail, name='detail'),
]