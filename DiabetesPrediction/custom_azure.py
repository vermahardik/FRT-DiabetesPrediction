from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'storagefrt123' # Must be replaced by your <storage_account_name>
    account_key = 'rehp+YB+0vK9Iq10xZAFz7VdM5DUP8dTQAoXooXdCDYNJJmLYRu5l1hf+AjhfP4qdAV1XR+RGi/H+AStCvNV2A==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'storagefrt123' # Must be replaced by your storage_account_name
    account_key = 'rehp+YB+0vK9Iq10xZAFz7VdM5DUP8dTQAoXooXdCDYNJJmLYRu5l1hf+AjhfP4qdAV1XR+RGi/H+AStCvNV2A==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None