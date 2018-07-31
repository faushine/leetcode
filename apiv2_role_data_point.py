import json

import requests


class Constant:
    url = 'https://api-data-stg.morningstar.com/dataapi/v2'
    headers = {
        'X-API-UserId': 'F915B38D-BA0F-45BF-A528-DAB67F9AD23E',
        'X-API-ProductId': 'APICenterV2User',
        'ApiKey': 'X0ryekOTDh5nx3E18P2XxP7r7KYtpVGp',
        "Content-Type": "application/json"
    }


class Role:
    url = '/roles/'

    def roles(self):
        response = requests.get(Constant.url + self.url, headers=Constant.headers)
        return response.json()['roles']


class DataPointGroup:
    url = '/roles/{0}/dataPointGroups'

    def groups(self, role_id):
        response = requests.get((Constant.url + self.url).format(role_id), headers=Constant.headers)
        return response.json()['datapointGroups']


class DataPoint:
    url = '/dataPointGroups/{0}/dataPoints?typeId=2'

    def data_points(self, group_id):
        response = requests.get((Constant.url + self.url).format(group_id), headers=Constant.headers)
        if response.ok:
            return response.json()['datapoints']
        else:
            return None


if __name__ == '__main__':
    roles = Role().roles()
    role_list = []
    for role in roles:
        role_obj = {
            'roleId': role['id'],
            'roleName': role['name']
        }
        data_points = []
        data_point_keys = []
        groups = DataPointGroup().groups(role['id'])
        for group in groups:
            dps = DataPoint().data_points(group['id'])
            if dps is not None:
                for dp in dps:
                    if dp['id'] not in data_point_keys:
                        data_point_keys.append(dp['id'])
                        data_points.append(dp)
        role_obj['dataPoints'] = sorted(data_points, key=lambda x: x['id'])
        role_list.append(role_obj)
    with open('./response.json', 'wb') as f:
        f.write(json.dumps(role_list).encode())
