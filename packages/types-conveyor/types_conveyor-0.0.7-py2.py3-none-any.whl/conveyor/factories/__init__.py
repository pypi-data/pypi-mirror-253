from typing import Mapping, Optional, Sequence, Tuple, Union

from airflow import DAG as DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.log.logging_mixin import LoggingMixin
from airflow.utils.task_group import TaskGroup

from conveyor.secrets import SecretValue as SecretValue


class ConveyorDbtTaskFactory(LoggingMixin):
    def __init__(
        self,
        *,
        manifest_file: str = "manifest.json",
        task_name_prefix: Optional[str] = None,
        task_name_suffix: Optional[str] = None,
        task_cmd: Sequence[str] = (),
        task_arguments: Sequence[str] = (
            "--no-use-colors",
            "{command}",
            "--target",
            "{{ macros.conveyor.env() }}",
            "--profiles-dir",
            "./..",
            "--select",
            "{model}",
        ),
        task_instance_type: str = "mx.micro",
        airflow_worker_instance_type: Optional[str] = None,
        task_instance_life_cycle: Optional[str] = None,
        task_aws_role: Optional[str] = None,
        task_azure_application_client_id: Optional[str] = None,
        task_env_vars: Optional[Mapping[str, Union[str, SecretValue]]] = None,
        start_task_name_override: Optional[str] = None,
        end_task_name_override: Optional[str] = None,
    ) -> None:
        ...

    def add_tasks_to_dag(
        self,
        dag: DAG,
        *,
        tags: Sequence[str] = ...,
        any_tag: bool = ...,
        test_tasks: bool = ...,
    ) -> Tuple[EmptyOperator, EmptyOperator]:
        ...

    def add_tasks_to_task_group(
        self,
        dag: DAG,
        *,
        task_group_name: str = ...,
        test_task_group_name: str = ...,
        tags: Sequence[str] = ...,
        any_tag: bool = ...,
    ) -> Tuple[TaskGroup, TaskGroup]:
        ...
