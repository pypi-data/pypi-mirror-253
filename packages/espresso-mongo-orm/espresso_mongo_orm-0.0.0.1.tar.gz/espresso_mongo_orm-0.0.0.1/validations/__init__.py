from ...espresso_orm.exception.api_exceptions import (
    RuntimeErrorException,
)
from ...espresso_orm.fields import Field
from ...espresso_orm.utils import get_related_model


def validate_many2one(cls):
    many2one_fields = [
        (f, _field)
        for f in dir(cls)
        if isinstance(_field := getattr(cls, f), Field) and _field.__class__.__name__ == "Many2one"
    ]  # noqa: W503
    for field_name, field in many2one_fields:
        related_model = get_related_model(cls, field.model)
        if related_model is None:
            raise RuntimeErrorException(
                f"Many2one model '{field.model}' of field '{field_name}' "
                f"not found in "
                f"the system"
            )
    return True


def validate_name_priority(cls):
    field_names = [f for f in dir(cls) if isinstance(_field := getattr(cls, f), Field)]
    field_name_alias = [
        f for f in dir(cls) if isinstance(_field := getattr(cls, f), Field) and _field.is_name
    ]
    if cls._config__name_priority and all(["name" not in field_names, not field_name_alias]):
        raise RuntimeErrorException(
            f"Many2one model: '{cls.__name__}' doesn't have name " f"or alias  name field"
        )
    return True


def validate_function_field(cls):
    func_field_names = [
        (field_name, _field)
        for field_name in dir(cls)
        if isinstance(_field := getattr(cls, field_name), Field) and _field.isFunctionField
    ]

    def validate_func_value_not_none():
        not_complied_func_field_sets = [(fn, f) for fn, f in func_field_names if f.func is None]
        if not_complied_func_field_sets:
            raise RuntimeErrorException(
                ", ".join(
                    [
                        f"\n{'#'*50} "
                        f"\nModel: '{cls.__name__}' "
                        f"\nField name: '{fn}'"
                        f"\nField type {_field.__class__.__name__}"
                        f"\n\033[91m`func` attribute is required \033[0m"
                        f"\n{'#'*50} "
                        for fn, f in not_complied_func_field_sets
                    ]
                )
            )

    def validate_target_func_existence():
        if not all(
            [type(getattr(cls, f.func)).__name__ == "function" for fn, f in func_field_names]
        ):
            raise RuntimeErrorException(
                ", ".join(
                    [
                        f"\n{'#'*50} "
                        f"\nModel: '{cls.__name__}' "
                        f"\nField name: '{fn}'"
                        f"\nField type {_field.__class__.__name__}"
                        f"\nFunction name: \033[91m'{f.func}' does not exit\033[0m"
                        f"\n{'#'*50} "
                        for fn, f in func_field_names
                        if type(getattr(cls, f.func)).__name__ != "function"
                    ]
                )
            )

    validate_func_value_not_none()
    validate_target_func_existence()

    return True
