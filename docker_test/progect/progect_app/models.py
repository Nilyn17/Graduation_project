from django.db import models
from django.contrib.auth.models import User


currency_choices = (("USD", "USD"), ("EUR", "EUR"), ("GBP", "GBP"))


class BalanceLessZeroError(Exception):
    """BalanceLessZeroError."""

class Wallet(models.Model):
    """User wallet model."""
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="wallet",
    )
    currency = models.CharField(max_length=3, choices=currency_choices)
    last_transaction_at = models.DateTimeField(null=True, blank=True)

    @property
    def balance(self):
        negative = sum(obj.total for obj in self.send_transactions.all())
        positive = sum(obj.total for obj in self.receive_transactions.all())
        return positive - negative

    def __str__(self) -> str:
        return f"{self.user.username} | balance: {self.balance}"


class Transaction(models.Model):
    transaction_statuses = (
        ("C", "Completed"),
        ("A", "Approved"),
        ("R", "Rejected"),
        ("P", "Pending"),
    )

    from_wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name="send_transactions",
    )
    to_wallet = models.ForeignKey(
        Wallet,
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
            if self.total <= 0:
                raise BalanceLessZeroError
        return super().save(*args, **kwargs)