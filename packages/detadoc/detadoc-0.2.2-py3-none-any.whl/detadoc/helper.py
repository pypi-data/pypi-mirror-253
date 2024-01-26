import re
from typing import Any

from starlette.requests import Request
from starlette.responses import RedirectResponse

from detadoc.models import Patient


async def check_session_user(request: Request):
    if not request.session.get('user'):
        return RedirectResponse('/login')

async def get_patient(request: Request):
    return await Patient.fetch_instance(
            request.path_params.get('patient_key', request.query_params.get('patient_key'))
    )

