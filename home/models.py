from django.db import models
from django import forms
from django.forms import ModelForm, TextInput, Select, FileInput
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

# Create your models here.

class Setting(models.Model):
    title = models.CharField(blank=True, max_length=500)
    title2 = models.CharField(blank=True, max_length=500)
    title3 = models.CharField(blank=True, max_length=500)
    company = RichTextField()

    def __str__(self):
        return self.title

class Qabul(models.Model):
    BRANCH = (
        ('Бакалавриат/Управление бизнесом (АПК)', 'Бакалавриат/Управление бизнесом (АПК)'),
        ('Бакалавриат/Экономика (сельское хозяйство)', 'Бакалавриат/Экономика (сельское хозяйство)'),
        ('Бакалавриат/Технология хранения и переработки сельскохозяйственной продукции (по видам продукции)', 'Бакалавриат/Технология хранения и переработки сельскохозяйственной продукции (по видам продукции)'),
        ('Бакалавриат/Декоративное садоводство и озеленение', 'Бакалавриат/Декоративное садоводство и озеленение'),
        ('Бакалавриат/Технология переработки животной продукции', 'Бакалавриат/Технология переработки животной продукции'),
        ('Бакалавриат/Зооинженерия: пчеловодство', 'Бакалавриат/Зооинженерия: пчеловодство'),
        ('Бакалавриат/Лесоводство', 'Бакалавриат/Лесоводство'),
        ('Магистратура/Технология хранения и переработки сельскохозяйственной продукции (по видам продукции)', 'Магистратура/Технология хранения и переработки сельскохозяйственной продукции (по видам продукции)'),
        ('Магистратура/Экономика (сельское хозяйство)', 'Магистратура/Экономика (сельское хозяйство)'),
        ('Магистратура/Агробизнес и инвестиционная деятельность', 'Магистратура/Агробизнес и инвестиционная деятельность'),


    )

    STATUS = (
        ('На рассмотрении', "Ko'rib chiqilmoqda"),
        ('Принято', "Qabul qilindi"),
    )

    name = models.CharField(max_length=50)
    date_birth = models.CharField(max_length=10)
    place_birth = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    pasport = models.CharField(max_length=9)
    study = models.CharField(max_length=90)
    year = models.CharField(max_length=10)
    diplom = models.CharField(max_length=10)
    direction_of_study = models.CharField(max_length=100, choices=BRANCH)
    pasport_photo = models.FileField(upload_to='file/')
    diplom_photo = models.FileField(upload_to='file/')
    photo3x4 = models.FileField(upload_to='file/')
    status = models.CharField(max_length=20, choices=STATUS, default='На рассмотрении')
    ip = models.CharField(blank=True, max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def photo_tag(self):
    #     return mark_safe('<img src="{}" height="50">'.format(self.photo.url))
    #
    # photo_tag.short_description = 'Photo'

# class PhotoForm(forms.Form):
#     photo = forms.FileField(
#         label = 'Select a file',
#         help_text = 'max. 42 megabytes'
#     )



class QabulForm(forms.ModelForm):
    class Meta:
        model = Qabul
        fields = (
            'direction_of_study', 'name', 'date_birth', 'place_birth', 'address', 'phone', 'pasport',
            'study', 'year', 'diplom', 'photo3x4', 'pasport_photo', 'diplom_photo',
        )
        widgets = {
            'direction_of_study': Select(attrs={'class': 'input'}),
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Фамилия Имя'}),
            'date_birth': TextInput(attrs={'class': 'input', 'placeholder': "Дата рождения (25.05.1995)"}),
            'place_birth': TextInput(attrs={'class': 'input', 'placeholder': "Место рождения (Ташкент)"}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'Адрес проживания (Город, Район, Улица)'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Телефонный номер (+998991234567)'}),
            'pasport': TextInput(attrs={'class': 'input', 'placeholder': 'Серия и номер паспорта (AA1234567)'}),
            'study': TextInput(attrs={'class': 'input', 'placeholder': "Выпускное учебное заведение (Школа, Колледж,Институт)"}),
            'year': TextInput(attrs={'class': 'input', 'placeholder': "Год выпуска"}),
            'diplom': TextInput(attrs={'class': 'input', 'placeholder': 'Номер и серия аттестат/диплома'}),
            'pasport_photo': FileInput(attrs={'class': 'input'}),
            'diplom_photo': FileInput(attrs={'class': 'input'}),
            'photo3x4': FileInput(attrs={'class': 'input'}),
        }