from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # ... other URL patterns ...
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.index, name='index'),
    path('view-activities/', views.view_activities, name='view_activities'),
    path('learn-more/', views.learn_more, name='learn_more'),
    path('contact-support/', views.contact_support, name='contact_support'),
    path('school-website/', views.school_website, name='school_website'),
    path('create/', views.create_activity, name='create_activity'),
    path('edit/<int:activity_id>/', views.edit_activity, name='edit_activity'),
    path('delete/<int:activity_id>/', views.delete_activity, name='delete_activity'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register-activity/<int:activity_id>/', views.register_for_activity, name='register_activity'),
    path('user-registered-activities/', views.user_registered_activities, name='user_registered_activities'),  # Added this line
    path('unregister-activity/<int:activity_id>/', views.unregister_activity, name='unregister_activity'),
]
