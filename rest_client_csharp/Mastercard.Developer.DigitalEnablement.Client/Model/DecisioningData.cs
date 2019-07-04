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
    /// DecisioningData
    /// </summary>
    [DataContract]
    public partial class DecisioningData :  IEquatable<DecisioningData>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DecisioningData" /> class.
        /// </summary>
        /// <param name="recommendation">__(OPTIONAL)__ &lt;br&gt; Digitization decision recommended by the Token Requestor. Must be either APPROVED (Recommend a decision of Approved), DECLINED (Recommend a decision of Decline). &lt;br&gt;   __Max Length:64__ .</param>
        /// <param name="recommendationAlgorithmVersion">__(OPTIONAL)__ &lt;br&gt; Version of the algorithm used by the Token Requestor to determine its recommendation. Must be a value of \&quot;01\&quot;. Other values may be supported in the future.&lt;br&gt;     __Max Length:16__ .</param>
        /// <param name="deviceScore">__(OPTIONAL)__ &lt;br&gt; Score assigned by the Token Requestor for the target device being provisioned. Must be a value from 1 to 5. .</param>
        /// <param name="accountScore">__(OPTIONAL)__ &lt;br&gt; Score assigned by the Token Requestor for the consumer account or relationship. Must be a value from 1 to 5. .</param>
        /// <param name="recommendationReasons">__(OPTIONAL)__ &lt;br&gt; Code indicating the reasons the Token Requestor is suggesting the digitization decision.  See table here - https://developer.mastercard.com/page/mdes-digitization-recommendation-reason-codes .</param>
        /// <param name="deviceCurrentLocation">__(OPTIONAL)__ &lt;br&gt; Latitude and longitude in the format \&quot;(sign) latitude, (sign) longitude\&quot; with a precision of 2 decimal places.  Ex - \&quot;38.63, -90.25\&quot;  Latitude is between -90 and 90.  Longitude between -180 and 180. Relates to the target device being provisioned. If there is no target device, then this should be the current consumer location, if available. &lt;br&gt;    __Max Length:14__ .</param>
        /// <param name="deviceIpAddress">__(OPTIONAL)__ &lt;br&gt; The IP address of the device through which the device reaches the internet. This may be a temporary or permanent IP address assigned to a home router, or the IP address of a gateway through which the device connects to a network. IPv4 address format of 4 octets separated by \&quot;.\&quot; Ex - 127.0.0.1 Relates to the target device being provisioned. If there is no target device, then this should be the current consumer IP address, if available.&lt;br&gt;     __Max Length:15__ .</param>
        /// <param name="mobileNumberSuffix">__(OPTIONAL)__&lt;br&gt; The last few digits (typically four) of the consumer&#39;s mobile phone number as available on file or on the consumer&#39;s current device, which may or may not be the mobile number of the target device being provisioned.&lt;br&gt;     __Max Length:32__ .</param>
        /// <param name="accountIdHash">__(OPTIONAL)__ &lt;br&gt; SHA-256 hash of the Cardholder’s account ID with the Token Requestor. Typically expected to be an email address.&lt;br&gt;  __Max Length:64__ Alpha-Numeric and Hex-encoded data (case-insensitive). .</param>
        public DecisioningData(string recommendation = default(string), string recommendationAlgorithmVersion = default(string), string deviceScore = default(string), string accountScore = default(string), List<string> recommendationReasons = default(List<string>), string deviceCurrentLocation = default(string), string deviceIpAddress = default(string), string mobileNumberSuffix = default(string), string accountIdHash = default(string))
        {
            this.Recommendation = recommendation;
            this.RecommendationAlgorithmVersion = recommendationAlgorithmVersion;
            this.DeviceScore = deviceScore;
            this.AccountScore = accountScore;
            this.RecommendationReasons = recommendationReasons;
            this.DeviceCurrentLocation = deviceCurrentLocation;
            this.DeviceIpAddress = deviceIpAddress;
            this.MobileNumberSuffix = mobileNumberSuffix;
            this.AccountIdHash = accountIdHash;
        }
        
        /// <summary>
        /// __(OPTIONAL)__ &lt;br&gt; Digitization decision recommended by the Token Requestor. Must be either APPROVED (Recommend a decision of Approved), DECLINED (Recommend a decision of Decline). &lt;br&gt;   __Max Length:64__ 
        /// </summary>
        /// <value>__(OPTIONAL)__ &lt;br&gt; Digitization decision recommended by the Token Requestor. Must be either APPROVED (Recommend a decision of Approved), DECLINED (Recommend a decision of Decline). &lt;br&gt;   __Max Length:64__ </value>
        [DataMember(Name="recommendation", EmitDefaultValue=false)]
        public string Recommendation { get; set; }

        /// <summary>
        /// __(OPTIONAL)__ &lt;br&gt; Version of the algorithm used by the Token Requestor to determine its recommendation. Must be a value of \&quot;01\&quot;. Other values may be supported in the future.&lt;br&gt;     __Max Length:16__ 
        /// </summary>
        /// <value>__(OPTIONAL)__ &lt;br&gt; Version of the algorithm used by the Token Requestor to determine its recommendation. Must be a value of \&quot;01\&quot;. Other values may be supported in the future.&lt;br&gt;     __Max Length:16__ </value>
        [DataMember(Name="recommendationAlgorithmVersion", EmitDefaultValue=false)]
        public string RecommendationAlgorithmVersion { get; set; }

        /// <summary>
        /// __(OPTIONAL)__ &lt;br&gt; Score assigned by the Token Requestor for the target device being provisioned. Must be a value from 1 to 5. 
        /// </summary>
        /// <value>__(OPTIONAL)__ &lt;br&gt; Score assigned by the Token Requestor for the target device being provisioned. Must be a value from 1 to 5. </value>
        [DataMember(Name="deviceScore", EmitDefaultValue=false)]
        public string DeviceScore { get; set; }

        /// <summary>
        /// __(OPTIONAL)__ &lt;br&gt; Score assigned by the Token Requestor for the consumer account or relationship. Must be a value from 1 to 5. 
        /// </summary>
        /// <value>__(OPTIONAL)__ &lt;br&gt; Score assigned by the Token Requestor for the consumer account or relationship. Must be a value from 1 to 5. </value>
        [DataMember(Name="accountScore", EmitDefaultValue=false)]
        public string AccountScore { get; set; }

        /// <summary>
        /// __(OPTIONAL)__ &lt;br&gt; Code indicating the reasons the Token Requestor is suggesting the digitization decision.  See table here - https://developer.mastercard.com/page/mdes-digitization-recommendation-reason-codes 
        /// </summary>
        /// <value>__(OPTIONAL)__ &lt;br&gt; Code indicating the reasons the Token Requestor is suggesting the digitization decision.  See table here - https://developer.mastercard.com/page/mdes-digitization-recommendation-reason-codes </value>
        [DataMember(Name="recommendationReasons", EmitDefaultValue=false)]
        public List<string> RecommendationReasons { get; set; }

        /// <summary>
        /// __(OPTIONAL)__ &lt;br&gt; Latitude and longitude in the format \&quot;(sign) latitude, (sign) longitude\&quot; with a precision of 2 decimal places.  Ex - \&quot;38.63, -90.25\&quot;  Latitude is between -90 and 90.  Longitude between -180 and 180. Relates to the target device being provisioned. If there is no target device, then this should be the current consumer location, if available. &lt;br&gt;    __Max Length:14__ 
        /// </summary>
        /// <value>__(OPTIONAL)__ &lt;br&gt; Latitude and longitude in the format \&quot;(sign) latitude, (sign) longitude\&quot; with a precision of 2 decimal places.  Ex - \&quot;38.63, -90.25\&quot;  Latitude is between -90 and 90.  Longitude between -180 and 180. Relates to the target device being provisioned. If there is no target device, then this should be the current consumer location, if available. &lt;br&gt;    __Max Length:14__ </value>
        [DataMember(Name="deviceCurrentLocation", EmitDefaultValue=false)]
        public string DeviceCurrentLocation { get; set; }

        /// <summary>
        /// __(OPTIONAL)__ &lt;br&gt; The IP address of the device through which the device reaches the internet. This may be a temporary or permanent IP address assigned to a home router, or the IP address of a gateway through which the device connects to a network. IPv4 address format of 4 octets separated by \&quot;.\&quot; Ex - 127.0.0.1 Relates to the target device being provisioned. If there is no target device, then this should be the current consumer IP address, if available.&lt;br&gt;     __Max Length:15__ 
        /// </summary>
        /// <value>__(OPTIONAL)__ &lt;br&gt; The IP address of the device through which the device reaches the internet. This may be a temporary or permanent IP address assigned to a home router, or the IP address of a gateway through which the device connects to a network. IPv4 address format of 4 octets separated by \&quot;.\&quot; Ex - 127.0.0.1 Relates to the target device being provisioned. If there is no target device, then this should be the current consumer IP address, if available.&lt;br&gt;     __Max Length:15__ </value>
        [DataMember(Name="deviceIpAddress", EmitDefaultValue=false)]
        public string DeviceIpAddress { get; set; }

        /// <summary>
        /// __(OPTIONAL)__&lt;br&gt; The last few digits (typically four) of the consumer&#39;s mobile phone number as available on file or on the consumer&#39;s current device, which may or may not be the mobile number of the target device being provisioned.&lt;br&gt;     __Max Length:32__ 
        /// </summary>
        /// <value>__(OPTIONAL)__&lt;br&gt; The last few digits (typically four) of the consumer&#39;s mobile phone number as available on file or on the consumer&#39;s current device, which may or may not be the mobile number of the target device being provisioned.&lt;br&gt;     __Max Length:32__ </value>
        [DataMember(Name="mobileNumberSuffix", EmitDefaultValue=false)]
        public string MobileNumberSuffix { get; set; }

        /// <summary>
        /// __(OPTIONAL)__ &lt;br&gt; SHA-256 hash of the Cardholder’s account ID with the Token Requestor. Typically expected to be an email address.&lt;br&gt;  __Max Length:64__ Alpha-Numeric and Hex-encoded data (case-insensitive). 
        /// </summary>
        /// <value>__(OPTIONAL)__ &lt;br&gt; SHA-256 hash of the Cardholder’s account ID with the Token Requestor. Typically expected to be an email address.&lt;br&gt;  __Max Length:64__ Alpha-Numeric and Hex-encoded data (case-insensitive). </value>
        [DataMember(Name="accountIdHash", EmitDefaultValue=false)]
        public string AccountIdHash { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DecisioningData {\n");
            sb.Append("  Recommendation: ").Append(Recommendation).Append("\n");
            sb.Append("  RecommendationAlgorithmVersion: ").Append(RecommendationAlgorithmVersion).Append("\n");
            sb.Append("  DeviceScore: ").Append(DeviceScore).Append("\n");
            sb.Append("  AccountScore: ").Append(AccountScore).Append("\n");
            sb.Append("  RecommendationReasons: ").Append(RecommendationReasons).Append("\n");
            sb.Append("  DeviceCurrentLocation: ").Append(DeviceCurrentLocation).Append("\n");
            sb.Append("  DeviceIpAddress: ").Append(DeviceIpAddress).Append("\n");
            sb.Append("  MobileNumberSuffix: ").Append(MobileNumberSuffix).Append("\n");
            sb.Append("  AccountIdHash: ").Append(AccountIdHash).Append("\n");
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
            return this.Equals(input as DecisioningData);
        }

        /// <summary>
        /// Returns true if DecisioningData instances are equal
        /// </summary>
        /// <param name="input">Instance of DecisioningData to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DecisioningData input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Recommendation == input.Recommendation ||
                    (this.Recommendation != null &&
                    this.Recommendation.Equals(input.Recommendation))
                ) && 
                (
                    this.RecommendationAlgorithmVersion == input.RecommendationAlgorithmVersion ||
                    (this.RecommendationAlgorithmVersion != null &&
                    this.RecommendationAlgorithmVersion.Equals(input.RecommendationAlgorithmVersion))
                ) && 
                (
                    this.DeviceScore == input.DeviceScore ||
                    (this.DeviceScore != null &&
                    this.DeviceScore.Equals(input.DeviceScore))
                ) && 
                (
                    this.AccountScore == input.AccountScore ||
                    (this.AccountScore != null &&
                    this.AccountScore.Equals(input.AccountScore))
                ) && 
                (
                    this.RecommendationReasons == input.RecommendationReasons ||
                    this.RecommendationReasons != null &&
                    this.RecommendationReasons.SequenceEqual(input.RecommendationReasons)
                ) && 
                (
                    this.DeviceCurrentLocation == input.DeviceCurrentLocation ||
                    (this.DeviceCurrentLocation != null &&
                    this.DeviceCurrentLocation.Equals(input.DeviceCurrentLocation))
                ) && 
                (
                    this.DeviceIpAddress == input.DeviceIpAddress ||
                    (this.DeviceIpAddress != null &&
                    this.DeviceIpAddress.Equals(input.DeviceIpAddress))
                ) && 
                (
                    this.MobileNumberSuffix == input.MobileNumberSuffix ||
                    (this.MobileNumberSuffix != null &&
                    this.MobileNumberSuffix.Equals(input.MobileNumberSuffix))
                ) && 
                (
                    this.AccountIdHash == input.AccountIdHash ||
                    (this.AccountIdHash != null &&
                    this.AccountIdHash.Equals(input.AccountIdHash))
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
                if (this.Recommendation != null)
                    hashCode = hashCode * 59 + this.Recommendation.GetHashCode();
                if (this.RecommendationAlgorithmVersion != null)
                    hashCode = hashCode * 59 + this.RecommendationAlgorithmVersion.GetHashCode();
                if (this.DeviceScore != null)
                    hashCode = hashCode * 59 + this.DeviceScore.GetHashCode();
                if (this.AccountScore != null)
                    hashCode = hashCode * 59 + this.AccountScore.GetHashCode();
                if (this.RecommendationReasons != null)
                    hashCode = hashCode * 59 + this.RecommendationReasons.GetHashCode();
                if (this.DeviceCurrentLocation != null)
                    hashCode = hashCode * 59 + this.DeviceCurrentLocation.GetHashCode();
                if (this.DeviceIpAddress != null)
                    hashCode = hashCode * 59 + this.DeviceIpAddress.GetHashCode();
                if (this.MobileNumberSuffix != null)
                    hashCode = hashCode * 59 + this.MobileNumberSuffix.GetHashCode();
                if (this.AccountIdHash != null)
                    hashCode = hashCode * 59 + this.AccountIdHash.GetHashCode();
                return hashCode;
            }
        }
    }

}
