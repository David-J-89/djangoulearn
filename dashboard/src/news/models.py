from django.db import models
from django.conf import settings
# Create your models here.
# model  -- headline (title, image, url)
# restrict the user to scraping once every 24hours,need to create a userprofile to monitor the scraping
# model -- userprofile(user, last_scrape(datetimefield))


class Headline(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    url = models.TextField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    last_scrape = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.user, self.last_scrape)

