from stock.config.config import get_config_from_yaml, Config
from stock.config.key_vault import KeyvaultClient

def test_get_config_from_yaml():
    config = get_config_from_yaml()
    assert config['key-vault']['name'] == 'keyvault-account'

def test_key_vault_get_sceret():
    config = Config()
    uri = f"https://{config.get('key-vault.name')}.vault.azure.net"
    client = KeyvaultClient(uri)
    assert "test-value" == client.get_secret_value('mock-test-value')