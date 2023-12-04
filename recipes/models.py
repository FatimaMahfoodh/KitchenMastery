from django.db import models

class Recipe(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.TextField()
    ingredients = models.TextField()  # Field to store ingredients as a comma-separated string
    instructions = models.TextField()  # Field to store instructions as a comma-separated string

    def get_ingredients(self):
        return self.ingredients.split(',') if self.ingredients else []

    def get_instructions(self):
        return self.instructions.split(',') if self.instructions else []
    
