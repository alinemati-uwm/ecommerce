from django.shortcuts import render

from . models import Donation

from django.conf import settings

from django.urls import reverse


import stripe






# My donation page

def my_donation(request):

  # - Please uncomment after watching the necessary lecture 

    '''
    stripe.api_key = settings.STRIPE_PRIVATE_KEY


    session = stripe.checkout.Session.create(
  
    line_items=[{
  
      'price': 'price_1M1wi6GkiAM9M64mioJVvc6K',
  
      'quantity': 1,
  
    }],
  
    mode='payment',
  
    success_url=request.build_absolute_uri(reverse('payment-success')) + '?session_id={CHECKOUT_SESSION_ID}',
  
    cancel_url=request.build_absolute_uri(reverse('payment-failed'))
  
  )

  '''

    donation = Donation.objects.get(id=1)



    # - Please uncomment after watching the necessary lecture 


    #context = {'donation':donation, 'session_id': session.id, 'stripe_public_key':settings.STRIPE_PUBLIC_KEY}


    # - Please uncomment after watching the necessary lecture


    #return render(request, 'donation/my-donation.html', context=context)

    return render(request, 'donation/my-donation.html')


# Payment success

def payment_success(request):

    return render(request, 'donation/payment-success.html')


# Payment failed

def payment_failed(request):

    return render(request, 'donation/payment-failed.html')



