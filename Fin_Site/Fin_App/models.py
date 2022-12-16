from django.db import models


currency_choices = (("USD", "USD"), ("EUR", "EUR"), ("BYN", "BYN"))


class CustomUser(models.Model):
    username = models.CharField(max_length=50)

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
    def cost_amount(self):
        return 

class Shit(models.Model):
    perks_choises = (
        ("A", "admin user"), 
        ("C", "casual user"), 
        ("M", "master user"), 
        )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    user_perk = models.CharField(max_length=1, choices=perks_choises)
    is_banned = models.BooleanField(default=False)

class SpandingCategories(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

class Spanding(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    category = models.ForeignKey(SpandingCategories, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, choices=currency_choices)
    expense = models.PositiveIntegerField()
    spanding_time = models.DateTimeField(auto_now_add=True)

class SpaceLogs(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action_time = models.DateTimeField(auto_now_add=True)
    action = models.TextField()

class ReferalCode(models.Model):
    code = models.CharField(max_length=255)                             #change !!!
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    expiring_time = models.DateTimeField(auto_now_add=True)