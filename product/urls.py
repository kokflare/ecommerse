from django.urls import path
from .views import Allproduct,Carddetail,Addtocard

urlpatterns=[
    path('',Allproduct.as_view(), name='all_products'),
    path('card/',Carddetail.as_view(),name='card_detail'),
    path('<int:pk>', Addtocard, name="addtocard"),
]

