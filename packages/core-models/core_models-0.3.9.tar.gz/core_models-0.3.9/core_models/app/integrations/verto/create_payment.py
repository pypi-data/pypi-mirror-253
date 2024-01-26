from typing import Optional

import requests

from core_models.utils import log_exception
from . import BaseVertoIntegration
from ..base_integration import BaseIntegrationParam


class VertoCreatePaymentIntegrationParam(BaseIntegrationParam):

    def __init__(self, token, beneficiary_id, purpose_id, amount,
                 wallet_id, reference, payment_id):
        self.token = token
        self.beneficiary_id = beneficiary_id
        self.purpose_id = purpose_id
        self.amount = amount
        self.wallet_id = wallet_id
        self.reference = reference
        self.payment_id = payment_id


class VertoCreatePaymentIntegration(BaseVertoIntegration):
    def __init__(self, param: VertoCreatePaymentIntegrationParam):
        super().__init__(param)

    def execute(self) -> tuple:
        url = f"{self.base_url}/profile/v2.2/request"
        payload = {
          "beneficiaryId": self.param.beneficiary_id,
          "purposeId": self.param.purpose_id,
          "amount": float(self.param.amount),
          "walletId": self.param.wallet_id,
          "clientReference": self.param.reference,
          "paymentId": self.param.payment_id
        }
        headers = {
            "Authorization": f"Bearer {self.param.token}"
        }
        try:
            resp = requests.post(url, json=payload, headers=headers)
            print("VertoCreatePaymentIntegration", resp.text)
            if resp.ok:
                data = resp.json()
                if data['success']:
                    return True, data['payment']
            return False, resp.text
        except Exception as ex:
            log_exception('VertoCreatePaymentIntegration', ex)
        return False, None
