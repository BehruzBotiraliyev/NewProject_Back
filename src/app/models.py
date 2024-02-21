from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid
from django.conf import settings

from utils.models import State

# Create your models here.

Languages = (
    ('uz', _('O\'zbek tili')),
    ('en', _('English')),
    ('ru', _('Russian')),
)


class Image(models.Model):
    image = models.ImageField(upload_to="images/", verbose_name=_("Rasm"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))

    def __str__(self):
        return self.image.url

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        return self

    def get_image_url(self):
        return settings.HOST + self.image.url

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

    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_('Xolati'), null=True)

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

    class Meta:
        verbose_name = _("Yangilik")
        verbose_name_plural = _("Yangiliklar")
        db_table = "news"
        indexes = [
            models.Index(fields=['title', 'state', 'created_at'])
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

    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_("Holati"), null=True)

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

    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_("Xolati"), null=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return settings.HOST + self.image.url

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(About, self).save(*args,  **kwargs)
        return self

    class Meta:
        verbose_name = _("Tizim haqida")
        verbose_name_plural = _("Tizim haqida")
        db_table = 'about'


class ServiceType(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("To'liq nomi [title]"))
    attr = models.CharField(max_length=200, verbose_name=_("Qisqa nomi [attr]"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Xizmat turi")
        verbose_name_plural = _("Xizmat turlari")
        db_table = 'service_type'


class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("To'liq nomi [title]"))
    content = models.TextField(verbose_name=_("Xizmat haqida ma'lumot"))
    icon = models.ImageField(upload_to='icons/', verbose_name=_("Ikonka"), null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))

    service_type = models.ForeignKey(ServiceType, on_delete=models.SET_NULL,verbose_name=_("Xizmat turi"), null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_("Xolati"), null=True)

    def __str__(self):
        return self.title

    def get_icon_url(self):
        return settings.HOST + self.icon.url

    class Meta:
        verbose_name = _("Xizmat")
        verbose_name_plural = _("Xizmatlar")
        db_table = "services"


class EmployeePositions(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("To'liq nomi [title]"))
    attr = models.CharField(max_length=200, verbose_name=_("Qisqa nomi [attr]"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))

    def __str__(self):
        return self.title

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

    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_("Xolati"), null=True)

    def __str__(self):
        return self.fullname

    def get_image_url(self):
        return settings.HOST + self.image.url

    class Meta:
        verbose_name = _("Xodim")
        verbose_name_plural = _("Xodimlar")
        db_table = 'employees'


class SendApplication(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("So'rov nomi"))
    content = models.TextField(verbose_name=_("So'rov haqida ma'lumot"))
    phone = models.CharField(max_length=200, verbose_name=_("Telefon raqamingiz"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Murojaat")
        verbose_name_plural = _("Murojaatlar")
        db_table = 'applications'




