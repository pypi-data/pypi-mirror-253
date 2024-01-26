# MODULES
from typing import (
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    Sequence,
)

# CONTEXTLIB
from contextlib import AbstractContextManager

# SQLALCHEMY
from sqlalchemy import ColumnExpressionArgument, Row, Select, and_, insert, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, InstrumentedAttribute

# DECORATORS
from pysql_repo.decorators import with_session

# UTILS
from pysql_repo.utils import (
    _FilterType,
    RelationshipOption,
    build_select_stmt,
    get_filters,
    select_distinct,
    apply_pagination,
)


_T = TypeVar("_T", bound=declarative_base())


class Repository:
    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[Session]],
    ) -> None:
        self._session_factory = session_factory

    def session_manager(self):
        return self._session_factory()

    def _build_query_paginate(
        self,
        session: Session,
        stmt: Select[Tuple[_T]],
        model: Type[_T],
        page: int,
        per_page: int,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        group_by: Optional[ColumnExpressionArgument] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[Union[List[str], str]] = None,
        limit: int = None,
    ) -> Tuple[Select[Tuple[_T]], str]:
        stmt = build_select_stmt(
            stmt=stmt,
            model=model,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            group_by=group_by,
            order_by=order_by,
            direction=direction,
            limit=limit,
        )

        return apply_pagination(
            session=session,
            stmt=stmt,
            page=page,
            per_page=per_page,
        )

    @with_session()
    def _select(
        self,
        model: Type[_T],
        distinct: Optional[ColumnExpressionArgument] = None,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        session: Optional[Session] = None,
    ) -> Optional[_T]:
        stmt = select_distinct(
            model=model,
            expr=distinct,
        )

        return self._select_stmt(
            stmt=stmt,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            session=session,
        )

    @with_session()
    def _select_stmt(
        self,
        stmt: Select[Tuple[_T]],
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        group_by: Optional[ColumnExpressionArgument] = None,
        session: Optional[Session] = None,
    ) -> Optional[_T]:
        stmt = build_select_stmt(
            stmt=stmt,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            group_by=group_by,
        )

        return session.execute(stmt).unique().scalar_one_or_none()

    @with_session()
    def _select_all(
        self,
        model: Type[_T],
        distinct: Optional[List[ColumnExpressionArgument]] = None,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[str] = None,
        limit: int = None,
        session: Optional[Session] = None,
    ) -> Sequence[_T]:
        stmt = select_distinct(
            model=model,
            expr=distinct,
        )

        return self._select_all_stmt(
            stmt=stmt,
            model=model,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            order_by=order_by,
            direction=direction,
            limit=limit,
            session=session,
        )

    @with_session()
    def _select_all_stmt(
        self,
        stmt: Select[Tuple[_T]],
        model: Type[_T],
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        group_by: Optional[ColumnExpressionArgument] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[Union[List[str], str]] = None,
        limit: int = None,
        session: Optional[Session] = None,
    ) -> Sequence[_T]:
        stmt = build_select_stmt(
            stmt=stmt,
            model=model,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            group_by=group_by,
            order_by=order_by,
            direction=direction,
            limit=limit,
        )

        return session.execute(stmt).scalars().unique().all()

    @with_session()
    def _select_paginate(
        self,
        model: Type[_T],
        page: int,
        per_page: int,
        distinct: Optional[ColumnExpressionArgument] = None,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[str] = None,
        limit: int = None,
        session: Optional[Session] = None,
    ) -> Tuple[Sequence[_T], str]:
        stmt = select_distinct(
            model=model,
            expr=distinct,
        )

        return self._select_paginate_stmt(
            stmt=stmt,
            model=model,
            page=page,
            per_page=per_page,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            order_by=order_by,
            direction=direction,
            limit=limit,
            session=session,
        )

    @with_session()
    def _select_paginate_stmt(
        self,
        stmt: Select[Tuple[_T]],
        model: Type[_T],
        page: int,
        per_page: int,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        group_by: Optional[ColumnExpressionArgument] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[str] = None,
        limit: int = None,
        session: Optional[Session] = None,
    ) -> Tuple[Sequence[_T], str]:
        stmt, pagination = self._build_query_paginate(
            session=session,
            stmt=stmt,
            model=model,
            page=page,
            per_page=per_page,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            group_by=group_by,
            order_by=order_by,
            direction=direction,
            limit=limit,
        )

        return session.execute(stmt).scalars().unique().all(), pagination

    @with_session()
    def _update_all(
        self,
        model: Type[_T],
        values: Dict,
        filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        flush: bool = False,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> Sequence[_T]:
        sequence = self._select_all(
            model=model,
            filters=filters,
            relationship_options=relationship_options,
            session=session,
        )
        for item in sequence:
            for key, value in values.items():
                setattr(item, key, value)

        if flush:
            session.flush()
        if commit:
            session.commit()

        [session.refresh(item) for item in sequence]

        return sequence

    @with_session()
    def _update(
        self,
        model: Type[_T],
        values: Dict,
        filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        flush: bool = False,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> _T:
        item = self._select(
            model=model,
            filters=filters,
            relationship_options=relationship_options,
            session=session,
        )

        for key, value in values.items():
            setattr(item, key, value)

        if flush:
            session.flush()
        if commit:
            session.commit()

        session.refresh(item)

        return item

    @with_session()
    def _add_all(
        self,
        data: Iterable[_T],
        flush: bool = False,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> Iterable[_T]:
        session.add_all(data)
        if flush:
            session.flush()
        if commit:
            session.commit()

        if flush or commit:
            [session.refresh(item) for item in data]

        return data

    @with_session()
    def _add(
        self,
        data: _T,
        flush: bool = False,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> _T:
        session.add(data)
        if flush:
            session.flush()
        if commit:
            session.commit()

        if flush or commit:
            session.refresh(data)

        return data

    @with_session()
    def _delete(
        self,
        model: Type[_T],
        filters: Optional[_FilterType] = None,
        flush: bool = True,
        commit: bool = False,
        session: Optional[Session] = None,
    ) -> bool:
        rows = self._select_all(
            model=model,
            filters=filters,
            session=session,
        )

        if len(rows) == 0:
            return False

        for row in rows:
            session.delete(row)

        if flush:
            session.flush()
        if commit:
            session.commit()

        return True
