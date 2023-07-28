from django.shortcuts import render, redirect
from .models import Product, Card
from django.views.generic import ListView

# Create your views here.
class Allproduct(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

class Carddetail(ListView):
    model = Card
    template_name = 'card.html'
    context_object_name = 'order'

def Addtocard(request,pk):
    product=Product.objects.get(id=pk)
    order=Card.objects.get(id=pk)
    if order is not None:
        order.quantity+=1
        order.save()
        return render(request, 'products.html')
    else:
        order=Card.objects.create(product=product)
        order.save()
        return redirect('card_detail')




