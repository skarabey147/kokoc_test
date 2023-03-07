from django.urls import path
from . import views

app_name = 'test'

urlpatterns = [
    path('', views.index, name='index'),
    path('donetest/', views.done_tests, name='done_tests'),
    path('test/<int:id>/', views.tests, name='tests'),
    path('test/<int:id>/answer/<int:id_q>/', views.answer, name='answer'),
    path('test/start/<int:id>/', views.start_test, name='start'),
]
