from django.contrib import admin
from .models import Category, LegoSet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_per_page = 20


@admin.register(LegoSet)
class LegoSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'set_number', 'category', 'price', 'in_stock')
    list_filter = ('category', 'in_stock', 'age_restriction', 'difficulty_level')
    search_fields = ('name', 'set_number')
    list_per_page = 20

    # Додаємо поля для відображення у формі редагування
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'set_number', 'category', 'description')
        }),
        ('Характеристики', {
            'fields': ('price', 'pieces_count', 'weight')
        }),
        ('Додаткові параметри', {
            'fields': ('age_restriction', 'difficulty_level', 'in_stock', 'release_date')
        }),
    )
