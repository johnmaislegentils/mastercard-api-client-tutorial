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
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.MdesForMerchants) {
      root.MdesForMerchants = {};
    }
    root.MdesForMerchants.TransactEncryptedData = factory(root.MdesForMerchants.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The TransactEncryptedData model module.
   * @module model/TransactEncryptedData
   * @version 1.2.7
   */

  /**
   * Constructs a new <code>TransactEncryptedData</code>.
   * @alias module:model/TransactEncryptedData
   * @class
   */
  var exports = function() {
    var _this = this;







  };

  /**
   * Constructs a <code>TransactEncryptedData</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/TransactEncryptedData} obj Optional instance to populate.
   * @return {module:model/TransactEncryptedData} The populated <code>TransactEncryptedData</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('accountNumber')) {
        obj['accountNumber'] = ApiClient.convertToType(data['accountNumber'], 'String');
      }
      if (data.hasOwnProperty('applicationExpiryDate')) {
        obj['applicationExpiryDate'] = ApiClient.convertToType(data['applicationExpiryDate'], 'String');
      }
      if (data.hasOwnProperty('panSequenceNumber')) {
        obj['panSequenceNumber'] = ApiClient.convertToType(data['panSequenceNumber'], 'String');
      }
      if (data.hasOwnProperty('track2Equivalent')) {
        obj['track2Equivalent'] = ApiClient.convertToType(data['track2Equivalent'], 'String');
      }
      if (data.hasOwnProperty('de48se43Data')) {
        obj['de48se43Data'] = ApiClient.convertToType(data['de48se43Data'], 'String');
      }
      if (data.hasOwnProperty('de55Data')) {
        obj['de55Data'] = ApiClient.convertToType(data['de55Data'], 'String');
      }
    }
    return obj;
  }

  /**
   * The Primary Account Number for the transaction � this is the Token PAN.  <br>__Min Length: 9__ <br>__Max Length: 19__ 
   * @member {String} accountNumber
   */
  exports.prototype['accountNumber'] = undefined;
  /**
   * Application expiry date for the Token. Expressed in YYMMDD format.  <br> __Length: 6__ 
   * @member {String} applicationExpiryDate
   */
  exports.prototype['applicationExpiryDate'] = undefined;
  /**
   * Application PAN sequence number for the Token <br>  __Length: 2__ 
   * @member {String} panSequenceNumber
   */
  exports.prototype['panSequenceNumber'] = undefined;
  /**
   * Track 2 equivalent data for the Token. Expressed according to ISO/IEC 7813, excluding start sentinel, end sentinel, and Longitudinal Redundancy Check (LRC), using hex nibble 'D' as field separator, and padded to whole bytes using one hex nibble 'F' as needed.  <br>   __Max Length: 38__ 
   * @member {String} track2Equivalent
   */
  exports.prototype['track2Equivalent'] = undefined;
  /**
   * Data for DE 48 Subelement 43 containing the cryptogram.<br> __Max Length: 32__ 
   * @member {String} de48se43Data
   */
  exports.prototype['de48se43Data'] = undefined;
  /**
   * Data for DE 55 if present<br> __Max Length: 200__ 
   * @member {String} de55Data
   */
  exports.prototype['de55Data'] = undefined;



  return exports;
}));


