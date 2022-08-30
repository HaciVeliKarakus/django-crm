from django.db import models


class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Lead(models.Model):
    SOURCE_CHOICES = (
        ("Youtube", "Youtube"),
        ("Google", "Google"),
        ("Newsletter", "Newsletter"),
    )


    age = models.PositiveSmallIntegerField(default=0)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=20)

    profile_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return

    def __unicode__(self):
        return
