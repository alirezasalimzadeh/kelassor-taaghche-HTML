from django.urls import path
from account import views

urlpatterns = [
    path('profile/', views.ProfileListCreateView.as_view()),
    path('profile/<int:pk>', views.ProfileRetrieveUpdateDestroyView.as_view()),
    path('payment/', views.PaymentListCreateView.as_view()),
    path('payment/<int:pk>', views.PaymentRetrieveUpdateDestroyView.as_view()),
    path('paymentHistory/', views.PaymentHistoryListCreateView.as_view()),
    path('paymentHistory/<int:pk>', views.PaymentHistoryRetrieveUpdateView.as_view())
]
