import datetime
import typing as t
from django.db import models
from django.utils.functional import cached_property
from django.utils.html import format_html


class Screen(models.Model):
    active = models.BooleanField(default=False)
    rotate_every = models.DurationField(default=datetime.timedelta(seconds=30))
    clock = models.ForeignKey("Clock", blank=True, null=True, default=None, on_delete=models.CASCADE)
    included_tags = models.ManyToManyField("Tag", related_name="included_tags", blank=True)
    excluded_tags = models.ManyToManyField("Tag", related_name="excluded_tags", blank=True)

    refresh = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Screen #{self.id}"
    

class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return self.name


class Background(models.Model):
    file = models.ImageField()
    tags = models.ManyToManyField("Tag")

    def __str__(self) -> str:
        return self.file.name
    
    @cached_property
    def display_image(self):
        html = "<img src='{img}' style='width:40vw;'>"
        return format_html(html, img=self.file.url)

    @cached_property
    def thumbnail_image(self):
        html = "<img src='{img}' style='width:10vw;'>"
        return format_html(html, img=self.file.url)
    
    @cached_property
    def tag_list_display(self) -> str:
        l = []
        for tag in self.tags.all():
            l.append(tag.name)
        l = sorted(l)
        return ", ".join(l)


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