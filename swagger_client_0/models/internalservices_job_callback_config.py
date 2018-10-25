# coding: utf-8

"""
    Speechmatics Management API

    Speechmatics offer a secure Management REST API that enables you to programatically control the lifecycle of the appliance, including stopping and rebooting the appliance, restarting services, licensing the appliance and controlling the available resources.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.internalservices_callback_format import InternalservicesCallbackFormat  # noqa: F401,E501


class InternalservicesJobCallbackConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        'format': 'InternalservicesCallbackFormat'
    }

    attribute_map = {
        'url': 'url',
        'format': 'format'
    }

    def __init__(self, url=None, format=None):  # noqa: E501
        """InternalservicesJobCallbackConfig - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._format = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if format is not None:
            self.format = format

    @property
    def url(self):
        """Gets the url of this InternalservicesJobCallbackConfig.  # noqa: E501


        :return: The url of this InternalservicesJobCallbackConfig.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InternalservicesJobCallbackConfig.


        :param url: The url of this InternalservicesJobCallbackConfig.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def format(self):
        """Gets the format of this InternalservicesJobCallbackConfig.  # noqa: E501


        :return: The format of this InternalservicesJobCallbackConfig.  # noqa: E501
        :rtype: InternalservicesCallbackFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this InternalservicesJobCallbackConfig.


        :param format: The format of this InternalservicesJobCallbackConfig.  # noqa: E501
        :type: InternalservicesCallbackFormat
        """

        self._format = format

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InternalservicesJobCallbackConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
