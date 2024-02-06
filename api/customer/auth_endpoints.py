from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse

from api.depends import get_session
from exceptions import NotFoundException, AuthenticationError, AlreadyExistsException
from schemas.auth_schemas import TokenSchema, ClientLoginIn, ClientOut, ClientIn, AllowedTimeToResendCode, \
    SendCodeEmailIn, SMSRecord
from schemas.user_schemas import User, Client
from usecases.auth_usecases import client_login_usecase, send_verification_code_email_usecase

router = APIRouter()


@router.post(
    '/login/',
    status_code=status.HTTP_200_OK,
    description='Customer login',
    response_model=TokenSchema,
)
async def customer_login(
    login_in: ClientLoginIn,
    db_session: Session = Depends(get_session),
):
    try:
        return await client_login_usecase(
            db_session,
            phone_number=login_in.country_code + login_in.receiving_phone,
            password=login_in.password,
        )
    except NotFoundException as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": e.message, "error_code": e.error_code},
        )
    except AuthenticationError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": e.message, "error_code": e.error_code},
        )


@router.post(
    "/send-code/email/",
    status_code=status.HTTP_200_OK,
    description="Send code to email",
    response_model=AllowedTimeToResendCode
)
async def send_code_email(
    client_in: SendCodeEmailIn,
    db_session: Session = Depends(get_session),
):
    try:
        sms_record = SMSRecord(
            email=client_in.email
        )
        await send_verification_code_email_usecase(db_session, sms_record)
    except AlreadyExistsException as error:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": error.message, "error_code": error.error_code},
        )

#
#
# @router.post(
#     "/register/",
#     status_code=status.HTTP_201_CREATED,
#     description="Client register",
#     response_model=ClientOut,
# )
# async def create_user_and_client(
#         profile_in: ClientIn,
#         db_session: Session = Depends(get_session)
# ):
#     client = Client(
#         user=User(
#             **profile_in.model_dump(include={"username", "email", "phone"})
#         )
#     )
#     try:
#         return await create_user_usecase(db_session, client, profile_in.password)
#     except AlreadyExistsException as error:
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"message": error.message, "error_code": error.error_code},
#         )
#

