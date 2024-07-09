from django.db import models

# Create your models here.
class EntryTest(models.Model):
    testname = models.CharField(max_length=200)
    testcatorgy = models.CharField(max_length=200)
    testmaterials = models.FileField()
    testlink = models.CharField(max_length=200)


    def __str__(self):
        return self.testname