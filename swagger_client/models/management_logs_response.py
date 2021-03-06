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


class ManagementLogsResponse(object):
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
        'count': 'str',
        'name': 'str',
        'log_lines': 'str'
    }

    attribute_map = {
        'count': 'count',
        'name': 'name',
        'log_lines': 'log_lines'
    }

    def __init__(self, count=None, name=None, log_lines=None):  # noqa: E501
        """ManagementLogsResponse - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._name = None
        self._log_lines = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if name is not None:
            self.name = name
        if log_lines is not None:
            self.log_lines = log_lines

    @property
    def count(self):
        """Gets the count of this ManagementLogsResponse.  # noqa: E501


        :return: The count of this ManagementLogsResponse.  # noqa: E501
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ManagementLogsResponse.


        :param count: The count of this ManagementLogsResponse.  # noqa: E501
        :type: str
        """

        self._count = count

    @property
    def name(self):
        """Gets the name of this ManagementLogsResponse.  # noqa: E501


        :return: The name of this ManagementLogsResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ManagementLogsResponse.


        :param name: The name of this ManagementLogsResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def log_lines(self):
        """Gets the log_lines of this ManagementLogsResponse.  # noqa: E501


        :return: The log_lines of this ManagementLogsResponse.  # noqa: E501
        :rtype: str
        """
        return self._log_lines

    @log_lines.setter
    def log_lines(self, log_lines):
        """Sets the log_lines of this ManagementLogsResponse.


        :param log_lines: The log_lines of this ManagementLogsResponse.  # noqa: E501
        :type: str
        """

        self._log_lines = log_lines

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
        if not isinstance(other, ManagementLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
