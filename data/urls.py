from django.urls import path 
from . import views
urlpatterns = [
	path('', views.index_view, name='index'),
	path('current/', views.current_view, name='current'),
	path('future/', views.future_view, name='future'),
	path('show/', views.show_plot, name="show")
]