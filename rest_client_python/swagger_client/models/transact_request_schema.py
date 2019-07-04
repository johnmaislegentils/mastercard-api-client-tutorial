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


class TransactRequestSchema(object):
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
        'token_unique_reference': 'str',
        'dsrp_type': 'str',
        'unpredictable_number': 'str',
        'amount': 'str',
        'currency_code': 'str'
    }

    attribute_map = {
        'response_host': 'responseHost',
        'request_id': 'requestId',
        'token_unique_reference': 'tokenUniqueReference',
        'dsrp_type': 'dsrpType',
        'unpredictable_number': 'unpredictableNumber',
        'amount': 'amount',
        'currency_code': 'currencyCode'
    }

    def __init__(self, response_host=None, request_id=None, token_unique_reference=None, dsrp_type=None, unpredictable_number=None, amount=None, currency_code=None):  # noqa: E501
        """TransactRequestSchema - a model defined in Swagger"""  # noqa: E501

        self._response_host = None
        self._request_id = None
        self._token_unique_reference = None
        self._dsrp_type = None
        self._unpredictable_number = None
        self._amount = None
        self._currency_code = None
        self.discriminator = None

        if response_host is not None:
            self.response_host = response_host
        self.request_id = request_id
        self.token_unique_reference = token_unique_reference
        self.dsrp_type = dsrp_type
        self.unpredictable_number = unpredictable_number
        if amount is not None:
            self.amount = amount
        if currency_code is not None:
            self.currency_code = currency_code

    @property
    def response_host(self):
        """Gets the response_host of this TransactRequestSchema.  # noqa: E501

        The host that originated the request. Future calls in the same conversation may be routed to this host.   # noqa: E501

        :return: The response_host of this TransactRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._response_host

    @response_host.setter
    def response_host(self, response_host):
        """Sets the response_host of this TransactRequestSchema.

        The host that originated the request. Future calls in the same conversation may be routed to this host.   # noqa: E501

        :param response_host: The response_host of this TransactRequestSchema.  # noqa: E501
        :type: str
        """

        self._response_host = response_host

    @property
    def request_id(self):
        """Gets the request_id of this TransactRequestSchema.  # noqa: E501

        Unique identifier for the request.   # noqa: E501

        :return: The request_id of this TransactRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this TransactRequestSchema.

        Unique identifier for the request.   # noqa: E501

        :param request_id: The request_id of this TransactRequestSchema.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def token_unique_reference(self):
        """Gets the token_unique_reference of this TransactRequestSchema.  # noqa: E501

        Globally unique identifier for the Token, as assigned by MDES.    __Max Length:64__   # noqa: E501

        :return: The token_unique_reference of this TransactRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._token_unique_reference

    @token_unique_reference.setter
    def token_unique_reference(self, token_unique_reference):
        """Sets the token_unique_reference of this TransactRequestSchema.

        Globally unique identifier for the Token, as assigned by MDES.    __Max Length:64__   # noqa: E501

        :param token_unique_reference: The token_unique_reference of this TransactRequestSchema.  # noqa: E501
        :type: str
        """
        if token_unique_reference is None:
            raise ValueError("Invalid value for `token_unique_reference`, must not be `None`")  # noqa: E501

        self._token_unique_reference = token_unique_reference

    @property
    def dsrp_type(self):
        """Gets the dsrp_type of this TransactRequestSchema.  # noqa: E501

        What type of DSRP cryptogram to create. Must be either UCAF or M_CHIP.     __Max Length:64__   # noqa: E501

        :return: The dsrp_type of this TransactRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._dsrp_type

    @dsrp_type.setter
    def dsrp_type(self, dsrp_type):
        """Sets the dsrp_type of this TransactRequestSchema.

        What type of DSRP cryptogram to create. Must be either UCAF or M_CHIP.     __Max Length:64__   # noqa: E501

        :param dsrp_type: The dsrp_type of this TransactRequestSchema.  # noqa: E501
        :type: str
        """
        if dsrp_type is None:
            raise ValueError("Invalid value for `dsrp_type`, must not be `None`")  # noqa: E501

        self._dsrp_type = dsrp_type

    @property
    def unpredictable_number(self):
        """Gets the unpredictable_number of this TransactRequestSchema.  # noqa: E501

        HEX Encoded data (case sensitive) provided by the merchant to provide variability and uniqueness to the generation of a cryptogram.  __Length:8__   # noqa: E501

        :return: The unpredictable_number of this TransactRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._unpredictable_number

    @unpredictable_number.setter
    def unpredictable_number(self, unpredictable_number):
        """Sets the unpredictable_number of this TransactRequestSchema.

        HEX Encoded data (case sensitive) provided by the merchant to provide variability and uniqueness to the generation of a cryptogram.  __Length:8__   # noqa: E501

        :param unpredictable_number: The unpredictable_number of this TransactRequestSchema.  # noqa: E501
        :type: str
        """
        if unpredictable_number is None:
            raise ValueError("Invalid value for `unpredictable_number`, must not be `None`")  # noqa: E501

        self._unpredictable_number = unpredictable_number

    @property
    def amount(self):
        """Gets the amount of this TransactRequestSchema.  # noqa: E501

        Transaction amount to be authorized. Note that refund transactions are not supported � this value must be a positive amount and can contain up to 12 digits, inclusive of any digits in the currency exponent.     __Max Length:13__   # noqa: E501

        :return: The amount of this TransactRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactRequestSchema.

        Transaction amount to be authorized. Note that refund transactions are not supported � this value must be a positive amount and can contain up to 12 digits, inclusive of any digits in the currency exponent.     __Max Length:13__   # noqa: E501

        :param amount: The amount of this TransactRequestSchema.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def currency_code(self):
        """Gets the currency_code of this TransactRequestSchema.  # noqa: E501

        The transaction currency. Expressed as a 3-character ISO 4217 currency code.   # noqa: E501

        :return: The currency_code of this TransactRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this TransactRequestSchema.

        The transaction currency. Expressed as a 3-character ISO 4217 currency code.   # noqa: E501

        :param currency_code: The currency_code of this TransactRequestSchema.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

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
        if issubclass(TransactRequestSchema, dict):
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
        if not isinstance(other, TransactRequestSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
