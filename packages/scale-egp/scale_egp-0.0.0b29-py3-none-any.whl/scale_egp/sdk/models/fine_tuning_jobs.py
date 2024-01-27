from enum import Enum
from typing import Any, Dict, Literal, Optional, Union

from pydantic import BaseModel, Field

from .model_enums import ModelVendor


class LaunchFineTuningJobConfiguration(BaseModel):
    vendor: Literal[ModelVendor.LAUNCH] = Field(ModelVendor.LAUNCH)
    hyperparameters: Optional[Dict[str, Any]]
    wandb_config: Optional[Dict[str, Any]]
    suffix: Optional[str]


class OpenAIFineTuningJobConfiguration(BaseModel):
    vendor: Literal[ModelVendor.OPENAI] = Field(ModelVendor.OPENAI)
    hyperparameters: Optional[Dict[str, Any]]
    suffix: Optional[str]


class FineTuningJobVendorConfiguration(BaseModel):
    __root__: Union[LaunchFineTuningJobConfiguration, OpenAIFineTuningJobConfiguration] = Field(
        ..., discriminator="vendor"
    )


class FineTuningJobEvent(BaseModel):
    timestamp: Optional[float]
    message: str
    level: str


class FineTuningJobStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    CANCELED = "CANCELED"
