from django.conf import settings
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

# This is just a dummy app to ensure Django is actually used
settings.configure(
    DEBUG=True,
    SECRET_KEY='dummy-key-for-testing',
    ROOT_URLCONF=__name__,
)

if __name__ == '__main__':
    print("Django version:", settings.VERSION) 