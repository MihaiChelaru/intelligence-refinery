from django.shortcuts import render


def home(request):
    """
    View Function for home page of the site.
    :param request:
    :return:
    """
    return render(
        request, 'main/home.html', context={}
    )
