import insightconnect_plugin_runtime
from .schema import PhoneLookupInput, PhoneLookupOutput, Input, Output, Component
from icon_ipqualityscore.util.api import PHONE_ENDPOINT


class PhoneLookup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='phoneLookup',
                description=Component.DESCRIPTION,
                input=PhoneLookupInput(),
                output=PhoneLookupOutput())

    def run(self, params={}) -> dict:

        phone_input = params.get(Input.PHONE)
        p_strictness = params.get(Input.STRICTNESS)
        try: 
            p_country = params.get(Input.COUNTRY)
        except ValueError:
            p_country = ""
        p_additional_params = {
            'strictness': p_strictness,
            'country': p_country

            }
        phone_params = {'phone': phone_input, 'params': p_additional_params}
        self.logger.info(f"[ACTION LOG] Getting information for Phone: {phone_input} \n")
        response = self.connection.ipqs_client.ipqs_lookup(PHONE_ENDPOINT, phone_params)
        return response

