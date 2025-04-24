from sqlmodel import Session, select
from src.books.schema import BookCreateModel, BookUpdateModel
from src.books.model import BookModel
class BookService:
    def create_book(bookdata:BookCreateModel, session:Session)->BookModel:
        book_as_dict = bookdata.model_dump()
        book_to_create = BookModel(**book_as_dict)
        session.add(book_to_create)
        session.commit()
        session.refresh(book_to_create)
        return book_to_create
    
    def get_all_books(session:Session):
        statement = select(BookModel)
        all_books = session.exec(statement).all()
        return all_books
    
    def get_single_book(id:str, session:Session):
        statement = select(BookModel).where(BookModel.id == id)
        result =  session.exec(statement).first()
        return result
    
    def update_book(id:str, update_body:BookUpdateModel, session:Session):
        update_dict = update_body.model_dump()
        statement = select(BookModel).where(BookModel.id == id)
        book_to_update = session.exec(statement).first()
        for key, value in update_dict.items():
            setattr(book_to_update, key, value)
        session.commit()
        session.refresh(book_to_update)
        return book_to_update
    
    def delete_book(id:str, session:Session):
        statement = select(BookModel).where(BookModel.id == id)
        book_to_delete =  session.exec(statement).one_or_none()
        session.delete(book_to_delete)
        session.commit()
        return {"message": "Book deleted successfully"}
      

