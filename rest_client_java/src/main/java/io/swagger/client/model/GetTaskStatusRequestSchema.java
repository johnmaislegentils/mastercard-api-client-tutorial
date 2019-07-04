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
 * GetTaskStatusRequestSchema
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-05-29T13:19:04.981+01:00")
public class GetTaskStatusRequestSchema {
  @SerializedName("responseHost")
  private String responseHost = null;

  @SerializedName("requestId")
  private String requestId = null;

  @SerializedName("tokenRequestorId")
  private String tokenRequestorId = null;

  @SerializedName("taskId")
  private String taskId = null;

  public GetTaskStatusRequestSchema responseHost(String responseHost) {
    this.responseHost = responseHost;
    return this;
  }

   /**
   * The host that originated the request. Future calls in the same conversation may be routed to this host. 
   * @return responseHost
  **/
  @ApiModelProperty(example = "site2.payment-app-provider.com", value = "The host that originated the request. Future calls in the same conversation may be routed to this host. ")
  public String getResponseHost() {
    return responseHost;
  }

  public void setResponseHost(String responseHost) {
    this.responseHost = responseHost;
  }

  public GetTaskStatusRequestSchema requestId(String requestId) {
    this.requestId = requestId;
    return this;
  }

   /**
   * Unique identifier for the request. 
   * @return requestId
  **/
  @ApiModelProperty(example = "123456", required = true, value = "Unique identifier for the request. ")
  public String getRequestId() {
    return requestId;
  }

  public void setRequestId(String requestId) {
    this.requestId = requestId;
  }

  public GetTaskStatusRequestSchema tokenRequestorId(String tokenRequestorId) {
    this.tokenRequestorId = tokenRequestorId;
    return this;
  }

   /**
   * Identifies the Token Requestor.  __Length:11__ 
   * @return tokenRequestorId
  **/
  @ApiModelProperty(example = "98765432101", value = "Identifies the Token Requestor.  __Length:11__ ")
  public String getTokenRequestorId() {
    return tokenRequestorId;
  }

  public void setTokenRequestorId(String tokenRequestorId) {
    this.tokenRequestorId = tokenRequestorId;
  }

  public GetTaskStatusRequestSchema taskId(String taskId) {
    this.taskId = taskId;
    return this;
  }

   /**
   * Unique identifier for this task. Must be an identifier previously used when requesting a task.    __Max Length:64__ 
   * @return taskId
  **/
  @ApiModelProperty(example = "123456", required = true, value = "Unique identifier for this task. Must be an identifier previously used when requesting a task.    __Max Length:64__ ")
  public String getTaskId() {
    return taskId;
  }

  public void setTaskId(String taskId) {
    this.taskId = taskId;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetTaskStatusRequestSchema getTaskStatusRequestSchema = (GetTaskStatusRequestSchema) o;
    return Objects.equals(this.responseHost, getTaskStatusRequestSchema.responseHost) &&
        Objects.equals(this.requestId, getTaskStatusRequestSchema.requestId) &&
        Objects.equals(this.tokenRequestorId, getTaskStatusRequestSchema.tokenRequestorId) &&
        Objects.equals(this.taskId, getTaskStatusRequestSchema.taskId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(responseHost, requestId, tokenRequestorId, taskId);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetTaskStatusRequestSchema {\n");
    
    sb.append("    responseHost: ").append(toIndentedString(responseHost)).append("\n");
    sb.append("    requestId: ").append(toIndentedString(requestId)).append("\n");
    sb.append("    tokenRequestorId: ").append(toIndentedString(tokenRequestorId)).append("\n");
    sb.append("    taskId: ").append(toIndentedString(taskId)).append("\n");
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

