from django.contrib import admin
from django import forms
from .models import Screen, Background, Clock, Tag


class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = "__all__"
        widgets = {
            'included_tags': forms.CheckboxSelectMultiple(),
            'excluded_tags': forms.CheckboxSelectMultiple()
        }


class ScreenAdmin(admin.ModelAdmin):
    form = ScreenForm


class BackgroundForm(forms.ModelForm):
    class Meta:
        model= Background
        fields = "__all__"
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }


class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_image', 'tag_list_display',)
    readonly_fields = ('display_image',)
    form = BackgroundForm


admin.site.register(Screen, ScreenAdmin)
admin.site.register(Clock)
admin.site.register(Background, BackgroundAdmin)
admin.site.register(Tag)
