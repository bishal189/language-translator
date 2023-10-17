from django.urls import path
from . import views
urlpatterns = [
    path('',views.renderer,name='indexrenderer'),
    path('check2ndfile',views.check2ndfile,name='check2ndfile')

]
