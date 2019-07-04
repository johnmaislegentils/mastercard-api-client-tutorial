# coding: utf-8

"""
    MDES for Merchants

    The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java)   # noqa: E501

    OpenAPI spec version: 1.2.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PhoneNumber(object):
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
        'country_dial_in_code': 'float',
        'phone_number': 'float'
    }

    attribute_map = {
        'country_dial_in_code': 'countryDialInCode',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, country_dial_in_code=None, phone_number=None):  # noqa: E501
        """PhoneNumber - a model defined in Swagger"""  # noqa: E501

        self._country_dial_in_code = None
        self._phone_number = None
        self.discriminator = None

        if country_dial_in_code is not None:
            self.country_dial_in_code = country_dial_in_code
        if phone_number is not None:
            self.phone_number = phone_number

    @property
    def country_dial_in_code(self):
        """Gets the country_dial_in_code of this PhoneNumber.  # noqa: E501

        __(OPTIONAL)__ The country code for the phone number. E.g. 1 for US or 44 for UK.<br> __Max Length: 4__   # noqa: E501

        :return: The country_dial_in_code of this PhoneNumber.  # noqa: E501
        :rtype: float
        """
        return self._country_dial_in_code

    @country_dial_in_code.setter
    def country_dial_in_code(self, country_dial_in_code):
        """Sets the country_dial_in_code of this PhoneNumber.

        __(OPTIONAL)__ The country code for the phone number. E.g. 1 for US or 44 for UK.<br> __Max Length: 4__   # noqa: E501

        :param country_dial_in_code: The country_dial_in_code of this PhoneNumber.  # noqa: E501
        :type: float
        """

        self._country_dial_in_code = country_dial_in_code

    @property
    def phone_number(self):
        """Gets the phone_number of this PhoneNumber.  # noqa: E501

        __(OPTIONAL)__ The phone number of the account holder <br>  __Max Length: 20__   # noqa: E501

        :return: The phone_number of this PhoneNumber.  # noqa: E501
        :rtype: float
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this PhoneNumber.

        __(OPTIONAL)__ The phone number of the account holder <br>  __Max Length: 20__   # noqa: E501

        :param phone_number: The phone_number of this PhoneNumber.  # noqa: E501
        :type: float
        """

        self._phone_number = phone_number

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
        if issubclass(PhoneNumber, dict):
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
        if not isinstance(other, PhoneNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
