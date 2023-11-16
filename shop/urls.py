from django.urls import path

from shop.views import ItemOfTelephone, ListOfTelephone

urlpatterns = [
    path('telephone/<int:pk>/', ItemOfTelephone.as_view()),
    path('telephone/', ListOfTelephone.as_view()),
]
