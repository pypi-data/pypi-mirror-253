from typing import Optional

import requests

from core_models.utils import log_exception
from . import BaseVertoIntegration
from ..base_integration import BaseIntegrationParam, IntegrationError


class VertoFxTrade:
    def __init__(
            self, trade_id, reference, amount_from, amount_to, rate,
            transaction_state, client_reference, currency_from,
            currency_to
    ):
        self.id = trade_id
        self.reference = reference
        self.amount_from = amount_from
        self.amount_to = amount_to
        self.rate = rate
        self.transaction_state = transaction_state
        self.client_reference = client_reference
        self.currency_from = currency_from
        self.currency_to = currency_to


class VertoCreateFxTradeIntegrationParam(BaseIntegrationParam):

    def __init__(self, token, vfx_token, amount, reference):
        self.token = token
        self.vfx_token = vfx_token
        self.amount = amount
        self.reference = reference


class VertoCreateFxTradeIntegration(BaseVertoIntegration):
    def __init__(self, param: VertoCreateFxTradeIntegrationParam):
        super().__init__(param)

    def execute(self) -> Optional[VertoFxTrade]:
        url = f"{self.base_url}/orders/v2.1/fx"
        payload = {
          "vfx_token": self.param.vfx_token,
          "side": "SELL",
          "amount": float(self.param.amount),
          "clientReference": self.param.reference.replace('-', ''),
        }
        headers = {
            "Authorization": f"Bearer {self.param.token}"
        }
        try:
            resp = requests.post(url, json=payload, headers=headers)
            print("VertoCreateFxTradeIntegration", resp.text)
            if resp.ok:
                data = resp.json()
                if data['success']:
                    return VertoFxTrade(
                        trade_id=data['order']['id'],
                        reference=data['order']['reference'],
                        amount_from=data['order']['amountFrom'],
                        amount_to=data['order']['amountTo'],
                        rate=data['order']['rate'],
                        transaction_state=data['order']['transactionState'],
                        client_reference=data['order']['clientReference'],
                        currency_from=data['order']['currencyFrom'],
                        currency_to=data['order']['currencyTo'],
                    )
                else:
                    raise IntegrationError(
                        data.get(
                            "message",
                            "An unexpected error occurred, please try again"
                        )
                    )
            else:
                data = resp.json()
                raise IntegrationError(
                    data.get(
                        "message",
                        "An unexpected error occurred, please try again"
                    )
                )
        except Exception as ex:
            log_exception('VertoCreateFxTradeIntegration', ex)
            if type(ex) is IntegrationError:
                raise ex
            raise IntegrationError(
                "An unexpected error occurred, please try again"
            )
