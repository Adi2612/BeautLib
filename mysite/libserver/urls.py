from django.urls import path
from . import views

urlpatterns = [
	path('' , views.test , name='test'),
	path('myfriend/content-<int:p_n>' , views.myfriend,name = 'myfriend'),
]