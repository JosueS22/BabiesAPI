from django.db import models

# Create your models here.
class Baby(models.Model):
    name = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    parent = models.ForeignKey(
        'parent.Parent',
        on_delete=models.SET_NULL
        null=True,
        blank=True
    )

    def __str__(self):
        return 'Baby: {}'.format(self.name, self.lastname)
