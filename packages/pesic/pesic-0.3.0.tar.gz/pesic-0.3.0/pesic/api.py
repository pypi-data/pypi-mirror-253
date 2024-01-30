from typing import Optional, Sequence
import logging
import os
from aiohttp import ClientSession
from .custom_exceptions import CredentialsError, UnsupportedMeterType, UnsupportedArgumentError
from .const import API_BASE, API_AUTH, API_GROUPS, API_ACCOUNTS

LOGLEVEL = os.environ.get('PESIC_LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)
_LOGGER = logging.getLogger(__name__)

class PESClient:
    """Wrapper around the PetroElectroSbyt API"""

    def __init__(self, username: str, password: str,  session=None):
        """Create a new REST API Client"""
        self._username = username
        self._password = password
        self._headers = {
                'accept-encoding': 'gzip',
                'content-type': 'application/json'
        }
        self.session = session
        self._token = None

    def get_session(self):
        return self.session or ClientSession()

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()

    async def request(self, method: str, endpoint: str,  data: dict = None):
        """Perform a request against the specified parameters."""
        if self._token is None:
            self._token = await self.get_token()
        headers = self._headers
        headers["Authorization"] = f"Bearer {self._token}"
        url = f"{API_BASE}{endpoint}"
        session = self.get_session()
        async with session.request(method, url, headers=headers, json=data) as response:
            result = await response.json(content_type=None)
            return result

    async def get(self, endpoint: str):
        """Perform a get request."""
        return await self.request("get", endpoint)

    async def get_token(self):
        """Fetch token logic."""
        headers = {'Accept': 'application/json, text/plain, */*', 'Captcha': 'none','Content-Type': 'application/json'}
        data = {'type': 'PHONE', 'login': self._username, 'password': self._password}
        url = f"{API_BASE}{API_AUTH}"
        session = self.get_session()
        async with session.post(url, headers=headers, json=data) as response:
            response.raise_for_status()
            result = await response.json()
        if type(result) == dict and result.get('code') == '3':
            raise CredentialsError("Wrong username or password")
        else:
            _LOGGER.debug(f"Got new token: { result['auth']}")
            return result['auth']

    async def post(self, endpoint: str, data: Optional[Sequence]):
        """Perform a post request."""
        return await self.request("post", endpoint, data=data)
    
    async def get_groups(self):
        """Get all groups."""
        result = await self.get(endpoint=API_GROUPS)
        _LOGGER.debug(f"Called '{API_GROUPS}' endpoint, got: {result}")
        return result

    async def get_accounts(self):
        """Get all accounts."""
        result = await self.get(endpoint=API_ACCOUNTS)
        _LOGGER.debug(f"Called '{API_ACCOUNTS}' endpoint, got: {result}")
        return result
    
    async def get_group_accounts(self, group_id: int):
        """Get all accounts for specific group."""
        endpoint = f'/v5/groups/{group_id}/accounts'
        result = await self.get(endpoint=endpoint)
        _LOGGER.debug(f"Called '{endpoint}' endpoint, got: {result}")
        return result

    async def get_account_details(self, account_id: int):
        """Get account details for specific account id."""
        endpoint = f'{API_ACCOUNTS}/{account_id}/details'
        result = await self.get(endpoint=endpoint)
        _LOGGER.debug(f"Called '{endpoint}' endpoint, got: {result}")
        return result

    async def get_meters_info(self, account_id: int):
        """Get meter(s) details for specific account id."""
        endpoint = f'{API_ACCOUNTS}/{account_id}/meters/info'
        result = await self.get(endpoint=endpoint)
        _LOGGER.debug(f"Called '{endpoint}' endpoint, got: {result}")
        return result
    
    async def set_meters_reading(self, account_id: int, readings: list):
        """Send meter readings."""
        meter_info = await self.get_meters_info(account_id=account_id)
        meter_id = meter_info[0].get('id').get('registration')
        indications = meter_info[0].get('indications')
        valid_scales = ['День', 'Ночь', 'Круглосуточный']
        current_readings = {}
        data = []
        for indication in indications:
            scale_name = indication.get('scaleName')
            if scale_name not in valid_scales:
                raise UnsupportedMeterType(f"Got wrong meter type. Updating '{scale_name}' currently not supported")
            else:
                scale_id = indication['meterScaleId']
                scale_reading = indication['previousReading']
                current_readings[scale_id] = int(scale_reading)
        if len(readings) != len(current_readings):
            raise UnsupportedArgumentError(f"Meters count mismatch. Updating '{len(current_readings)}' meter(s) with '{len(readings)}' value(s) not allowed")
        for reading in readings:
            reading_id = reading['scale_id']
            reading_value = reading['scale_value']
            if current_readings.get(reading_id) is None:
                raise UnsupportedArgumentError(f"Meter scale with id '{reading_id}' not found.")
            if reading_value <= current_readings[reading_id]:
                raise UnsupportedArgumentError(f"Reading value must be greater then current reading. Current reading '{current_readings[reading_id]}', got '{reading_value}' as a new value.")
            data.append({'scaleId': reading_id, 'value': reading_value})
        endpoint = f'{API_ACCOUNTS}/{account_id}/meters/{meter_id}/reading'
        await self.post(endpoint=endpoint, data=data)