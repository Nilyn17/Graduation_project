from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum

# Create your models here.

currency_choices = (("USD", "USD"), ("EUR", "EUR"), ("BYN", "BYN"))


class BalanceLessZeroError(Exception):
    """BalanceLessZeroError."""

class CustomUser(AbstractUser):
    telegram_id = models.PositiveIntegerField(null=True)
    

class Space(models.Model):
    title = models.CharField(max_length=25)
    currency = models.CharField(max_length=3, choices=currency_choices)

    """User wallet model."""
    users = models.ManyToManyField(
        CustomUser,
        related_name="space",
        through="Shit"
    )

    @property
    def spend(self):
        money = sum(obj.total for obj in self.send_transactions.all())
        return money

    def __str__(self) -> str:
        return f"{self.user.username} | balance: {self.balance}"

class Shit(models.Model):
    perks_choises = (
        ("A", "admin user"), 
        ("C", "casual user"), 
        ("M", "master user"),
        )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    user_perk = models.CharField(max_length=1, choices=perks_choises)



class Spanding(models.Model):
    transaction_statuses = (
        ("C", "Completed"),
        ("A", "Approved"),
        ("R", "Rejected"),
        ("P", "Pending"),
    )

    category = models.CharField()

    from_wallet = models.ForeignKey(
        Space,
        on_delete=models.PROTECT,
        related_name="send_transactions",
    )
    to_wallet = models.ForeignKey(
        Space,
        on_delete=models.PROTECT,
        related_name="receive_transactions",
    )
    status = models.CharField(
        max_length=1,
        choices=transaction_statuses,
        default=transaction_statuses[-1],
    )
    total = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.CharField(max_length=3, choices=currency_choices)
    processed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.status} | total: {self.total}"

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.from_wallet.balance - self.total < 0:
                raise BalanceLessZeroError
        return super().save(*args, **kwargs)