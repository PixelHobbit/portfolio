from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#class BlogType(models.Model):
    #type_name = models.CharField(max_length=15)

    #def __str__(self):
        #return self.type_name

class Blog(models.Model):
    title = models.CharField(default='文章标题',max_length=50)
    date = models.DateField()
    image = models.ImageField(default='default.png',upload_to='Images/')
    text = models.TextField(default='正文')
    #blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    #author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "<Blog: %s>" % self.title

    def short_text(self):
        if len(self.text) > 100:
           return self.text[:100] + '→ To Be Continue';
        else:
            return self.text;
