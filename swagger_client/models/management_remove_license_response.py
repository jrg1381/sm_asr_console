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


class ManagementRemoveLicenseResponse(object):
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
        'transcription_secs_returned': 'int'
    }

    attribute_map = {
        'transcription_secs_returned': 'transcription_secs_returned'
    }

    def __init__(self, transcription_secs_returned=None):  # noqa: E501
        """ManagementRemoveLicenseResponse - a model defined in Swagger"""  # noqa: E501

        self._transcription_secs_returned = None
        self.discriminator = None

        if transcription_secs_returned is not None:
            self.transcription_secs_returned = transcription_secs_returned

    @property
    def transcription_secs_returned(self):
        """Gets the transcription_secs_returned of this ManagementRemoveLicenseResponse.  # noqa: E501


        :return: The transcription_secs_returned of this ManagementRemoveLicenseResponse.  # noqa: E501
        :rtype: int
        """
        return self._transcription_secs_returned

    @transcription_secs_returned.setter
    def transcription_secs_returned(self, transcription_secs_returned):
        """Sets the transcription_secs_returned of this ManagementRemoveLicenseResponse.


        :param transcription_secs_returned: The transcription_secs_returned of this ManagementRemoveLicenseResponse.  # noqa: E501
        :type: int
        """

        self._transcription_secs_returned = transcription_secs_returned

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
        if not isinstance(other, ManagementRemoveLicenseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
