from django.urls import path 
from . import views
urlpatterns = [
	path('', views.index_view, name='index'),
	path('home/', views.index_view, name='home'),
	path('future/', views.future_view, name='future'),
	path('current/', views.current_view, name='current'),
	path('plot/', views.create_plot, name='plot')

]