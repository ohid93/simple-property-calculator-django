from django.db import models


class Property(models.Model):
    choices = (
      ('Terrace House', "Terrace House"),
      ('Bunglow House', "Bunglow House"),
      ('Apartment', "Apartment"),
      ('DuplexHouse', "Duplex"),
    )
    property_type = models.CharField(max_length=255, choices=choices)
    property_name = models.CharField(max_length=255)
    property_address = models.CharField(max_length=255)
    land_area = models.FloatField()
    transaction_price = models.FloatField()
    price_per_ft2 = models.FloatField(editable=False)
    date = models.DateField()
    built_up_area = models.FloatField()

    def save(self, *args, **kwargs):
      self.price_per_ft2 = self.transaction_price / self.land_area
      return super(Property, self).save(*args, **kwargs) 

    def __str__(self):
      return self.property_name