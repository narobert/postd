from django.db import models
from django.contrib.auth.models import User
	
class Picture(models.Model):
    user = models.ForeignKey(User, related_name='user')
    user_from = models.ForeignKey(User, related_name='user_from')
    id = models.AutoField('#', primary_key=True)
    paths = models.ImageField(upload_to='%Y/%m/%d')
    name = models.CharField(max_length=200)
    upvotes = models.PositiveIntegerField(u"Upvote", default=0)
    time = models.DateField()

    def for_json(self):
        return {"paths": str(self.paths), "name": self.name, "id_picture": self.id, "id": self.user.id, "id_from": self.user_from.id, "time": str(self.time), "username": self.user.username, "username_from": self.user_from.username}


class Vote(models.Model):
    user = models.ForeignKey(User)
    picture = models.ForeignKey(Picture)
    upvoted = models.BooleanField(u"Upvote", default=False)


class Profile(models.Model):
    id = models.AutoField('#', primary_key=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username

    def for_json(self):
        return {"username": self.user.username}



