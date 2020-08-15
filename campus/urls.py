
from django.urls import path
from . import views
app_name = 'campus'
urlpatterns = [
    path('', views.home),
    path('add-level/', views.AddLevel.as_view(), name='add_level'),
    path('levels/', views.Levels.as_view(), name='levels'),
    path('add-class-room/', views.AddClassRoom.as_view(), name='add_class_room'),
    path('class-rooms/', views.ClassRooms.as_view(), name='class_rooms'),

    
]
