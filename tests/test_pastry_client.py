import mock
import unittest

from pastry.pastry_client import PastryClient


class PastryClientTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PastryClient._server = None
        PastryClient._organization = None
        PastryClient._client = None
        PastryClient._keypath = None

    def test_initialize(self):
        PastryClient.initialize('server', 'organization', 'client', 'keypath')
        self.assertEqual(PastryClient._server, 'server')
        self.assertEqual(PastryClient._organization, 'organization')
        self.assertEqual(PastryClient._client, 'client')
        self.assertEqual(PastryClient._keypath, 'keypath')

    @mock.patch('pastry.pastry_client.PastryClient.initialize')
    def test_get_url(self, init):
        self.assertEqual((None, 'endpoint'), PastryClient.get_url('endpoint'))

    @mock.patch('pastry.pastry_client.requests')
    @mock.patch('pastry.pastry_client.signed_headers')
    @mock.patch('pastry.pastry_client.PastryClient.get_url')
    def test_call(self, get_url, signed_headers, requests):
        get_url.return_value = ('server', 'path')
        signed_headers.return_value = 'headers'
        PastryClient.call('endpoint')
        requests.get.assert_called_with('serverpath', headers='headers', verify=PastryClient.verify)
