from django.forms import inlineformset_factory, modelformset_factory

from .models import Payments, InvoiceItem, Receipt

InvoiceItemFormset = inlineformset_factory(
    Payments, InvoiceItem, fields=["description", "amount"], extra=1, can_delete=True
)

InvoiceReceiptFormSet = inlineformset_factory(
    Payments,
    Receipt,
    fields=("amount_paid", "date_paid", "comment"),
    extra=0,
    can_delete=True,
)

Invoices = modelformset_factory(Payments, exclude=(), extra=4)
