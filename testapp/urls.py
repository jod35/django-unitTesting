from . import views
from django.urls import path

app_name='testapp'

urlpatterns = [
    path('/',views.index,name='home'),
    path('about/',views.about,name='about'),
]