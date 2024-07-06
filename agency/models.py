from django.db import models


class Header(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length=12)
    telegram_link = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    body_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Tours(models.Model):
    name = models.CharField(max_length=100)
    aviakompaniya = models.CharField(max_length=200)
    davomiyligi = models.CharField(max_length=200)
    ovqatlanish = models.CharField(max_length=200)
    viza = models.CharField(max_length=200)
    tibbiy_yordam = models.CharField(max_length=100)
    git = models.CharField(max_length=200)
    suv = models.CharField(max_length=200)
    jilet = models.CharField(max_length=100)
    bonus = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Networks(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Footer(models.Model):
    phone_number = models.CharField(max_length=13)
    application_time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    telegram_link = models.CharField(max_length=100)
    instagram_link = models.CharField(max_length=100)















