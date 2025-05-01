import datetime
from django.db import models


class Screen(models.Model):
    active = models.BooleanField(default=False)
    rotate_every = models.DurationField(default=datetime.timedelta(seconds=30))
    clock = models.ForeignKey("Clock", blank=True, null=True, default=None, on_delete=models.CASCADE)

    refresh = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Screen #{self.id}"


class Background(models.Model):
    file = models.ImageField()

    def __str__(self) -> str:
        return self.file.name


class Clock(models.Model):
    show_time = models.BooleanField(default=True)
    show_date = models.BooleanField(default=False)
    time_format = models.CharField(max_length=64, default="%-I:%M:%S %p")
    date_format = models.CharField(max_length=64, default="%-d/%-m/%Y")
    size = models.CharField(max_length=16, default="5rem")
    x = models.IntegerField(blank=False, null=False, default=50)
    y = models.IntegerField(blank=False, null=False, default=50)

    @property
    def show_datetime(self) -> bool:
        return self.show_date and self.show_time

    def __str__(self):
        for screen in self.screen_set.filter(clock=self):
            return f"Clock of {str(screen)}"
        else:
            return f"Unassociated clock #{self.id}"