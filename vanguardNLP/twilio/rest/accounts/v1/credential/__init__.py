# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.accounts.v1.credential.aws import AwsList
from twilio.rest.accounts.v1.credential.public_key import PublicKeyList


class CredentialList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the CredentialList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.accounts.v1.credential.CredentialList
        :rtype: twilio.rest.accounts.v1.credential.CredentialList
        """
        super(CredentialList, self).__init__(version)

        # Path Solution
        self._solution = {}

        # Components
        self._public_key = None
        self._aws = None

    @property
    def public_key(self):
        """
        Access the public_key

        :returns: twilio.rest.accounts.v1.credential.public_key.PublicKeyList
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyList
        """
        if self._public_key is None:
            self._public_key = PublicKeyList(self._version)
        return self._public_key

    @property
    def aws(self):
        """
        Access the aws

        :returns: twilio.rest.accounts.v1.credential.aws.AwsList
        :rtype: twilio.rest.accounts.v1.credential.aws.AwsList
        """
        if self._aws is None:
            self._aws = AwsList(self._version)
        return self._aws

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.CredentialList>'


class CredentialPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the CredentialPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.accounts.v1.credential.CredentialPage
        :rtype: twilio.rest.accounts.v1.credential.CredentialPage
        """
        super(CredentialPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CredentialInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.accounts.v1.credential.CredentialInstance
        :rtype: twilio.rest.accounts.v1.credential.CredentialInstance
        """
        return CredentialInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.CredentialPage>'


class CredentialInstance(InstanceResource):
    """  """

    def __init__(self, version, payload):
        """
        Initialize the CredentialInstance

        :returns: twilio.rest.accounts.v1.credential.CredentialInstance
        :rtype: twilio.rest.accounts.v1.credential.CredentialInstance
        """
        super(CredentialInstance, self).__init__(version)

        # Context
        self._context = None
        self._solution = {}

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.CredentialInstance>'
