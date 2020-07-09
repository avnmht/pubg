from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('tester',views.tester,name='tester'),
    path('register', views.reg,name='reg'),
    path('registerr',views.registerr,name='registerr'),
    path('login',views.login,name='login'),
    path('log',views.log,name='log'),
    path('info',views.info,name='info'),
    path('createform',views.createformer,name='createform'),
    path('mainformer',views.mainformer,name='mainformer'),
    path('theirform',views.theirformer,name='theirformer'),
    path('regioner',views.regioner,name='regioner'),
    path('characterer',views.characterer,name='characterer'),
    path('tierer',views.tierer,name="tierer"),
    path('ingamenameer',views.ingamenameer,name="ingamenameer"),
    path('kperder',views.kperder,name="kperder")
]
