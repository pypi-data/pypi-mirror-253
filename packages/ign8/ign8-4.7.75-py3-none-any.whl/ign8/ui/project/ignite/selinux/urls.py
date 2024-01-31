from django.urls import path, include
from .viewsets import selinuxAPIview
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'selinux', selinuxAPIview)

urlpatterns = [
    path('api/', include(router.urls)),
]
