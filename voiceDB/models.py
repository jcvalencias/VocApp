from django.db import models

# Create your models here.


class VocabDB(models.Model):

    class Meta:
        app_label = "voiceDB"

    French = models.TextField()
    Spanish = models.TextField()
    Example = models.TextField()
    learning_rate = models.FloatField(null=True)
    audio_file = models.TextField()
    