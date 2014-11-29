from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User)
    id = models.AutoField('#', primary_key=True)
    path = models.ImageField(upload_to='%Y/%m/%d')

    def for_json(self):
        return {"path": str(self.path)}
