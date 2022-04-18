from pydantic import AnyUrl, BaseModel, EmailStr, validator
from typing import Any, Dict, List, Optional  # noqa: F401

class NSD_Model(BaseModel):
    id: str
    href: str
    category: Optional[str] = None
    description: Optional[str] = None