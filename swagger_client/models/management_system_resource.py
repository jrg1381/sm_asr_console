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


class ManagementSystemResource(object):
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
        'r_id': 'str',
        'percentage': 'float'
    }

    attribute_map = {
        'r_id': 'rId',
        'percentage': 'percentage'
    }

    def __init__(self, r_id=None, percentage=None):  # noqa: E501
        """ManagementSystemResource - a model defined in Swagger"""  # noqa: E501

        self._r_id = None
        self._percentage = None
        self.discriminator = None

        if r_id is not None:
            self.r_id = r_id
        if percentage is not None:
            self.percentage = percentage

    @property
    def r_id(self):
        """Gets the r_id of this ManagementSystemResource.  # noqa: E501


        :return: The r_id of this ManagementSystemResource.  # noqa: E501
        :rtype: str
        """
        return self._r_id

    @r_id.setter
    def r_id(self, r_id):
        """Sets the r_id of this ManagementSystemResource.


        :param r_id: The r_id of this ManagementSystemResource.  # noqa: E501
        :type: str
        """

        self._r_id = r_id

    @property
    def percentage(self):
        """Gets the percentage of this ManagementSystemResource.  # noqa: E501


        :return: The percentage of this ManagementSystemResource.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this ManagementSystemResource.


        :param percentage: The percentage of this ManagementSystemResource.  # noqa: E501
        :type: float
        """

        self._percentage = percentage

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
        if not isinstance(other, ManagementSystemResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other