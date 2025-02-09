from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional, List

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True

class BookmarkBase(BaseModel):
    title: str
    url: HttpUrl
    description: Optional[str] = None
    category_id: Optional[int] = None

class BookmarkCreate(BookmarkBase):
    pass

class Bookmark(BookmarkBase):
    id: int
    created_at: datetime
    user_id: int
    category: Optional[Category] = None

    class Config:
        from_attributes = True

class CategoryWithBookmarks(Category):
    bookmarks: List[Bookmark] = []

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    bookmarks: List[Bookmark] = []
    categories: List[Category] = []

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
