from django.urls import path

from . import views

app_name = 'appl_1_app'
urlpatterns = [
    path('', views.form_1, name='form_1'),
    path('form_1/', views.form_1, name='form_1'),
    path('get/', views.get, name='get'),
    path('form_2/', views.form_2, name='form_2'),
    path('form_3/', views.form_3, name='form_3'),
    path('result/', views.result, name='result'),
    path('table/', views.table, name='table'),
]
