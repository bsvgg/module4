from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()


class Advertisement(models.Model):

    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        "изображение",
        upload_to='advertisements/'
    )

    # Название товара
    # CharField - короткое текстове поле
    # 'заголовок' - verbose_name - человекочитаемое название
    title = models.CharField('заголовок', max_length=128)

    # Описание товара
    # Длинное текстовое поле
    description = models.TextField('описание')

    # Цена
    # числовое поле с фиксированной точкой
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    # Уместен ли торг
    # Булевое поле (логическое) (окшн)
    auction = models.BooleanField('торг', help_text='Отметьте, если хотите торговаться')

    # Дата публикации
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения/обновления + что изменилось
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_date = self.created_at.strftime("%H:%M:%S")
            return format_html(
                '<span style="color:green; font-weight:bold;"> Сегодня в {} </span>',
                created_date
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата изменения')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_date = self.updated_at.strftime("%H:%M:%S")
            return format_html(
                '<span style="color:red; font-weight:bold;"> Сегодня в {} </span>',
                updated_date
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Фото")
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{}" style="max-height:80px; max-width:80px;">',
                self.image.url
            )

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'


    # Продавец (имя продавца, контакты для связи, отзывы)
    # Фото объявления
    # Рейтинг
    # В продаже/не в продаже - актуальность
