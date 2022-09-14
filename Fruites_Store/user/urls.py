from django.urls import path
from user import views


urlpatterns = [
    path('', views.UserView.as_view()),
    path('login', views.TokenObtainPairView.as_view()),
    path('<username>', views.UserView.as_view()),
    path('order/<user_id>', views.OrderView.as_view()),
    path('order/edit/<int:order_id>', views.OrderView.as_view()),
]
