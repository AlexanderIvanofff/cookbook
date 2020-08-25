from django.contrib import admin
from .models import Recipe, Ingredient


class IngredientInline(admin.TabularInline):
    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInline,
    ]


admin.site.register(Recipe, RecipeAdmin)
