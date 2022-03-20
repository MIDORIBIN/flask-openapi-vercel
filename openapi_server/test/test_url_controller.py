# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestUrlController(BaseTestCase):
    """UrlController integration test stubs"""

    def test_get_image_for_url(self):
        """Test case for get_image_for_url

        urlを入力に、画像を出力する
        """
        query_string = [('url', 'url_example')]
        headers = { 
            'Accept': 'application/octet-stream',
        }
        response = self.client.open(
            '/url',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
