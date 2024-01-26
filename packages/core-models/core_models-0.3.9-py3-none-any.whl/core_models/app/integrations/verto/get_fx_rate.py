from typing import Optional

import requests

from core_models.utils import log_exception
from . import BaseVertoIntegration
from ..base_integration import BaseIntegrationParam


class VertoRate:
    def __init__(self, token: str, rate: float, expiry: str):
        self.token = token
        self.rate = rate
        self.expiry = expiry

    def to_dict(self):
        return {
            "token": self.token,
            "rate": self.rate,
            "expiry": self.expiry,
        }


class VertoGetFxRateIntegrationParam(BaseIntegrationParam):

    def __init__(self, token, from_currency, to_currency):
        self.token = token
        self.from_currency = from_currency
        self.to_currency = to_currency


class VertoGetFxRateIntegration(BaseVertoIntegration):
    def __init__(self, param: VertoGetFxRateIntegrationParam):
        super().__init__(param)

    def execute(self) -> Optional[VertoRate]:
        url = f"{self.base_url}/orders/v2.1/fx"
        params = {
          "currencyFrom": self.param.from_currency,
          "currencyTo": self.param.to_currency,
        }
        headers = {
            "Authorization": f"Bearer {self.param.token}"
        }
        try:
            resp = requests.get(url, params=params, headers=headers)
            if resp.ok:
                data = resp.json()
                if data['success']:
                    return VertoRate(
                        token=data['vfx_token'],
                        rate=data['rate'],
                        expiry=data['expiry']
                    )
        except Exception as ex:
            log_exception('VertoGetFxRateIntegration', ex)
        return None
