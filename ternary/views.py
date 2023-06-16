from django.shortcuts import render

from .algorithms.ternarySearch_element import *
from .algorithms.ternarySearch_extremum import *
from .forms import ElementSearchForm, ExtremumSearchForm


# Create your views here.

def first_page(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def extremum_search(request):
    if request.method == 'POST':
        submitionButton = request.POST.get('submit')
        form = ExtremumSearchForm(request.POST)
        if form.is_valid():
            func = form.cleaned_data.get('func')
            left = form.cleaned_data.get('left')
            right = form.cleaned_data.get('right')
            eps = form.cleaned_data.get('eps')
            mode_min = form.cleaned_data.get('mode_min')
            mode_max = form.cleaned_data.get('mode_max')

            f = eval('lambda x: ' + func) # унимодальная функция

            if mode_min:
                if eps == 0:
                    result = ternarySearchExtrMin_int(f, left, right)
                else:
                    result = ternarySearchExtrMin_real(f, left, right, eps)
            elif mode_max:
                if eps == 0:
                    result = ternarySearchExtrMax_int(f, left, right)
                else:
                    result = ternarySearchExtrMax_real(f, left, right, eps)
            else:
                result = 'выберите min или max'

        context = {'form': form, 'result': result, 'submitionButton': submitionButton}
        return render(request, 'extremum_search.html', context)
    else:
        form = ExtremumSearchForm()
        return render(request, 'extremum_search.html', {'form': form})


def element_search_d(request):
    if request.method == 'POST':
        submitionButton = request.POST.get('submit')
        form = ElementSearchForm(request.POST)
        arr = ''
        element = ''
        result = ''
        if form.is_valid():

            arr = form.cleaned_data.get('arr').split(' ')
            arr = list(map(int, arr))
            element = int(form.cleaned_data.get('element'))
            if arr[0] > arr[1]:
                result = ternary_search_decrease(arr, element)
            else:
                result = ternary_search_increase(arr, element)

        context = {'form': form, 'result': result, 'submitionButton': submitionButton}
        return render(request, 'element_search.html', context)
    else:
        form = ElementSearchForm()
        return render(request, 'element_search.html', {'form': form})
