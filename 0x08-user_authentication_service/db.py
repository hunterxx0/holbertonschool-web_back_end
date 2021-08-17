"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Creates and returns a User object
        """
        u = User(email=email, hashed_password=hashed_password)
        self._session.add(u)
        self._session.commit()
        return u

    def find_user_by(self, **kwargs) -> User:
        """
        Takes in arbitrary keyword arguments
        and returns the first row found in the users table
        as filtered by the method’s input arguments.
        """
        try:
            res = self._session.query(User).filter_by(**kwargs).first()
        except TypeError:
            raise InvalidRequestError
        if res is None:
            raise NoResultFound
        return res

    def update_user(self, user_id, **kwargs) -> User:
        """
        Locate the user to update,
        then will update the user’s attributes
        as passed in the method’s arguments
        then commit changes to the database.
        """
        u = self.find_user_by(id=user_id)
        atts = User.__table__.columns
        for k, v in kwargs.items():
            if k in atts:
                setattr(u, k, v)
            else:
                raise ValueError
        self._session.commit()
