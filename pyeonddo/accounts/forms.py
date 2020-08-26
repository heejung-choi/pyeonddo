from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from stores.models import Store
from .models import User

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
    category = forms.ChoiceField(
        choices=[("1", "음료"),
                 ("2", "아이스크림"),
                 ("3", "과자"),
                 ("4", "간편식사"),
                 ("5", "생활용품")],
        widget=forms.Select,
        label='선호상품',
        help_text='해당 할인 상품을 추천해드립니다.'
    )
    prefer_store = forms.ChoiceField(
        choices=[("1", "GS25"),
                 ("2", "CU"),
                 ("3", "이마트24"),
                 ("4", "세븐일레븐"),
                 ("5", "미니스톱")],
        widget=forms.Select,
        label='단골편의점',
        help_text='해당 지점의 이벤트를 안내해드립니다.'
    )         

    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ('username','password1','password2','name_kr','phone','category','prefer_store')
        widgets =(
            ''
        ) 

class CustomUserChangeForm(UserChangeForm):
    username =  forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={'title':'', 'readonly':'readonly'}
    ))
    phone = forms.CharField(
        label='휴대폰번호',
    )
    name_kr = forms.CharField(
        label='이름',
    )
    category = forms.ChoiceField(
        choices=[("1", "음료"),
                 ("2", "아이스크림"),
                 ("3", "과자"),
                 ("4", "간편식사"),
                 ("5", "생활용품")],
        widget=forms.Select,
        label='선호상품'
    )
    prefer_store = forms.ChoiceField(
        choices=[("1", "GS25"),
                 ("2", "CU"),
                 ("3", "이마트24"),
                 ("4", "세븐일레븐"),
                 ("5", "미니스톱")],
        widget=forms.Select,
        label='단골편의점',
    )  

    class Meta:
        model = get_user_model()
        fields = ('username','phone','name_kr','category','prefer_store')        

