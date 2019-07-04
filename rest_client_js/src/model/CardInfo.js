/**
 * MDES for Merchants
 * The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously.  
 *
 * OpenAPI spec version: 1.2.7
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
    define(['ApiClient', 'model/CardInfoData'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./CardInfoData'));
  } else {
    // Browser globals (root is window)
    if (!root.MdesForMerchants) {
      root.MdesForMerchants = {};
    }
    root.MdesForMerchants.CardInfo = factory(root.MdesForMerchants.ApiClient, root.MdesForMerchants.CardInfoData);
  }
}(this, function(ApiClient, CardInfoData) {
  'use strict';




  /**
   * The CardInfo model module.
   * @module model/CardInfo
   * @version 1.2.7
   */

  /**
   * Constructs a new <code>CardInfo</code>.
   * @alias module:model/CardInfo
   * @class
   */
  var exports = function() {
    var _this = this;








  };

  /**
   * Constructs a <code>CardInfo</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/CardInfo} obj Optional instance to populate.
   * @return {module:model/CardInfo} The populated <code>CardInfo</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('panUniqueReference')) {
        obj['panUniqueReference'] = ApiClient.convertToType(data['panUniqueReference'], 'String');
      }
      if (data.hasOwnProperty('tokenUniqueReferenceForPanInfo')) {
        obj['tokenUniqueReferenceForPanInfo'] = ApiClient.convertToType(data['tokenUniqueReferenceForPanInfo'], 'String');
      }
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
        obj['encryptedData'] = CardInfoData.constructFromObject(data['encryptedData']);
      }
    }
    return obj;
  }

  /**
   *  __(CONDITIONAL)__ <br>  For repeat digitizations, the unique reference allocated to the Primary Account Number. When supplied, the tokenUniqueReferenceForPanInfo, accountNumber, expiryMonth and expiryYear must be omitted from CardInfoData.   Only allowed if  tokenUniqueReferenceForPanInfo is not present and encrypted data does not contain the account information. <br> __Max Length:64__ 
   * @member {String} panUniqueReference
   */
  exports.prototype['panUniqueReference'] = undefined;
  /**
   *  __(CONDITIONAL)__<br>  For repeat digitizations, the unique reference allocated to the token will be used to retrieve the account number and expiration date. When supplied, the panUniqueReference, accountNumber, expiryMonth and expiryYear must be omitted from CardInfoData.    Only allowed if panUniqueReference is not present and encrypted data does not contain the account information. <br> __Max Length:64__ 
   * @member {String} tokenUniqueReferenceForPanInfo
   */
  exports.prototype['tokenUniqueReferenceForPanInfo'] = undefined;
  /**
   * The fingerprint of the public key used to encrypt the ephemeral AES key. Required if encryptedData is present.<br>     __Max Length:64__ Hex-encoded data (case-insensitive). 
   * @member {String} publicKeyFingerprint
   */
  exports.prototype['publicKeyFingerprint'] = undefined;
  /**
   * One-time use AES key encrypted by the MasterCard public key (as identified by 'publicKeyFingerprint') using the OAEP or RSA Encryption Standard PKCS #1 v1.5  (depending on the value of 'oaepHashingAlgorithm'. Requirement is for a 128-bit key (with 256-bit key supported as an option). Required if encrypted data is present. <br>   __Max Length:512__ Hex-encoded data (case-insensitive).\" 
   * @member {String} encryptedKey
   */
  exports.prototype['encryptedKey'] = undefined;
  /**
   * Hashing algorithm used with the OAEP scheme. Must be either SHA256 or SHA512.     __Max Length:6__ 
   * @member {String} oaepHashingAlgorithm
   */
  exports.prototype['oaepHashingAlgorithm'] = undefined;
  /**
   * It is recommended to supply a random initialization vector when encrypting the data using the one-time use AES key. Must be exactly 16 bytes (32 character hex string) to match the block size. Hex-encoded data (case-insensitive).  <br>__Max Length:32__ 
   * @member {String} iv
   */
  exports.prototype['iv'] = undefined;
  /**
   * @member {module:model/CardInfoData} encryptedData
   */
  exports.prototype['encryptedData'] = undefined;



  return exports;
}));


