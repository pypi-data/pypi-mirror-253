
from django.urls import path, include
from .views import selinux_list, selinux_event_list , UploadSelinuxDataView, UploadSElinuxEventView, message_list
from .views import SetroubleshootEntry_list, SetroubleshootEntry_host, SetroubleshootEntryAPIview, messageAPIview, suggestionAPIview
from .views import SetroubleshootEntry_list_full, host_message
from .viewsets import selinuxAPIview

from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'selinux', selinuxAPIview)

urlpatterns = [
    path('', selinux_list, name='selinux_list'),
    path('messages/', message_list, name='selinux_messages_list'),
    path('messages/<pk>', message_list, name='selinux_messages_by_host_list'),
    path('selinux_event_list/', selinux_event_list, name='selinux_event_list'),
    path('upload_selinux_data/', UploadSelinuxDataView, name='upload_selinux_data'),
    path('upload_selinux_event/', UploadSElinuxEventView, name='upload_selinux_event'),
    path('api/setroubleshoot/upload/', SetroubleshootEntryAPIview, name='upload_setroubleshoot_entry'),
    path('api/message/upload/', messageAPIview, name='upload_message'),
    path('api/suggestion/upload/', suggestionAPIview, name='upload_suggestion'),
    path('SetroubleshootEntry/<str:hostname>/', SetroubleshootEntry_host, name='SetroubleshootEntry_host'),
    path('SetroubleshootEntry_list/', SetroubleshootEntry_list, name='SetroubleshootEntry_list'),
    path('SetroubleshootEntry_list_full/', SetroubleshootEntry_list, name='SetroubleshootEntry_list'),
    path('api/', include(router.urls)),
]