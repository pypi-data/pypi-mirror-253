# MODULES
import asyncio
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
from contextlib import AbstractAsyncContextManager

# SQLALCHEMY
from sqlalchemy import ColumnExpressionArgument, Row, Select, and_, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import InstrumentedAttribute, joinedload

# DECORATORS
from pysql_repo.asyncio.async_decorator import with_async_session

# UTILS
from pysql_repo.utils import (
    _FilterType,
    RelationshipOption,
    apply_filters,
    async_apply_pagination,
    build_select_stmt,
    build_update_stmt,
    get_filters,
    select_distinct,
)
from tests.models.database.database import User


_T = TypeVar("_T", bound=declarative_base())


class AsyncRepository:
    def __init__(
        self,
        session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]],
    ) -> None:
        self._session_factory = session_factory

    def session_manager(self):
        return self._session_factory()

    async def _build_query_paginate(
        self,
        session: AsyncSession,
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

        return await async_apply_pagination(
            session=session,
            stmt=stmt,
            page=page,
            per_page=per_page,
        )

    @with_async_session()
    async def _select(
        self,
        model: Type[_T],
        distinct: Optional[ColumnExpressionArgument] = None,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        session: Optional[AsyncSession] = None,
    ) -> Optional[_T]:
        stmt = select_distinct(
            model=model,
            expr=distinct,
        )

        return await self._select_stmt(
            stmt=stmt,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            session=session,
        )

    @with_async_session()
    async def _select_stmt(
        self,
        stmt: Select[Tuple[_T]],
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        group_by: Optional[ColumnExpressionArgument] = None,
        session: Optional[AsyncSession] = None,
    ) -> Optional[Row[_T]]:
        stmt = build_select_stmt(
            stmt=stmt,
            filters=filters,
            optional_filters=optional_filters,
            relationship_options=relationship_options,
            group_by=group_by,
        )

        result = await session.execute(stmt)

        return result.unique().scalar_one_or_none()

    @with_async_session()
    async def _select_all(
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
        session: Optional[AsyncSession] = None,
    ) -> Sequence[_T]:
        stmt = select_distinct(
            model=model,
            expr=distinct,
        )

        return await self._select_all_stmt(
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

    @with_async_session()
    async def _select_all_stmt(
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
        session: Optional[AsyncSession] = None,
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

        result = await session.execute(stmt)

        return result.scalars().unique().all()

    @with_async_session()
    async def _select_paginate(
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
        session: Optional[AsyncSession] = None,
    ) -> Tuple[Sequence[_T], str]:
        stmt = select_distinct(
            model=model,
            expr=distinct,
        )

        return await self._select_paginate_stmt(
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

    @with_async_session()
    async def _select_paginate_stmt(
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
        session: Optional[AsyncSession] = None,
    ) -> Tuple[Sequence[_T], str]:
        stmt, pagination = await self._build_query_paginate(
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

        result = await session.execute(stmt)

        return result.scalars().unique().all(), pagination

    @with_async_session()
    async def _update_all(
        self,
        model: Type[_T],
        values: Dict,
        filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        flush: bool = False,
        commit: bool = False,
        session: Optional[AsyncSession] = None,
    ) -> Sequence[_T]:
        sequence = await self._select_all(
            model=model,
            filters=filters,
            relationship_options=relationship_options,
            session=session,
        )
        for item in sequence:
            for key, value in values.items():
                setattr(item, key, value)

        if flush:
            await session.flush()
        if commit:
            await session.commit()

        [await session.refresh(item) for item in sequence]

        return sequence

    @with_async_session()
    async def _update(
        self,
        model: Type[_T],
        values: Dict,
        filters: Optional[_FilterType] = None,
        relationship_options: Optional[
            Dict[InstrumentedAttribute, RelationshipOption]
        ] = None,
        flush: bool = False,
        commit: bool = False,
        session: Optional[AsyncSession] = None,
    ) -> _T:
        item = await self._select(
            model=model,
            filters=filters,
            relationship_options=relationship_options,
            session=session,
        )

        for key, value in values.items():
            setattr(item, key, value)

        if flush:
            await session.flush()
        if commit:
            await session.commit()

        await session.refresh(item)

        return item

    @with_async_session()
    async def _add_all(
        self,
        data: Iterable[_T],
        flush: bool = False,
        commit: bool = False,
        session: Optional[AsyncSession] = None,
    ) -> Iterable[_T]:
        session.add_all(data)
        if flush:
            await session.flush()
        if commit:
            await session.commit()

        if flush or commit:
            [await session.refresh(item) for item in data]

        return data

    @with_async_session()
    async def _add(
        self,
        data: _T,
        flush: bool = False,
        commit: bool = False,
        session: Optional[AsyncSession] = None,
    ) -> _T:
        session.add(data)
        if flush:
            await session.flush()
        if commit:
            await session.commit()

        if flush or commit:
            await session.refresh(data)

        return data

    @with_async_session()
    async def _delete(
        self,
        model: Type[_T],
        filters: Optional[_FilterType] = None,
        flush: bool = True,
        commit: bool = False,
        session: Optional[AsyncSession] = None,
    ) -> bool:
        rows = await self._select_all(
            model=model,
            filters=filters,
            session=session,
        )

        if len(rows) == 0:
            return False

        for row in rows:
            await session.delete(row)

        if flush:
            await session.flush()
        if commit:
            await session.commit()

        return True
