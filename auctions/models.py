from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Categorie(models.Model):
    categorie = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.categorie}"

class Action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="myactions")
    title = models.CharField(max_length=256)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie,  blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    ended = models.DateTimeField(blank=True, null=True)
    image = models.URLField(blank = True)
    win = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="mywins")
    initial_bid = models.DecimalField(max_digits=19, decimal_places=2)
    watch = models.ManyToManyField(User, related_name="mywatchs", blank=True, null=True)

    def finish(self):
        self.ended = timezone.now()
        if self.bids.order_by('-bid').first():
            self.win = self.bids.order_by('-bid').first().user
        else:
            self.win = self.user
        self.save()

    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mybids")
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name="bids")
    bid = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return f"{self.user}: R${self.bid} in {self.action}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mycomments")
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name="comments")
    title = models.CharField(max_length=64)
    comment = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user}: {self.title}"