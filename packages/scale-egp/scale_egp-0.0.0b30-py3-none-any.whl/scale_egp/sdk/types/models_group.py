from datetime import datetime
from typing import Optional
from pydantic import Field
from scale_egp.utils.model_utils import BaseModel, Entity

class ModelGroup(Entity):
    """
    Entity for grouping models which are tied to the base model. E.g.: gpt-4 can be a group containing all gpt-4 fine-tuned models

    Attributes:
        id: The unique identifier of the entity.
        name: The name of the group
        base_model_id: The ID of the account that owns the given entity.
        base_model_metadata: Metadata of the base model in a JSON format.
    """

    name: str
    description: str
    base_model_id: Optional[str] = Field(None)
    base_model_metadata: Optional[str] = Field(None)
    id: str = Field(..., description="The unique identifier of the entity.")
    created_at: datetime = Field(
        ..., description="The date and time when the entity was created in ISO format."
    )
    account_id: str = Field(..., description="The ID of the account that owns the given entity.")
    created_by_user_id: str = Field(..., description="The user who originally created the entity.")



class ModelGroupRequest(BaseModel):
    name: str
    description: Optional[str]
    base_model_id: Optional[str] = Field(None, description="The ID of the model that is grouping all its related models")
    base_model_metadata: Optional[str] = Field(None)
    account_id: str = Field(..., description="The ID of the account that owns the given entity.")
