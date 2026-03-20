from django.db import models

# Create your models here.

class Card(models.Model):
    card_id    = models.IntegerField(primary_key=True)
    name       = models.CharField(max_length=100)
    type       = models.CharField(max_length=100)
    frame_type = models.CharField(max_length=100)
    desc       = models.TextField()
    race       = models.CharField(max_length=100)
    archetype  = models.CharField(max_length=100, blank=True, default='')
    atk        = models.IntegerField(null=True, blank=True)
    def_points = models.IntegerField(null=True, blank=True)
    level      = models.IntegerField(null=True, blank=True)
    attribute  = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.name

class CardImage(models.Model):
    card        = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='images')
    image_url   = models.URLField()
    image_small = models.URLField()
    image_cropped = models.URLField()

class CardPrice(models.Model):
    card             = models.OneToOneField(Card, on_delete=models.CASCADE, related_name='price')
    tcgplayer_price  = models.CharField(max_length=20)
    ebay_price       = models.CharField(max_length=20)
    amazon_price     = models.CharField(max_length=20)
    cardmarket_price = models.CharField(max_length=20)


class CardSet(models.Model):
    card       = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='sets')
    set_name   = models.CharField(max_length=200)
    set_code   = models.CharField(max_length=50)
    set_rarity = models.CharField(max_length=100)
    set_price  = models.CharField(max_length=20)
