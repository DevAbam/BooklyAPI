from fastapi import APIRouter, Depends, status, HTTPException
from src.books.schema import BookCreateModel, BookResponse,  BookUpdateModel, AllBookResponse
from sqlmodel import Session
from src.db.db_config import get_session
from src.books.service import BookService
from typing import List
from uuid import UUID

books_router = APIRouter()

@books_router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED )
def create_book(book_create_data:BookCreateModel, session:Session = Depends(get_session)):
    new_book = BookService.create_book(book_create_data,session)
    if new_book == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Error creating book")
    return {"data" : new_book}

@books_router.get("/", response_model=AllBookResponse, status_code=status.HTTP_200_OK)
def get_all_books(session:Session = Depends(get_session)):
    all_books = BookService.get_all_books(session)
    if all_books == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No book found")
    return {"data": all_books}

@books_router.get("/{id}", status_code=status.HTTP_200_OK, response_model=BookResponse)
def get_a_book(id:UUID, session:Session = Depends(get_session)):
    book =  BookService.get_single_book(id,session)
    if book == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")
    return {"data": book}

@books_router.patch("/{id}",status_code=status.HTTP_200_OK, response_model=BookResponse) 
def update_a_book(id:UUID, book_update_data:BookUpdateModel, session:Session = Depends(get_session))->dict:
    updated_book = BookService.update_book(id, book_update_data, session)
    if updated_book == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")
    return {"data": updated_book}

@books_router.delete("/{id}")
def delete_a_book(id: UUID, session: Session = Depends(get_session)) -> dict:
    result = BookService.delete_book(id, session)
    if result:
        return result 
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {id} not found"
        )
