from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='دسته بندی')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='دسته بندی والد')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class BaseBook(models.Model):
    BOOK_TYPE_CHOICES = [
        ('epub', 'EPUB'),
        ('pdf', 'PDF'),
        ('mobi', 'MOBI'),
        ('mp3', 'MP3'),
        ('wav', 'WAV')
    ]
    name = models.CharField(max_length=100, verbose_name="نام کتاب")
    image = models.ImageField(upload_to='book_images', verbose_name="تصویر", null=True, blank=True)
    author = models.CharField(max_length=100, verbose_name="نویسنده")
    translator = models.CharField(max_length=100, blank=True, null=True, verbose_name="مترجم")
    rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)],
                             verbose_name="امتیاز")
    volume = models.FloatField(blank=True, null=True, verbose_name="حجم")
    book_type = models.CharField(choices=BOOK_TYPE_CHOICES, max_length=4, verbose_name="نوع")
    price = models.PositiveIntegerField(verbose_name="قیمت")
    is_discount = models.BooleanField(default=False, verbose_name="تخفیف دارد؟")
    about = models.TextField(blank=True, null=True, verbose_name="معرفی کتاب")
    description = models.TextField(blank=True, null=True, verbose_name="درباره کتاب")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} | {self.author} | {self.rate}"


class PrintedBook(BaseBook):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books', verbose_name="دسته بندی")
    collector = models.CharField(max_length=100, blank=True, null=True, verbose_name="گرد آورنده")
    publisher = models.CharField(max_length=100, verbose_name="انتشارات")
    year = models.IntegerField(verbose_name="سال انتشار")
    pages = models.IntegerField(verbose_name="تعداد صفحه ها")

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'


class AudioBook(BaseBook):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='audiobooks',
                                 verbose_name="دسته بندی")
    speaker = models.CharField(max_length=100, verbose_name="گوینده")
    time = models.PositiveIntegerField(default=0, verbose_name="زمان")
    is_transferable = models.BooleanField(default=False, verbose_name="قابلیت انتقال دارد؟")

    class Meta:
        verbose_name = 'صوتی'
        verbose_name_plural = 'صوتی'
