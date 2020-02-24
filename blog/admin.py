from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','created_time', 'modified_time', 'author']
    list_filter = ('category', 'created_time', 'modified_time', 'tags')  # 过滤器
    search_fields = ('title',)  # 搜索字段
    filter_horizontal = ('tags',)
    fields = (('title', 'category'),'body', 'tags','created_time', 'modified_time', 'author')
    #list_filter = ('category', 'created_time', 'modified_time', 'tags')  # 过滤器
    #search_fields = ('servtitleer', 'category', 'tags')  # 搜索字段
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.site_header = 'SmartzLink后台管理'
admin.site.site_title = '后台管理'


