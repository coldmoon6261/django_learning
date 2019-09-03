from django.urls import path
from django.urls import include
from rango import views
from about import views as aboutviews

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', include('about.urls')),
]
