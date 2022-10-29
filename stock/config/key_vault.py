from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


class KeyvaultCache:
    def __init__(self, config):
        self.cache = dict()
        self.config = config
        self.load()

    def load(self):
        keyvault_name = self.config.get('key-vault.name')
        uri = f"https://{keyvault_name}.vault.azure.net"
        keyvault_client = KeyvaultClient(uri)

        secret_names = self.config.get("key-vault.secrets")
        for secret_name in secret_names:
            value = keyvault_client.get_secret_value(secret_name)
            self.cache.update({secret_name: value})

    def get(self, key):
        return self.cache.get(key)


class KeyvaultClient:
    def __init__(self, url):
        credential = DefaultAzureCredential()
        self.__secret_client = SecretClient(
            vault_url=url, credential=credential)

    def get_secret_value(self, name):
        secret_bundle = self.__secret_client.get_secret(name)
        return secret_bundle.value
