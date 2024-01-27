import pytest

from cloudshell.shell.standards.attribute_names import (
    CLI_CONNECTION_TYPE,
    CLI_TCP_PORT,
    CONSOLE_PASSWORD,
    CONSOLE_PORT,
    CONSOLE_SERVER_IP_ADDRESS,
    CONSOLE_USER,
    DISABLE_SNMP,
    ENABLE_PASSWORD,
    ENABLE_SNMP,
    PASSWORD,
    SESSION_CONCURRENCY_LIMIT,
    SNMP_READ_COMMUNITY,
    SNMP_V3_AUTH_PROTOCOL,
    SNMP_V3_PASSWORD,
    SNMP_V3_PRIVACY_PROTOCOL,
    SNMP_V3_PRIVATE_KEY,
    SNMP_V3_USER,
    SNMP_VERSION,
    SNMP_WRITE_COMMUNITY,
    USER,
    VRF_MANAGEMENT_NAME,
)
from cloudshell.shell.standards.resource_config_generic_models import (
    CliConnectionType,
    SnmpV3AuthProtocol,
    SnmpV3PrivProtocol,
    SnmpVersion,
)

from cloudshell.shell.standards.pdu.resource_config import PDUResourceConfig


@pytest.fixture
def attributes():
    return {
        USER: "user",
        SNMP_READ_COMMUNITY: "community",
        SNMP_WRITE_COMMUNITY: "write community",
        SNMP_V3_USER: "snmp user",
        SNMP_V3_PASSWORD: "snmp password",
        SNMP_V3_PRIVATE_KEY: "snmp private key",
        SNMP_V3_AUTH_PROTOCOL: "sha",
        SNMP_V3_PRIVACY_PROTOCOL: "DES",
        SNMP_VERSION: "v2c",
        ENABLE_SNMP: "True",
        DISABLE_SNMP: "False",
        VRF_MANAGEMENT_NAME: "vrf",
        PASSWORD: "password",
        CLI_CONNECTION_TYPE: "ssh",
        CLI_TCP_PORT: "22",
        SESSION_CONCURRENCY_LIMIT: "1",
        ENABLE_PASSWORD: "enable password",
        CONSOLE_PASSWORD: "console password",
        CONSOLE_PORT: "3322",
        CONSOLE_SERVER_IP_ADDRESS: "192.168.1.1",
        CONSOLE_USER: "console user",
    }


def test_pdu_resource_config(api, attributes, context_creator):
    shell_name = "Shell name"
    resource_name = "Resource name"
    context = context_creator(resource_name, shell_name, "CS_PDU", "NA", attributes)

    config = PDUResourceConfig.from_context(context, api)

    assert config.user == attributes[USER]
    assert config.enable_password == attributes[ENABLE_PASSWORD]
    assert config.snmp_read_community == attributes[SNMP_READ_COMMUNITY]
    assert config.snmp_write_community == attributes[SNMP_WRITE_COMMUNITY]
    assert config.snmp_v3_user == attributes[SNMP_V3_USER]
    assert config.snmp_v3_password == attributes[SNMP_V3_PASSWORD]
    assert config.snmp_v3_private_key == attributes[SNMP_V3_PRIVATE_KEY]
    assert config.snmp_v3_auth_protocol is SnmpV3AuthProtocol(
        attributes[SNMP_V3_AUTH_PROTOCOL]
    )
    assert config.snmp_v3_priv_protocol is SnmpV3PrivProtocol(
        attributes[SNMP_V3_PRIVACY_PROTOCOL]
    )
    assert config.snmp_version is SnmpVersion(attributes[SNMP_VERSION])
    assert config.enable_snmp is True
    assert config.disable_snmp is False
    assert config.vrf_management_name == attributes[VRF_MANAGEMENT_NAME]
    assert config.password == attributes[PASSWORD]
    assert config.cli_connection_type is CliConnectionType(
        attributes[CLI_CONNECTION_TYPE]
    )
    assert config.console_password == attributes[CONSOLE_PASSWORD]
    assert config.console_port == int(attributes[CONSOLE_PORT])
    assert config.console_server_ip_address == attributes[CONSOLE_SERVER_IP_ADDRESS]
    assert config.console_user == attributes[CONSOLE_USER]
