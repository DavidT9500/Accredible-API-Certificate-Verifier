from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class CredentialEvent(BaseModel):
    type: Optional[str]
    data: Optional[Dict[str, Any]]

class CredentialResponse(BaseModel):
    verify: bool
    name: Optional[str]
    certification: Optional[str]
    description: Optional[str]
    issued_on: Optional[str]
    expires_on: Optional[str]
    id: Optional[str]
    blockchain_address: Optional[str]
    events: List[CredentialEvent] = []
