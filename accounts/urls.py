from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    # path(
    #     'change-password',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='common/change-password.html',
    #         success_url='/'
    #     ),
    #     name='change-password'
    # ),



   


]