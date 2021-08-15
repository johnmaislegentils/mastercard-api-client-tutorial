=begin
#MDES Digital Enablement API

#These APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br><br> **Authentication** <br><br> Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br><br> 1. A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br><br> **Encryption** <br><br> All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br><br> **Additional Encryption of Sensitive Data** <br><br> In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 

The version of the OpenAPI document: 1.3.0

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 5.2.0

=end

require 'cgi'

module OpenapiClient
  class SuspendApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Used to temporarily suspend one or more Tokens.
    # This API is used to temporarily suspend one or more Tokens (for example, suspending all Tokens on a device in response to the device being lost).  The API is limited to 10 Tokens per request. MDES will coordinate the suspension of the Tokens and notify any relevant parties that the Tokens have been suspended. A suspended Token can be unsuspended using the Unsuspend resource. 
    # @param [Hash] opts the optional parameters
    # @option opts [SuspendRequestSchema] :suspend_request_schema Contains the details of the request message. 
    # @return [SuspendResponseSchema]
    def create_suspend(opts = {})
      data, _status_code, _headers = create_suspend_with_http_info(opts)
      data
    end

    # Used to temporarily suspend one or more Tokens.
    # This API is used to temporarily suspend one or more Tokens (for example, suspending all Tokens on a device in response to the device being lost).  The API is limited to 10 Tokens per request. MDES will coordinate the suspension of the Tokens and notify any relevant parties that the Tokens have been suspended. A suspended Token can be unsuspended using the Unsuspend resource. 
    # @param [Hash] opts the optional parameters
    # @option opts [SuspendRequestSchema] :suspend_request_schema Contains the details of the request message. 
    # @return [Array<(SuspendResponseSchema, Integer, Hash)>] SuspendResponseSchema data, response status code and response headers
    def create_suspend_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: SuspendApi.create_suspend ...'
      end
      # resource path
      local_var_path = '/digitization/static/1/0/suspend'

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      # HTTP header 'Content-Type'
      header_params['Content-Type'] = @api_client.select_header_content_type(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body] || @api_client.object_to_http_body(opts[:'suspend_request_schema'])

      # return_type
      return_type = opts[:debug_return_type] || 'SuspendResponseSchema'

      # auth_names
      auth_names = opts[:debug_auth_names] || []

      new_options = opts.merge(
        :operation => :"SuspendApi.create_suspend",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: SuspendApi#create_suspend\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
