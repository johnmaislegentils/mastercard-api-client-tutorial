# coding: utf-8

"""
    MDES for Merchants

    The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously.    # noqa: E501

    OpenAPI spec version: 1.2.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SuspendRequestSchema(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'response_host': 'str',
        'request_id': 'str',
        'payment_app_instance_id': 'str',
        'token_unique_references': 'list[str]',
        'caused_by': 'str',
        'reason': 'str',
        'reason_code': 'str'
    }

    attribute_map = {
        'response_host': 'responseHost',
        'request_id': 'requestId',
        'payment_app_instance_id': 'paymentAppInstanceId',
        'token_unique_references': 'tokenUniqueReferences',
        'caused_by': 'causedBy',
        'reason': 'reason',
        'reason_code': 'reasonCode'
    }

    def __init__(self, response_host=None, request_id=None, payment_app_instance_id=None, token_unique_references=None, caused_by=None, reason=None, reason_code=None):  # noqa: E501
        """SuspendRequestSchema - a model defined in Swagger"""  # noqa: E501

        self._response_host = None
        self._request_id = None
        self._payment_app_instance_id = None
        self._token_unique_references = None
        self._caused_by = None
        self._reason = None
        self._reason_code = None
        self.discriminator = None

        if response_host is not None:
            self.response_host = response_host
        self.request_id = request_id
        if payment_app_instance_id is not None:
            self.payment_app_instance_id = payment_app_instance_id
        self.token_unique_references = token_unique_references
        self.caused_by = caused_by
        if reason is not None:
            self.reason = reason
        self.reason_code = reason_code

    @property
    def response_host(self):
        """Gets the response_host of this SuspendRequestSchema.  # noqa: E501

        The host that originated the request. Future calls in the same conversation may be routed to this host.   # noqa: E501

        :return: The response_host of this SuspendRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._response_host

    @response_host.setter
    def response_host(self, response_host):
        """Sets the response_host of this SuspendRequestSchema.

        The host that originated the request. Future calls in the same conversation may be routed to this host.   # noqa: E501

        :param response_host: The response_host of this SuspendRequestSchema.  # noqa: E501
        :type: str
        """

        self._response_host = response_host

    @property
    def request_id(self):
        """Gets the request_id of this SuspendRequestSchema.  # noqa: E501

        Unique identifier for the request.   # noqa: E501

        :return: The request_id of this SuspendRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this SuspendRequestSchema.

        Unique identifier for the request.   # noqa: E501

        :param request_id: The request_id of this SuspendRequestSchema.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def payment_app_instance_id(self):
        """Gets the payment_app_instance_id of this SuspendRequestSchema.  # noqa: E501

        Identifier for the specific Mobile Payment App instance, unique across a given Wallet Identifier. This value cannot be changed after digitization. This field is alphanumeric and additionally web-safe base64 characters per RFC 4648 (minus \"-\", underscore \"_\") up to a maximum length of 48, = should not be URL encoded. Conditional - not applicable for server based tokens but required otherwise.     __Max Length:48__   # noqa: E501

        :return: The payment_app_instance_id of this SuspendRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._payment_app_instance_id

    @payment_app_instance_id.setter
    def payment_app_instance_id(self, payment_app_instance_id):
        """Sets the payment_app_instance_id of this SuspendRequestSchema.

        Identifier for the specific Mobile Payment App instance, unique across a given Wallet Identifier. This value cannot be changed after digitization. This field is alphanumeric and additionally web-safe base64 characters per RFC 4648 (minus \"-\", underscore \"_\") up to a maximum length of 48, = should not be URL encoded. Conditional - not applicable for server based tokens but required otherwise.     __Max Length:48__   # noqa: E501

        :param payment_app_instance_id: The payment_app_instance_id of this SuspendRequestSchema.  # noqa: E501
        :type: str
        """

        self._payment_app_instance_id = payment_app_instance_id

    @property
    def token_unique_references(self):
        """Gets the token_unique_references of this SuspendRequestSchema.  # noqa: E501

        The specific Token to be suspended. Array of more or more valid references as assigned by MDES    # noqa: E501

        :return: The token_unique_references of this SuspendRequestSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._token_unique_references

    @token_unique_references.setter
    def token_unique_references(self, token_unique_references):
        """Sets the token_unique_references of this SuspendRequestSchema.

        The specific Token to be suspended. Array of more or more valid references as assigned by MDES    # noqa: E501

        :param token_unique_references: The token_unique_references of this SuspendRequestSchema.  # noqa: E501
        :type: list[str]
        """
        if token_unique_references is None:
            raise ValueError("Invalid value for `token_unique_references`, must not be `None`")  # noqa: E501

        self._token_unique_references = token_unique_references

    @property
    def caused_by(self):
        """Gets the caused_by of this SuspendRequestSchema.  # noqa: E501

        Who or what caused the Token to be suspended. Must be either the 'CARDHOLDER' (operation requested by the Cardholder) or 'TOKEN_REQUESTOR' (operation requested by the token requestor).     __Max Length:64__   # noqa: E501

        :return: The caused_by of this SuspendRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._caused_by

    @caused_by.setter
    def caused_by(self, caused_by):
        """Sets the caused_by of this SuspendRequestSchema.

        Who or what caused the Token to be suspended. Must be either the 'CARDHOLDER' (operation requested by the Cardholder) or 'TOKEN_REQUESTOR' (operation requested by the token requestor).     __Max Length:64__   # noqa: E501

        :param caused_by: The caused_by of this SuspendRequestSchema.  # noqa: E501
        :type: str
        """
        if caused_by is None:
            raise ValueError("Invalid value for `caused_by`, must not be `None`")  # noqa: E501

        self._caused_by = caused_by

    @property
    def reason(self):
        """Gets the reason of this SuspendRequestSchema.  # noqa: E501

        Free form reason why the Tokens are being suspended.     __Max Length:256__   # noqa: E501

        :return: The reason of this SuspendRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this SuspendRequestSchema.

        Free form reason why the Tokens are being suspended.     __Max Length:256__   # noqa: E501

        :param reason: The reason of this SuspendRequestSchema.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def reason_code(self):
        """Gets the reason_code of this SuspendRequestSchema.  # noqa: E501

        The reason for the action to be suspended. Must be one of 'SUSPECTED_FRAUD' (suspected fraudulent token transactions), 'OTHER' (Other - default used if value not provided).     __Max Length:64__   # noqa: E501

        :return: The reason_code of this SuspendRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this SuspendRequestSchema.

        The reason for the action to be suspended. Must be one of 'SUSPECTED_FRAUD' (suspected fraudulent token transactions), 'OTHER' (Other - default used if value not provided).     __Max Length:64__   # noqa: E501

        :param reason_code: The reason_code of this SuspendRequestSchema.  # noqa: E501
        :type: str
        """
        if reason_code is None:
            raise ValueError("Invalid value for `reason_code`, must not be `None`")  # noqa: E501

        self._reason_code = reason_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SuspendRequestSchema, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SuspendRequestSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
