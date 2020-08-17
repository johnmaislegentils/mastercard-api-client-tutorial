/**
 * MDES for Merchants
 * The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously. <br> __Authentication__ Mastercard uses OAuth 1.0a with body hash extension for authenticating the API clients. This requires every request that you send to  Mastercard to be signed with an RSA private key. A private-public RSA key pair must be generated consisting of: <br> 1 . A private key for the OAuth signature for API requests. It is recommended to keep the private key in a password-protected or hardware keystore. <br> 2. A public key is shared with Mastercard during the project setup process through either a certificate signing request (CSR) or the API Key Generator. Mastercard will use the public key to verify the OAuth signature that is provided on every API call.<br>  An OAUTH1.0a signer library is available on [GitHub](https://github.com/Mastercard/oauth1-signer-java) <br>  __Encryption__<br>  All communications between Issuer web service and the Mastercard gateway is encrypted using TLS. <br> __Additional Encryption of Sensitive Data__ In addition to the OAuth authentication, when using MDES Digital Enablement Service, any PCI sensitive and all account holder Personally Identifiable Information (PII) data must be encrypted. This requirement applies to the API fields containing encryptedData. Sensitive data is encrypted using a symmetric session (one-time-use) key. The symmetric session key is then wrapped with an RSA Public Key supplied by Mastercard during API setup phase (the Customer Encryption Key). <br>  Java Client Encryption Library available on [GitHub](https://github.com/Mastercard/client-encryption-java) 
 *
 * The version of the OpenAPI document: 1.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 *
 * OpenAPI Generator version: 4.3.1
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/AccountHolderData', 'model/CardAccountDataInbound'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./AccountHolderData'), require('./CardAccountDataInbound'));
  } else {
    // Browser globals (root is window)
    if (!root.MdesForMerchants) {
      root.MdesForMerchants = {};
    }
    root.MdesForMerchants.FundingAccountData = factory(root.MdesForMerchants.ApiClient, root.MdesForMerchants.AccountHolderData, root.MdesForMerchants.CardAccountDataInbound);
  }
}(this, function(ApiClient, AccountHolderData, CardAccountDataInbound) {
  'use strict';



  /**
   * The FundingAccountData model module.
   * @module model/FundingAccountData
   * @version 1.2.10
   */

  /**
   * Constructs a new <code>FundingAccountData</code>.
   * @alias module:model/FundingAccountData
   * @class
   */
  var exports = function() {
    var _this = this;

  };

  /**
   * Constructs a <code>FundingAccountData</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/FundingAccountData} obj Optional instance to populate.
   * @return {module:model/FundingAccountData} The populated <code>FundingAccountData</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('cardAccountData')) {
        obj['cardAccountData'] = CardAccountDataInbound.constructFromObject(data['cardAccountData']);
      }
      if (data.hasOwnProperty('accountHolderData')) {
        obj['accountHolderData'] = AccountHolderData.constructFromObject(data['accountHolderData']);
      }
      if (data.hasOwnProperty('source')) {
        obj['source'] = ApiClient.convertToType(data['source'], 'String');
      }
    }
    return obj;
  }

  /**
   * @member {module:model/CardAccountDataInbound} cardAccountData
   */
  exports.prototype['cardAccountData'] = undefined;
  /**
   * @member {module:model/AccountHolderData} accountHolderData
   */
  exports.prototype['accountHolderData'] = undefined;
  /**
   * (__Required as minimum for Tokenization__)  The source of the account. Must be one of   * ACCOUNT_ON_FILE   * ACCOUNT_ADDED_MANUALLY   * ACCOUNT_ADDED_VIA_APPLICATION  __Max Length:32__ 
   * @member {String} source
   */
  exports.prototype['source'] = undefined;



  return exports;
}));


