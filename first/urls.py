from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.ulogin,name='ulogin'),
    path('start/',views.start,name='start'),
    path('createtodo/',views.createtodo,name='createtodo'),
    path('current/',views.currenttodo,name='currenttodo'),
    path('current/<int:id>/',views.viewtodo,name='viewtodo'),
    path('<int:id>/complete/',views.complete,name='complete'),
    path('<int:id>/delete/',views.delete,name='delete'),
    path('completed/',views.completedtodo,name='completedtodo'),
    path('logout/',views.ulogout,name='ulogout'),

]