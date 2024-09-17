from django.urls import path
from main.views import show_main, enter, show_xml

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('enter/', enter, name='enter'),
    path('xml/', show_xml, name='show_xml'),
]