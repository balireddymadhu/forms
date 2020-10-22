from django import forms
class StudentForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    Feedback = forms.CharField(widget=forms.Textarea)

