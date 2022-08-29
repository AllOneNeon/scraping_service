from django import forms



class FindForm(forms.Form):
    city = forms.ModelChoiceField(initial='class')


