"""This app is a tutorial"""

import asyncio

from azure.identity.aio import ClientSecretCredential
from kiota_abstractions.api_error import APIError

from msgraph import GraphServiceClient

credential = ClientSecretCredential("517c3bf7-db40-48f4-95ef-479526a937bc",
                                    "b9122b4d-9b88-4cdf-9cec-ac90c593cf05",
                                    "1W.8Q~VJ_3ak_l3TeEGKbgK2lFtm0TRra.UFjbUj")
scopes = ['https://graph.microsoft.com/.default']

client = GraphServiceClient(credential, scopes)

async def get_user_chats():
    try:
        messages = await client.users.by_user_id("AlexW@M365x86781558.OnMicrosoft.com").chats.get()

        for msg in messages.value:
            print(
                msg.topic
            )
    except Exception as e_rr:
        print(f'Error: {e_rr.error.message}')
        
asyncio.run(get_user_chats())
