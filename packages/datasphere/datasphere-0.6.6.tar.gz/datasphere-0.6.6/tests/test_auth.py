from unittest.mock import Mock
import re

import pytest

from datasphere.auth import create_iam_token
from yandex.cloud.iam.v1.iam_token_service_pb2 import CreateIamTokenRequest, CreateIamTokenResponse


def test_create_iam_token_with_sdk(mocker):
    def Create(req: CreateIamTokenRequest):  # noqa
        return CreateIamTokenResponse(iam_token=f'iam token for oauth token {req.yandex_passport_oauth_token}')

    stub = mocker.patch('datasphere.auth.IamTokenServiceStub')()
    stub.Create = Create

    assert create_iam_token('AQAD***') == 'iam token for oauth token AQAD***'


def test_create_iam_token_with_yc(mocker):
    yc_process = Mock()
    yc_process.stdout = """

You are going to be authenticated via federation-id 'team.example.federation'.
Your federation authentication web site will be opened.
After your successful authentication, you will be redirected to cloud console'.

Press 'enter' to continue...
t1.9eudm***
    """

    mocker.patch('subprocess.run', return_value=yc_process)

    assert create_iam_token(None) == 't1.9eudm***'


def test_get_iam_token_from_env(mocker):
    mocker.patch.dict('os.environ', {'YC_IAM_TOKEN': 'iam token'})
    assert create_iam_token(None) == 'iam token'


def test_error_no_yc(mocker):
    mocker.patch('subprocess.run', side_effect=FileNotFoundError)

    with pytest.raises(RuntimeError, match=re.escape(
            'You have not provided OAuth token. You have to install Yandex Cloud CLI '
            '(https://cloud.yandex.com/docs/cli/) to authenticate automatically.'
    )):
        create_iam_token(None)
