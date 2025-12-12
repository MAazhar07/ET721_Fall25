from django.contrib import admin
from .models import Item, Feedback

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment', 'item__name')