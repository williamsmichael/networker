from django.contrib import admin

from .models import *


class ForumAdmin(admin.ModelAdmin):
	pass

class ThreadAdmin(admin.ModelAdmin):
	list_display = ('title', 'forum', 'creator', 'created')
	list_filter = ('forum', 'creator')

class PostAdmin(admin.ModelAdmin):
	search_fields = ('title', 'creator')
	list_display = ('title', 'thread', 'creator', 'created')


# Register your models here.
admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)



