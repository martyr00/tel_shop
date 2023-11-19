from django.urls import path

from shop.views import TelephoneAPIView

urlpatterns = [
    path('telephone/<int:telephone_id>/', TelephoneAPIView.as_view()),
    path('telephone/', TelephoneAPIView.as_view()),
]
