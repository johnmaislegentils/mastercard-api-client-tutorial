# coding: utf-8

"""
    MDES for Merchants

    The MDES APIs are designed as RPC style stateless web services where each API endpoint represents an operation to be performed.  All request and response payloads are sent in the JSON (JavaScript Object Notation) data-interchange format. Each endpoint in the API specifies the HTTP Method used to access it. All strings in request and response objects are to be UTF-8 encoded.  Each API URI includes the major and minor version of API that it conforms to.  This will allow multiple concurrent versions of the API to be deployed simultaneously.    # noqa: E501

    OpenAPI spec version: 1.2.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SearchTokensApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_tokens(self, **kwargs):  # noqa: E501
        """Used to get basic token information for all tokens on a specified device, or all tokens mapped to the given Account PAN.  # noqa: E501

        This API is used to get basic token information for all tokens on a specified device, or all tokens mapped to the given Account PAN. It may be used to check current Token(s) state or, in exception scenarios (such as network time out), to ensure that external systems remain in sync with the Token state as maintained by MDES. Deactivated tokens are not returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_tokens(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchTokensRequestSchema search_tokens_request_schema: Contains the details of the request message. 
        :return: SearchTokensResponseSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_tokens_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_tokens_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_tokens_with_http_info(self, **kwargs):  # noqa: E501
        """Used to get basic token information for all tokens on a specified device, or all tokens mapped to the given Account PAN.  # noqa: E501

        This API is used to get basic token information for all tokens on a specified device, or all tokens mapped to the given Account PAN. It may be used to check current Token(s) state or, in exception scenarios (such as network time out), to ensure that external systems remain in sync with the Token state as maintained by MDES. Deactivated tokens are not returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_tokens_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchTokensRequestSchema search_tokens_request_schema: Contains the details of the request message. 
        :return: SearchTokensResponseSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_tokens_request_schema']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_tokens" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_tokens_request_schema' in params:
            body_params = params['search_tokens_request_schema']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/digitization/static/1/0/searchTokens', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchTokensResponseSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
