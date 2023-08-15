from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    """Настроки отображения модели Advertisement."""
    list_display = ['id', 'title', 'description',
                    'price', 'created_date', 'updated_date', 'auction', 'get_html_image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_is_false', 'make_auction_is_true']

    fieldsets = (
        (
            'Общее',
            (
                {
                    'fields': ('title', 'description', 'image')
                }
            )
        ),
        (
            'Финансы',
            (
                {
                    'fields': ('price', 'auction'),
                    'classes': ['collapse']
                }
            )
        )
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_is_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_is_true(self, request, queryset):
        queryset.update(auction=True)

# Регистрация модели в админке
admin.site.register(Advertisement, AdvertisementAdmin)
