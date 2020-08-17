# coding: utf-8

"""
    MDES for Merchants

    The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java)   # noqa: E501

    The version of the OpenAPI document: 1.2.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class DecisioningData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'recommendation': 'str',
        'recommendation_algorithm_version': 'str',
        'device_score': 'str',
        'account_score': 'str',
        'recommendation_reasons': 'list[str]',
        'device_current_location': 'str',
        'device_ip_address': 'str',
        'mobile_number_suffix': 'str',
        'account_id_hash': 'str'
    }

    attribute_map = {
        'recommendation': 'recommendation',
        'recommendation_algorithm_version': 'recommendationAlgorithmVersion',
        'device_score': 'deviceScore',
        'account_score': 'accountScore',
        'recommendation_reasons': 'recommendationReasons',
        'device_current_location': 'deviceCurrentLocation',
        'device_ip_address': 'deviceIpAddress',
        'mobile_number_suffix': 'mobileNumberSuffix',
        'account_id_hash': 'accountIdHash'
    }

    def __init__(self, recommendation=None, recommendation_algorithm_version=None, device_score=None, account_score=None, recommendation_reasons=None, device_current_location=None, device_ip_address=None, mobile_number_suffix=None, account_id_hash=None, local_vars_configuration=None):  # noqa: E501
        """DecisioningData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._recommendation = None
        self._recommendation_algorithm_version = None
        self._device_score = None
        self._account_score = None
        self._recommendation_reasons = None
        self._device_current_location = None
        self._device_ip_address = None
        self._mobile_number_suffix = None
        self._account_id_hash = None
        self.discriminator = None

        if recommendation is not None:
            self.recommendation = recommendation
        if recommendation_algorithm_version is not None:
            self.recommendation_algorithm_version = recommendation_algorithm_version
        if device_score is not None:
            self.device_score = device_score
        if account_score is not None:
            self.account_score = account_score
        if recommendation_reasons is not None:
            self.recommendation_reasons = recommendation_reasons
        if device_current_location is not None:
            self.device_current_location = device_current_location
        if device_ip_address is not None:
            self.device_ip_address = device_ip_address
        if mobile_number_suffix is not None:
            self.mobile_number_suffix = mobile_number_suffix
        if account_id_hash is not None:
            self.account_id_hash = account_id_hash

    @property
    def recommendation(self):
        """Gets the recommendation of this DecisioningData.  # noqa: E501

        __(OPTIONAL)__ <br> Digitization decision recommended by the Token Requestor. Must be either APPROVED (Recommend a decision of Approved), DECLINED (Recommend a decision of Decline). <br>   __Max Length:64__   # noqa: E501

        :return: The recommendation of this DecisioningData.  # noqa: E501
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """Sets the recommendation of this DecisioningData.

        __(OPTIONAL)__ <br> Digitization decision recommended by the Token Requestor. Must be either APPROVED (Recommend a decision of Approved), DECLINED (Recommend a decision of Decline). <br>   __Max Length:64__   # noqa: E501

        :param recommendation: The recommendation of this DecisioningData.  # noqa: E501
        :type: str
        """

        self._recommendation = recommendation

    @property
    def recommendation_algorithm_version(self):
        """Gets the recommendation_algorithm_version of this DecisioningData.  # noqa: E501

        __(OPTIONAL)__ <br> Version of the algorithm used by the Token Requestor to determine its recommendation. Must be a value of \"01\". Other values may be supported in the future.<br>     __Max Length:16__   # noqa: E501

        :return: The recommendation_algorithm_version of this DecisioningData.  # noqa: E501
        :rtype: str
        """
        return self._recommendation_algorithm_version

    @recommendation_algorithm_version.setter
    def recommendation_algorithm_version(self, recommendation_algorithm_version):
        """Sets the recommendation_algorithm_version of this DecisioningData.

        __(OPTIONAL)__ <br> Version of the algorithm used by the Token Requestor to determine its recommendation. Must be a value of \"01\". Other values may be supported in the future.<br>     __Max Length:16__   # noqa: E501

        :param recommendation_algorithm_version: The recommendation_algorithm_version of this DecisioningData.  # noqa: E501
        :type: str
        """

        self._recommendation_algorithm_version = recommendation_algorithm_version

    @property
    def device_score(self):
        """Gets the device_score of this DecisioningData.  # noqa: E501

        __(OPTIONAL)__ <br> Score assigned by the Token Requestor for the target device being provisioned. Must be a value from 1 to 5.   # noqa: E501

        :return: The device_score of this DecisioningData.  # noqa: E501
        :rtype: str
        """
        return self._device_score

    @device_score.setter
    def device_score(self, device_score):
        """Sets the device_score of this DecisioningData.

        __(OPTIONAL)__ <br> Score assigned by the Token Requestor for the target device being provisioned. Must be a value from 1 to 5.   # noqa: E501

        :param device_score: The device_score of this DecisioningData.  # noqa: E501
        :type: str
        """

        self._device_score = device_score

    @property
    def account_score(self):
        """Gets the account_score of this DecisioningData.  # noqa: E501

        __(OPTIONAL)__ <br> Score assigned by the Token Requestor for the consumer account or relationship. Must be a value from 1 to 5.   # noqa: E501

        :return: The account_score of this DecisioningData.  # noqa: E501
        :rtype: str
        """
        return self._account_score

    @account_score.setter
    def account_score(self, account_score):
        """Sets the account_score of this DecisioningData.

        __(OPTIONAL)__ <br> Score assigned by the Token Requestor for the consumer account or relationship. Must be a value from 1 to 5.   # noqa: E501

        :param account_score: The account_score of this DecisioningData.  # noqa: E501
        :type: str
        """

        self._account_score = account_score

    @property
    def recommendation_reasons(self):
        """Gets the recommendation_reasons of this DecisioningData.  # noqa: E501

        __(OPTIONAL)__ <br> Code indicating the reasons the Token Requestor is suggesting the digitization decision.  See table here - https://developer.mastercard.com/page/mdes-digitization-recommendation-reason-codes   # noqa: E501

        :return: The recommendation_reasons of this DecisioningData.  # noqa: E501
        :rtype: list[str]
        """
        return self._recommendation_reasons

    @recommendation_reasons.setter
    def recommendation_reasons(self, recommendation_reasons):
        """Sets the recommendation_reasons of this DecisioningData.

        __(OPTIONAL)__ <br> Code indicating the reasons the Token Requestor is suggesting the digitization decision.  See table here - https://developer.mastercard.com/page/mdes-digitization-recommendation-reason-codes   # noqa: E501

        :param recommendation_reasons: The recommendation_reasons of this DecisioningData.  # noqa: E501
        :type: list[str]
        """

        self._recommendation_reasons = recommendation_reasons

    @property
    def device_current_location(self):
        """Gets the device_current_location of this DecisioningData.  # noqa: E501

        __(OPTIONAL)__ <br> Latitude and longitude in the format \"(sign) latitude, (sign) longitude\" with a precision of 2 decimal places.  Ex - \"38.63, -90.25\"  Latitude is between -90 and 90.  Longitude between -180 and 180. Relates to the target device being provisioned. If there is no target device, then this should be the current consumer location, if available. <br>    __Max Length:14__   # noqa: E501

        :return: The device_current_location of this DecisioningData.  # noqa: E501
        :rtype: str
        """
        return self._device_current_location

    @device_current_location.setter
    def device_current_location(self, device_current_location):
        """Sets the device_current_location of this DecisioningData.

        __(OPTIONAL)__ <br> Latitude and longitude in the format \"(sign) latitude, (sign) longitude\" with a precision of 2 decimal places.  Ex - \"38.63, -90.25\"  Latitude is between -90 and 90.  Longitude between -180 and 180. Relates to the target device being provisioned. If there is no target device, then this should be the current consumer location, if available. <br>    __Max Length:14__   # noqa: E501

        :param device_current_location: The device_current_location of this DecisioningData.  # noqa: E501
        :type: str
        """

        self._device_current_location = device_current_location

    @property
    def device_ip_address(self):
        """Gets the device_ip_address of this DecisioningData.  # noqa: E501

        __(OPTIONAL)__ <br> The IP address of the device through which the device reaches the internet. This may be a temporary or permanent IP address assigned to a home router, or the IP address of a gateway through which the device connects to a network. IPv4 address format of 4 octets separated by \".\" Ex - 127.0.0.1 Relates to the target device being provisioned. If there is no target device, then this should be the current consumer IP address, if available.<br>     __Max Length:15__   # noqa: E501

        :return: The device_ip_address of this DecisioningData.  # noqa: E501
        :rtype: str
        """
        return self._device_ip_address

    @device_ip_address.setter
    def device_ip_address(self, device_ip_address):
        """Sets the device_ip_address of this DecisioningData.

        __(OPTIONAL)__ <br> The IP address of the device through which the device reaches the internet. This may be a temporary or permanent IP address assigned to a home router, or the IP address of a gateway through which the device connects to a network. IPv4 address format of 4 octets separated by \".\" Ex - 127.0.0.1 Relates to the target device being provisioned. If there is no target device, then this should be the current consumer IP address, if available.<br>     __Max Length:15__   # noqa: E501

        :param device_ip_address: The device_ip_address of this DecisioningData.  # noqa: E501
        :type: str
        """

        self._device_ip_address = device_ip_address

    @property
    def mobile_number_suffix(self):
        """Gets the mobile_number_suffix of this DecisioningData.  # noqa: E501

        __(OPTIONAL)__<br> The last few digits (typically four) of the consumer's mobile phone number as available on file or on the consumer's current device, which may or may not be the mobile number of the target device being provisioned.<br>     __Max Length:32__   # noqa: E501

        :return: The mobile_number_suffix of this DecisioningData.  # noqa: E501
        :rtype: str
        """
        return self._mobile_number_suffix

    @mobile_number_suffix.setter
    def mobile_number_suffix(self, mobile_number_suffix):
        """Sets the mobile_number_suffix of this DecisioningData.

        __(OPTIONAL)__<br> The last few digits (typically four) of the consumer's mobile phone number as available on file or on the consumer's current device, which may or may not be the mobile number of the target device being provisioned.<br>     __Max Length:32__   # noqa: E501

        :param mobile_number_suffix: The mobile_number_suffix of this DecisioningData.  # noqa: E501
        :type: str
        """

        self._mobile_number_suffix = mobile_number_suffix

    @property
    def account_id_hash(self):
        """Gets the account_id_hash of this DecisioningData.  # noqa: E501

        __(OPTIONAL)__ <br> SHA-256 hash of the Cardholder’s account ID with the Token Requestor. Typically expected to be an email address.<br>  __Max Length:64__ Alpha-Numeric and Hex-encoded data (case-insensitive).   # noqa: E501

        :return: The account_id_hash of this DecisioningData.  # noqa: E501
        :rtype: str
        """
        return self._account_id_hash

    @account_id_hash.setter
    def account_id_hash(self, account_id_hash):
        """Sets the account_id_hash of this DecisioningData.

        __(OPTIONAL)__ <br> SHA-256 hash of the Cardholder’s account ID with the Token Requestor. Typically expected to be an email address.<br>  __Max Length:64__ Alpha-Numeric and Hex-encoded data (case-insensitive).   # noqa: E501

        :param account_id_hash: The account_id_hash of this DecisioningData.  # noqa: E501
        :type: str
        """

        self._account_id_hash = account_id_hash

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DecisioningData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DecisioningData):
            return True

        return self.to_dict() != other.to_dict()
