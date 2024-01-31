from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ('', include('main.urls'))
]


#SelinuxSerializer
 #   path('', include("main.urls")),
 #   path('selinux/', include('selinux.urls')),