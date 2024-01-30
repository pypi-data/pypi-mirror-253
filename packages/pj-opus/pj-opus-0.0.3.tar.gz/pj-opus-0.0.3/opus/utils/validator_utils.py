from schema import Schema, SchemaError
import click
import sys

def validate_schema(obj, schema: Schema, err_msg_prefix='', skip_none=True):
    """Validates an object against a given JSON schema.

    Args:
        obj: The object to validate.
        schema: The JSON schema against which to validate the object.
        err_msg_prefix: The string to prepend to the error message if
          validation fails.
        skip_none: If True, removes fields with value None from the object
          before validation. This is useful for objects that will never contain
          None because yaml.safe_load() loads empty fields as None.

    Raises:
        ValueError: if the object does not match the schema.
    """
    if skip_none:
        obj = {k: v for k, v in obj.items() if v is not None}
    try:
        schema.validate(obj)
    except SchemaError as e:
        click.secho('{} {}'.format(err_msg_prefix, e), fg='red', nl=True)
        sys.exit(1)