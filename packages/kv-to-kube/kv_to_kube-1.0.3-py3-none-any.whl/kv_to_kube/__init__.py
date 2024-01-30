"""kv-to-kube main module."""

from __future__ import annotations

import json
from base64 import b64encode

import click
import kr8s
from kr8s.objects import Secret
from loguru import logger
from pydantic import BaseModel, ValidationError


class KVToKubeSecret(BaseModel):
    """Object for Syncing with Kubernetes."""

    name: str
    data: dict[str, str]

class KVToKube:
    """Main application logic."""

    def __init__(self, keyvault_name: str, excluded_namespaces: list[str]) -> None:
        """Initialize KVToKube class."""
        self.keyvault_name = keyvault_name
        self.excluded_namespaces = excluded_namespaces

    def get_secrets(self) -> dict[str, KVToKubeSecret]:
        """Get secrets from Azure Key Vault, return them as a dict."""
        from azure.identity import DefaultAzureCredential
        from azure.keyvault.secrets import SecretClient

        credential = DefaultAzureCredential()
        vault_url = f"https://{self.keyvault_name}.vault.azure.net/"
        client = SecretClient(vault_url=vault_url, credential=credential)
        secrets = {}

        for secret in client.list_properties_of_secrets():
            if secret._tags is not None and secret._tags.get("kube_secret_name"):
                kube_secret_name = secret._tags.get("kube_secret_name")
                value = json.loads(SecretClient.get_secret(client, secret.name).value)
                try:
                    secrets[secret.name] = KVToKubeSecret(name=kube_secret_name, data=value)
                except ValidationError:
                    logger.warning(f"Skipping secret {secret.name} because it contains non-string values")
                    continue
        return secrets

    def get_namespaces(self) -> list[str]:
        """Get namespaces from Kubernetes, return them as a list."""
        return [
            namespace.metadata.name
            for namespace in kr8s.get("namespaces")
            if namespace.metadata.name not in self.excluded_namespaces
        ]

    def create_or_update_secret(self, namespace: str, secret_obj: KVToKubeSecret) -> None:
        """Create or update secret in Kubernetes."""
        secret_name = secret_obj.name
        secret_data = {k:b64encode(v.encode()).decode() for (k, v) in secret_obj.data.items()}
        k8s_obj = Secret(secret_name, namespace=namespace)
        if k8s_obj.exists():
            k8s_obj.refresh()
            if k8s_obj.raw["data"] != secret_data:
                logger.info(f"Deleting secret {secret_name} in namespace {namespace}")
                k8s_obj.delete()
            else:
                logger.info(f"Secret {secret_name} in namespace {namespace} is up-to-date")
                return
        logger.info(f"Creating secret {secret_name} in namespace {namespace}")
        Secret({
            "apiVersion": "v1",
            "kind": "Secret",
            "metadata": {"name": secret_name, "namespace": namespace},
            "type": "Opaque",
            "data": secret_data,
        }).create()

    def run(self) -> None:
        """Run the application."""
        namespaces = self.get_namespaces()
        secrets = self.get_secrets()

        for namespace in namespaces:
            for secret in secrets.values():
                self.create_or_update_secret(namespace, secret)

@click.command()
@click.option(
    "--keyvault-name",
    type=str,
    help="Name of the Azure Key Vault",
    required=True,
)
@click.option(
    "--excluded-namespaces",
    type=str,
    help="Namespaces to exclude",
    required=False,
    show_default=True,
    default="kv-to-kube,kube-system",
)
def cli(keyvault_name: str, excluded_namespaces: str) -> None:
    """kv-to-kube main command."""
    KVToKube(keyvault_name, excluded_namespaces.split(",")).run()

cli(max_content_width=256)
