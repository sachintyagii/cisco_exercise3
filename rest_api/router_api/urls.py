from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import RouterView

urlpatterns = [
    path('router/', RouterView.as_view(), name='router_list_add_view'),
    path('update/<str:ip>/', RouterView.as_view(), name='update_view'),
    path('api-token-auth/', obtain_auth_token, name='api_auth_token'),
]