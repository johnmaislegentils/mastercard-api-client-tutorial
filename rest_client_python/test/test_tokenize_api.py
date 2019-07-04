# coding: utf-8

"""
    MDES for Merchants

    The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java)   # noqa: E501

    OpenAPI spec version: 1.2.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest
import os
import json

import swagger_client
from swagger_client.api.tokenize_api import TokenizeApi
from swagger_client.rest import ApiException

from oauth1.signer_interceptor import add_signing_layer
from oauth1.signer_interceptor import get_signing_layer

from client_encryption.field_level_encryption_config import FieldLevelEncryptionConfig
from client_encryption.api_encryption import add_encryption_layer
from swagger_client.api_client import ApiClient

FLE_CONFIG_PATH = "resources/fle_config.json"
BASE_PATH = "https://sandbox.api.mastercard.com/mdes"
P12 = '/Users/marcorocco/development/projects/mastercard/client-encryption-nodejs-service-tests/services/digital-enablement/Oauth_libs-sandbox.p12' # TODO
KEY_PASSWORD = 'keystorepassword' # TODO
CONSUMER_KEY = 'q_zC8ga1WQhV7eSQx6gdstilnlXGohRHwlKUp_G3147e715a!737b9380526f4daa9f49fcd0047c3e9c0000000000000000' # TODO

class TestTokenizeApi(unittest.TestCase):

    def setUp(self):
        c = swagger_client.Configuration()
        c.host = BASE_PATH
        self.cli = swagger_client.ApiClient(c)
        ## Add OAuth1.0a interceptor
        add_signing_layer(self, self.cli, P12, KEY_PASSWORD, CONSUMER_KEY)
        ## Add Field Level Encryption interceptor
        config_file = os.path.join(os.path.dirname(__file__), FLE_CONFIG_PATH)
        add_encryption_layer(self.cli, config_file)


    def test_create_tokenize(self):
        """TokenizeApi create_tokenize unit test"""
        api = swagger_client.api.tokenize_api.TokenizeApi(self.cli)
        res = api.create_tokenize(tokenize_request_schema=self.create_body())
        # print(res)
        assert(res)
        self.assertEqual(res.decision, 'APPROVED')


    def create_body(self):
        return {  
            "requestId":"123456",
            "taskId":"123456",
            "tokenType":"CLOUD",
            "tokenRequestorId":"98765432101",
            "cardInfo":{  
                "publicKeyFingerprint":"8FC11150A7508F14BACA07285703392A399CC57C",
                "encryptedKey":"A1B2C3D4E5F6112233445566",
                "oaepHashingAlgorithm":"SHA512",
                "iv":"NA",
                "encryptedData":{  
                    "accountNumber":"5123456789012345",
                    "source":"CARD_ON_FILE",
                    "cardholderName":"John Doe",
                    "securityCode":"123",
                    "expiryYear":"21",
                    "expiryMonth":"09",
                    "billingAddress":{  
                        "line1":"100 1st Street",
                        "line2":"Apt. 4B",
                        "city":"St. Louis",
                        "countrySubdivision":"MO",
                        "postalCode":"61000"
                    }
                }
            }
        }



if __name__ == '__main__':
    unittest.main()
