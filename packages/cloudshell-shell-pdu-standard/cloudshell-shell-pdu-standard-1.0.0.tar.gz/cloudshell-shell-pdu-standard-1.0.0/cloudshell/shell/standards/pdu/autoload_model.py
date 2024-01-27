import cloudshell.shell.standards.attribute_names as attribute_names
from cloudshell.shell.standards.autoload_generic_models import GenericResourceModel
from cloudshell.shell.standards.core.autoload.resource_model import (
    AbstractResource,
    ResourceAttribute,
)

__all__ = ["GenericResourceModel", "PowerSocket", "PDUResourceModel"]

from cloudshell.shell.standards.core.namespace_type import NameSpaceType


class PowerSocket(AbstractResource):
    _RESOURCE_MODEL = "PowerSocket"
    _RELATIVE_ADDRESS_PREFIX = "PS"
    _NAME_TEMPLATE = "Power Socket {}"
    _FAMILY_NAME = "CS_PowerSocket"

    # Attributes
    model_name = ResourceAttribute(
        attribute_names.MODEL_NAME, NameSpaceType.FAMILY_NAME
    )


class PDUResourceModel(GenericResourceModel):
    SUPPORTED_FAMILY_NAMES = ["CS_PDU"]
    model_name = ResourceAttribute(
        attribute_names.MODEL_NAME, NameSpaceType.FAMILY_NAME
    )

    @property
    def entities(self):
        class _PDUEntities:
            PowerSocket = PowerSocket

        return _PDUEntities

    def connect_power_socket(self, power_socket: PowerSocket) -> None:
        """Connect power socket sub resource."""
        self._add_sub_resource_with_type_restrictions(power_socket, [PowerSocket])
