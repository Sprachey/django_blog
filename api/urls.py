from rest_framework import routers
from .views import UserViewset,BlogPostViewSet
from django.urls import path,include
from rest_framework.authtoken import views
from .views import LoginView



router = routers.DefaultRouter()
router.register(r'user',UserViewset)
router.register(r'blog',BlogPostViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('login/', LoginView.as_view(), name='user-login')
   
]


