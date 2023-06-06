import insightconnect_plugin_runtime
from .schema import EmailLookupInput, EmailLookupOutput, Input, Output, Component
from icon_ipqualityscore.util.api import EMAIL_ENDPOINT


class EmailLookup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='emailLookup',
            description=Component.DESCRIPTION,
            input=EmailLookupInput(),
            output=EmailLookupOutput())

    def run(self, params={}) -> dict:
        email_input = params.get(Input.EMAILADDRESS)
        abuse_strictness = params.get(Input.ABUSE_STRICTNESS)
        fast = params.get(Input.FAST)
        timeout = params.get(Input.TIMEOUT)
        suggest_domain = params.get(Input.SUGGEST_DOMAIN)
        additional_params = {
                        'abuse_strictness': abuse_strictness,
                        'fast': fast,
                        'timeout': timeout,
                        'suggest_domain': suggest_domain
        }
        email_params = {'email': email_input, 'params': additional_params}
        self.logger.info(f"[ACTION LOG] Getting information for Email address: {email_input} \n")
        response = self.connection.ipqs_client.ipqs_lookup(EMAIL_ENDPOINT, email_params)
        return response
