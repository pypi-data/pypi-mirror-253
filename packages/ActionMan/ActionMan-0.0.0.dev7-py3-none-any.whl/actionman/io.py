from typing import Callable as _Callable, get_type_hints as _get_type_hints, Type as _Type
import os as _os
import json as _json
import inspect as _inspect
import base64 as _base64

from actionman.log import Logger as _Logger, LogStatus as _LogStatus


def read_environment_variable(
    name: str,
    typ: _Type[str | bool | int | float | list | dict] = str,
    missing_ok: bool = False,
    logger: _Logger | None = None,
    log_value: bool = True,
) -> str | bool | int | float | list | dict | None:
    """
    Parse inputs from environment variables.
    """
    def log(status: _LogStatus, summary: str):
        if logger:
            logger.entry(
                status=status,
                title=f"Read environment variable '{name}'",
                summary=summary,
                details=[
                    f"Name: {name}",
                    f"Type: {typ.__name__}",
                    f"Required: {'No' if missing_ok else 'Yes'}",
                    f"Value: {value if log_value else '**REDACTED**'}"
                ],
            )
        return

    def raise_casting_error(expected_typ: str, exception: Exception | None = None):
        log(status=_LogStatus.FAIL, summary=f"Value could not be casted to {expected_typ}.")
        error_summary = f"Environment variable {name} could not be casted to {expected_typ}."
        if logger:
            logger.error(summary=error_summary)
        final_exception = TypeError(error_summary)
        if exception:
            raise final_exception from exception
        else:
            raise final_exception

    value = _os.environ.get(name)
    if value is None:
        if missing_ok:
            log(
                status=_LogStatus.SKIP,
                summary=f"Environment variable '{name}' is not set, but it is not required."
            )
            return
        else:
            log(status=_LogStatus.FAIL, summary=f"Environment variable '{name}' is not set.")
            raise ValueError(f"Environment variable '{name}' is not set.")
    if typ is str:
        if isinstance(value, str):
            value_casted = value
        else:
            try:
                value_casted = str(value)
            except Exception as e:
                raise_casting_error(expected_typ="string", exception=e)
    elif typ is bool:
        if isinstance(value, bool):
            value_casted = value
        elif isinstance(value, str) and value.lower() in ("true", "false", ""):
            value_casted = value.lower() == "true"
        else:
            raise_casting_error(expected_typ="boolean")
    elif typ is int:
        if isinstance(value, int):
            value_casted = value
        elif isinstance(value, str):
            try:
                value_casted = int(value)
            except Exception as e:
                raise_casting_error(expected_typ="integer", exception=e)
        else:
            raise_casting_error(expected_typ="integer")
    elif typ is float:
        if isinstance(value, float):
            value_casted = value
        elif isinstance(value, str):
            try:
                value_casted = float(value)
            except Exception as e:
                raise_casting_error(expected_typ="float", exception=e)
        else:
            raise_casting_error(expected_typ="float")
    elif typ is list:
        if isinstance(value, list):
            value_casted = value
        elif isinstance(value, str):
            try:
                value_casted = _json.loads(value, strict=False)
            except Exception as e:
                raise_casting_error(expected_typ="list", exception=e)
        else:
            raise_casting_error(expected_typ="list")
    elif typ is dict:
        if isinstance(value, dict):
            value_casted = value
        elif isinstance(value, str):
            try:
                value_casted = _json.loads(value, strict=False)
            except Exception as e:
                raise_casting_error(expected_typ="dict", exception=e)
        else:
            raise_casting_error(expected_typ="dict")
    else:
        raise TypeError(f"The specified type '{typ}' for environment variable '{name}' is not supported.")
    log(status=_LogStatus.PASS, summary=f"Environment variable '{name}' was read successfully.")
    return value_casted


def read_environment_variables(
    *variables_data: tuple[str, _Type[str | bool | int | float | list | dict], bool, bool],
    name_prefix: str = "",
    logger: _Logger | None = None,
    log_section_name: str = "Inputs",
) -> dict[str, str | bool | int | float | list | dict | None]:
    """
    Parse inputs from environment variables.
    """
    if logger:
        logger.section(log_section_name)
    variables = {}
    for name, typ, missing_ok, log_value in variables_data:
        variables[name] = read_environment_variable(
            name=f"{name_prefix}{name}",
            typ=typ,
            missing_ok=missing_ok,
            logger=logger,
            log_value=log_value,
        )
    if logger:
        logger.section_end()
    return variables


def read_function_args_from_environment_variables(
    function: _Callable,
    name_prefix: str = "",
    hide_args: tuple[str, ...] | list[str] = tuple(),
    ignore_params: tuple[str, ...] | list[str] = tuple(),
    logger: _Logger | None = None,
    log_section_name: str = "Inputs",
) -> dict[str, str | bool | int | float | list | dict | None]:
    """
    Parse inputs from environment variables.
    """
    if logger:
        logger.section(log_section_name.format(function=function.__qualname__))
    default_args = {
        k: v.default for k, v in _inspect.signature(function).parameters.items()
        if v.default is not _inspect.Parameter.empty
    }
    params = _get_type_hints(function)
    params.pop("return", None)
    args = {}
    for name, typ in params.items():
        if name not in ignore_params:
            arg = read_environment_variable(
                name=f"{name_prefix}{name}".upper(),
                typ=typ,
                missing_ok=name in default_args,
                logger=logger,
                log_value=name not in hide_args,
            )
            args[name] = arg if arg is not None else default_args[name]
    if logger:
        logger.section_end()
    return args


def write_github_outputs(
    kwargs: dict,
    to_env: bool = False,
    hide_args: tuple[str, ...] | list[str] = tuple(),
    logger: _Logger | None = None,
    log_title: str = "Write Step Outputs",
    log_title_env: str = "Write Environment Variables",
) -> None:

    def format_output(var_name, var_value) -> str | None:
        if isinstance(var_value, str):
            if "\n" in var_value:
                with open("/dev/urandom", "rb") as f:
                    random_bytes = f.read(15)
                random_delimeter = _base64.b64encode(random_bytes).decode("utf-8")
                return f"{var_name}<<{random_delimeter}\n{var_value}\n{random_delimeter}"
        elif isinstance(var_value, (dict, list, tuple, bool, int)):
            var_value = _json.dumps(var_value)
        else:
            return
        return f"{var_name}={var_value}"
    if logger:
        logger.section(log_title_env if to_env else log_title)
    with open(_os.environ["GITHUB_ENV" if to_env else "GITHUB_OUTPUT"], "a") as fh:
        for idx, (name, value) in enumerate(kwargs.items()):
            name_formatted = name.replace("_", "-") if not to_env else name.upper()
            title = f"Write '{name_formatted}' ({type(value).__name__})"
            value_formatted = format_output(name_formatted, value)
            if not value_formatted:
                summary = f"Invalid type {type(value)} for variable '{name_formatted}': {value}."
                error_summary = f"Failed to write output variable '{name}'."
                if logger:
                    logger.entry(
                        status=_LogStatus.FAIL,
                        title=title,
                        summary=summary,
                    )
                    logger.error(summary=error_summary, details=summary)
                raise TypeError(f"{error_summary}\n{summary}")
            print(value_formatted, file=fh)
            if logger:
                logger.entry(
                    status=_LogStatus.PASS,
                    title=title,
                    summary=(
                        f"Output variable '{name_formatted}' ({type(value).__name__}) "
                        f"was successfully written to {'environment' if to_env else 'step'} outputs."
                    ),
                    details=[value_formatted] if name not in hide_args else [],
                )
    if logger:
        logger.section_end()
    return


def write_github_summary(
    content: str,
    logger: _Logger | None = None,
    log_title: str = "Write Job Summary",
) -> None:
    with open(_os.environ["GITHUB_STEP_SUMMARY"], "a") as fh:
        print(content, file=fh)
    if logger:
        logger.entry(
            status=_LogStatus.PASS,
            title=log_title,
            summary=(
                f"Job summary ({len(content)} chars) was successfully written "
                f"to 'GITHUB_STEP_SUMMARY' environment variable."
            ),
        )
    return
