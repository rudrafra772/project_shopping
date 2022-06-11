from re import template
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_Views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm



urlpatterns = [

    #path('', views.home),
    path('', views.ProductView.as_view(),name='home'),

    path('product-detail/<int:pk>', views.Product_DetailView.as_view(), name='product-detail'),

    #path('cart/', views.add_to_cart, name='add-to-cart'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

    path('cart/', views.show_cart, name='showcart'),



    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
  
    path('address/', views.address, name='address'),

    path('orders/', views.orders, name='orders'),





    path('passwordchange/', auth_Views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm ,success_url='/passwordchangedone/'),name='passwordchange'),

    path('passwordchangedone/', auth_Views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone' ),

    path('password-reset/', auth_Views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_Views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_Views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),    

    path('password-reset-complete/', auth_Views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    path('mobile/', views.mobile, name='mobile'),

    path('mobile/<slug:data>', views.mobile, name='mobiledata'),


    #path('login/', views.login, name='login'),
    path('accounts/login/', auth_Views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),

    path('logout/', auth_Views.LogoutView.as_view(next_page='login'), name='logout'),

    #path('registration/', views.customerregistration, name='customerregistration'),

    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),

    path('checkout/', views.checkout, name='checkout'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)