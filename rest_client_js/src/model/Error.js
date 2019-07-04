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
    root.MdesForMerchants.Error = factory(root.MdesForMerchants.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The Error model module.
   * @module model/Error
   * @version 1.2.7
   */

  /**
   * Constructs a new <code>Error</code>.
   * Only returned in the event of an error condition.
   * @alias module:model/Error
   * @class
   */
  var exports = function() {
    var _this = this;





  };

  /**
   * Constructs a <code>Error</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Error} obj Optional instance to populate.
   * @return {module:model/Error} The populated <code>Error</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('source')) {
        obj['source'] = ApiClient.convertToType(data['source'], 'String');
      }
      if (data.hasOwnProperty('description')) {
        obj['description'] = ApiClient.convertToType(data['description'], 'String');
      }
      if (data.hasOwnProperty('reasonCode')) {
        obj['reasonCode'] = ApiClient.convertToType(data['reasonCode'], 'String');
      }
      if (data.hasOwnProperty('recoverable')) {
        obj['recoverable'] = ApiClient.convertToType(data['recoverable'], 'Boolean');
      }
    }
    return obj;
  }

  /**
   * An element used to indicate the source of the issue causing this error. Must be one of   * 'MDES'  * 'INPUT'<br>   __Max Length: 32__ 
   * @member {String} source
   */
  exports.prototype['source'] = undefined;
  /**
   * Description of the reason the operation failed. See API Response Errors <br> __Max Length: 256__ 
   * @member {String} description
   */
  exports.prototype['description'] = undefined;
  /**
   * A reason code for the error that has occurred.<br> __Max Length: 100__ 
   * @member {String} reasonCode
   */
  exports.prototype['reasonCode'] = undefined;
  /**
   * Generated by the gateway to indicate if the request could presented again for processing. Either \"TRUE\" or \"FALSE\" 
   * @member {Boolean} recoverable
   */
  exports.prototype['recoverable'] = undefined;



  return exports;
}));


