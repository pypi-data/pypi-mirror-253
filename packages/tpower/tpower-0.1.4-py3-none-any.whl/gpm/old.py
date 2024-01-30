import aiohttp
import logging 
import requests 


class ASYNC_GPM:
    BASE_URL = 'https://webapisungrow.horizon.greenpowermonitor.com'

    def __init__(self, username, password):
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        self.credentials = {
            'username': username,
            'password': password
        }

    async def authenticate(self):
        async with aiohttp.ClientSession() as session:
            url = self.BASE_URL + '/api/Account/Token'
            async with session.post(url, headers=self.headers, json=self.credentials) as response:
                if response.status == 200:
                    res = await response.json()
                    self.headers['Authorization'] = 'Bearer ' + res['AccessToken']
                else:
                    logging.error(f'[GPM]: Failed to authenticate user. Status code: {response.status}')

    async def make_api_call(self, endpoint, data):
        url = self.BASE_URL + endpoint
        async with aiohttp.ClientSession() as session:
            try:
                if endpoint == '/api/Account/Token':
                    response = await session.post(url, headers=self.headers, json=data)
                else:
                    response = await session.get(url, headers=self.headers, params=data)

                if response.status == 200:
                    return await response.json()
                else:
                    logging.error(f'[GPM]: Failed to make API call: {response.status}')
                    return None
            except Exception as e:
                logging.error(f'[GPM]: Exception in API call: {e}')
                return None

    async def get_data_list(self, datasources, start_date, end_date, grouping='minute', granularity=1):
        params = {
                'startDate': start_date,
                'endDate': end_date,
                'grouping': grouping,
                'granularity': granularity,
        }
        params['dataSourceIds'] = ','.join(map(str, datasources))
        return await self.make_api_call('/api/DataList/v2', params)
               
    async def get_data_list_in_batches(self, datasources, start_date, end_date, grouping='minute', granularity=1):
        batches = [datasources[i:i + 10] for i in range(0, len(datasources), 10)]
        tasks = [self.get_data_list(batch, start_date, end_date, grouping=grouping, granularity=granularity) for batch in batches]
        results = await asyncio.gather(*tasks)
        
        combined = []
        for result in results:
            combined.extend(result)
        return combined