from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='mainIndex'),
    path('meet-staff/', views.meetStaff, name="meetStaff"),
    path('whatwedo/adventure-training/', views.at, name="at"),
    path('whatwedo/camps/', views.camps, name='camps'),
    path('whatwedo/flying-and-gliding/', views.flying, name='flying'),
    path('whatwedo/shooting-and-marksmanship/', views.shooting, name='shooting'),
    path('whatwedo/sport/', views.sport, name='sport'),
    path('whatwedo/training-and-education/', views.education, name='education'),
    path('news/', views.comingSoon, name="news"),
    path('gallery/', views.comingSoon, name='gallery'),
    path('resources-download/', views.resources, name='resources'),
    path('join-as-a-cadet/', views.joincadet, name="joincadet"),
    path('join-as-a-staff-volunteer/', views.joinstaff, name="joinstaff"),
    path('for-parents/', views.forParents, name="joincommittee"),
    path('contactus/', views.contactus, name='contactus'),
]