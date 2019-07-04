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


class Error(object):
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
        'source': 'str',
        'description': 'str',
        'reason_code': 'str',
        'recoverable': 'bool'
    }

    attribute_map = {
        'source': 'source',
        'description': 'description',
        'reason_code': 'reasonCode',
        'recoverable': 'recoverable'
    }

    def __init__(self, source=None, description=None, reason_code=None, recoverable=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self._description = None
        self._reason_code = None
        self._recoverable = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if description is not None:
            self.description = description
        if reason_code is not None:
            self.reason_code = reason_code
        if recoverable is not None:
            self.recoverable = recoverable

    @property
    def source(self):
        """Gets the source of this Error.  # noqa: E501

        An element used to indicate the source of the issue causing this error. Must be one of   * 'MDES'  * 'INPUT'<br>   __Max Length: 32__   # noqa: E501

        :return: The source of this Error.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Error.

        An element used to indicate the source of the issue causing this error. Must be one of   * 'MDES'  * 'INPUT'<br>   __Max Length: 32__   # noqa: E501

        :param source: The source of this Error.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def description(self):
        """Gets the description of this Error.  # noqa: E501

        Description of the reason the operation failed. See API Response Errors <br> __Max Length: 256__   # noqa: E501

        :return: The description of this Error.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Error.

        Description of the reason the operation failed. See API Response Errors <br> __Max Length: 256__   # noqa: E501

        :param description: The description of this Error.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def reason_code(self):
        """Gets the reason_code of this Error.  # noqa: E501

        A reason code for the error that has occurred.<br> __Max Length: 100__   # noqa: E501

        :return: The reason_code of this Error.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this Error.

        A reason code for the error that has occurred.<br> __Max Length: 100__   # noqa: E501

        :param reason_code: The reason_code of this Error.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def recoverable(self):
        """Gets the recoverable of this Error.  # noqa: E501

        Generated by the gateway to indicate if the request could presented again for processing. Either \"TRUE\" or \"FALSE\"   # noqa: E501

        :return: The recoverable of this Error.  # noqa: E501
        :rtype: bool
        """
        return self._recoverable

    @recoverable.setter
    def recoverable(self, recoverable):
        """Sets the recoverable of this Error.

        Generated by the gateway to indicate if the request could presented again for processing. Either \"TRUE\" or \"FALSE\"   # noqa: E501

        :param recoverable: The recoverable of this Error.  # noqa: E501
        :type: bool
        """

        self._recoverable = recoverable

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
        if issubclass(Error, dict):
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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
