from django.contrib import admin
from django.utils.html import format_html
from .models import Category, LegoSet

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_per_page = 20


@admin.register(LegoSet)
class LegoSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'set_number', 'category', 'price', 'in_stock', 'preview_image')
    list_filter = ('category', 'in_stock', 'age_restriction', 'difficulty_level')
    search_fields = ('name', 'set_number')
    list_per_page = 20

    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'set_number', 'category', 'description', 'image')  # ⬅️ image додано
        }),
        ('Характеристики', {
            'fields': ('price', 'pieces_count', 'weight')
        }),
        ('Додаткові параметри', {
            'fields': ('age_restriction', 'difficulty_level', 'in_stock', 'release_date')
        }),
    )

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" />', obj.image.url)
        return "—"
    preview_image.short_description = "Зображення"
