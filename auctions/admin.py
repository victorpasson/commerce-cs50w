from django.contrib import admin
from .models import Categorie, Action, Bid, Comment, User


# Register your models here.
class ActionAdmin(admin.ModelAdmin):
    filter_horizontal = ("watch",)

admin.site.register(User)
admin.site.register(Categorie)
admin.site.register(Action, ActionAdmin)
admin.site.register(Bid)
admin.site.register(Comment)
