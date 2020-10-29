from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('',views.index,name='index'),
    path('sign',views.sign,name='sign'),
    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # path(
    #     'change-password',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='common/change-password.html',
    #         success_url='/'
    #     ),
    #     name='change-password'
    # ),

    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
    name="password_reset" ),
    
    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
    name='password_reset_confirm'),
    
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
    name='password_reset_complete'),


    

]