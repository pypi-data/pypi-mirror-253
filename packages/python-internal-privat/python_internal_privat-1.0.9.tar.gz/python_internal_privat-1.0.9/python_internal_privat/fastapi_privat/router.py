from typing import Dict
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_privat.database import async_session
from fastapi_privat.schemas import (
    PrivatSchema,
    PrivatSchemaPayment,
    PrivatSchemaUpdate,
)
from async_privat.manager import AsyncPrivatManager
from fastapi_privat import crud


router = APIRouter(tags=["Privat"])


@router.post("/add-privat")
async def add_privatbank(
    schema: PrivatSchema, session: AsyncSession = Depends(async_session)
) -> Dict:
    try:
        return await crud.create_privat(schema, session)
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.put("/change-privat")
async def change_privatbank(
    user_id: str,
    schema: PrivatSchemaUpdate,
    session: AsyncSession = Depends(async_session),
) -> Dict:
    try:
        return await crud.update_privat(user_id, schema, session)
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.delete("/delete-privat")
async def delete_privatbank(
    user_id: str, session: AsyncSession = Depends(async_session)
) -> Dict:
    try:
        return await crud.delete_privat(user_id, session)
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/currencies")
async def currencies(cashe_rate: bool) -> Dict:
    try:
        mng = AsyncPrivatManager()
        return await mng.get_currencies(cashe_rate)
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/client_info")
async def client_info(
    user_id: str, session: AsyncSession = Depends(async_session)
) -> Dict:
    try:
        mng = AsyncPrivatManager()
        payload = await crud.read_privat(user_id, session)
        if payload is not None:
            mng.token = payload[0].privat_token
            mng.iban = payload[0].privat_iban
            return await mng.get_client_info()
        return mng.does_not_exsists_exception()
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/balance")
async def balance(user_id: str, session: AsyncSession = Depends(async_session)) -> Dict:
    try:
        mng = AsyncPrivatManager()
        payload = await crud.read_privat(user_id, session)
        if payload is not None:
            mng.token = payload[0].privat_token
            mng.iban = payload[0].privat_iban
            return await mng.get_balance()
        return mng.does_not_exsists_exception()
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.get("/statement")
async def statement(
    user_id: str,
    period: int,
    limit: int,
    session: AsyncSession = Depends(async_session),
) -> Dict:
    try:
        mng = AsyncPrivatManager()
        payload = await crud.read_privat(user_id, session)
        if payload is not None:
            mng.token = payload[0].privat_token
            mng.iban = payload[0].privat_iban
            return await mng.get_statement(period, limit)
        return mng.does_not_exsists_exception()
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception


@router.post("/payment")
async def payment(
    schema: PrivatSchemaPayment, session: AsyncSession = Depends(async_session)
) -> Dict:
    try:
        mng = AsyncPrivatManager()
        payload = await crud.read_privat(schema.user_id, session)
        if payload is not None:
            mng.token = payload[0].privat_token
            mng.iban = payload[0].privat_iban
            return await mng.create_payment(schema.recipient, schema.amount)
        return mng.does_not_exsists_exception()
    except Exception as exc:
        exception = {"detail": str(exc)}
        return exception
