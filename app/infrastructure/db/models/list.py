from django.db import models


class List(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"

    def items(self):
        return self.item_set.all()
