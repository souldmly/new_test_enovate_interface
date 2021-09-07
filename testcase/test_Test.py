
import json

import pytest
import requests


def test_Test(env_config):
    url = env_config['host']['url']
    # 拼接请求URL
    params = {'channelId': 10}
    # 传参参数
    r = requests.get(url, params=params)
    # 发出get请求、传参
    r_dict = json.loads(r.text)
    # 将返回数据转为字典
    assert r_dict['message'] == '执行成功'
    # 断言判断结果是否正确


if __name__ == '__main__':
    pytest.main(["-s", "test_Test.py"])





