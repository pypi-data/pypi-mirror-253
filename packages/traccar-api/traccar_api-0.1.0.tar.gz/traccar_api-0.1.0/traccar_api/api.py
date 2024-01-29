from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

from traccar_api.traccar_errors.traccar_api_errors import *


class TraccarApi:
    def __init__(self, traccar_api_url: str, traccar_api_mail: str, traccar_api_pass: str):
        self.__traccar_api_url = traccar_api_url
        self.__traccar_api_mail = traccar_api_mail
        self.__traccar_api_pass = traccar_api_pass
        self.__traccar_api_session = None
        self.__traccar_api_session = requests.Session()
        self.__traccar_api_token = None

    def get_traccar_api_url(self):
        return self.__traccar_api_url

    def get_traccar_api_mail(self):
        return self.__traccar_api_mail

    def get_traccar_api_pass(self):
        return self.__traccar_api_pass

    def get_traccar_api_token(self):
        return self.__traccar_api_token

    def set_traccar_api_url(self, traccar_api_url: str) -> None:
        self.__traccar_api_url = traccar_api_url

    def set_traccar_api_mail(self, traccar_api_mail: str) -> None:
        self.__traccar_api_mail = traccar_api_mail

    def set_traccar_api_pass(self, traccar_api_pass: str) -> None:
        self.__traccar_api_pass = traccar_api_pass

    def set_traccar_api_token(self, token: str) -> None:
        self.__traccar_api_token = token

    def login(self):
        login_url = f"{self.__traccar_api_url}/api/session"
        self.__traccar_api_session.auth = HTTPBasicAuth(self.__traccar_api_mail, self.__traccar_api_pass)
        login_data = {
            'email': self.__traccar_api_mail,
            'password': self.__traccar_api_pass
        }
        try:
            response = self.__traccar_api_session.post(login_url, data=login_data)

            if response.status_code == 200:
                print('Login successful')
                cookies = self.__traccar_api_session.cookies.get_dict()
                self.set_traccar_api_token(cookies['JSESSIONID'])
                return response.json()
            else:
                raise TraccarApiAuthenticationError(
                    "Authentication failed",
                    status_code=response.status_code,
                    response_body=response.text,
                    details="Check username and password"
                )
        except requests.exceptions.RequestException as e:
            raise TraccarApiError(f"Request failed: {str(e)}")

    def logout(self):
        logout_url = f"{self.__traccar_api_url}/api/session"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.delete(logout_url)
                response.raise_for_status()

                print('Logout successful')
                self.__traccar_api_session.cookies.clear()
                self.__traccar_api_session.close()

                self.__traccar_api_session = None
                self.set_traccar_api_token(None)

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 401:
                    raise TraccarApiAuthenticationError(
                        "Failed to logout due to authentication issue",
                        status_code=e.response.status_code,
                        response_body=e.response.text
                    )
                else:
                    raise TraccarApiError(
                        "Failed to logout",
                        status_code=e.response.status_code,
                        response_body=e.response.text
                    )
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Request failed during logout: {str(e)}")
        else:
            raise TraccarApiError("Error: No session established for logout.")

    def get_devices(self):
        url = f"{self.__traccar_api_url}/api/devices"
        if self.__traccar_api_session is not None:
            try:
                response = self.__traccar_api_session.get(url)
                response.raise_for_status()

                return response.json()

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 401:
                    raise TraccarApiAuthenticationError(
                        "Authentication error, please login again",
                        status_code=e.response.status_code,
                        response_body=e.response.text
                    )
                else:
                    raise TraccarApiError(
                        "Failed to retrieve devices",
                        status_code=e.response.status_code,
                        response_body=e.response.text
                    )
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Request failed: {str(e)}")
        else:
            raise TraccarApiError("Session not established. Please login to continue.")

    def get_device(self, *, device_ids=None, device_unique_ids=None, user_id=None):
        url = f"{self.__traccar_api_url}/api/devices"
        params = {}

        if user_id:
            params['userId'] = user_id
        if device_ids:
            params['id'] = device_ids
        if device_unique_ids:
            params['uniqueId'] = device_unique_ids

        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url, params=params)
                response.raise_for_status()

                return response.json()

            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve device: {str(e)}")

        else:
            raise TraccarApiError("Error: Missing session for get_device.")

    def get_users(self):
        url = f"{self.__traccar_api_url}/api/users"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve user: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_users.")

    def get_user(self, user_id):
        url = f"{self.__traccar_api_url}/api/users/{user_id}"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve user: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_user.")

    def get_server(self):
        url = f"{self.__traccar_api_url}/api/server"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve server info: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_server.")

    def get_drivers(self, *, device_ids: list = None, user_id: int = None, group_ids: list = None,
                    refresh: bool = None):
        url = f"{self.__traccar_api_url}/api/drivers"
        params = {}
        if user_id:
            params['userId'] = user_id
        if device_ids:
            params['id'] = device_ids
        if group_ids:
            params['groupId'] = group_ids
        if refresh is not None:
            params['refresh'] = refresh
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url, params=params)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve drivers: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_drivers.")

    def get_driver(self, driver_id):
        url = f"{self.__traccar_api_url}/api/drivers/{driver_id}"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve driver: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_driver.")

    def get_groups(self, *, user_ids: list = None):
        url = f"{self.__traccar_api_url}/api/groups"
        params = {}
        if user_ids is not None:
            params['user_ids'] = user_ids
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url, params=params)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve groups: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_groups.")

    def get_group(self, group_id):
        url = f"{self.__traccar_api_url}/api/groups/{group_id}"

        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve group: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_group.")

    def test_error(self):
        url = f"{self.__traccar_api_url}/api/permissions"
        if self.__traccar_api_session is not None:
            response = self.__traccar_api_session.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f'ERROR: {response.status_code} - {response.text}')
                return []
        else:
            print(f'Error: missing session')
            return None

    def get_current_user_resources(self):
        groups = self.get_groups()
        devices = self.get_devices()
        users = self.get_users()
        drivers = self.get_drivers()

        return {
            'groups': groups,
            'devices': devices,
            'users': users,
            'drivers': drivers
        }

    def link_device_user(self, *, device_id, user_id):
        url = f"{self.__traccar_api_url}/api/permissions"
        params = {"userId": user_id, "deviceId": str(device_id)}
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.post(url, headers={'Content-Type': 'application/json'},
                                                           json=params)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to link device to user: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for link_device_user.")

    def unlink_device_user(self, *, device_id, user_id):
        url = f"{self.__traccar_api_url}/api/permissions"
        params = {"userId": user_id, "deviceId": str(device_id)}
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.delete(url, headers={'Content-Type': 'application/json'},
                                                             json=params)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to unlink device from user: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for unlink_device_user.")

    def link_driver_device(self, *, driver_id, device_id):
        url = f"{self.__traccar_api_url}/api/permissions"
        params = {"deviceId": str(device_id), "driverId": driver_id}
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.post(url, headers={'Content-Type': 'application/json'},
                                                           json=params)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to link driver to device: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for link_driver_device.")

    def unlink_driver_device(self, *, driver_id, device_id):
        url = f"{self.__traccar_api_url}/api/permissions"
        params = {"deviceId": str(device_id), "driverId": driver_id}
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.delete(url, headers={'Content-Type': 'application/json'},
                                                             json=params)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to unlink driver from device: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for unlink_driver_device.")

    def update_device(self, device: dict):
        url = f'{self.__traccar_api_url}/api/devices/{device["id"]}'
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.put(url, headers={'Content-Type': 'application/json'},
                                                          json=device)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to update device: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for update_device.")

    def create_device(self, device: dict):
        url = f"{self.__traccar_api_url}/api/devices"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.post(url, headers={'Content-Type': 'application/json'},
                                                           json=device)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to create device: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for create device.")

    def delete_device(self, device: dict):
        url = f"{self.__traccar_api_url}/api/devices/{device['id']}"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.delete(url)
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 401:
                    raise TraccarApiAuthenticationError(
                        "Failed to delete device due to authentication issue",
                        status_code=e.response.status_code,
                        response_body=e.response.text
                    )
                else:
                    raise TraccarApiError(
                        "Failed to delete device",
                        status_code=e.response.status_code,
                        response_body=e.response.text
                    )
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Request failed during delete device: {str(e)}")
        else:
            raise TraccarApiError("Error: No session established for delete_device.")

    def update_driver(self, driver: dict):
        url = f'{self.__traccar_api_url}/api/drivers/{driver["id"]}'
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.put(url, headers={'Content-Type': 'application/json'},
                                                          json=driver)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to update driver: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for update_driver.")

    def delete_driver(self, driver: dict):
        url = f"{self.__traccar_api_url}/api/drivers/{driver['id']}"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.delete(url)
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 401:
                    raise TraccarApiAuthenticationError(
                        "Failed to delete driver due to authentication issue",
                        status_code=e.response.status_code,
                        response_body=e.response.text
                    )
                else:
                    raise TraccarApiError(
                        "Failed to delete driver",
                        status_code=e.response.status_code,
                        response_body=e.response.text
                    )
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Request failed during delete driver: {str(e)}")
        else:
            raise TraccarApiError("Error: No session established for delete_driver.")

    def create_driver(self, driver: dict):
        url = f"{self.__traccar_api_url}/api/drivers"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.post(url, headers={'Content-Type': 'application/json'},
                                                           json=driver)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to create driver: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for create_driver.")

    def create_group(self, group: dict):
        url = f"{self.__traccar_api_url}/api/groups"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.post(url, headers={'Content-Type': 'application/json'},
                                                           json=group)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to create group: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for create_group.")

    def delete_group(self, group: dict):
        url = f"{self.__traccar_api_url}/api/drivers/{group['id']}"
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.delete(url)
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 401:
                    raise TraccarApiAuthenticationError(
                        "Failed to delete group due to authentication issue",
                        status_code=e.response.status_code,
                        response_body=e.response.text
                    )
                else:
                    raise TraccarApiError(
                        "Failed to delete group",
                        status_code=e.response.status_code,
                        response_body=e.response.text
                    )
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Request failed during delete group: {str(e)}")
        else:
            raise TraccarApiError("Error: No session established for delete_group.")

    def update_group(self, group: dict):
        url = f'{self.__traccar_api_url}/api/groups/{group["id"]}'
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.put(url, headers={'Content-Type': 'application/json'},
                                                          json=group)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to update group: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for update_group.")

    def get_positions(self, *, device_id: int = None, from_date: datetime = None, to_date: datetime = None):
        url = f"{self.__traccar_api_url}/api/positions"
        params = {}
        if device_id:
            params['deviceId'] = device_id
        if from_date:
            params['from'] = from_date.isoformat().replace('+00:00', 'Z')
        if to_date:
            params['to'] = to_date.isoformat().replace('+00:00', 'Z')
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url, params=params)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve positions: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_positions.")

    def get_latest_position(self, *, device_id: int = None):
        url = f"{self.__traccar_api_url}/api/positions"
        params = {}
        if device_id:
            params['deviceId'] = device_id

        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url, params=params)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve drivers: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_drivers.")

    def delete_positions(self, *, device_id: int, from_date: datetime, to_date: datetime):
        url = f"{self.__traccar_api_url}/api/positions"
        params = {
            'deviceId': device_id,
            'from': from_date.isoformat(),
            'to': to_date.isoformat()
        }
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.delete(url, params=params)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to delete positions: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_positions.")

    def get_statistics(self, *, from_date: datetime, to_date: datetime):
        url = f"{self.__traccar_api_url}/api/statistics"
        params = {
            'from': from_date.isoformat(),
            'to': to_date.isoformat()
        }
        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url, params=params)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve statistics: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_statistics.")

    def get_ports(self, *, port_ids: list = None):
        url = f"{self.__traccar_api_url}/api/ports"
        params = {}
        if port_ids:
            params['id'] = port_ids

        if self.__traccar_api_session:
            try:
                response = self.__traccar_api_session.get(url, params=params)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                raise TraccarApiError(f"Failed to retrieve ports: {str(e)}")
        else:
            raise TraccarApiError("Error: Missing session for get_ports.")
