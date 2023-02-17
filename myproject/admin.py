from django.contrib import admin
from .models import Post,Room,Message,Contact
# Register your models here.
admin.site.register(Post)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Contact)

