from .tasks import test_func
from django.http import HttpResponse
# Create your views here.
def test(request):

    # this is actual calling of celery function
    test_func.delay()

    return HttpResponse("Done final")
