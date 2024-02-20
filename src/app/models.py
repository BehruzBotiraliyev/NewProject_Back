from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid
from django.conf import settings

# Create your models here.

Languages = (
    ('uz', _('O\'zbek tili')),
    ('en', _('English')),
    ('ru', _('Russian')),
)


class Image(models.Model):
    image = models.ImageField(upload_to="images/", verbose_name=_("Rasm"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))

    image_count = models.IntegerField(default=0, verbose_name=_("Rasmlar soni"))

    def __str__(self):
        return self.image.url

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        return self

    def get_image_url(self):
        return settings.HOST + self.image.url

    def increase_images(self):
        self.image_count += 1
        self.save()
        return self

    class Meta:
        verbose_name = _("Rasm")
        verbose_name_plural = _("Rasmlar")
        db_table = 'images'


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Sarlavha [title]"))
    content = models.TextField(verbose_name=_("Ma'lumot [content]"), null=True)

    image = models.ManyToManyField(Image, verbose_name=_("Rasm"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Tahrirlangan vaqti"))

    published_at = models.DateField(verbose_name=_("Chop etilgan vaqt"), null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name=_("UUID"))

    views = models.IntegerField(default=0, verbose_name=_('Ko\'rishlar soni'))
    images_count = models.IntegerField(default=0, verbose_name=_('Rasmlar soni'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(News, self).save(*args, **kwargs)
        return self

    def increase_views(self):
        self.views += 1
        self.save()
        return self

    def increase_images(self):
        self.images_count += 1
        self.save()
        return self

    class Meta:
        verbose_name = _("Yangilik")
        verbose_name_plural = _("Yangiliklar")
        db_table = "news"
        indexes = [
            models.Index(fields=['title', 'content', 'created_at'])
        ]


class Footer(models.Model):
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=200, verbose_name=_("Telefon raqamlar"))
    address = models.CharField(max_length=200, verbose_name=_("Manzil"))
    logo = models.ImageField(upload_to="images/", verbose_name=_("Logo"), null=True, blank=True)
    facebook = models.URLField(verbose_name=_("Facebook manzili"), null=True, blank=True)
    instagram = models.URLField(verbose_name=_("Instagram manzili"), null=True, blank=True)
    telegram = models.URLField(verbose_name=_("Telegram manzili"), null=True, blank=True)
    youtube = models.URLField(verbose_name=_("Youtube manzili"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Tahrirlangan vaqti"))

    def __str__(self):
        return self.email

    def get_logo_url(self):
        return settings.HOST + self.logo.url

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Footer, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = _("Footer[saytni pasti qismi]")
        verbose_name_plural = _("Footer[saytni pastki qismi]")
        db_table = "footer"


class About(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name=_('Ma\'lumot'), null=True)

    image = models.ImageField(upload_to='images/', verbose_name=_("Rasm"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqt"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Tahrirlangan vaqt"))

    def __str__(self):
        return self.title

    def get_image_url(self):
        return settings.HOST + self.image.url

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(About, self).save(*args,  **kwargs)
        return self

    class Meta:
        verbose_name = _("Sayt haqida")
        verbose_name_plural = _("Sayt haqida")
        db_table = 'about'


class Services(models.Model):
    service_type = models.CharField(max_length=200, verbose_name=_("Xizmat turi"))

    class Meta:
        verbose_name = _("Xizmat")
        verbose_name_plural = _("Xizmatlar")
        db_table = "services"


class EmployeePositions(models.Model):
    position = models.CharField(max_length=240, verbose_name=_("Lavozim [position]"))

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = _("Lavozim")
        verbose_name_plural = _("Lavozimlar")
        db_table = 'employee_positions'


class Employees(models.Model):
    fullname = models.CharField(max_length=200, verbose_name=_("Ism va familiyangiz [fullname]"))
    address = models.CharField(max_length=500, verbose_name=_("Manzilingiz"))
    position = models.ForeignKey(EmployeePositions, on_delete=models.SET_NULL, verbose_name=_("Lavozimingiz"), null=True)
    image = models.ImageField(upload_to="images/", verbose_name=_("Rasm"), null=True)
    phone = models.CharField(max_length=200, verbose_name=_("Telefon raqamingiz"), null=True)
    email = models.EmailField(verbose_name=_("Email manzilingiz"))
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name=_("UUID"))

    def __str__(self):
        return self.fullname

    def get_image_url(self):
        return settings.HOST + self.image.url

    class Meta:
        verbose_name = _("Xodim")
        verbose_name_plural = _("Xodimlar")
        db_table = 'employees'




