from django.db import models


currency_choices = (("USD", "USD"), ("EUR", "EUR"), ("BYN", "BYN"))

class BaseDateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(BaseDateMixin):

    username = models.CharField(max_length=50)
    telegram_id = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class Space(BaseDateMixin):
    title = models.CharField(max_length=25)
    currency = models.CharField(max_length=3, choices=currency_choices)

    users = models.ManyToManyField(
        CustomUser,
        related_name="space",
        through="Shit"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def cost_amount(self):
        res = self.spanding_space.all()
        print(res)
        return 

    def __str__(self):
        return self.title
    

class Shit(BaseDateMixin):
    perks_choises = (
        ("A", "admin user"), 
        ("C", "casual user"), 
        ("M", "master user"), 
        )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_space")
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name="shit_space")
    user_perk = models.CharField(max_length=1, choices=perks_choises)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} | {self.space} | {self.grade}'

class SpendingCategory(BaseDateMixin):
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name="spanding_category")
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Spending(BaseDateMixin):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, related_name="spanding_space", on_delete=models.CASCADE)
    category = models.ForeignKey(SpendingCategory, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, choices=currency_choices)
    expense = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.user} | {self.category} | {self.space} | {self.expense} {self.currency}"

class SpaceLog(BaseDateMixin):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action_time = models.DateTimeField(auto_now_add=True)
    action = models.TextField()

    def __str__(self):
        return f'{self.user} | {self.action}'

class ReferalCode(BaseDateMixin):
    code = models.CharField(max_length=255)                             #change !!!
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expiring_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.code} | {self.expiration_time}'