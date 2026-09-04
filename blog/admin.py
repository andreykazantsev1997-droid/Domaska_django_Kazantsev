from django.contrib import admin
from blog.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_indicator')

    list_filter = ('publication_indicator',)

    search_fields = ('title', 'content')