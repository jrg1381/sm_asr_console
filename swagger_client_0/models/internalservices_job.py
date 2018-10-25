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

from swagger_client.models.internalservices_job_status import InternalservicesJobStatus  # noqa: F401,E501
from swagger_client.models.internalservices_job_type import InternalservicesJobType  # noqa: F401,E501


class InternalservicesJob(object):
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
        'status': 'InternalservicesJobStatus',
        'uuid': 'str',
        'created_at': 'str',
        'name': 'str',
        'type': 'InternalservicesJobType',
        'id': 'int',
        'metadata': 'str'
    }

    attribute_map = {
        'status': 'status',
        'uuid': 'uuid',
        'created_at': 'created_at',
        'name': 'name',
        'type': 'type',
        'id': 'id',
        'metadata': 'metadata'
    }

    def __init__(self, status=None, uuid=None, created_at=None, name=None, type=None, id=None, metadata=None):  # noqa: E501
        """InternalservicesJob - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._uuid = None
        self._created_at = None
        self._name = None
        self._type = None
        self._id = None
        self._metadata = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if uuid is not None:
            self.uuid = uuid
        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if metadata is not None:
            self.metadata = metadata

    @property
    def status(self):
        """Gets the status of this InternalservicesJob.  # noqa: E501


        :return: The status of this InternalservicesJob.  # noqa: E501
        :rtype: InternalservicesJobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InternalservicesJob.


        :param status: The status of this InternalservicesJob.  # noqa: E501
        :type: InternalservicesJobStatus
        """

        self._status = status

    @property
    def uuid(self):
        """Gets the uuid of this InternalservicesJob.  # noqa: E501


        :return: The uuid of this InternalservicesJob.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InternalservicesJob.


        :param uuid: The uuid of this InternalservicesJob.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def created_at(self):
        """Gets the created_at of this InternalservicesJob.  # noqa: E501


        :return: The created_at of this InternalservicesJob.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InternalservicesJob.


        :param created_at: The created_at of this InternalservicesJob.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this InternalservicesJob.  # noqa: E501


        :return: The name of this InternalservicesJob.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InternalservicesJob.


        :param name: The name of this InternalservicesJob.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this InternalservicesJob.  # noqa: E501


        :return: The type of this InternalservicesJob.  # noqa: E501
        :rtype: InternalservicesJobType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InternalservicesJob.


        :param type: The type of this InternalservicesJob.  # noqa: E501
        :type: InternalservicesJobType
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this InternalservicesJob.  # noqa: E501


        :return: The id of this InternalservicesJob.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InternalservicesJob.


        :param id: The id of this InternalservicesJob.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this InternalservicesJob.  # noqa: E501


        :return: The metadata of this InternalservicesJob.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InternalservicesJob.


        :param metadata: The metadata of this InternalservicesJob.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

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
        if not isinstance(other, InternalservicesJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other