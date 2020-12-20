from . models import Absence
from django import forms

class Absence(forms.ModelForm):
    
    date=forms.CharField(label='التاريح',widget=forms.DateInput(attrs={'class':'form-control w-25','type':"date"}))
    time=forms.CharField(label='التوقيت',widget=forms.TimeInput(attrs={'class':'form-control w-25','type':"time",
    'value':"13:45:00"}))
    
    class Meta:
        model=Absence
        fields=('name_student','Excuse','Reason')
        widgets={
            'Reason':forms.Textarea(attrs={'class':'form-control rounded-0','rows':'4','style':'width:300px;'}) ,
             }