=begin
#MDES Digital Enablement API

#These APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br><br> **Authentication** <br><br> Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br><br> 1. A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br><br> **Encryption** <br><br> All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br><br> **Additional Encryption of Sensitive Data** <br><br> In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 

The version of the OpenAPI document: 1.3.0

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 5.2.0

=end

# Common files
require 'openapi_client/api_client'
require 'openapi_client/api_error'
require 'openapi_client/version'
require 'openapi_client/configuration'

# Models
require 'openapi_client/models/account_holder_data'
require 'openapi_client/models/account_holder_data_outbound'
require 'openapi_client/models/asset_response_schema'
require 'openapi_client/models/authentication_methods'
require 'openapi_client/models/billing_address'
require 'openapi_client/models/card_account_data_inbound'
require 'openapi_client/models/card_account_data_outbound'
require 'openapi_client/models/decisioning_data'
require 'openapi_client/models/delete_request_schema'
require 'openapi_client/models/delete_response_schema'
require 'openapi_client/models/encrypted_payload'
require 'openapi_client/models/encrypted_payload_transact'
require 'openapi_client/models/error'
require 'openapi_client/models/errors_response'
require 'openapi_client/models/funding_account_data'
require 'openapi_client/models/funding_account_info'
require 'openapi_client/models/funding_account_info_encrypted_payload'
require 'openapi_client/models/gateway_error'
require 'openapi_client/models/gateway_errors_response'
require 'openapi_client/models/gateway_errors_schema'
require 'openapi_client/models/get_task_status_request_schema'
require 'openapi_client/models/get_task_status_response_schema'
require 'openapi_client/models/get_token_request_schema'
require 'openapi_client/models/get_token_response_schema'
require 'openapi_client/models/media_content'
require 'openapi_client/models/notify_token_encrypted_payload'
require 'openapi_client/models/notify_token_updated_request_schema'
require 'openapi_client/models/notify_token_updated_response_schema'
require 'openapi_client/models/phone_number'
require 'openapi_client/models/product_config'
require 'openapi_client/models/search_tokens_request_schema'
require 'openapi_client/models/search_tokens_response_schema'
require 'openapi_client/models/suspend_request_schema'
require 'openapi_client/models/suspend_response_schema'
require 'openapi_client/models/token'
require 'openapi_client/models/token_detail'
require 'openapi_client/models/token_detail_data'
require 'openapi_client/models/token_detail_data_get_token_only'
require 'openapi_client/models/token_detail_data_par_only'
require 'openapi_client/models/token_detail_get_token_only'
require 'openapi_client/models/token_detail_par_only'
require 'openapi_client/models/token_for_get_token'
require 'openapi_client/models/token_for_lcm'
require 'openapi_client/models/token_for_ntu'
require 'openapi_client/models/token_info'
require 'openapi_client/models/token_info_for_ntu_and_get_token'
require 'openapi_client/models/tokenize_request_schema'
require 'openapi_client/models/tokenize_response_schema'
require 'openapi_client/models/transact_encrypted_data'
require 'openapi_client/models/transact_error'
require 'openapi_client/models/transact_request_schema'
require 'openapi_client/models/transact_response_schema'
require 'openapi_client/models/un_suspend_request_schema'
require 'openapi_client/models/un_suspend_response_schema'

# APIs
require 'openapi_client/api/delete_api'
require 'openapi_client/api/get_asset_api'
require 'openapi_client/api/get_task_status_api'
require 'openapi_client/api/get_token_api'
require 'openapi_client/api/notify_token_updated_api'
require 'openapi_client/api/search_tokens_api'
require 'openapi_client/api/suspend_api'
require 'openapi_client/api/tokenize_api'
require 'openapi_client/api/transact_api'
require 'openapi_client/api/unsuspend_api'

module OpenapiClient
  class << self
    # Customize default settings for the SDK using block.
    #   OpenapiClient.configure do |config|
    #     config.username = "xxx"
    #     config.password = "xxx"
    #   end
    # If no block given, return the default Configuration object.
    def configure
      if block_given?
        yield(Configuration.default)
      else
        Configuration.default
      end
    end
  end
end
