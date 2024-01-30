from typing import Any, Mapping, Optional, Sequence, Union

from airflow.models import BaseOperator
from airflow.models.xcom import XCOM_RETURN_KEY

from conveyor.secrets import SecretValue as SecretValue


class ConveyorContainerOperatorV2(BaseOperator):
    def __init__(
        self,
        *,
        instance_type: Optional[str] = None,
        airflow_worker_instance_type: Optional[str] = None,
        validate_docker_image_exists=True,
        image: str = "{{ macros.conveyor.default_image(dag) }}",
        cmds: Optional[Sequence[str]] = None,
        arguments: Optional[Sequence[str]] = None,
        env_vars: Optional[Mapping[str, Union[str, SecretValue]]] = None,
        aws_role: Optional[str] = None,
        azure_application_client_id: Optional[str] = None,
        instance_life_cycle: Optional[str] = None,
        disk_size: Optional[int] = None,
        disk_mount_path: str = "/var/data",
        xcom_push: bool = False,
        xcom_key: str = XCOM_RETURN_KEY,
        **kwargs,
    ) -> None:
        ...


class ConveyorSparkSubmitOperatorV2(BaseOperator):
    def __init__(
        self,
        *,
        application: str = "",
        application_args: Optional[Sequence[Any]] = None,
        conf: Optional[Mapping[str, str]] = None,
        java_class: Optional[str] = None,
        num_executors: Optional[int] = None,
        spark_main_version: int = 2,
        validate_docker_image_exists=True,
        driver_instance_type: Optional[str] = None,
        executor_instance_type: Optional[str] = None,
        aws_role: Optional[str] = None,
        azure_application_client_id: Optional[str] = None,
        image: str = "{{ macros.conveyor.default_image(dag) }}",
        env_vars: Optional[Mapping[str, Union[str, SecretValue]]] = None,
        instance_life_cycle: Optional[str] = None,
        airflow_worker_instance_type: Optional[str] = None,
        s3_committer: Optional[str] = None,
        abfs_committer: Optional[str] = None,
        executor_disk_size: Optional[int] = None,
        mode: Optional[str] = None,
        aws_availability_zone: Optional[str] = None,
        verbose: bool = False,
        **kwargs,
    ) -> None:
        ...
