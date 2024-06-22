from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messaging.views import MessageViewSet

router = DefaultRouter()
router.register(r'', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
