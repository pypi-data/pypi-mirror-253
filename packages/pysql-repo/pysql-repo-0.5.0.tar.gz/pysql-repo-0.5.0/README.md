The pysql-repo library is a Python library that is designed to use the session/repository pattern to interact with databases in Python projects. It provides a more flexible notation for running SQL queries and is built on top of SQLAlchemy, a popular Python SQL toolkit. With pysql_repo, users can write SQL queries using a new, more intuitive syntax, simplifying the process of working with SQL databases in Python and making it easier to write and maintain complex queries.

## Installing pysql-repo

To install pysql-repo, if you already have Python, you can install with:

```
pip install pysql_repo
```

## How to import pysql-repo

To access pysql-repo and its functions import it in your Python code like this:

```
from pysql_repo import Repository, Service, with_session, Operators, LoadingTechnique
from pysql_repo.utils import RelationshipOption
```

## Reading the example code

To create a repository, you just have to inherit your class from Repository.

```
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = "CITY"

    id = Column(
        "ID",
        Integer,
        primary_key=True,
        index=True,
    )
    name = Column(
        "NAME",
        String,
        index=True,
    )
    state = Column(
        "STATE",
        String,
        index=True,
    )

    addresses = relationship(
        "Address",
        back_populates="city",
    )


class Address(Base):
    __tablename__ = "ADDRESS"

    id = Column(
        "ID",
        Integer,
        primary_key=True,
        index=True,
    )
    street = Column(
        "STREET",
        String,
        index=True,
    )
    zip_code = Column(
        "ZIP_CODE",
        Integer,
        index=True,
    )
    user_id = Column(
        "USER_ID",
        Integer,
        ForeignKey("USER.ID"),
    )
    city_id = Column(
        "CITY_ID",
        Integer,
        ForeignKey("CITY.ID"),
    )

    user = relationship(
        "User",
        back_populates="addresses",
    )
    city = relationship(
        "City",
        back_populates="addresses",
    )


class User(Base):
    __tablename__ = "USER"

    id = Column(
        "ID",
        Integer,
        primary_key=True,
        index=True,
    )
    email = Column(
        "EMAIL",
        String,
        unique=True,
        index=True,
    )
    hashed_password = Column(
        "HASHED_PASSWORD",
        String,
    )
    full_name = Column(
        "FULL_NAME",
        String,
        index=True,
    )
    is_active = Column(
        "IS_ACTIVE",
        Boolean,
        default=True,
    )

    addresses = relationship(
        "Address",
        back_populates="user",
    )


class UserRepository(Repository):
    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[Session]],
    ) -> None:
        super().__init__(session_factory)

    @classmethod
    def __get_filters(
        cls,
        ids: Optional[List[int]] = None,
    ):
        return {
            User.id: {
                Operators.IN: ids,
            }
        }

    @classmethod
    def __get_relationship_options(cls):
        return {
            User.adresses: RelationshipOption(
                lazy=LoadingTechnique.JOINED,
                children={
                    Adress.city: RelationshipOption(
                        lazy=LoadingTechnique.LAZY
                    )
                },
            ),
        }

    def get_all(
        self,
        ids: Optional[List[int]] = None,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
        session: Optional[Session] = None,
    ) -> List[User]:
        users = self._select_all(
            session=session,
            model=User,
            optional_filters=self.__get_filters(
                ids=ids;
            ),
            relationship_options=self.__get_relationship_options(),
            order_by=order_by,
            direction=direction,
        )

        return users

    def get_paginate(
        self,
        page: int,
        per_page: int,
        ids: Optional[List[int]] = None,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
        session: Optional[Session] = None,
    ) -> Tuple[List[User], str]:
        users, pagination = self._select_paginate(
            page=page,
            per_page=per_page,
            model=User,
            optional_filters=self.__get_filters(
                ids=ids,
            ),
            relationship_options=self.__get_relationship_options(),
            order_by=order_by,
            direction=direction,
            session=session,
        )

        return users, pagination

    def get_by_id(
        self,
        id: int,
        session: Optional[Session] = None,
    ) -> Optional[User]:
        user = self._select(
            session=session,
            model=User,
            filters={
                User.id: {
                    Operators.EQUAL: id,
                },
            },
        )

        return user

    def get_by_email(
        self,
        email: str,
        session: Optional[Session] = None,
    ) -> Optional[User]:
        user = self._select(
            session=session,
            model=User,
            filters={
                User.email: {
                    Operators.IEQUAL: email,
                },
            },
        )

        return user

    def create(
        self,
        data: UserCreateSchema,
        flush: bool = False,
        commit: bool = True,
        session: Optional[Session] = None,
    ) -> User:
        user = self._add(
            data=User(
                **{
                    User.email.key: data.email,
                    User.hashed_password.key: data.hashed_password,
                    User.full_name.key: data.full_name,
                }
            ),
            flush=flush,
            commit=commit,
            session=session,
        )

        return user

    def patch_active(
        self,
        id: int,
        is_active: bool,
        flush: bool = False,
        commit: bool = True,
        session: Optional[Session] = None,
    ) -> User:
        user = self._update(
            session=session,
            model=User,
            values={
                User.is_active.key: is_active,
            },
            filters={
                User.id: {
                    Operators.EQUAL: id,
                },
            },
            flush=flush,
            commit=commit,
        )

        return user

    def delete(
        self,
        id: int,
        flush: bool = False,
        commit: bool = True,
        session: Optional[Session] = None,
    ) -> bool:
        is_deleted = self._delete(
            model=User,
            filters={
                User.id: {
                    Operators.EQUAL: id,
                },
            },
            flush=flush,
            commit=commit,
            session=session,
        )

        return is_deleted
```


To create a service, you just have to inherit your class from Service.

```
T = TypeVar("T", bound=UserReadSchema)

class UserService(Service[UserRepository]):

    def __init__(
            self,
            repository: UserRepository,
            logger: Logger,
    ) -> None:
        super().__init__(
            repository=repository,
            logger=logger,
        )


    @with_session()
    def get_users(
        self,
        ids: Optional[List[int]] = None,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
        schema: Type[T] = UserReadSchema,
        session: Optional[Session] = None,
    ) -> List[T]:
        users = self._repository.get_all(
            ids=ids,
            order_by=order_by,
            direction=direction,
            session=session,
        )

        return [schema.model_validate(user) for user in users]

    @with_session()
    def get_users_paginate(
        self,
        page: int,
        per_page: int,
        user_permissions: List[str],
        ids: Optional[List[int]] = None,
        order_by: Optional[List[str]] = None,
        direction: Optional[List[str]] = None,
        schema: Type[T] = RecipeInspectionFviReadSchema,
        session: Optional[Session] = None,
    ) -> Tuple[List[T], str]:
        users, pagination = self._repository.get_paginate(
            page=page,
            per_page=per_page,
            ids=ids,
            order_by=order_by,
            direction=direction,
            session=session,
        )

        return [schema.model_validate(user) for user in users], pagination


    @with_session()
    def get_user_by_id(
        self,
        id: int,
        schema: Type[T] = UserReadSchema,
        session: Optional[Session] = None,
    ) -> T:
        user = self._repository.get_by_id(
            id=id,
            session=session,
        )

        if user is None:
            raise ValueError("User not found")

        return schema.model_validate(user)

    @with_session()
    async def create_user(
        self,
        data: UserCreateSchema,
        commit: bool = True,
        schema: Type[T] = UserReadSchema,
        session: Optional[Session] = None,
    ) -> T:
        user = self._repository.get_by_email(
            email=data.email,
            session=session,
        )

        if user is not None:
            self._logger.error(
                "Unable to create new user because email already used bu another one"
            )

            raise ValueError(
                "User already exists with same email"
            )

        user = self._repository.create(
            data=data,
            flush=True,
            commit=False,
            session=session,
        )

        return schema.model_validate(user)


    @with_session()
    async def delete_user(
        self,
        id: int,
        commit: bool = True,
        session: Optional[Session] = None,
    ) -> bool:
        current_user = self._repository.get_by_id(
            id=id,
            session=session,
        )

        if current_user is None:
            raise ValueError(f"No user with {id=}")

        is_deleted = self._repository.delete(
            id=id,
            flush=True,
            commit=False,
            session=session,
        )

        if commit:
            session.commit()

        self._logger.info(
            f"User was successfully deleted"
        )

        return is_deleted
```