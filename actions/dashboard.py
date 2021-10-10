"""Device Manager Database Add module"""
from lib.actions import BaseMerakiAction
from meraki.exceptions import APIError

__all__ = [
    'Dashboard'
]


class Dashboard(BaseMerakiAction):
    """Default Organizations action class"""

    def run(self, **kwargs):
        """
        Default organization action method.
        :api_key: key used to authenticate
        :api_debug: bool used to show package debug
        :api_module: meraki module to use
        :api_method: module method to use
        """

        api_key = kwargs.pop("api_key")
        api_debug = kwargs.pop("api_debug")
        api_module = kwargs.pop("api_module")
        self.logger.debug(f"Python Module : {api_module}")
        api_method = kwargs.pop("api_method")
        self.logger.debug(f"Python Method : {api_method}")
        api_payload = kwargs.pop("api_payload")
        parameters = {}
        if api_payload:
            parameters = {k: v for k, v in api_payload.items() if v is not None}

        dash = self.merakiconnector(api_key=api_key, api_debug=api_debug)
        call = getattr(getattr(dash, api_module), api_method)

        try:
            response = call(**parameters)
            return (True, response)
        except APIError as err:
            error = {
                "message": err.message,
                "operation": err.operation,
                "reason": err.reason,
                "status": err.status,
                "tag": err.tag,
            }
            return (False, error)
