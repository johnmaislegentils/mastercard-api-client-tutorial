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
    define(['ApiClient', 'model/EncryptedPayload'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./EncryptedPayload'));
  } else {
    // Browser globals (root is window)
    if (!root.MdesForMerchants) {
      root.MdesForMerchants = {};
    }
    root.MdesForMerchants.NotifyTokenUpdatedRequestSchema = factory(root.MdesForMerchants.ApiClient, root.MdesForMerchants.EncryptedPayload);
  }
}(this, function(ApiClient, EncryptedPayload) {
  'use strict';




  /**
   * The NotifyTokenUpdatedRequestSchema model module.
   * @module model/NotifyTokenUpdatedRequestSchema
   * @version 1.2.7
   */

  /**
   * Constructs a new <code>NotifyTokenUpdatedRequestSchema</code>.
   * @alias module:model/NotifyTokenUpdatedRequestSchema
   * @class
   * @param responseHost {String} The host that originated the request. Future calls in the same conversation should be routed to this host. 
   * @param requestId {String} Unique identifier for the request. 
   * @param encryptedPayload {module:model/EncryptedPayload} 
   */
  var exports = function(responseHost, requestId, encryptedPayload) {
    var _this = this;

    _this['responseHost'] = responseHost;
    _this['requestId'] = requestId;
    _this['encryptedPayload'] = encryptedPayload;
  };

  /**
   * Constructs a <code>NotifyTokenUpdatedRequestSchema</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/NotifyTokenUpdatedRequestSchema} obj Optional instance to populate.
   * @return {module:model/NotifyTokenUpdatedRequestSchema} The populated <code>NotifyTokenUpdatedRequestSchema</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('responseHost')) {
        obj['responseHost'] = ApiClient.convertToType(data['responseHost'], 'String');
      }
      if (data.hasOwnProperty('requestId')) {
        obj['requestId'] = ApiClient.convertToType(data['requestId'], 'String');
      }
      if (data.hasOwnProperty('encryptedPayload')) {
        obj['encryptedPayload'] = EncryptedPayload.constructFromObject(data['encryptedPayload']);
      }
    }
    return obj;
  }

  /**
   * The host that originated the request. Future calls in the same conversation should be routed to this host. 
   * @member {String} responseHost
   */
  exports.prototype['responseHost'] = undefined;
  /**
   * Unique identifier for the request. 
   * @member {String} requestId
   */
  exports.prototype['requestId'] = undefined;
  /**
   * @member {module:model/EncryptedPayload} encryptedPayload
   */
  exports.prototype['encryptedPayload'] = undefined;



  return exports;
}));


