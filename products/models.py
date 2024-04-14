from django.db import models


class Detail(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlıq")
    description = models.CharField(max_length=255, verbose_name="Açıqlama")

    def __str__(self):
        return self.title


class Types(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlıq")
    description = models.CharField(max_length=255, verbose_name="Açıqlama")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Qiymət")
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Endirimli qiymət"
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Məhsul adı")
    description = models.TextField(verbose_name="Məhsul haqqında")
    types = models.ManyToManyField(Types, verbose_name="Növlər")
    initial_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Başlanğıc qiyməti",
        null=True,
        blank=True,
    )
    discounted_initial_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Endirimli başlanğıc qiyməti",
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True, verbose_name="Aktivdir?")
    details = models.ManyToManyField(Detail, verbose_name="Xüsusiyyətlər")

    image = models.ImageField(upload_to="products/images/", verbose_name="Şəkil")
    likes = models.PositiveIntegerField(default=0, verbose_name="Bəyənilmə sayı")
    views = models.PositiveIntegerField(default=0, verbose_name="Baxış sayı")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Yaradılma tarixi"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dəyişiklik tarixi")

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlıq")
    description = models.TextField(verbose_name="Məzmun")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Məhsul"
    )
    image = models.ImageField(upload_to="news/images/", verbose_name="Şəkil")
    is_active = models.BooleanField(default=True, verbose_name="Aktivdir?")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Yaradılma tarixi"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dəyişiklik tarixi")

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="Sual")
    answer = models.TextField(verbose_name="Cavab")

    def __str__(self):
        return self.question

class Subscriptions(models.Model):
    mobile = models.CharField(max_length=255, verbose_name="Mobil nömrə")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma tarixi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dəyişiklik tarixi")

    def __str__(self):
        return self.mobile
