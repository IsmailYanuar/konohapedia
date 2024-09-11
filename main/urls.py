from django.urls import path
from main.views import show_main, enter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('enter/', enter, name='enter'),
]