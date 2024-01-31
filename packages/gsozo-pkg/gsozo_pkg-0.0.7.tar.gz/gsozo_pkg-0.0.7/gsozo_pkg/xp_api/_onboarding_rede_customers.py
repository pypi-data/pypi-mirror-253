class OnboardingRedeCustomers():
    """
    Access 'onboarding rede customers' api.
    Have some methods to direct access some endpoints.
    """

    def __init__(self, client):
        self.client = client
        self.base_url = 'api.xpi.com.br/onboarding-rede-customers'
        self.subscription_key = 'aaa32b63cff04fc2aa6c4324fcd06583'


    def get_from_url(self, api_path, params={}):
        '''
        Get something from the url 'api.xpi.com.br/onboarding-rede-customers'.
        You don't need to pass the base route, only the path for this api.
        The path must start with '/'.

        e.g.: get_from_url('/api/v1/rede/customer/details/code/{customer_code}', params)
        '''

        full_url = self.base_url + api_path
        return self.client.request(full_url, params, self.subscription_key)


    def get_customer_details(self, xp_code, params={}):
        '''
        Get customer wallet from xp api

        e.g.: get_customer_details(
            123321,             # Customer xp code. Can be string or int
            params              # A dict with other params (not full mapped yet)
        )
        '''
        return self.get_from_url(
            '/api/v1/rede/customer/details/code/{}'.format(str(xp_code)),
            params
        )
