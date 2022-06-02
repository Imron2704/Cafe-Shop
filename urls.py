from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about),
    path('contact/', contact),
    path('blog/', blog),
    path('payment/', payment),
    path('order/', order),
    # path('cafe view/', cafestore),


    path('cafe/view/', cache_page(60 * 10)(CafeListView.as_view()), name="coffees"),
    path('cafe/create/', CafeCreateView.as_view()),
    path('cafe/update/<pk>', CafeUpdateView.as_view()),
    path('cafe/delete/<pk>', CafeDeleteView.as_view()),

]