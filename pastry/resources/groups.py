'''groups provides the methods for chef group resources'''

from .base import Base


class Groups(Base):
    '''
    Provides access to the chef `groups` resource
    '''
    _base_url = '/organizations/%(org)s/groups'

    @classmethod
    def index(cls):
        '''
        Fetches all of the groups on the chef server

        :return: All the chef groups with a url for each group
        :rtype: hash
        '''
        return super(Groups, cls).index()

    @classmethod
    def get(cls, groupname):
        '''
        Fetches a group from the chef server

        :param groupname: The Group's name
        :type groupname: string
        :return: The chef group and members
        :rtype: hash
        '''
        return super(Groups, cls).get(groupname)

    @classmethod
    def create(cls, groupname):
        '''
        Creates a new chef group on the server

        :param groupname: The name of the group to create
        :type groupname: string
        :return: The groupname and url
        :rtype: hash
        '''
        return super(Groups, cls).create(groupname)

    @classmethod
    def delete(cls, groupname):
        '''
        Deletes a group from the chef server

        :param groupname: The Group's groupname
        :type usename: string
        :return: The deleted group's name
        :rtype: hash
        '''
        return super(Groups, cls).delete(groupname)
