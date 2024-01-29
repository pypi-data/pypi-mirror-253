import os
from temporalio.client import Client


API_KEY_ENV = "API_KEY"
API_KEY_MD_KEY = "durable_api_key"


async def get_client(api_key: str=None) -> Client:
    if not api_key and API_KEY_ENV in os.environ:
        api_key = os.environ[API_KEY_ENV]

    if not api_key:
        raise KeyError("Durable SDK could not find API key")

    # TODO: Remove specific namespace
    return await Client.connect("localhost:7233", namespace='65b1872cdb6ba5ac49fc5274', rpc_metadata={
        API_KEY_MD_KEY: api_key
    })
