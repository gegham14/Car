from django.db import models

Drafts = (('super car', 'super car'),
          ('Off-Road', 'Off-Road Adventure SUV'),
          ('Luxury', 'Luxury  Sedan'),
          ('Hybrid', 'Hybrid Crossover'),
          ('sports car', ' Sports Car'))

Colors = (('green', 'Green'),
          ('white', 'White'),
          ('black', 'Black'),
          ('blue', 'Blue'),
          ('red', 'Red'))


class Manufacture(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30, unique=True)
    address = models.CharField(max_length=30,
                               default='Armenia')
    photo = models.ImageField(upload_to='media/cars/')
    draft = models.CharField(max_length=15, choices=Drafts)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30, unique=True)
    email = models.EmailField()
    phone = models.BigIntegerField()
    date = models.DateField
    draft = models.CharField(max_length=15, choices=Drafts)
    colors = models.CharField(max_length=15, choices=Colors)
    photo = models.ImageField(upload_to='media/cars/')

    def __str__(self):
        return self.name
