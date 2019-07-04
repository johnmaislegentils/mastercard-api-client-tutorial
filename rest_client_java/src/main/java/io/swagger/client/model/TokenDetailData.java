/*
 * MDES for Merchants
 * The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously.  
 *
 * OpenAPI spec version: 1.2.7
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * TokenDetailData
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-05-29T13:19:04.981+01:00")
public class TokenDetailData {
  @SerializedName("tokenNumber")
  private String tokenNumber = null;

  @SerializedName("expiryMonth")
  private String expiryMonth = null;

  @SerializedName("expiryYear")
  private String expiryYear = null;

  @SerializedName("dataValidUntilTimestamp")
  private String dataValidUntilTimestamp = null;

  @SerializedName("paymentAccountReference")
  private String paymentAccountReference = null;

  public TokenDetailData tokenNumber(String tokenNumber) {
    this.tokenNumber = tokenNumber;
    return this;
  }

   /**
   * Globally unique identifier for the Token, as assigned by MDES.     __Max Length:64__ 
   * @return tokenNumber
  **/
  @ApiModelProperty(example = "1234435456134525612451341", value = "Globally unique identifier for the Token, as assigned by MDES.     __Max Length:64__ ")
  public String getTokenNumber() {
    return tokenNumber;
  }

  public void setTokenNumber(String tokenNumber) {
    this.tokenNumber = tokenNumber;
  }

  public TokenDetailData expiryMonth(String expiryMonth) {
    this.expiryMonth = expiryMonth;
    return this;
  }

   /**
   * The expiry month for the account. 
   * @return expiryMonth
  **/
  @ApiModelProperty(example = "09", value = "The expiry month for the account. ")
  public String getExpiryMonth() {
    return expiryMonth;
  }

  public void setExpiryMonth(String expiryMonth) {
    this.expiryMonth = expiryMonth;
  }

  public TokenDetailData expiryYear(String expiryYear) {
    this.expiryYear = expiryYear;
    return this;
  }

   /**
   * The expiry year for the account. 
   * @return expiryYear
  **/
  @ApiModelProperty(example = "21", value = "The expiry year for the account. ")
  public String getExpiryYear() {
    return expiryYear;
  }

  public void setExpiryYear(String expiryYear) {
    this.expiryYear = expiryYear;
  }

  public TokenDetailData dataValidUntilTimestamp(String dataValidUntilTimestamp) {
    this.dataValidUntilTimestamp = dataValidUntilTimestamp;
    return this;
  }

   /**
   * \&quot;The date/time after which this CardInfoData object is considered invalid. If present, all systems must reject this CardInfoData object after this time and treat it as invalid data. Must be expressed in ISO 8601 extended format as one of the following: YYYY-MM-DDThh:mm:ss[.sss]Z YYYY-MM-DDThh:mm:ss[.sss]�hh:mm Where [.sss] is optional and can be 1 to 3 digits. Must be a value no more than 30 days in the future. MasterCard recommends using a value of (Current Time + 30 minutes).\&quot; 
   * @return dataValidUntilTimestamp
  **/
  @ApiModelProperty(example = "YYYY-MM-DDThh:mm:ss[.sss]Z", value = "\"The date/time after which this CardInfoData object is considered invalid. If present, all systems must reject this CardInfoData object after this time and treat it as invalid data. Must be expressed in ISO 8601 extended format as one of the following: YYYY-MM-DDThh:mm:ss[.sss]Z YYYY-MM-DDThh:mm:ss[.sss]�hh:mm Where [.sss] is optional and can be 1 to 3 digits. Must be a value no more than 30 days in the future. MasterCard recommends using a value of (Current Time + 30 minutes).\" ")
  public String getDataValidUntilTimestamp() {
    return dataValidUntilTimestamp;
  }

  public void setDataValidUntilTimestamp(String dataValidUntilTimestamp) {
    this.dataValidUntilTimestamp = dataValidUntilTimestamp;
  }

  public TokenDetailData paymentAccountReference(String paymentAccountReference) {
    this.paymentAccountReference = paymentAccountReference;
    return this;
  }

   /**
   * \&quot;The unique account reference assigned to the PAN. Conditionally returned if the Token Requestor has opted to receive PAR and providing PAR is assigned by Mastercard or the Issuer provides PAR in the authorization message response.    __Max Length:__ - 29\&quot; 
   * @return paymentAccountReference
  **/
  @ApiModelProperty(example = "5001a9f027e5629d11e3949a0800a", value = "\"The unique account reference assigned to the PAN. Conditionally returned if the Token Requestor has opted to receive PAR and providing PAR is assigned by Mastercard or the Issuer provides PAR in the authorization message response.    __Max Length:__ - 29\" ")
  public String getPaymentAccountReference() {
    return paymentAccountReference;
  }

  public void setPaymentAccountReference(String paymentAccountReference) {
    this.paymentAccountReference = paymentAccountReference;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TokenDetailData tokenDetailData = (TokenDetailData) o;
    return Objects.equals(this.tokenNumber, tokenDetailData.tokenNumber) &&
        Objects.equals(this.expiryMonth, tokenDetailData.expiryMonth) &&
        Objects.equals(this.expiryYear, tokenDetailData.expiryYear) &&
        Objects.equals(this.dataValidUntilTimestamp, tokenDetailData.dataValidUntilTimestamp) &&
        Objects.equals(this.paymentAccountReference, tokenDetailData.paymentAccountReference);
  }

  @Override
  public int hashCode() {
    return Objects.hash(tokenNumber, expiryMonth, expiryYear, dataValidUntilTimestamp, paymentAccountReference);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TokenDetailData {\n");
    
    sb.append("    tokenNumber: ").append(toIndentedString(tokenNumber)).append("\n");
    sb.append("    expiryMonth: ").append(toIndentedString(expiryMonth)).append("\n");
    sb.append("    expiryYear: ").append(toIndentedString(expiryYear)).append("\n");
    sb.append("    dataValidUntilTimestamp: ").append(toIndentedString(dataValidUntilTimestamp)).append("\n");
    sb.append("    paymentAccountReference: ").append(toIndentedString(paymentAccountReference)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

