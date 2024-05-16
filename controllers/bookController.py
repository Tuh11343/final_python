from prismaConfig import get_db
from pydantic import BaseModel
from typing import Optional

from enum import Enum

class BookType(str,Enum):
    PREMIUM = "PREMIUM"
    NORMAL = "NORMAL"

class Book(BaseModel):
    id:Optional[int]=None
    name: str
    description: Optional[str] = None
    rating: int
    progress: float
    published_year: int
    image: Optional[str] = None
    language: str
    book_type: BookType
    src_audio: str
    lyric: str


async def findAll(limit: int = None, offset: int = None):
    prisma = await get_db()

    if limit is None:
        books = await prisma.book.find_many()
        return {"books": books}
    else:
        length = await prisma.book.count()
        books = await prisma.book.find_many(take=limit, skip=offset)
        return {"books": books, "length": length}


async def findByID(id: int):
    prisma = await get_db()
    book = await prisma.book.find_unique(where={"id": id})
    return {"book": book}

    # async def findByName(name:str,limit:int=None,offset:int=None):
    prisma = await get_db()

    if limit is None:
        books = await prisma.book.find_many(
            where={
                "OR": [
                    {
                        "name": {"contains": name},
                        "bookAuthor": {
                            "some": {"author": {"name": {"contains": name}}}
                        },
                    }
                ]
            },
            include={"bookAuthor": True},
        )
        return {"books": books}
    else:
        length = await prisma.book.count(
            where={
                "OR": [
                    {
                        "name": {"contains": name},
                        "bookAuthor": {
                            "some": {"author": {"name": {"contains": name}}}
                        },
                    }
                ]
            }
        )
        books = await prisma.book.find_many(
            where={
                "OR": [
                    {
                        "name": {"contains": name},
                        "bookAuthor": {
                            "some": {"author": {"name": {"contains": name}}}
                        },
                    }
                ]
            },
            take=limit,
            skip=offset,
            include={"bookAuthor": True},
        )
        return {"books": books, "length": length}


async def findByGenreID(id: int, limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        books = await prisma.book.find_many(
            where={"bookGenres": {"some": {"genre_id": id}}},
            include={"bookGenres": True},
        )
        return {"books": books}
    else:
        length = await prisma.book.count(
            where={"bookGenres": {"some": {"genre_id": id}}}
        )
        books = await prisma.book.find_many(
            where={}, take=limit, skip=offset, include={"bookGenres": True}
        )
        return {"books": books, "length": length}


async def findByAuthorID(id: int, limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        books = await prisma.book.find_many(
            where={"bookAuthor": {"some": {"author_id": id}}},
            include={"bookAuthor": True},
        )
        return {"books": books}
    else:
        length = await prisma.book.count(
            where={"bookAuthor": {"some": {"author_id": id}}}
        )
        books = await prisma.book.find_many(
            where={"bookAuthor": {"some": {"author_id": id}}},
            take=limit,
            skip=offset,
            include={"bookAuthor": True},
        )
        return {"books": books, "length": length}


async def findByFavorite(id: int, limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        books = await prisma.book.find_many(
            where={"bookFavorite": {"some": {"user_id": id}}},
            include={"bookFavorite": True},
        )
        return {"books": books}
    else:
        length = await prisma.book.count(
            where={"bookFavorite": {"some": {"user_id": id}}}
        )
        books = await prisma.book.find_many(
            where={"book": {"some": {"author_id": id}}},
            include={"bookAuthor": True},
            take=limit,
            skip=offset,
        )
        return {"books": books, "length": length}


async def findByNameAndGenre(name: str, genre_id: int, limit: int = None, offset: int = None):
    prisma = await get_db()
    
    if not name:
        if limit is None:
            books = await prisma.book.find_many(
                where={
                    "bookGenres": {"some": {"genre_id": genre_id}},
                },
                include={"bookGenres": True},
            )
        else:
            books = await prisma.book.find_many(
                where={
                    "bookGenres": {"some": {"genre_id": genre_id}},
                },
                include={"bookGenres": True},
                take=limit,
                skip=offset,
            )
            length = await prisma.book.count(
                where={
                    "bookGenres": {"some": {"genre_id": genre_id}},
                }
            )
            return {"books": books, "length": length}
        return {"books": books}
    
    if limit is None:
        books = await prisma.book.find_many(
            where={
                "name": {"contains": name},
                "bookGenres": {"some": {"genre_id": genre_id}},
            },
            include={"bookGenres": True},
        )
        return {"books": books}
    else:
        length = await prisma.book.count(
            where={
                "name": {"contains": name},
                "bookGenres": {"some": {"genre_id": genre_id}},
            }
        )
        books = await prisma.book.find_many(
            where={
                "name": {"contains": name},
                "bookGenres": {"some": {"genre_id": genre_id}},
            },
            include={"bookGenres": True},
            take=limit,
            skip=offset,
        )
        return {"books": books, "length": length}



async def findByName(name: str, limit: int = None, offset: int = None):
    prisma = await get_db()
    if not name:
        if limit is None:
            books = await prisma.book.find_many()
            return {"books": books}
        else:
            books = await prisma.book.find_many(take=limit, skip=offset)
            length = await prisma.book.count()
            return {"books": books, "length": length}

    if limit is None:
        books = await prisma.book.find_many(
            where={
                "name": {"contains": name},
            }
        )
        return {"books": books}
    else:
        length = await prisma.book.count(where={"name": {"contains": name}})
        books = await prisma.book.find_many(
            where={
                "name": {"contains": name},
            },
            take=limit,
            skip=offset,
        )
        return {"books": books, "length": length}


async def findNormal(limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        books = await prisma.book.find_many(where={"book_type": "NORMAL"})
        return {"books": books}
    else:
        length = await prisma.book.count(where={"book_type": "NORMAL"})
        books = await prisma.book.find_many(
            where={"book_type": "NORMAL"}, take=limit, skip=offset
        )
        return {"books": books, "length": length}


async def findPremium(limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        books = await prisma.book.find_many(where={"book_type": "PREMIUM"})
        return {"books": books}
    else:
        length = await prisma.book.count(where={"book_type": "PREMIUM"})
        books = await prisma.book.find_many(
            where={"book_type": "PREMIUM"}, take=limit, skip=offset
        )
        return {"books": books, "length": length}


async def findTopRating(limit: int = None, offset: int = None):
    prisma = await get_db()
    if limit is None:
        books = await prisma.book.find_many(order={"rating": "desc"})
        return {"books": books}
    else:
        length = await prisma.book.find_many(order={"rating": "desc"})
        books = await prisma.book.find_many(
            order={"rating": "desc"}, take=limit, skip=offset
        )
        return {"books": books, "length": length}


async def delete(id: int):
    prisma = await get_db()
    foundBook = await prisma.book.find_unique(where={"id": id})
    if foundBook is None:
        return {"book": None}
    else:
        deletedBook = await prisma.book.delete(where={"id": id})
        return {"book": deletedBook}


async def update(book: Book):
    prisma = await get_db()
    foundBook = await prisma.book.find_unique(where={"id": book.id})
    if foundBook is None:
        return {"book": None}
    else:
        updatedBook = await prisma.book.update(where={"id": book.id}, data=dict(book))
    return {"book": updatedBook}


async def create(book: Book):
    prisma = await get_db()
    createdBook = await prisma.book.create(data=book.dict(exclude_none=True))
    return {"book": createdBook}
