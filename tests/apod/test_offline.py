import unittest
from unittest import mock
from datetime import datetime
from apod import utility
import requests

class TestOfflineFallback(unittest.TestCase):
    @mock.patch('apod.utility.requests.get')
    def test_fallback_when_network_fails(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError()
        data = utility.parse_apod(datetime(2021, 1, 1))
        self.assertEqual(data['title'], 'Default Image')
        self.assertEqual(data['media_type'], 'image')

