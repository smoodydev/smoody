from django.db import models

# Programming languages attached to projects
class Language(models.Model):
    name = models.CharField(max_length=254)
    url_safe = models.CharField(max_length=254, blank=True, null=True)
    def __str__(self):
        return self.name


# What type of project it is - something small or large?
class Category(models.Model):
    name = models.CharField(max_length=254)
    url_safe = models.CharField(max_length=254, blank=True, null=True)
    def __str__(self):
        return self.name


# Main Projects Model
class Project(models.Model):
    categories = models.ManyToManyField('Category', blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    languages = models.ManyToManyField("Language")
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    source_link = models.URLField(blank=True)
    deployment_link = models.URLField(blank=True)
    other_link = models.URLField(blank=True)
    recommended = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/projects")

    def __str__(self):
        return self.name
