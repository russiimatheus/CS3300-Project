from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view-activities/', views.view_activities, name='view_activities'),
    path('learn-more/', views.learn_more, name='learn_more'),
    path('contact-support/', views.contact_support, name='contact_support'),
    path('school-website/', views.school_website, name='school_website'),
    path('create/', views.create_activity, name='create_activity'),
    path('edit/<int:activity_id>/', views.edit_activity, name='edit_activity'),
    path('delete/<int:activity_id>/', views.delete_activity, name='delete_activity'),
]
