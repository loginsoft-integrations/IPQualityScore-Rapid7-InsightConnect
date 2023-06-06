import insightconnect_plugin_runtime
from .schema import UrlLookupInput, UrlLookupOutput, Input, Output, Component
from icon_ipqualityscore.util.api import URL_ENDPOINT


class UrlLookup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='urlLookup',
            description=Component.DESCRIPTION,
            input=UrlLookupInput(),
            output=UrlLookupOutput())

    def run(self, params={}) -> dict:
        ud_strictness = params.get(Input.STRICTNESS)
        ud_fast = params.get(Input.FAST)
        additional_params = {
            'strictness': ud_strictness,
            'fast': ud_fast
        }
        domain_input = params.get(Input.URL)
        self.logger.info(f"[ACTION LOG] Getting information for Domain: {domain_input} \n")
        ud_params = {'url': domain_input, 'params': additional_params}
        response = self.connection.ipqs_client.ipqs_lookup(URL_ENDPOINT, ud_params)
        return response
