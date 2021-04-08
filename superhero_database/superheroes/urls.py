from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('/', views.update_superhero, name='update_superhero'),
    path('/', views.delete_superhero, name='delete_superhero')
]
