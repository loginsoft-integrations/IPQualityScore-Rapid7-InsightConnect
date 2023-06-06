import insightconnect_plugin_runtime
from .schema import IpLookupInput, IpLookupOutput, Input, Output, Component
from icon_ipqualityscore.util.api import IP_ENDPOINT


class IpLookup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='ipLookup',
            description=Component.DESCRIPTION,
            input=IpLookupInput(),
            output=IpLookupOutput())

    def run(self, params={}) -> dict:
        ip_input = params.get(Input.IPADDRESS)
        ip_strictness = params.get(Input.STRICTNESS)
        try:
            ip_user_agent = params.get(Input.USER_AGENT)
        except ValueError:
            ip_strictness = ""
        try:
            ip_user_language = params.get(Input.USER_LANGUAGE)
        except ValueError:
            ip_user_language = ""
        ip_fast = params.get(Input.FAST)
        ip_mobile = params.get(Input.MOBILE)
        ip_allow_public_access_points = params.get(Input.ALLOW_PUBLIC_ACCESS_POINTS)
        ip_lighter_penalties = params.get(Input.LIGHTER_PENALTIES)
        ip_additional_params = {
            'strictness': ip_strictness,
            'user_agent': ip_user_agent,
            'user_language': ip_user_language,
            'fast': ip_fast,
            'mobile': ip_mobile,
            'allow_public_access_points': ip_allow_public_access_points,
            'lighter_penalties': ip_lighter_penalties
        }
        self.logger.info(f"[ACTION LOG] Getting information for IP address: {ip_input} \n")
        ip_params = {'ip': ip_input, 'params': ip_additional_params}
        response = self.connection.ipqs_client.ipqs_lookup(IP_ENDPOINT, ip_params)
        return response
