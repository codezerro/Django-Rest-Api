from django.db import models
from django.conf import settings
# Create your models here.


def update_upload_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    imgae = models.ImageField(
        upload_to=update_upload_image, blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or ""
