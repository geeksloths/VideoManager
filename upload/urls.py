from django.urls import path
from upload import views

app_name='upload'

urlpatterns = [
    path('', views.index, name='index')
]