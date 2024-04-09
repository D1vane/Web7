from django.contrib import admin
from .models import Underground,Underground_Facts
@admin.register(Underground)
class UndergroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'time_create','is_red_book','class_of_animal','count_symbols','name_to_slug')
    list_display_links = ('id', 'animal')
    ordering = ['time_create','animal']
    list_editable = ('is_red_book',)
    list_per_page = 5
    actions = ['set_red_book', 'delete_red_book']
    @admin.display(description="Количество символов")
    def count_symbols(self, underground: Underground):
        return f"Содержит {len(underground.content) + len(underground.unique_fact.content)} символов."

    @admin.display(description="Совпадение длины слага с именем")
    def name_to_slug(self, underground: Underground):
        temp = "Нет"
        if (len(underground.animal) == len(underground.page_name)):
            temp = "Да"
        else:
            temp = "Нет"
        return temp

    @admin.action(description="Занести в красную книгу")
    def set_red_book(self, request, queryset):
        count = queryset.update(is_red_book=Underground.Status.RARE)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description="Убрать из красной книги")
    def delete_red_book(self, request, queryset):
        count = queryset.update(is_red_book=Underground.Status.USUAL)
        self.message_user(request, f"Изменено {count} записи(ей).")

# Register your models here.
@admin.register(Underground_Facts)
class FactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    list_display_links = ('id', 'content')
    ordering = ['id']
    list_per_page = 5
