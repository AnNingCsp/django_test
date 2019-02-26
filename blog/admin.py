from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Tui,Article,Banner,Link

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Tui)
admin.site.register(Article)
admin.site.register(Banner)
admin.site.register(Link)