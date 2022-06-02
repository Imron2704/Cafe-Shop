from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(default = '')
    price = models.FloatField(default = 1.2)
    image = models.ImageField(upload_to = 'media/coffee-images', null = True)

    class Meta:
        ordering = ['-name']

    def __str__(self) -> str:
        return self.name


class Payment(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete = models.CASCADE)
    user_email = models.EmailField()
    user_phone_number = models.IntegerField(default = 0)
    user_password = models.CharField(max_length = 30)


    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.coffee
