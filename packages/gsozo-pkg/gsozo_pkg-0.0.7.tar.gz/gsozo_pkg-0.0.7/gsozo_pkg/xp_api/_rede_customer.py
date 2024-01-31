class RedeCustomer():
    """
    Access 'rede customers' api.
    Have some methods to direct access some endpoints.
    """

    def __init__(self, client):
        self.client = client
        self.base_url = 'api.xpi.com.br/rede-customer'
        self.subscription_key = 'b63f9758680845afb25dbd47a5e95c4a'


    def get_from_url(self, api_path, params={}):
        '''
        Get something from the url 'api.xpi.com.br/rede-customer'.
        You don't need to pass the base route, only the path for this api.
        The path must start with '/'.

        e.g.: get_from_url('/v2/customers/{customer_code}/positions', params)
        '''

        full_url = self.base_url + api_path
        return self.client.request(full_url, params, self.subscription_key)


    def get_customer_positions(self, xp_code, params={}):
        '''
        Get customer positions from xp api

        e.g.: get_customer_positions(
            123321,                     # Customer xp code. Can be string or int
            {
                'createCache': True      # We thing that this force xp api to cache this request
            }
        )
        '''
        return self.get_from_url(
            '/v2/customers/{}/positions'.format(str(xp_code)),
            params
        )
