from django.db import models

class Folder(models.Model):
    """Représente un dossier contenant des vidéos."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    """Représente une vidéo dans un dossier."""
    title = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='videos/')
    folder = models.ForeignKey(Folder, related_name='videos', on_delete=models.CASCADE, null=True)


    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)
        if not self.title:
            self.title = self.file.name
            self.save()

    def __str__(self):
        return self.title
