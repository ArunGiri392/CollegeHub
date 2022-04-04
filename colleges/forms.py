from django import forms
class ScoresForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    SAT = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': ' Your SAT Score'}),min_value=1000, max_value=1600)
    GPA = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Your GPA'}),min_value=2.5,max_value=4.0)

