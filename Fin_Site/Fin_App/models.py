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

    dick_list = models.ManyToManyField(
        "Ban_and_KickList",
        related_name="banlist",
        through="Dick"
    )

    @property
    def spend(self):
        # money = sum()
        return 

    def __str__(self) -> str:
        return f"{self.user.username} | balance: {self.balance}"

class Shit(models.Model):
    perks_choises = (
        ("A", "admin user"), 
        ("C", "casual user"), 
        ("M", "master user"),
        ("B", "banned user"), 
        )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    user_perk = models.CharField(max_length=1, choices=perks_choises)



class SpandingCategories(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    title = models.CharField(max_length=9999)

    def __str__(self) -> str:
        return self.title

class Spanding(models.Model):

    category = models.ForeignKey(SpandingCategories, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, choices=currency_choices)
    spend = models.PositiveIntegerField()
    spanding_time = models.DateTimeField(auto_now_add=True)

class SpaceLogs(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action_time = models.DateTimeField(auto_now_add=True)
    action = models.CharField()

class ReferalCode(models.Model):
    code = models.CharField(max_length=255)                             #change !!!
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    expiring_time = models.DateTimeField(auto_now_add=True)