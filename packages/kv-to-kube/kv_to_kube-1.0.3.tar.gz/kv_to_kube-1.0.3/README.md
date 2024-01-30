# kv-to-kube

Syncs Azure Key Vault Secrets with a `kube_secret_name` label to Kubernetes Secrets.

## Installation

### Via Kustomize/Flux for Kubernetes

Installation via Kustomize/Flux 2.0 is the recommended installation approach for kv-to-kube, note this requires [Azure Workload Identity](https://github.com/Azure/azure-workload-identity) to be setup and working along with the respective OIDC Federated Credentials.

Create a `kustomize.yaml` file with the following content, being sure to replace `keyvault-name`, `excluded-namespaces`, and `azure.workload.identity/client-id` with your desired values:

```yaml
resources:
  - github.com/cpressland/kv-to-kube/deploy

patches:
  - target:
      kind: CronJob
    patch: |
      - op: replace
        path: /spec/jobTemplate/spec/template/spec/containers/0/command
        value:
        - kv-to-kube
        - --keyvault-name=my-keyvault
        - --excluded-namespaces=kube-system
  - target:
      kind: ServiceAccount
    patch: |
      - op: replace
        path: /metadata/annotations/azure.workload.identity~1client-id
        value: 5d4017fa-3f60-4fcb-a15c-2ffbd8081807
```

Apply this to your cluster with `kubectl apply -k .` or using Flux 2.0.

### Via Pipx

Pipx is the recommended installation method for running locally, outside of Kubernetes, note this requires `azure-cli` to be installed and working.

`pipx install kv-to-kube`

## Usage

Once the application is installed either locally or in your cluster, simply create or update secrets within your Key Vault to match the following spec:

```json
{
    "postgres_user": "lunalux",
    "postgres_pass": "asmr",
    "postgres_host": "katherina.postgres.database.azure.com"
}
```
with a tag of: `{"kube_secret_name": "azure-postgres"}`

This will create a Kubernetes Secret in all namespaces, as follows:

```json
{
    "apiVersion": "v1",
    "kind": "Secret",
    "metadata": {
        "name": "azure-postgres",
        "namespace": "default",
    },
    "data": {
        "postgres_host": "a2F0aGVyaW5hLnBvc3RncmVzLmRhdGFiYXNlLmF6dXJlLmNvbQ==",
        "postgres_pass": "YXNtcg==",
        "postgres_user": "bHVuYWx1eA=="
    },
    "type": "Opaque"
}
```

## FAQs

Q: What would I use this for?
A: I use it with Terraform. During the creation of something like a Postgres Server we store the connection details in Azure Key Vault, AKS then uses `kv-to-kube` to syncronise those secrets so they can be used in a Pods environment variables.

Q: Why does this delete and re-create secrets instead of updating them?
A: I couldn't find an elegant way to perform this operation with the `kr8s` library. I've opened an issue [here](https://github.com/kr8s-org/kr8s/issues/201), should that get a satifactory resolution I'll change this to update and provide an annotation on the secret for the last updated time. Because of this, I wouldn't recommend using this for secrets that require mounting as a volume. But if thats your use case, you should probably be using a [Secrets Store CSI Driver](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver)
