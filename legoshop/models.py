from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    description = models.TextField(verbose_name="Опис категорії", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class LegoSet(models.Model):
    DIFFICULTY_CHOICES = [
        ('E', 'Легкий'),
        ('M', 'Середній'),
        ('H', 'Складний'),
    ]

    AGE_CHOICES = [
        ('4+', '4+'),
        ('6+', '6+'),
        ('8+', '8+'),
        ('12+', '12+'),
        ('18+', '18+'),
    ]

    name = models.CharField(max_length=200, verbose_name="Назва набору")
    set_number = models.CharField(max_length=20, unique=True, verbose_name="Номер набору")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    pieces_count = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Кількість деталей")
    age_restriction = models.CharField(max_length=4, choices=AGE_CHOICES, default='6+', verbose_name="Вікове обмеження")
    difficulty_level = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, default='M',
                                        verbose_name="Рівень складності")
    in_stock = models.BooleanField(default=True, verbose_name="В наявності")
    release_date = models.DateField(verbose_name="Дата випуску")
    weight = models.FloatField(help_text="Вага в грамах", default=0, verbose_name="Вага")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Зображення")

    class Meta:
        verbose_name = "LEGO набір"
        verbose_name_plural = "LEGO набори"
        ordering = ['-release_date']

    def __str__(self):
        return f"{self.name} ({self.set_number})"


from django.db import models

class Order(models.Model):
    lego_set = models.ForeignKey('LegoSet', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення #{self.id} - {self.lego_set.name} x{self.quantity}"
