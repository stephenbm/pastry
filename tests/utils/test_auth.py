import mock
import unittest

from pastry.utils import auth


class AuthTestCase(unittest.TestCase):

    @mock.patch('pastry.utils.auth.encode', return_value='encoded')
    @mock.patch('pastry.utils.auth.sha1')
    def test_hashencode(self, sha1, encode):
        self.assertEqual(auth.hashencode('content'), 'encoded')
        sha1.assert_called_with('content')

    @mock.patch('pastry.utils.auth.b64encode')
    def test_encode(self, b64encode):
        expected = [
            u'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij',
            u'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij',
            u'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij',
            u'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij',
            u'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij'
        ]
        b64encode.return_value = ''.join('abcdefghij' * 30)
        self.assertEqual(auth.encode('hashed'), expected)

    @mock.patch('pastry.utils.auth.encode')
    @mock.patch('pastry.utils.auth.sign', return_value='signature')
    def test_authorization_headers(self, sign, encode):
        encode.return_value = ['part1', 'part2', 'part3']
        expected_result = {
            'X-ops-authorization-1': 'part1',
            'X-ops-authorization-2': 'part2',
            'X-ops-authorization-3': 'part3'
        }
        with mock.patch('pastry.utils.auth.open', mock.mock_open(read_data='key')):
            self.assertEqual(
                auth.authorization_headers('keypath', 'canonical_source'),
                expected_result
            )
