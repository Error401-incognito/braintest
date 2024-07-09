from .models import EntryTest
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model= EntryTest
        fields= ["testname", "testcatorgy", "testmaterials", "testlink"]