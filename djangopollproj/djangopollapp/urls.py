from django.urls import path
from . import views
from .views import RegisterView,LoginView,PollView,ChoiceView,Pollupdate,Polldelete,Count,Home,WelcomeHome,PollViewall

urlpatterns = [
    path('register/',views.RegisterView),
    path('register/login/',views.LoginView),
    path('login/',views.LoginView),
    path('login/poll/',views.PollView),
    path('poll/',views.PollView),
    path('login/home/poll/',views.PollView),
    path('register/login/home/poll/',views.PollView),
    path('choice/',views.ChoiceView),
    path('login/home/choice/',views.ChoiceView),
    path('register/login/home/choice/',views.ChoiceView),
    path('login/home/choice/count/',views.Count),
    path('register/login/home/choice/count/',views.Count),
    path('count/',views.Count),
    path('choice/count/',views.Count),
    path('register/choice/count/',views.Count),
    path('pollupdate/<id>/',views.Pollupdate),
    path('pollupdate/<id>/delete/',views.Polldelete),
    path('delete/<id>/',views.Polldelete),
    path('home/',views.Home),
    path('login/home/',views.Home),
    path('register/login/home/',views.Home),
    path('welcomehome',views.WelcomeHome),
    path('all',views.PollViewall),

]
