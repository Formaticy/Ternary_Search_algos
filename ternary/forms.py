from django import forms


class ElementSearchForm(forms.Form):
    arr = forms.CharField(max_length=255, label='Введите массив:', initial='')
    element = forms.CharField(max_length=255, label='Введите элемент:', initial='')


class ExtremumSearchForm(forms.Form):
    func = forms.CharField(max_length=255, label='Введите функцию:', initial='', required=True)
    left = forms.FloatField(label='Введите левую границу:', initial='', required=True)
    right = forms.FloatField(label='Введите правую границу:', initial='', required=True)
    eps = forms.FloatField(label='Введите эпсилон:', initial=10**(-6), required=True)
    mode_min = forms.BooleanField(required=False)
    mode_max = forms.BooleanField(required=False)

