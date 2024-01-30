
from django.urls import path, include
from .views import selinux_list, UploadSElinuxEventView
from .viewsets import selinuxAPIview
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'selinux', selinuxAPIview)

urlpatterns = [
    path('', selinux_list, name='selinux_list'),
    path('api/', include(router.urls)),
]
