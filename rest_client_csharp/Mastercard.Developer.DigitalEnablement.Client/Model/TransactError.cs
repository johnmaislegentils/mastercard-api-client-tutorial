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
    /// Only returned in the event of an error condition for the Transact API
    /// </summary>
    [DataContract]
    public partial class TransactError :  IEquatable<TransactError>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="TransactError" /> class.
        /// </summary>
        /// <param name="source">An element used to indicate the source of the issue causing this error. Must be one of   * &#39;MDES&#39;  * &#39;INPUT&#39; &lt;br&gt; __Max Length: 32__ .</param>
        /// <param name="errorCode">A reason code or information pertaining to the error that has occurred. This will contain the error reported by the platform (e.g. authentication errors) or service (e.g. invalid TUR)&lt;br&gt; __Max Length: 100__ .</param>
        /// <param name="description">Description of the reason why the operation failed. &lt;br&gt; __Max Length: 256__ .</param>
        /// <param name="reasonCode">A reason code or information pertaining to the error that has occurred from the service (e.g. invalid TUR). See API Response Errors&lt;br&gt; __Max Length: 100__         .</param>
        /// <param name="errorDescription">__DEPRECATED__&lt;br&gt; Use description instead.&lt;br&gt; __Max Length: 100__  .</param>
        public TransactError(string source = default(string), string errorCode = default(string), string description = default(string), string reasonCode = default(string), string errorDescription = default(string))
        {
            this.Source = source;
            this.ErrorCode = errorCode;
            this.Description = description;
            this.ReasonCode = reasonCode;
            this.ErrorDescription = errorDescription;
        }
        
        /// <summary>
        /// An element used to indicate the source of the issue causing this error. Must be one of   * &#39;MDES&#39;  * &#39;INPUT&#39; &lt;br&gt; __Max Length: 32__ 
        /// </summary>
        /// <value>An element used to indicate the source of the issue causing this error. Must be one of   * &#39;MDES&#39;  * &#39;INPUT&#39; &lt;br&gt; __Max Length: 32__ </value>
        [DataMember(Name="source", EmitDefaultValue=false)]
        public string Source { get; set; }

        /// <summary>
        /// A reason code or information pertaining to the error that has occurred. This will contain the error reported by the platform (e.g. authentication errors) or service (e.g. invalid TUR)&lt;br&gt; __Max Length: 100__ 
        /// </summary>
        /// <value>A reason code or information pertaining to the error that has occurred. This will contain the error reported by the platform (e.g. authentication errors) or service (e.g. invalid TUR)&lt;br&gt; __Max Length: 100__ </value>
        [DataMember(Name="errorCode", EmitDefaultValue=false)]
        public string ErrorCode { get; set; }

        /// <summary>
        /// Description of the reason why the operation failed. &lt;br&gt; __Max Length: 256__ 
        /// </summary>
        /// <value>Description of the reason why the operation failed. &lt;br&gt; __Max Length: 256__ </value>
        [DataMember(Name="description", EmitDefaultValue=false)]
        public string Description { get; set; }

        /// <summary>
        /// A reason code or information pertaining to the error that has occurred from the service (e.g. invalid TUR). See API Response Errors&lt;br&gt; __Max Length: 100__         
        /// </summary>
        /// <value>A reason code or information pertaining to the error that has occurred from the service (e.g. invalid TUR). See API Response Errors&lt;br&gt; __Max Length: 100__         </value>
        [DataMember(Name="reasonCode", EmitDefaultValue=false)]
        public string ReasonCode { get; set; }

        /// <summary>
        /// __DEPRECATED__&lt;br&gt; Use description instead.&lt;br&gt; __Max Length: 100__  
        /// </summary>
        /// <value>__DEPRECATED__&lt;br&gt; Use description instead.&lt;br&gt; __Max Length: 100__  </value>
        [DataMember(Name="errorDescription", EmitDefaultValue=false)]
        public string ErrorDescription { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class TransactError {\n");
            sb.Append("  Source: ").Append(Source).Append("\n");
            sb.Append("  ErrorCode: ").Append(ErrorCode).Append("\n");
            sb.Append("  Description: ").Append(Description).Append("\n");
            sb.Append("  ReasonCode: ").Append(ReasonCode).Append("\n");
            sb.Append("  ErrorDescription: ").Append(ErrorDescription).Append("\n");
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
            return this.Equals(input as TransactError);
        }

        /// <summary>
        /// Returns true if TransactError instances are equal
        /// </summary>
        /// <param name="input">Instance of TransactError to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(TransactError input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Source == input.Source ||
                    (this.Source != null &&
                    this.Source.Equals(input.Source))
                ) && 
                (
                    this.ErrorCode == input.ErrorCode ||
                    (this.ErrorCode != null &&
                    this.ErrorCode.Equals(input.ErrorCode))
                ) && 
                (
                    this.Description == input.Description ||
                    (this.Description != null &&
                    this.Description.Equals(input.Description))
                ) && 
                (
                    this.ReasonCode == input.ReasonCode ||
                    (this.ReasonCode != null &&
                    this.ReasonCode.Equals(input.ReasonCode))
                ) && 
                (
                    this.ErrorDescription == input.ErrorDescription ||
                    (this.ErrorDescription != null &&
                    this.ErrorDescription.Equals(input.ErrorDescription))
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
                if (this.Source != null)
                    hashCode = hashCode * 59 + this.Source.GetHashCode();
                if (this.ErrorCode != null)
                    hashCode = hashCode * 59 + this.ErrorCode.GetHashCode();
                if (this.Description != null)
                    hashCode = hashCode * 59 + this.Description.GetHashCode();
                if (this.ReasonCode != null)
                    hashCode = hashCode * 59 + this.ReasonCode.GetHashCode();
                if (this.ErrorDescription != null)
                    hashCode = hashCode * 59 + this.ErrorDescription.GetHashCode();
                return hashCode;
            }
        }
    }

}
