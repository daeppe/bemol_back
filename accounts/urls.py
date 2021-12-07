from django.urls import path
from .views import AccountsView, LoginView, AccountsByIdView


urlpatterns = [
    path('accounts/', AccountsView.as_view()),
    path('accounts/<str:username>/', AccountsByIdView.as_view()),
    path('login/', LoginView.as_view())
]
