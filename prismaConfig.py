from prisma import Prisma

async def get_db():
    prisma = Prisma()
    await prisma.connect()
    return prisma
    # try:
    #     return prisma
    # finally:
    #     await prisma.disconnect()