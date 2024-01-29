import logging
import traceback
import uuid
from collections import namedtuple
from random import randint

from django.conf import settings

from core_models import constants

MailAttachment = namedtuple('MailAttachment', ['name', 'content', 'mime'])


def log_exception(source: str, exception: Exception):
    """
    To log exception to console
    usage: log_exception(MyClass, exception_object)
    
    :param source: 
    :param exception: 
    :return: 
    """
    traceback.print_exc()
    logger = logging.getLogger(source)
    logger.exception(exception)


def random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.lower()     # Make all characters uppercase.
    random = random.replace("-", "")    # Remove the UUID '-'.
    return random[0:string_length]  # Return the random string.


def random_numbers(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def send_invoice_update_to_seller(invoice, request=None):
    from .app import notification_manager
    emails = list(invoice.seller_company.users.values_list('email', flat=True))
    print(f"Sending invoice update mailto {emails}")
    notification_manager.send_mail(
        subject=f"Your invoice #{invoice.reference}'s status has changed",
        template_dir='seller-invoice',
        to=emails,
        context_dict={
            "invoice": invoice,
            "action_url": f"{settings.SELLER_VIEW_INVOICE_PAGE_URL}"
                          f"/{invoice.id}"
        },
        request=request
    )
    print(f"Invoice update mail sent to {emails}")


def send_contract_feedback_mail_to_seller(contract, log, request=None):
    from .app import notification_manager
    emails = list(contract.seller_company.users.values_list('email', flat=True))
    print(f"Sending contract feedback mail from {contract.buyer.email} to "
          f"{emails}")
    if contract.status == constants.ACCEPTED_CONTRACT_STATUS:
        subject = 'Liquify Contract Accepted'
    else:
        subject = '[Action Required] Liquify Contract Feedback'
    notification_manager.send_mail(
        subject=subject,
        template_dir='contract',
        to=emails,
        context_dict={
            "log": log,
            "contract": contract,
            "action_url": f"{settings.VIEW_CONTRACT_PAGE_URL}/{contract.id}",
            "CONTRACT_CONFIRMED_NOTIF_TYPE":
                constants.CONTRACT_CONFIRMED_NOTIF_TYPE,
            "MODIFY_CONTRACT_STATUS":
                constants.MODIFY_CONTRACT_STATUS,
            "REJECTED_CONTRACT_STATUS":
                constants.REJECTED_CONTRACT_STATUS,
            "ACCEPTED_CONTRACT_STATUS":
                constants.ACCEPTED_CONTRACT_STATUS,
        },
        request=request
    )
    print(f"Contract feedback mail from {contract.buyer.email} sent to "
          f"{contract.seller.email}")

