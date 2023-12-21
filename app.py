"""This app is a tutorial"""

import asyncio

from azure.identity.aio import ClientSecretCredential
from kiota_abstractions.api_error import APIError

from msgraph import GraphServiceClient

credential = ClientSecretCredential("517c3bf7-db40-48f4-95ef-479526a937bc", 
                                    "7c37e961-b7ce-49ac-a77f-d4cb6a20edb2",
                                    "Hho8Q~6oRgDK15WDvhJzGVE5KA_m4GGYq4ftmagX")
scopes = ['https://graph.microsoft.com/.default']

client = GraphServiceClient(credential, scopes)

async def get_user_messages():
    try:
        messages = await client.users.by_user_id("AlexW@M365x86781558.OnMicrosoft.com").messages.get()

        for msg in messages.value:
            print(
                msg.subject
            )
    except Exception as e_rr:
        print(f'Error: {e_rr.error.message}')

asyncio.run(get_user_messages())