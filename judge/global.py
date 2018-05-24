from django.conf import settings
def global_setting(request):
    return {
        'ONPAGE':settings.ONPAGE
    }