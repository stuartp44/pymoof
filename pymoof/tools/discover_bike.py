import asyncio

async def query(scanner):
    devices = await scanner.discover(
        service_uuids=[
            "6acc5540-e631-4069-944d-b8ca7598ad50",
            "8e7f1a50-087a-44c9-b292-a2c628fdd9aa",
            "6acb5520-e631-4069-944d-b8ca7598ad50",
        ],
    )
    for device in devices:
        if "6acc5540-e631-4069-944d-b8ca7598ad50" in device.metadata["uuids"]:
            print("Found SX3:", device.address)
        if "8e7f1a50-087a-44c9-b292-a2c628fdd9aa" in device.metadata["uuids"]:
            print("Found SX1/SX2:", device.address)
        if "6acb5520-e631-4069-944d-b8ca7598ad50" in device.metadata["uuids"]:
            print("Found Smart SX1:", device.address")
    print("No Vanmoof bikes found")
    
    return devices


if __name__ == "__main__":
    asyncio.run(query())
