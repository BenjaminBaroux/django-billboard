from django.db import models

class Post(models.Model):

    name = models.CharField(max_length=80, unique=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=100, default="empty title", null=True)
    content= models.TextField(null=True)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.title)

