"""
Functions and schemas relating to specification 214, for level 0 FITS files.

This submodule generates a hybrid spec 122 / spec 214 schema for level 0 files
ingested by the data center.
"""
from typing import Any, Optional

from dkist_fits_specifications import spec122, spec214
from dkist_fits_specifications.spec122 import update_122_schema_requiredness
from dkist_fits_specifications.spec214 import expand_214_schema
from dkist_fits_specifications.utils import (
    frozendict,
    raw_schema_type_hint,
    schema_type_hint,
)

__all__ = ["load_level0_spec214"]


def rename_only_spec214(schema: raw_schema_type_hint, **header: dict[str, Any]) -> schema_type_hint:
    """
    Parse a 214 schema and filter out all keys which do not have a type of rename.
    """
    new_schema = {}
    for key, key_schema in schema[1].items():
        if "rename" in key_schema:
            new_schema[key] = key_schema

    preprocessed_schema = spec214.preprocess_schema((schema[0], new_schema), include_level0=True)
    return process_level0_spec214_section(preprocessed_schema, **header)


def spec214_key_lookup(
    spec_122_schemas: dict[str, schema_type_hint] = None,
    raw_214_schemas: dict[str, raw_schema_type_hint] = None,
) -> dict[str, tuple[str, str, str]]:
    """
    Generate a mapping of the level 0 214 name to a tuple of (122_key, 122_section, 214_section)
    """
    # If custom schemas are not passed, load the full schemas
    if spec_122_schemas is None:
        spec_122_schemas = spec122.load_processed_spec122()
    if raw_214_schemas is None:
        raw_214_schemas = spec214.load_raw_spec214()

    spec_214_122_map = {}

    for section_214, schema_214 in raw_214_schemas.items():
        combined_schema = {
            name: {**schema_214[0]["spec214"], **schema} for name, schema in schema_214[1].items()
        }
        for key_214, key_schema in combined_schema.items():
            name_122 = key_schema.get("rename")
            if name_122 is not None:
                section_122 = key_schema["section_122"]
                spec_214_122_map[key_214] = (name_122, section_122, section_214)

    return spec_214_122_map


def spec214_122_key_map(
    spec_122_schemas: dict[str, schema_type_hint] = None,
    raw_214_schemas: dict[str, raw_schema_type_hint] = None,
) -> dict[str, str]:
    """
    Generate a mapping of level0 214 key to 122 for translation of a 122 header.
    """
    return {
        key: value[0]
        for key, value in spec214_key_lookup(spec_122_schemas, raw_214_schemas).items()
    }


def load_level0_spec214(
    glob: Optional[str] = None, **header: dict[str, Any]
) -> dict[str, schema_type_hint]:
    """
    Return the loaded schemas for Level 0 214 files.

    This schema is a superset of the 122 schemas, with all 214 key schemas
    added if the 214 key is a rename of a 122 key.
    """

    spec_122_schemas = spec122.load_processed_spec122(glob, **header)
    raw_214_schemas = spec214.load_raw_spec214(glob)

    spec_214_122_map = spec214_key_lookup(spec_122_schemas, raw_214_schemas)

    level0_schemas = {}

    for key_214, (key_122, section_122, section_214) in spec_214_122_map.items():
        rename_214 = rename_only_spec214(raw_214_schemas[section_214], **header)
        schema_122 = spec_122_schemas[section_122]
        level0_schemas[section_214] = {**schema_122, **rename_214}

    return frozendict(level0_schemas)


def process_level0_spec214_section(
    schema: schema_type_hint, **header: dict[str, Any]
) -> schema_type_hint:
    """
    Apply expansions and requiredness to a single section of the level0 214 schema.

    We take the conditional requiredness from 122 (because the headers haven't been processed yet and are therefore
    missing some of the keys needed for full 214 conditional requirdness) and the expansions from 214.
    """
    schema = update_122_schema_requiredness(schema, **header)
    schema = expand_214_schema(schema, **header)

    return schema
