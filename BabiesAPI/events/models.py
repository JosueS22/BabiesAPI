from django.db import models

# Create your models here.
class Event(models.Model):
    event_type = models.CharField(max_length=80, null=False)
    dateTime = models.DateTimeField()
    info = models.CharField(max_length=200, null=False)
    baby = models.ForeignKey(
        'baby.Baby',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )

    def __str__(self):
        return 'Event: {} baby:{} date:{}'.format(self.event_type, self.baby, self.dateTime)
        

