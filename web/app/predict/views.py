from django.shortcuts import render


def index(request):

    if request.method == 'POST':
        print(request.POST.get('int1', ''))

    context = {'data': 'this is predict app'}
    return render(request, 'predict/index.html', context)
