import mock
import unittest

from pastry.resources.base import Base


class BaseTestCase(unittest.TestCase):

    def test_base_url(self):
        Base._base_url = 'url'
        self.assertEqual(Base.base_url(), 'url')
        Base._base_url = None
        self.assertRaises(ValueError, Base.base_url)

    @mock.patch('pastry.resources.base.Base.base_url', return_value='url')
    @mock.patch('pastry.resources.base.PastryClient')
    def test_index(self, pastry_client, base_url):
        pastry_client.call.return_value = 'result'
        self.assertEqual(Base.index(), 'result')
        pastry_client.call.assert_called_with('url')

    @mock.patch('pastry.resources.base.Base.base_url', return_value='url')
    @mock.patch('pastry.resources.base.PastryClient')
    def test_get(self, pastry_client, base_url):
        pastry_client.call.return_value = 'result'
        self.assertEqual(Base.get('instance'), 'result')
        pastry_client.call.assert_called_with('url/instance')

    @mock.patch('pastry.resources.base.Base.base_url', return_value='url')
    @mock.patch('pastry.resources.base.PastryClient')
    def test_create(self, pastry_client, base_url):
        pastry_client.call.return_value = 'result'
        self.assertEqual(Base.create({}), 'result')
        pastry_client.call.assert_called_with('url', method='POST', data={})

    @mock.patch('pastry.resources.base.Base.base_url', return_value='url')
    @mock.patch('pastry.resources.base.PastryClient')
    def test_delete(self, pastry_client, base_url):
        pastry_client.call.return_value = 'result'
        self.assertEqual(Base.delete('instanceid'), 'result')
        pastry_client.call.assert_called_with('url/instanceid', method='DELETE')
