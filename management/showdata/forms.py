from django import forms 
from .models import applyleave


class leaveform(forms.ModelForm):
    class Meta:
        model = applyleave
        fields = ['leave','holidayfrom','holidayto','detail']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['leave'].widget.attrs.update({'class':'selection'})
        self.fields['holidayfrom'].widget.attrs.update({'type':'date'})
        self.fields['detail'].widget.attrs.update({'class':'form-control','placeholder':'Discription','id':'validationTextarea','rows':'5'})
