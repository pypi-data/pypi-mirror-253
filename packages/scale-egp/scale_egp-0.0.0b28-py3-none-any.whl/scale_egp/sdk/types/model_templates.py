from __future__ import annotations

from datetime import datetime
from typing import Optional, List, Dict, Literal

from pydantic import Field

from scale_egp.sdk.enums import ModelEndpointType, ModelType, ModelVendor, GPUType
from scale_egp.sdk.types.models import ParameterSchema
from scale_egp.utils.model_utils import Entity, BaseModel


class ModelBundleConfig(BaseModel):
    """
    Configuration that describes where to download the model execution code from.

    Attributes:
        registry: The docker registry to pull the image from.
        image: The docker image to pull.
        tag: The tag of the docker image to pull.
        command: The command to run when starting the model.
        env: The environment variables to set when starting the model.
        readiness_initial_delay_seconds: The number of seconds to wait before checking if the model
            is ready.
    """

    registry: str
    image: str
    tag: str
    command: List[str] = Field(default_factory=list)
    env: Dict[str, str] = Field(default_factory=dict)
    readiness_initial_delay_seconds: int = Field(120)
    streaming_command: Optional[List[str]] = Field(None)
    healthcheck_route: str = Field("/readyz")
    predict_route: str = Field("/predict")
    streaming_predict_route: Optional[str] = Field("/generate_streaming")

    @property
    def full_repository_name(self):
        return "/".join([self.registry, self.image])


class ModelEndpointConfig(BaseModel):
    """
    Configuration for a model endpoint.

    Attributes:
        cpus: The number of CPUs to allocate to each worker.
        memory: The amount of memory to allocate to each worker.
        storage: The amount of storage to allocate to each worker.
        gpus: The number of GPUs to allocate to each worker.
        min_workers: The minimum number of workers to keep running.
        max_workers: The maximum number of workers to keep running.
        per_worker: The number of requests to process per worker before shutting down.
        gpu_type: The type of GPU to allocate to each worker.
        endpoint_type: The type of endpoint to launch.
        high_priority: Whether or not to launch the endpoint with high priority.
    """

    cpus: int = Field(3)
    memory: str = Field("8Gi")
    storage: str = Field("16Gi")
    gpus: int = Field(0)
    # By default, we create model endpoints with min_workers = 0 so unused model endpoints can be
    # autoscaled down to
    # 0 workers, costing nothing.
    min_workers: int = Field(0)
    max_workers: int = Field(1)
    per_worker: int = Field(10)
    gpu_type: Optional[GPUType] = Field(None)
    endpoint_type: ModelEndpointType = Field(ModelEndpointType.ASYNC)
    high_priority: Optional[bool] = Field(False)


class LaunchVendorConfiguration(BaseModel):
    """
    Configuration for launching a model using the Launch service which is an internal and
    self-hosted service developed by Scale that deploys models on Kubernetes.

    Attributes:
        vendor: The vendor of the model template
        bundle_config: The bundle configuration of the model template
        endpoint_config: The endpoint configuration of the model template
    """

    # this field is required for forward compatibility (other providers will have different
    # "vendor" fields)
    vendor: Literal[ModelVendor.LAUNCH] = Field(ModelVendor.LAUNCH)
    bundle_config: ModelBundleConfig
    endpoint_config: Optional[ModelEndpointConfig]


# TODO: This is a copy of LaunchVendorConfiguration. Make this a discriminated union when we have
#  more than one vendor.
class ModelVendorConfiguration(LaunchVendorConfiguration):
    """
    Configuration for launching a model using the Launch service which is an internal and
    self-hosted service developed by Scale that deploys models on Kubernetes.

    Attributes:
        vendor: The vendor of the model template
        bundle_config: The bundle configuration of the model template
        endpoint_config: The endpoint configuration of the model template
    """


class ModelTemplate(Entity):
    """
    This is a template for types of models that can be quickly customized by end users.
    It allows users to upload static docker images that can run specific types of models.
    These docker images will expose parameters that can be injected at ModelAlias creation
    time to customize the functionality. A common example of this is to use a
    HuggingFace LLM template, but swap out model weights for a finetuned model.

    Attributes:
        id: The unique identifier of the entity.
        created_at: The date and time when the entity was created in ISO format.
        account_id: The ID of the account that owns the given entity.
        created_by_user_id: The user who originally created the entity.
        name: The name of the model template
        endpoint_type: The type of endpoint that the model template will create
        model_type: The type of model that the model template will create
        vendor_configuration: The vendor configuration of the model template
        model_creation_parameters_schema: The field names and types of available parameter fields
            which may be specified during model creation
        model_request_parameters_schema: The field names and types of available parameter fields
            which may be specified in a model execution API's `model_request_parameters` field.
    """

    name: str
    endpoint_type: ModelEndpointType
    model_type: ModelType
    vendor_configuration: ModelVendorConfiguration
    model_creation_parameters_schema: Optional[ParameterSchema] = Field(
        None,
        description="The field names and types of available parameter fields which may be "
        "specified during model creation",
    )
    model_request_parameters_schema: Optional[ParameterSchema] = Field(
        None,
        description="The field names and types of available parameter fields which may be "
        "specified in a model execution API's `model_request_parameters` field.",
    )
    id: str = Field(..., description="The unique identifier of the entity.")
    created_at: datetime = Field(
        ..., description="The date and time when the entity was created in ISO format."
    )
    account_id: str = Field(..., description="The ID of the account that owns the given entity.")
    created_by_user_id: str = Field(..., description="The user who originally created the entity.")


class ModelTemplateRequest(BaseModel):
    name: str
    endpoint_type: ModelEndpointType
    model_type: ModelType
    vendor_configuration: ModelVendorConfiguration
    model_creation_parameters_schema: Optional[ParameterSchema] = Field(
        None,
        description="The field names and types of available parameter fields which may be "
        "specified during model creation",
    )
    model_request_parameters_schema: Optional[ParameterSchema] = Field(
        None,
        description="The field names and types of available parameter fields which may be "
        "specified in a model execution API's `model_request_parameters` field.",
    )
    account_id: str = Field(..., description="The ID of the account that owns the given entity.")
