from cloudshell.shell.standards.pdu.autoload_model import PDUResourceModel, PowerSocket


def test_resource_model(api):
    resource_name = "resource name"
    shell_name = "shell name"
    family_name = "CS_PDU"

    resource = PDUResourceModel(resource_name, shell_name, family_name, api)

    assert resource.family_name == family_name
    assert resource.shell_name == shell_name
    assert resource.name == resource_name
    assert repr(resource.relative_address) == ""
    assert resource.resource_model == "GenericResource"
    assert resource.cloudshell_model_name == f"{shell_name}.{resource.resource_model}"

    assert resource.entities.PowerSocket == PowerSocket

    assert isinstance(resource.unique_identifier, str)
    assert resource.unique_identifier
