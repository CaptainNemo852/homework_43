from django.contrib import admin
from webapp.models import User, Article, Comment, Mark

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('favorite',)


admin.site.register(User, UserAdmin)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Mark)
