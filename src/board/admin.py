from django.contrib import admin
from board.models import DevBoardBsc
# Register your models here.

@admin.register(DevBoardBsc)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'update_dt')
    list_filter = ('update_dt',)
    search_fields = ('title', 'content')