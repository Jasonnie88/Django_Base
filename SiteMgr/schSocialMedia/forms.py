from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['host','topic','name', 'content']
        exclude =['host', 'participants']


class CustomUserCreationForm(UserCreationForm):
    def __init__(self,  *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # for field in self.fields:
        #     #self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('mobile',)


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gender', 'hobies', 'instruction', 'mobile']

