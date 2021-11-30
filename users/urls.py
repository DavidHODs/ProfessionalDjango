from django.urls import path
from .views import SignupPageView

app_name = 'users'

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
]