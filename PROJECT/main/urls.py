from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('', views.home, name='homepage'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                  path("login/", auth_views.LoginView.as_view(template_name='account/login.html'), name="login"),
                  path("signup/", views.SignupView.as_view(), name="signup"),
                  path("profile/", auth_views.PasswordChangeView.as_view(
                      template_name='profile.html',
                      success_url='/'
                  ), name='profile'),
                  path('password_reset/',
                       auth_views.PasswordResetView.as_view(
                           template_name='passres/password_reset.html',
                           subject_template_name='passres/password_reset_subject.txt',
                           email_template_name='passres/password_reset_email.html',
                       ),
                       name='password_reset'),
                  path('password_reset/done/',
                       auth_views.PasswordResetDoneView.as_view(
                           template_name='passres/password_reset_done.html'
                       ),
                       name='password_reset_done'),
                  path('reset/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(
                           template_name='passres/password_reset_confirm.html'
                       ),
                       name='password_reset_confirm'),
                  path('reset/done/',
                       auth_views.PasswordResetCompleteView.as_view(
                           template_name='passres/password_reset_complete.html'
                       ),
                       name='password_reset_complete'), ] + static(settings.STATIC_URL,
                                                                   document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
