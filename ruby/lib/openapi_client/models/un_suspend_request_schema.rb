=begin
#MDES Digital Enablement API

#These APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br><br> **Authentication** <br><br> Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br><br> 1. A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br><br> **Encryption** <br><br> All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br><br> **Additional Encryption of Sensitive Data** <br><br> In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 

The version of the OpenAPI document: 1.3.0

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 5.2.0

=end

require 'date'
require 'time'

module OpenapiClient
  class UnSuspendRequestSchema
    # The host that originated the request. Future calls in the same conversation may be routed to this host. 
    attr_accessor :response_host

    # Unique identifier for the request. 
    attr_accessor :request_id

    # Identifier for the specific Mobile Payment App instance, unique across a given Wallet Identifier. This value cannot be changed after digitization. This field is alphanumeric and additionally web-safe base64 characters per RFC 4648 (minus \"-\", underscore \"_\") up to a maximum length of 48, = should not be URL encoded. Conditional - not applicable for server based tokens but required otherwise. 
    attr_accessor :payment_app_instance_id

    # The specific Token to be unsuspended. Array of more or more valid references as assigned by MDES 
    attr_accessor :token_unique_references

    # Who or what caused the Token to be unsuspended. Must be either the 'CARDHOLDER' (operation requested by the Cardholder) or 'TOKEN_REQUESTOR' (operation requested by the token requestor). 
    attr_accessor :caused_by

    # Free form reason why the Tokens are being suspended. 
    attr_accessor :reason

    # The reason for the action to be unsuspended. Must be one of 'SUSPECTED_FRAUD' (suspected fraudulent token transactions), 'OTHER' (Other - default used if value not provided). 
    attr_accessor :reason_code

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'response_host' => :'responseHost',
        :'request_id' => :'requestId',
        :'payment_app_instance_id' => :'paymentAppInstanceId',
        :'token_unique_references' => :'tokenUniqueReferences',
        :'caused_by' => :'causedBy',
        :'reason' => :'reason',
        :'reason_code' => :'reasonCode'
      }
    end

    # Returns all the JSON keys this model knows about
    def self.acceptable_attributes
      attribute_map.values
    end

    # Attribute type mapping.
    def self.openapi_types
      {
        :'response_host' => :'String',
        :'request_id' => :'String',
        :'payment_app_instance_id' => :'String',
        :'token_unique_references' => :'Array<String>',
        :'caused_by' => :'String',
        :'reason' => :'String',
        :'reason_code' => :'String'
      }
    end

    # List of attributes with nullable: true
    def self.openapi_nullable
      Set.new([
      ])
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      if (!attributes.is_a?(Hash))
        fail ArgumentError, "The input argument (attributes) must be a hash in `OpenapiClient::UnSuspendRequestSchema` initialize method"
      end

      # check to see if the attribute exists and convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h|
        if (!self.class.attribute_map.key?(k.to_sym))
          fail ArgumentError, "`#{k}` is not a valid attribute in `OpenapiClient::UnSuspendRequestSchema`. Please check the name to make sure it's valid. List of attributes: " + self.class.attribute_map.keys.inspect
        end
        h[k.to_sym] = v
      }

      if attributes.key?(:'response_host')
        self.response_host = attributes[:'response_host']
      end

      if attributes.key?(:'request_id')
        self.request_id = attributes[:'request_id']
      end

      if attributes.key?(:'payment_app_instance_id')
        self.payment_app_instance_id = attributes[:'payment_app_instance_id']
      end

      if attributes.key?(:'token_unique_references')
        if (value = attributes[:'token_unique_references']).is_a?(Array)
          self.token_unique_references = value
        end
      end

      if attributes.key?(:'caused_by')
        self.caused_by = attributes[:'caused_by']
      end

      if attributes.key?(:'reason')
        self.reason = attributes[:'reason']
      end

      if attributes.key?(:'reason_code')
        self.reason_code = attributes[:'reason_code']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      if @request_id.nil?
        invalid_properties.push('invalid value for "request_id", request_id cannot be nil.')
      end

      if !@payment_app_instance_id.nil? && @payment_app_instance_id.to_s.length > 48
        invalid_properties.push('invalid value for "payment_app_instance_id", the character length must be smaller than or equal to 48.')
      end

      if @token_unique_references.nil?
        invalid_properties.push('invalid value for "token_unique_references", token_unique_references cannot be nil.')
      end

      if @caused_by.nil?
        invalid_properties.push('invalid value for "caused_by", caused_by cannot be nil.')
      end

      if @caused_by.to_s.length > 64
        invalid_properties.push('invalid value for "caused_by", the character length must be smaller than or equal to 64.')
      end

      if !@reason.nil? && @reason.to_s.length > 256
        invalid_properties.push('invalid value for "reason", the character length must be smaller than or equal to 256.')
      end

      if @reason_code.nil?
        invalid_properties.push('invalid value for "reason_code", reason_code cannot be nil.')
      end

      if @reason_code.to_s.length > 64
        invalid_properties.push('invalid value for "reason_code", the character length must be smaller than or equal to 64.')
      end

      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      return false if @request_id.nil?
      return false if !@payment_app_instance_id.nil? && @payment_app_instance_id.to_s.length > 48
      return false if @token_unique_references.nil?
      return false if @caused_by.nil?
      return false if @caused_by.to_s.length > 64
      return false if !@reason.nil? && @reason.to_s.length > 256
      return false if @reason_code.nil?
      return false if @reason_code.to_s.length > 64
      true
    end

    # Custom attribute writer method with validation
    # @param [Object] payment_app_instance_id Value to be assigned
    def payment_app_instance_id=(payment_app_instance_id)
      if !payment_app_instance_id.nil? && payment_app_instance_id.to_s.length > 48
        fail ArgumentError, 'invalid value for "payment_app_instance_id", the character length must be smaller than or equal to 48.'
      end

      @payment_app_instance_id = payment_app_instance_id
    end

    # Custom attribute writer method with validation
    # @param [Object] caused_by Value to be assigned
    def caused_by=(caused_by)
      if caused_by.nil?
        fail ArgumentError, 'caused_by cannot be nil'
      end

      if caused_by.to_s.length > 64
        fail ArgumentError, 'invalid value for "caused_by", the character length must be smaller than or equal to 64.'
      end

      @caused_by = caused_by
    end

    # Custom attribute writer method with validation
    # @param [Object] reason Value to be assigned
    def reason=(reason)
      if !reason.nil? && reason.to_s.length > 256
        fail ArgumentError, 'invalid value for "reason", the character length must be smaller than or equal to 256.'
      end

      @reason = reason
    end

    # Custom attribute writer method with validation
    # @param [Object] reason_code Value to be assigned
    def reason_code=(reason_code)
      if reason_code.nil?
        fail ArgumentError, 'reason_code cannot be nil'
      end

      if reason_code.to_s.length > 64
        fail ArgumentError, 'invalid value for "reason_code", the character length must be smaller than or equal to 64.'
      end

      @reason_code = reason_code
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          response_host == o.response_host &&
          request_id == o.request_id &&
          payment_app_instance_id == o.payment_app_instance_id &&
          token_unique_references == o.token_unique_references &&
          caused_by == o.caused_by &&
          reason == o.reason &&
          reason_code == o.reason_code
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Integer] Hash code
    def hash
      [response_host, request_id, payment_app_instance_id, token_unique_references, caused_by, reason, reason_code].hash
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def self.build_from_hash(attributes)
      new.build_from_hash(attributes)
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def build_from_hash(attributes)
      return nil unless attributes.is_a?(Hash)
      self.class.openapi_types.each_pair do |key, type|
        if attributes[self.class.attribute_map[key]].nil? && self.class.openapi_nullable.include?(key)
          self.send("#{key}=", nil)
        elsif type =~ /\AArray<(.*)>/i
          # check to ensure the input is an array given that the attribute
          # is documented as an array but the input is not
          if attributes[self.class.attribute_map[key]].is_a?(Array)
            self.send("#{key}=", attributes[self.class.attribute_map[key]].map { |v| _deserialize($1, v) })
          end
        elsif !attributes[self.class.attribute_map[key]].nil?
          self.send("#{key}=", _deserialize(type, attributes[self.class.attribute_map[key]]))
        end
      end

      self
    end

    # Deserializes the data based on type
    # @param string type Data type
    # @param string value Value to be deserialized
    # @return [Object] Deserialized data
    def _deserialize(type, value)
      case type.to_sym
      when :Time
        Time.parse(value)
      when :Date
        Date.parse(value)
      when :String
        value.to_s
      when :Integer
        value.to_i
      when :Float
        value.to_f
      when :Boolean
        if value.to_s =~ /\A(true|t|yes|y|1)\z/i
          true
        else
          false
        end
      when :Object
        # generic object (usually a Hash), return directly
        value
      when /\AArray<(?<inner_type>.+)>\z/
        inner_type = Regexp.last_match[:inner_type]
        value.map { |v| _deserialize(inner_type, v) }
      when /\AHash<(?<k_type>.+?), (?<v_type>.+)>\z/
        k_type = Regexp.last_match[:k_type]
        v_type = Regexp.last_match[:v_type]
        {}.tap do |hash|
          value.each do |k, v|
            hash[_deserialize(k_type, k)] = _deserialize(v_type, v)
          end
        end
      else # model
        # models (e.g. Pet) or oneOf
        klass = OpenapiClient.const_get(type)
        klass.respond_to?(:openapi_one_of) ? klass.build(value) : klass.build_from_hash(value)
      end
    end

    # Returns the string representation of the object
    # @return [String] String presentation of the object
    def to_s
      to_hash.to_s
    end

    # to_body is an alias to to_hash (backward compatibility)
    # @return [Hash] Returns the object in the form of hash
    def to_body
      to_hash
    end

    # Returns the object in the form of hash
    # @return [Hash] Returns the object in the form of hash
    def to_hash
      hash = {}
      self.class.attribute_map.each_pair do |attr, param|
        value = self.send(attr)
        if value.nil?
          is_nullable = self.class.openapi_nullable.include?(attr)
          next if !is_nullable || (is_nullable && !instance_variable_defined?(:"@#{attr}"))
        end

        hash[param] = _to_hash(value)
      end
      hash
    end

    # Outputs non-array value in the form of hash
    # For object, use to_hash. Otherwise, just return the value
    # @param [Object] value Any valid value
    # @return [Hash] Returns the value in the form of hash
    def _to_hash(value)
      if value.is_a?(Array)
        value.compact.map { |v| _to_hash(v) }
      elsif value.is_a?(Hash)
        {}.tap do |hash|
          value.each { |k, v| hash[k] = _to_hash(v) }
        end
      elsif value.respond_to? :to_hash
        value.to_hash
      else
        value
      end
    end

  end

end
