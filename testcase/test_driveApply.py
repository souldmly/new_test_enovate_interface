import json

import pytest
import requests

from testcase.conftest import env_config


def test_driveApply(env_config):
    url = env_config('driveApply.yml')['tests'][0]['http']['path']
    data = env_config('driveApply.yml')[0]['http']['parameters']
    response = requests.post(url, data=data)
    validate_response = json.loads(response)
    assert validate_response['message'] == '执行成功'


if __name__ == '__main__':
    pytest.main(['-s', 'test_driveApply.py'])