from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(default='文章标题',max_length=50)
    image = models.ImageField(default='default.png',upload_to='Images/')
    description = models.TextField(default='正文')

    def __str__(self):
       return self.title

    def short_description(self):
        if len(self.description) > 100:
           return self.description[:100] + '→ To Be Continue';
        else:
            return self.description;
