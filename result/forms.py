from django import forms
from django.forms import modelformset_factory

from app.models import Session, Semester
from course.models import Course
from accounts.models import Student

from .models import Result


class CreateResults(forms.Form):
    session = forms.ModelChoiceField(queryset=Session.objects.all())
    # term = forms.ModelChoiceField(queryset=Semester.objects.all())
    subjects = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple
    )


EditResults = modelformset_factory(
    Result, fields=("test_score", "exam_score"), extra=0, can_delete=True
)

