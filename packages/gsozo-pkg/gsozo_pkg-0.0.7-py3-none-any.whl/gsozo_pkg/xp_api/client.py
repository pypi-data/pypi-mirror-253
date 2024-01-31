from ._investment_funds import InvestmentFunds
from ._onboarding_rede_customers import OnboardingRedeCustomers
from ._pension_funds import PensionFunds
from ._rede_advisors import RedeAdvisors
from ._rede_customer import RedeCustomer

import requests
import json

class Client():
    """
    Core methods to access xp api
    """
    def __init__(self, access_token):
        self.access_token = access_token

        self.investment_funds = InvestmentFunds(self)
        self.onboarding_rede_customers = OnboardingRedeCustomers(self)
        self.pension_funds = PensionFunds(self)
        self.rede_advisors = RedeAdvisors(self)
        self.rede_customer = RedeCustomer(self)


    def request(self, url, params={}, subscription_key="", token_type="Bearer"):
        r = requests.get(
            url="https://" + url,
            params=params,
            headers={
                "Authorization": "{} {}".format(token_type, self.access_token),
                "ocp-apim-subscription-key": subscription_key,
                "Host": "api.xpi.com.br",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
                "Accept": "application/json",
                "accept-language": "en-US,en-CA;q=0.9,en;q=0.8,hi-IN;q=0.7,hi;q=0.6",
            }
        )

        try:
            return json.loads(r.text)
        except Exception as e:
            print("Error at request to xp api")
            raise e
