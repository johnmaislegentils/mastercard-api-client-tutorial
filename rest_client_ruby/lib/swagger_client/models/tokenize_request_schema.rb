=begin
#MDES for Merchants

#The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously.  

OpenAPI spec version: 1.2.7

Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 2.4.0-SNAPSHOT

=end

require 'date'

module SwaggerClient
  class TokenizeRequestSchema
    # \"The host that originated the request. Future calls in the same conversation may be routed to this host. Must be provided as: host[:port][/contextRoot] Where port and contextRoot are optional. If contextRoot is not provided, the default (per the URL Scheme) is assumed and must be used.\" 
    attr_accessor :response_host

    # Unique identifier for the request. 
    attr_accessor :request_id

    # The type of Token requested. Must be CLOUD       __Max Length:32__    
    attr_accessor :token_type

    # Identifies the Token Requestor       __Max Length:11__  
    attr_accessor :token_requestor_id

    # Identifier for this task as assigned by the Token Requestor, unique across a given Token Requestor Identifier. May be used in the Get Task Status API to query the status of this task.      __Max Length:64__ 
    attr_accessor :task_id

    attr_accessor :card_info

    # Language preference selected by the consumer. Formatted as an ISO- 639-1 two-letter language code.    __Max Length:2__ 
    attr_accessor :consumer_language

    # The Tokenization Authentication Value (TAV) as cryptographically signed by the Issuer to authorize this digitization request.      __Max Length:2048__ 
    attr_accessor :tokenization_authentication_value

    attr_accessor :decisioning_data

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'response_host' => :'responseHost',
        :'request_id' => :'requestId',
        :'token_type' => :'tokenType',
        :'token_requestor_id' => :'tokenRequestorId',
        :'task_id' => :'taskId',
        :'card_info' => :'cardInfo',
        :'consumer_language' => :'consumerLanguage',
        :'tokenization_authentication_value' => :'tokenizationAuthenticationValue',
        :'decisioning_data' => :'decisioningData'
      }
    end

    # Attribute type mapping.
    def self.swagger_types
      {
        :'response_host' => :'String',
        :'request_id' => :'String',
        :'token_type' => :'String',
        :'token_requestor_id' => :'String',
        :'task_id' => :'String',
        :'card_info' => :'CardInfo',
        :'consumer_language' => :'String',
        :'tokenization_authentication_value' => :'String',
        :'decisioning_data' => :'DecisioningData'
      }
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      return unless attributes.is_a?(Hash)

      # convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h| h[k.to_sym] = v }

      if attributes.has_key?(:'responseHost')
        self.response_host = attributes[:'responseHost']
      end

      if attributes.has_key?(:'requestId')
        self.request_id = attributes[:'requestId']
      end

      if attributes.has_key?(:'tokenType')
        self.token_type = attributes[:'tokenType']
      end

      if attributes.has_key?(:'tokenRequestorId')
        self.token_requestor_id = attributes[:'tokenRequestorId']
      end

      if attributes.has_key?(:'taskId')
        self.task_id = attributes[:'taskId']
      end

      if attributes.has_key?(:'cardInfo')
        self.card_info = attributes[:'cardInfo']
      end

      if attributes.has_key?(:'consumerLanguage')
        self.consumer_language = attributes[:'consumerLanguage']
      end

      if attributes.has_key?(:'tokenizationAuthenticationValue')
        self.tokenization_authentication_value = attributes[:'tokenizationAuthenticationValue']
      end

      if attributes.has_key?(:'decisioningData')
        self.decisioning_data = attributes[:'decisioningData']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      if @token_type.nil?
        invalid_properties.push('invalid value for "token_type", token_type cannot be nil.')
      end

      if @token_requestor_id.nil?
        invalid_properties.push('invalid value for "token_requestor_id", token_requestor_id cannot be nil.')
      end

      if @task_id.nil?
        invalid_properties.push('invalid value for "task_id", task_id cannot be nil.')
      end

      if @card_info.nil?
        invalid_properties.push('invalid value for "card_info", card_info cannot be nil.')
      end

      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      return false if @token_type.nil?
      return false if @token_requestor_id.nil?
      return false if @task_id.nil?
      return false if @card_info.nil?
      true
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          response_host == o.response_host &&
          request_id == o.request_id &&
          token_type == o.token_type &&
          token_requestor_id == o.token_requestor_id &&
          task_id == o.task_id &&
          card_info == o.card_info &&
          consumer_language == o.consumer_language &&
          tokenization_authentication_value == o.tokenization_authentication_value &&
          decisioning_data == o.decisioning_data
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Fixnum] Hash code
    def hash
      [response_host, request_id, token_type, token_requestor_id, task_id, card_info, consumer_language, tokenization_authentication_value, decisioning_data].hash
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def build_from_hash(attributes)
      return nil unless attributes.is_a?(Hash)
      self.class.swagger_types.each_pair do |key, type|
        if type =~ /\AArray<(.*)>/i
          # check to ensure the input is an array given that the the attribute
          # is documented as an array but the input is not
          if attributes[self.class.attribute_map[key]].is_a?(Array)
            self.send("#{key}=", attributes[self.class.attribute_map[key]].map { |v| _deserialize($1, v) })
          end
        elsif !attributes[self.class.attribute_map[key]].nil?
          self.send("#{key}=", _deserialize(type, attributes[self.class.attribute_map[key]]))
        end # or else data not found in attributes(hash), not an issue as the data can be optional
      end

      self
    end

    # Deserializes the data based on type
    # @param string type Data type
    # @param string value Value to be deserialized
    # @return [Object] Deserialized data
    def _deserialize(type, value)
      case type.to_sym
      when :DateTime
        DateTime.parse(value)
      when :Date
        Date.parse(value)
      when :String
        value.to_s
      when :Integer
        value.to_i
      when :Float
        value.to_f
      when :BOOLEAN
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
        temp_model = SwaggerClient.const_get(type).new
        temp_model.build_from_hash(value)
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
        next if value.nil?
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
