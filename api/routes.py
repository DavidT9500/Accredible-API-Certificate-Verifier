from fastapi import APIRouter, HTTPException
from services.credential_verifier import verify_credential_data

router = APIRouter()

@router.get("/verify/{credential_id}")
async def verify_credential(credential_id: int):
    try:
        result = await verify_credential_data(credential_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
