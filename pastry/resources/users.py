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
