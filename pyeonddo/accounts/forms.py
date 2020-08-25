from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
    )
    phone = forms.CharField(
        label='휴대폰번호',
    )
    name_kr = forms.CharField(
        label='이름',
    )
    category = forms.CharField(
        label='즐겨찾는 상품',
    )
    prefer_store = forms.CharField(
        label='즐겨찾는 매장',
    )         

    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ('username','password1','password2','name_kr','phone','category','prefer_store')

class CustomUserChangeForm(UserChangeForm):
    phone = forms.CharField(
        label='휴대폰번호',
    )
    name_kr = forms.CharField(
        label='이름',
    )
    category = forms.CharField(
        label='즐겨찾는 상품',
    )
    prefer_store = forms.CharField(
        label='즐겨찾는 매장',
    )  

    class Meta:
        model = get_user_model()
        fields = ('phone','name_kr','category','prefer_store','store')        

