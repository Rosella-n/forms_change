from django.urls import path,include
import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('',views.login_page,name='login'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('home/',views.homepage,name='home'),
    path('signup/',views.signup,name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('activation_sent/',views.account_activation_sent,name='activation_sent'),
    path('activate/<uid>/<token>/', views.activate, name='activate'),
    path('password_reset/',views.password_reset,name='password_reset'),
    path('password_change/',views.password_change,name='password_change'),
]