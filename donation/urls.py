from django.urls import path

from . import views

urlpatterns = [


    # My donation page

    path('', views.my_donation, name=''),


    # Payment success

    path('payment-success', views.payment_success, name='payment-success'),


    # Payment failed

    path('payment-failed', views.payment_failed, name='payment-failed'),


]









