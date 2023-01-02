from django.contrib.messages.views import SuccessMessageMixin

class OperationSuccessMessageViewMixin(SuccessMessageMixin):
    success_message = "Operacja została pomyślnie zakończona."
