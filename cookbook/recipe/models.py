from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=90)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredient', on_delete=models.CASCADE)
    title = models.CharField(max_length=90)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title
