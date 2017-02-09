'''users provides the methods for chef user resources'''

from .base import Base


class Users(Base):
    '''
    Provides access to the chef `users` resource
    '''
    _base_url = '/users'

    @classmethod
    def index(cls):
        '''
        Fetches all of the users on the chef server

        :return: All the chef users with a url for each user
        :rtype: hash
        '''
        return super(Users, cls).index()

    @classmethod
    def get(cls, username):
        '''
        Fetches a user from the chef server

        :param username: The User's username
        :type username: string
        :return: The chef user
        :rtype: hash
        '''
        return super(Users, cls).get(username)

    @classmethod
    def create(cls, user):
        '''
        Creates a new chef user on the server

        The user hash should be in the form::

            {
                'username': <username>,
                'display_name': <display_name>,
                'first_name': <first name>,
                'middle_name': <middle name>, # optional
                'last_name': <last name>,
                'email': <email>,
                'password': <password>
            }

        :param user: The user to create
        :type user: hash
        :return: The username and url
        :rtype: hash
        '''
        return super(Users, cls).create(user)
