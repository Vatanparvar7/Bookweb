
from django import forms
from .models import Comments,FeedModel
class CommentForm(forms.ModelForm):
    comments = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment here!',
            'rows': 4,
            'cols': 50
        }))

    class Meta:
        model = Comments
        fields = ['comments']

class BookCreateForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter book name',
        }))
    title = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            "rows":6,
            'placeholder': 'You descreption your book',
        }))
    image = forms.ImageField(label="Book image choose", widget=forms.FileInput(
        attrs={

        }))
    file = forms.FileField(label="Book file choose ", widget=forms.FileInput(
        attrs={
        }))

    class Meta:
        model = FeedModel
        fields = ['name','title','image','file']

class ExampleForm(forms.Form):
    CHOISES=[
        (1,''),
    ]
    num1=forms.ChoiceField(required=False,choices=CHOISES,widget=forms.RadioSelect(attrs={
        # 'class':'num',
        # 'value':1,
    }))
    num2=forms.ChoiceField(required=False,choices=CHOISES,widget=forms.RadioSelect(attrs={
        # 'class':'num',
        # 'value':1,
    }))
    num3=forms.ChoiceField(required=False,choices=CHOISES,widget=forms.RadioSelect(attrs={
        # 'class':'num',
        # 'value':1,
    }))
    num4=forms.ChoiceField(required=False,choices=CHOISES,widget=forms.RadioSelect(attrs={
        # 'class':'num',
        # 'value':1,
    }))
    num5=forms.ChoiceField(required=False,choices=CHOISES,widget=forms.RadioSelect(attrs={
        # 'class':'num',
        # 'value':1,
    }))
    comments = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            
        }))
class ExampleForms(forms.ModelForm):
    CHOISES=[
        (1,None),
    ]
    num1=forms.ChoiceField(required=False,choices=CHOISES,widget=forms.RadioSelect(attrs={
        # 'class':'num',
        # 'value':1,
    }))
    num2=forms.ChoiceField(required=False,choices=CHOISES,widget=forms.RadioSelect(attrs={
        # 'class':'num',
        # 'value':1,
    }))
    num3=forms.ChoiceField(required=False,choices=CHOISES,widget=forms.RadioSelect(attrs={
        # 'class':'num',
        # 'value':1,
    }))
    num4=forms.ChoiceField(required=False,choices=CHOISES,widget=forms.RadioSelect(attrs={
        # 'class':'num',
        # 'value':1,
    }))
    num5=forms.ChoiceField(required=False,choices=CHOISES,widget=forms.RadioSelect(attrs={
        # 'class':'num',
        # 'value':1,
    }))
    comments = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            
        }))
    class Meta:
        model = Comments
        fields = ['comments']