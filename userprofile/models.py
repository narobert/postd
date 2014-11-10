from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    path = models.ImageField(upload_to='%Y/%m/%d')
    user = models.ForeignKey(User)

    def for_json(self):
        return {"path": str(self.path)}
