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


class ManagementLicenseCode(object):
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
        'username': 'str',
        'email_address': 'str',
        'company_name': 'str',
        'license': 'str'
    }

    attribute_map = {
        'username': 'username',
        'email_address': 'email_address',
        'company_name': 'company_name',
        'license': 'license'
    }

    def __init__(self, username=None, email_address=None, company_name=None, license=None):  # noqa: E501
        """ManagementLicenseCode - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._email_address = None
        self._company_name = None
        self._license = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if email_address is not None:
            self.email_address = email_address
        if company_name is not None:
            self.company_name = company_name
        if license is not None:
            self.license = license

    @property
    def username(self):
        """Gets the username of this ManagementLicenseCode.  # noqa: E501


        :return: The username of this ManagementLicenseCode.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ManagementLicenseCode.


        :param username: The username of this ManagementLicenseCode.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email_address(self):
        """Gets the email_address of this ManagementLicenseCode.  # noqa: E501


        :return: The email_address of this ManagementLicenseCode.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this ManagementLicenseCode.


        :param email_address: The email_address of this ManagementLicenseCode.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def company_name(self):
        """Gets the company_name of this ManagementLicenseCode.  # noqa: E501


        :return: The company_name of this ManagementLicenseCode.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ManagementLicenseCode.


        :param company_name: The company_name of this ManagementLicenseCode.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def license(self):
        """Gets the license of this ManagementLicenseCode.  # noqa: E501


        :return: The license of this ManagementLicenseCode.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this ManagementLicenseCode.


        :param license: The license of this ManagementLicenseCode.  # noqa: E501
        :type: str
        """

        self._license = license

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
        if not isinstance(other, ManagementLicenseCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other