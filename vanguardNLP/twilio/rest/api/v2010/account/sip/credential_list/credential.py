# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class CredentialList(ListResource):
    """  """

    def __init__(self, version, account_sid, credential_list_sid):
        """
        Initialize the CredentialList

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param credential_list_sid: The credential_list_sid

        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialList
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialList
        """
        super(CredentialList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'credential_list_sid': credential_list_sid}
        self._uri = '/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams CredentialInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'])

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists CredentialInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CredentialInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size})

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return CredentialPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CredentialInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CredentialPage(self._version, response, self._solution)

    def create(self, username, password):
        """
        Create a new CredentialInstance

        :param unicode username: The username
        :param unicode password: The password

        :returns: Newly created CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        data = values.of({'Username': username, 'Password': password})

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return CredentialInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            credential_list_sid=self._solution['credential_list_sid'],
        )

    def get(self, sid):
        """
        Constructs a CredentialContext

        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        """
        return CredentialContext(
            self._version,
            account_sid=self._solution['account_sid'],
            credential_list_sid=self._solution['credential_list_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a CredentialContext

        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        """
        return CredentialContext(
            self._version,
            account_sid=self._solution['account_sid'],
            credential_list_sid=self._solution['credential_list_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CredentialList>'


class CredentialPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the CredentialPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The account_sid
        :param credential_list_sid: The credential_list_sid

        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialPage
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialPage
        """
        super(CredentialPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CredentialInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        return CredentialInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            credential_list_sid=self._solution['credential_list_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CredentialPage>'


class CredentialContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, credential_list_sid, sid):
        """
        Initialize the CredentialContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param credential_list_sid: The credential_list_sid
        :param sid: The sid

        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        """
        super(CredentialContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'credential_list_sid': credential_list_sid, 'sid': sid}
        self._uri = '/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a CredentialInstance

        :returns: Fetched CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return CredentialInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            credential_list_sid=self._solution['credential_list_sid'],
            sid=self._solution['sid'],
        )

    def update(self, password=values.unset):
        """
        Update the CredentialInstance

        :param unicode password: The password

        :returns: Updated CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        data = values.of({'Password': password})

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return CredentialInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            credential_list_sid=self._solution['credential_list_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the CredentialInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.CredentialContext {}>'.format(context)


class CredentialInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid, credential_list_sid,
                 sid=None):
        """
        Initialize the CredentialInstance

        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        super(CredentialInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'credential_list_sid': payload['credential_list_sid'],
            'username': payload['username'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'uri': payload['uri'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'credential_list_sid': credential_list_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CredentialContext for this CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        """
        if self._context is None:
            self._context = CredentialContext(
                self._version,
                account_sid=self._solution['account_sid'],
                credential_list_sid=self._solution['credential_list_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def credential_list_sid(self):
        """
        :returns: The credential_list_sid
        :rtype: unicode
        """
        return self._properties['credential_list_sid']

    @property
    def username(self):
        """
        :returns: The username
        :rtype: unicode
        """
        return self._properties['username']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a CredentialInstance

        :returns: Fetched CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        return self._proxy.fetch()

    def update(self, password=values.unset):
        """
        Update the CredentialInstance

        :param unicode password: The password

        :returns: Updated CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        return self._proxy.update(password=password)

    def delete(self):
        """
        Deletes the CredentialInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.CredentialInstance {}>'.format(context)
