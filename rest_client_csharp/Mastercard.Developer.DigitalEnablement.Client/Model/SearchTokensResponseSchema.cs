/* 
 * MDES for Merchants
 *
 * The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously.  
 *
 * OpenAPI spec version: 1.2.7
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using OpenAPIDateConverter = Mastercard.Developer.DigitalEnablement.Client.Client.OpenAPIDateConverter;

namespace Mastercard.Developer.DigitalEnablement.Client.Model
{
    /// <summary>
    /// SearchTokensResponseSchema
    /// </summary>
    [DataContract]
    public partial class SearchTokensResponseSchema :  IEquatable<SearchTokensResponseSchema>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SearchTokensResponseSchema" /> class.
        /// </summary>
        /// <param name="responseHost">The host that originated the request. Future calls in the same conversation may be routed to this host. .</param>
        /// <param name="responseId">Unique identifier for the response. .</param>
        /// <param name="tokens">tokens.</param>
        /// <param name="errorCode">__CONDITIONAL__&lt;br&gt; Returned in the event of and error and contains the reason the operation failed. Only use if errors object is not present.&lt;br&gt; __Max Length: 32__ .</param>
        /// <param name="errorDescription">__CONDITIONAL__&lt;br&gt; Returned in the event of and error and contains a description of why the operation failed. Only use if errors object is not present.&lt;br&gt; __Max Length: 32__   .</param>
        /// <param name="errors">errors.</param>
        public SearchTokensResponseSchema(string responseHost = default(string), string responseId = default(string), List<Token> tokens = default(List<Token>), string errorCode = default(string), string errorDescription = default(string), Error errors = default(Error))
        {
            this.ResponseHost = responseHost;
            this.ResponseId = responseId;
            this.Tokens = tokens;
            this.ErrorCode = errorCode;
            this.ErrorDescription = errorDescription;
            this.Errors = errors;
        }
        
        /// <summary>
        /// The host that originated the request. Future calls in the same conversation may be routed to this host. 
        /// </summary>
        /// <value>The host that originated the request. Future calls in the same conversation may be routed to this host. </value>
        [DataMember(Name="responseHost", EmitDefaultValue=false)]
        public string ResponseHost { get; set; }

        /// <summary>
        /// Unique identifier for the response. 
        /// </summary>
        /// <value>Unique identifier for the response. </value>
        [DataMember(Name="responseId", EmitDefaultValue=false)]
        public string ResponseId { get; set; }

        /// <summary>
        /// Gets or Sets Tokens
        /// </summary>
        [DataMember(Name="tokens", EmitDefaultValue=false)]
        public List<Token> Tokens { get; set; }

        /// <summary>
        /// __CONDITIONAL__&lt;br&gt; Returned in the event of and error and contains the reason the operation failed. Only use if errors object is not present.&lt;br&gt; __Max Length: 32__ 
        /// </summary>
        /// <value>__CONDITIONAL__&lt;br&gt; Returned in the event of and error and contains the reason the operation failed. Only use if errors object is not present.&lt;br&gt; __Max Length: 32__ </value>
        [DataMember(Name="errorCode", EmitDefaultValue=false)]
        public string ErrorCode { get; set; }

        /// <summary>
        /// __CONDITIONAL__&lt;br&gt; Returned in the event of and error and contains a description of why the operation failed. Only use if errors object is not present.&lt;br&gt; __Max Length: 32__   
        /// </summary>
        /// <value>__CONDITIONAL__&lt;br&gt; Returned in the event of and error and contains a description of why the operation failed. Only use if errors object is not present.&lt;br&gt; __Max Length: 32__   </value>
        [DataMember(Name="errorDescription", EmitDefaultValue=false)]
        public string ErrorDescription { get; set; }

        /// <summary>
        /// Gets or Sets Errors
        /// </summary>
        [DataMember(Name="errors", EmitDefaultValue=false)]
        public Error Errors { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class SearchTokensResponseSchema {\n");
            sb.Append("  ResponseHost: ").Append(ResponseHost).Append("\n");
            sb.Append("  ResponseId: ").Append(ResponseId).Append("\n");
            sb.Append("  Tokens: ").Append(Tokens).Append("\n");
            sb.Append("  ErrorCode: ").Append(ErrorCode).Append("\n");
            sb.Append("  ErrorDescription: ").Append(ErrorDescription).Append("\n");
            sb.Append("  Errors: ").Append(Errors).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as SearchTokensResponseSchema);
        }

        /// <summary>
        /// Returns true if SearchTokensResponseSchema instances are equal
        /// </summary>
        /// <param name="input">Instance of SearchTokensResponseSchema to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SearchTokensResponseSchema input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.ResponseHost == input.ResponseHost ||
                    (this.ResponseHost != null &&
                    this.ResponseHost.Equals(input.ResponseHost))
                ) && 
                (
                    this.ResponseId == input.ResponseId ||
                    (this.ResponseId != null &&
                    this.ResponseId.Equals(input.ResponseId))
                ) && 
                (
                    this.Tokens == input.Tokens ||
                    this.Tokens != null &&
                    this.Tokens.SequenceEqual(input.Tokens)
                ) && 
                (
                    this.ErrorCode == input.ErrorCode ||
                    (this.ErrorCode != null &&
                    this.ErrorCode.Equals(input.ErrorCode))
                ) && 
                (
                    this.ErrorDescription == input.ErrorDescription ||
                    (this.ErrorDescription != null &&
                    this.ErrorDescription.Equals(input.ErrorDescription))
                ) && 
                (
                    this.Errors == input.Errors ||
                    (this.Errors != null &&
                    this.Errors.Equals(input.Errors))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.ResponseHost != null)
                    hashCode = hashCode * 59 + this.ResponseHost.GetHashCode();
                if (this.ResponseId != null)
                    hashCode = hashCode * 59 + this.ResponseId.GetHashCode();
                if (this.Tokens != null)
                    hashCode = hashCode * 59 + this.Tokens.GetHashCode();
                if (this.ErrorCode != null)
                    hashCode = hashCode * 59 + this.ErrorCode.GetHashCode();
                if (this.ErrorDescription != null)
                    hashCode = hashCode * 59 + this.ErrorDescription.GetHashCode();
                if (this.Errors != null)
                    hashCode = hashCode * 59 + this.Errors.GetHashCode();
                return hashCode;
            }
        }
    }

}
