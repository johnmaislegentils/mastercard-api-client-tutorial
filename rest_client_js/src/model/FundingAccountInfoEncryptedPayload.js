/**
 * MDES for Merchants
 * The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 
 *
 * OpenAPI spec version: 1.2.8
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.0-SNAPSHOT
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/FundingAccountData'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./FundingAccountData'));
  } else {
    // Browser globals (root is window)
    if (!root.MdesForMerchants) {
      root.MdesForMerchants = {};
    }
    root.MdesForMerchants.FundingAccountInfoEncryptedPayload = factory(root.MdesForMerchants.ApiClient, root.MdesForMerchants.FundingAccountData);
  }
}(this, function(ApiClient, FundingAccountData) {
  'use strict';




  /**
   * The FundingAccountInfoEncryptedPayload model module.
   * @module model/FundingAccountInfoEncryptedPayload
   * @version 1.2.8
   */

  /**
   * Constructs a new <code>FundingAccountInfoEncryptedPayload</code>.
   * @alias module:model/FundingAccountInfoEncryptedPayload
   * @class
   */
  var exports = function() {
    var _this = this;






  };

  /**
   * Constructs a <code>FundingAccountInfoEncryptedPayload</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/FundingAccountInfoEncryptedPayload} obj Optional instance to populate.
   * @return {module:model/FundingAccountInfoEncryptedPayload} The populated <code>FundingAccountInfoEncryptedPayload</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('publicKeyFingerprint')) {
        obj['publicKeyFingerprint'] = ApiClient.convertToType(data['publicKeyFingerprint'], 'String');
      }
      if (data.hasOwnProperty('encryptedKey')) {
        obj['encryptedKey'] = ApiClient.convertToType(data['encryptedKey'], 'String');
      }
      if (data.hasOwnProperty('oaepHashingAlgorithm')) {
        obj['oaepHashingAlgorithm'] = ApiClient.convertToType(data['oaepHashingAlgorithm'], 'String');
      }
      if (data.hasOwnProperty('iv')) {
        obj['iv'] = ApiClient.convertToType(data['iv'], 'String');
      }
      if (data.hasOwnProperty('encryptedData')) {
        obj['encryptedData'] = FundingAccountData.constructFromObject(data['encryptedData']);
      }
    }
    return obj;
  }

  /**
   * The fingerprint of the public key used to encrypt the ephemeral AES key.<br> __Max Length: 64__ 
   * @member {String} publicKeyFingerprint
   */
  exports.prototype['publicKeyFingerprint'] = undefined;
  /**
   * One-time use AES key encrypted by the MasterCard public key (as identified by publicKeyFingerprint) using the OAEP or PKCS#1 v1.5 scheme (depending on the value of oaepHashingAlgorithm. <br> __Max Length: 512__ 
   * @member {String} encryptedKey
   */
  exports.prototype['encryptedKey'] = undefined;
  /**
   * Hashing algorithm used with the OAEP scheme. Must be either SHA256 or SHA512. 
   * @member {String} oaepHashingAlgorithm
   */
  exports.prototype['oaepHashingAlgorithm'] = undefined;
  /**
   * The initialization vector used when encrypting data using the one-time use AES key. Must be exactly 16 bytes (32 character hex string) to match the block size. If not present, an IV of zero is assumed.  <br>__Length: 32__ 
   * @member {String} iv
   */
  exports.prototype['iv'] = undefined;
  /**
   * @member {module:model/FundingAccountData} encryptedData
   */
  exports.prototype['encryptedData'] = undefined;



  return exports;
}));


