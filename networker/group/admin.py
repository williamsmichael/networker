from django.contrib import admin
from .models import NetworkerGroup
from .models import GroupUser
from .models import MessageSystemTopic
from .models import MessageSystemMessage

# Register your models here.
admin.site.register(NetworkerGroup)
admin.site.register(GroupUser)
admin.site.register(MessageSystemTopic)
admin.site.register(MessageSystemMessage)

