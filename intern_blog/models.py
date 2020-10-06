#load uploads
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Post(models.Model):

    CATEGORIES=(
        ('summer','summer'),
        ('academics','academics'),
        ('campus','campus'),
        ('other','other')
    )

    title=models.CharField(max_length=100)
    content=models.TextField()
    date = models.DateTimeField(default=timezone.now())
   # photo=models.ImageField(upload_to=user_directory_path)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=100,default="other",choices=CATEGORIES)
    photo = models.TextField(
        default="https://www.pngkey.com/png/detail/516-5169774_iif-internships-icon.png")  # remove later

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('PostDetail', kwargs={'pk':self.pk})
