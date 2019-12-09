from django.contrib.auth.models import User
from django_filters import FilterSet,CharFilter,NumberFilter
from django import forms
from django.contrib.auth.models import User,Group
from django_filters import ModelMultipleChoiceFilter

from django_filters import FilterSet
from .models import Shop
class ShopFilter(FilterSet):
    거래처코드 = CharFilter(lookup_expr='icontains')
    거래처명 = CharFilter(lookup_expr='icontains')
    내용 = CharFilter(lookup_expr='icontains')
    # 생성시간 = NumberFilter(field_name = '생성시간', lookup_expr = 'year')
    # groups = ModelMultipleChoiceFilter(
    #     queryset = Group.objects.all(),       # 필터링 데이터
    #     widget = forms.CheckboxSelectMultiple # 필터링 방법(CheckBox)
    #     )

    class Meta:
        model = Shop
        fields = ['거래처코드', '거래처명', '생성시간','수정시간','내용']