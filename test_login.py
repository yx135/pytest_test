import pytest
import requests
import json
import yaml
import os
import allure

print(os.getcwd())
config_file = os.getcwd() + '/config.yaml'
login_file = os.getcwd() + '/login.yaml'

with open(config_file, 'r') as file:
    config_data = yaml.safe_load(file)
url = config_data['host'] + '/user/login'

with open(login_file, 'r') as file:
    login_data = yaml.safe_load(file)
login_nodes = {key: value for key, value in login_data.items() if key.startswith('login')}

def login(username,password):
    parm = {
        'username': username,
        'password': password
    }
    r = requests.post(url, json=parm)  # 修改这里，使用json
    print(r)
    j = r.json()  # 简化json解析
    print(j)
    return j

@allure.epic("开发平台接口")
@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录")
    @pytest.mark.parametrize('in_data', login_nodes.values()) 
    def test_login(self, in_data):
        print(in_data['data']['username'])
        username=in_data['data']['username']
        password=in_data['data']['password']
        assert_code=in_data['assert']['errorCode']['value']
        response=login(username,password)
        assert response['errorCode']==assert_code