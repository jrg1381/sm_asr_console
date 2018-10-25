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

from swagger_client.models.internalservices_job import InternalservicesJob  # noqa: F401,E501
from swagger_client.models.internalservices_transcription_config import InternalservicesTranscriptionConfig  # noqa: F401,E501


class InternalservicesJobInfo(object):
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
        'base': 'InternalservicesJob',
        'config': 'InternalservicesTranscriptionConfig'
    }

    attribute_map = {
        'base': 'base',
        'config': 'config'
    }

    def __init__(self, base=None, config=None):  # noqa: E501
        """InternalservicesJobInfo - a model defined in Swagger"""  # noqa: E501

        self._base = None
        self._config = None
        self.discriminator = None

        if base is not None:
            self.base = base
        if config is not None:
            self.config = config

    @property
    def base(self):
        """Gets the base of this InternalservicesJobInfo.  # noqa: E501


        :return: The base of this InternalservicesJobInfo.  # noqa: E501
        :rtype: InternalservicesJob
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this InternalservicesJobInfo.


        :param base: The base of this InternalservicesJobInfo.  # noqa: E501
        :type: InternalservicesJob
        """

        self._base = base

    @property
    def config(self):
        """Gets the config of this InternalservicesJobInfo.  # noqa: E501


        :return: The config of this InternalservicesJobInfo.  # noqa: E501
        :rtype: InternalservicesTranscriptionConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this InternalservicesJobInfo.


        :param config: The config of this InternalservicesJobInfo.  # noqa: E501
        :type: InternalservicesTranscriptionConfig
        """

        self._config = config

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
        if not isinstance(other, InternalservicesJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
