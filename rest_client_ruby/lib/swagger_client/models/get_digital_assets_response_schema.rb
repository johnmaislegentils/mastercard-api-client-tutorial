=begin
#MDES for Merchants

#The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 

OpenAPI spec version: 1.2.8

Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 2.4.0-SNAPSHOT

=end

require 'date'

module SwaggerClient
  class GetDigitalAssetsResponseSchema
    # Unique identifier for the response. 
    attr_accessor :response_id

    # The host that originated the request. Future calls in the same conversation may be routed to this host. 
    attr_accessor :response_host

    # The MasterCard or Maestro brand logo associated with this card. Provided as an Asset ID ? use the Get Asset API to retrieve the actual asset. Always returned in Product Configuration object <br>    __Max Length: 64__<br> __Required: Yes__ 
    attr_accessor :brand_logo_asset_id

    # The logo of the issuing bank. Provided as an Asset ID ? use the Get Asset API to retrieve the actual asset. Always returned in Product Configuration object <br>     __Max Length:64__<br> __Required: Yes__ 
    attr_accessor :issuer_logo_asset_id

    # Whether the product is co-branded. Must be either true (this is a co-branded product) or false (this is not a co-branded product). Always returned in Product Configuration object <br>    __Max Length:5__<br> __Required: Yes__ 
    attr_accessor :is_co_branded

    # Textual name of the co-brand partner. Required if CoBranded is true, not present otherwise.  <br>   __Max Length:128__<br> __Required: Conditional ? required if isCoBranded = \"true\". Not present otherwise__ 
    attr_accessor :co_brand_name

    # The co-brand logo (if any) for this product. Provided as an Asset ID ? use the Get Asset API to retrieve the actual asset. <br>   __Max Length:64__<br> __Required: No__ 
    attr_accessor :co_brand_logo_asset_id

    # The card image used to represent the digital card in the wallet. This ?combined? option contains the MasterCard, bank and any co- brand logos.  Provided as an Asset ID ? use the Get Asset API to retrieve the actual asset.     __Max Length:64__<br> __Required: Conditional ? either CardBackgroundCombined or CardBackground will be provided__ 
    attr_accessor :card_background_combined_asset_id

    # The card image used to represent the digital card in the wallet. This ?non-combined? option does not contain the MasterCard, bank, or co-brand logos. Provided as an Asset ID ? use the Get Asset API to retrieve the actual asset. <br>     __Max Length:64__<br> __Required: Conditional ? either CardBackgroundCombined or CardBackground will be provided__ 
    attr_accessor :card_background_asset_id

    # The icon representing the primary brand(s) associated with this product. Provided as an Asset ID ? use the Get Asset API to retrieve the actual asset. Always returned in Product Configuration object<br>    __Max Length:64__<br> __Required: Yes__ 
    attr_accessor :icon_asset_id

    # Foreground color, used to overlay text on top of the card image. Always returned in Product Configuration object<br>    __Max Length:6__ Hexadecimal RGB color format (case-insensitive).<br> __Required: Yes__ 
    attr_accessor :foreground_color

    # Name of the issuing bank. Always returned in Product Configuration object <br>    __Max Length:64__<br> __Required: Yes__ 
    attr_accessor :issuer_name

    # A short description for this product. Always returned in Product Configuration object  <br>   __Max Length:128__<br> __Required: Yes__ 
    attr_accessor :short_description

    # A long description for this product.  <br>   __Max Length:256__<br> __Required: No__ 
    attr_accessor :long_description

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'response_id' => :'responseId',
        :'response_host' => :'responseHost',
        :'brand_logo_asset_id' => :'brandLogoAssetId',
        :'issuer_logo_asset_id' => :'issuerLogoAssetId',
        :'is_co_branded' => :'isCoBranded',
        :'co_brand_name' => :'coBrandName',
        :'co_brand_logo_asset_id' => :'coBrandLogoAssetId',
        :'card_background_combined_asset_id' => :'cardBackgroundCombinedAssetId',
        :'card_background_asset_id' => :'cardBackgroundAssetId',
        :'icon_asset_id' => :'iconAssetId',
        :'foreground_color' => :'foregroundColor',
        :'issuer_name' => :'issuerName',
        :'short_description' => :'shortDescription',
        :'long_description' => :'longDescription'
      }
    end

    # Attribute type mapping.
    def self.swagger_types
      {
        :'response_id' => :'String',
        :'response_host' => :'String',
        :'brand_logo_asset_id' => :'String',
        :'issuer_logo_asset_id' => :'String',
        :'is_co_branded' => :'String',
        :'co_brand_name' => :'String',
        :'co_brand_logo_asset_id' => :'String',
        :'card_background_combined_asset_id' => :'String',
        :'card_background_asset_id' => :'String',
        :'icon_asset_id' => :'String',
        :'foreground_color' => :'String',
        :'issuer_name' => :'String',
        :'short_description' => :'String',
        :'long_description' => :'String'
      }
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      return unless attributes.is_a?(Hash)

      # convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h| h[k.to_sym] = v }

      if attributes.has_key?(:'responseId')
        self.response_id = attributes[:'responseId']
      end

      if attributes.has_key?(:'responseHost')
        self.response_host = attributes[:'responseHost']
      end

      if attributes.has_key?(:'brandLogoAssetId')
        self.brand_logo_asset_id = attributes[:'brandLogoAssetId']
      end

      if attributes.has_key?(:'issuerLogoAssetId')
        self.issuer_logo_asset_id = attributes[:'issuerLogoAssetId']
      end

      if attributes.has_key?(:'isCoBranded')
        self.is_co_branded = attributes[:'isCoBranded']
      end

      if attributes.has_key?(:'coBrandName')
        self.co_brand_name = attributes[:'coBrandName']
      end

      if attributes.has_key?(:'coBrandLogoAssetId')
        self.co_brand_logo_asset_id = attributes[:'coBrandLogoAssetId']
      end

      if attributes.has_key?(:'cardBackgroundCombinedAssetId')
        self.card_background_combined_asset_id = attributes[:'cardBackgroundCombinedAssetId']
      end

      if attributes.has_key?(:'cardBackgroundAssetId')
        self.card_background_asset_id = attributes[:'cardBackgroundAssetId']
      end

      if attributes.has_key?(:'iconAssetId')
        self.icon_asset_id = attributes[:'iconAssetId']
      end

      if attributes.has_key?(:'foregroundColor')
        self.foreground_color = attributes[:'foregroundColor']
      end

      if attributes.has_key?(:'issuerName')
        self.issuer_name = attributes[:'issuerName']
      end

      if attributes.has_key?(:'shortDescription')
        self.short_description = attributes[:'shortDescription']
      end

      if attributes.has_key?(:'longDescription')
        self.long_description = attributes[:'longDescription']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      true
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          response_id == o.response_id &&
          response_host == o.response_host &&
          brand_logo_asset_id == o.brand_logo_asset_id &&
          issuer_logo_asset_id == o.issuer_logo_asset_id &&
          is_co_branded == o.is_co_branded &&
          co_brand_name == o.co_brand_name &&
          co_brand_logo_asset_id == o.co_brand_logo_asset_id &&
          card_background_combined_asset_id == o.card_background_combined_asset_id &&
          card_background_asset_id == o.card_background_asset_id &&
          icon_asset_id == o.icon_asset_id &&
          foreground_color == o.foreground_color &&
          issuer_name == o.issuer_name &&
          short_description == o.short_description &&
          long_description == o.long_description
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Fixnum] Hash code
    def hash
      [response_id, response_host, brand_logo_asset_id, issuer_logo_asset_id, is_co_branded, co_brand_name, co_brand_logo_asset_id, card_background_combined_asset_id, card_background_asset_id, icon_asset_id, foreground_color, issuer_name, short_description, long_description].hash
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
