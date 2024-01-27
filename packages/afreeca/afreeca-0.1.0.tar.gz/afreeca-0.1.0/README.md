# Afreeca

AfreecaTV API Wrapper

## Usage

```python
import asyncio
from afreeca import AfreecaTV, Chat, UserCredential

async def callback(chat: Chat):
    print(f"{chat.nickname}: {chat.message}")

async def main():
    cred = await UserCredential.login("ID", "PW")
    afreeca = AfreecaTV(credential=cred)

    chat = await afreeca.create_chat("BJ")

    chat.add_callback(callback)

    await chat.start()


asyncio.run(main())
```
