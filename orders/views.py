from django.shortcuts import render, redirect
from rest_framework.response import Response
from shop.models import Product
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
import environ, math, random, requests
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            name = obj.first_name + " " + obj.last_name
            email = obj.email
            phone = obj.phone_number
            
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )  

            list = []
            for item in cart:           
                amounts = int(item['price'] * item['quantity'])
                list.append(amounts)
            price = sum(list)
            
            for item in cart:       
                slug = item['my-slug']
            cart.clear()

            #EVERYTHING FLUTTERWAVE AND PAYMENT
            auth_token= env('SECRET_KEY')
            hed = {'Authorization': 'Bearer ' + auth_token}
            data = {
                "tx_ref":''+str(math.floor(1000000 + random.random()*9000000)),
                "amount":price,
                "currency":"NGN",
                "redirect_url":"https://a1a7-197-210-45-62.ngrok.io/orders/webhook",
                "payment_options":"card",
                "meta":{
                    "consumer_id":1,
                    "consumer_mac":"92a3-912ba-1192a"
                },
                "customer":{
                    "email":email,
                    "phonenumber":int(phone),
                    "name":name
                },

                "customizations":{
                    "title":"JummertyCollection store",
                    "description":"Best store in Nigeria",
                    "logo":"https://avatars.githubusercontent.com/u/63419117?v=4"
                }
                }
            url = 'https://api.flutterwave.com/v3/payments'
            response = requests.post(url, json=data, headers=hed)
            response=response.json()
            link=response['data']['link']
            return redirect(link)      
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})

@csrf_exempt
@require_http_methods(['POST', 'GET'])
def webhook(request):
    request_json = request.body
    print(request_json)
    return HttpResponse("Successful")






