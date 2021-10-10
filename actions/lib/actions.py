"""Base module for Meraki pack"""
from st2common.runners.base_action import Action
import meraki
# import os

__all__ = [
    'BaseMerakiAction'
]


class BaseMerakiAction(Action):
    """ Base Action for Meraki pack"""

    def __init__(self, config=None, action_service=None):
        super(BaseMerakiAction, self).__init__(
            config=config, action_service=action_service)

        self.host = self.config['Host'].strip('/')
        self.base_path = self.config['BasePath'].strip('/')
        self._dashboard = meraki.DashboardAPI

    def merakiconnector(self, api_key=None, api_debug=False):
        """Default connector for Meraki Dashboard"""
        dashboard = self._dashboard(api_key=api_key,
                                    base_url=f"https://{self.host}/{self.base_path}/",
                                    print_console=api_debug
                                    )
        return dashboard
