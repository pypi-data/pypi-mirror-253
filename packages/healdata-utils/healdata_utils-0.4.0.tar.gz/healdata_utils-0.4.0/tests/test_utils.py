from healdata_utils import utils
import jsonschema


schema_version = {"schemaVersion": {"type": "string"}}
another_field_to_rearrange = {
    "anotherFieldToEmbed": {
        "items": {"type": "object", "properties": {"thisone": {"type": "string"}}}
    }
}
schema_to_rearrange = {
    "version": "0.2.0",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "test",
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        **schema_version,
        **another_field_to_rearrange,
        "anotherFieldToEmbed": {
            "items": {
                "type": "object",
                "properties": {"thisone": {"type": "string"}},
            }
        },
        "fields": {
            "type": "array",
            "items": {
                "properties": {
                    "type": "object",
                    "justAField": {"type": "string"},
                    **schema_version,
                    **another_field_to_rearrange,
                }
            },
        },
    },
}
def test_add_missing_fields():
    # data (note one var not in schema)
    data = [
        {"var2": 2, "var3": 3, "var1": 1},
        {
            "var5": 10,
            "var4": 9,
            "var1": 1,
        },
    ]
    # fields from schema
    fields = ["var1", "var2", "var3", "var4"]

    data_with_missing = utils.sync_fields(data, fields)
    assert data_with_missing == [
        {"var1": 1, "var2": 2, "var3": 3, "var4": None},
        {"var1": 1, "var2": None, "var3": None, "var4": 9, "var5": 10},
    ]


def test_unflatten_jsonpath():
    input = {
        "module": "Testing",
        "constraints.enum": "1|2|3|4",
        "standardsMappings[1].item.url": "http//:helloitem1",
        "standardsMappings[0].item.url": "http//:helloitem2",
        "standardsMappings[1].instrument.url": "http//:helloworld4",
        "test1.test2.test3[1]": "test3_1",
        "test1.test2.test3[0].test4": "test4_1",
    }

    output = {
        "module": "Testing",
        "constraints": {"enum": "1|2|3|4"},
        "standardsMappings": [
            {"item": {"url": "http//:helloitem2"}},
            {
                "item": {"url": "http//:helloitem1"},
                "instrument": {"url": "http//:helloworld4"},
            },
        ],
        "test1": {"test2": {"test3": [{"test4": "test4_1"}, {"test3": "test3_1"}]}},
    }
    field_json = utils.unflatten_from_jsonpath(input)
    assert (
        field_json == output
    ), "Problem with converting input dictionary to output dictionary"


input = {
    "schemaVersion": "0.2.0",
    "anotherFieldToEmbed": [{"thisone": "helloworld"}],
    "fields": [{"justAField": "cool"}, {"justAField": "sad"}],
}


def test_embed_data_dictionary_props():

    flat_root = {
        "schemaVersion": "0.2.0",
        "anotherFieldToEmbed[0].thisone": "helloworld",
    }
    flat_fields_array = [{"justAField": "cool"}, {"justAField": "sad"}]
    flat_fields = utils.embed_data_dictionary_props(flat_fields_array, flat_root, schema_to_rearrange)

    assert flat_fields.to_dict(orient="records") == [
        {
            "justAField": "cool",
            "schemaVersion": "0.2.0",
            "anotherFieldToEmbed[0].thisone": "helloworld",
        },
        {
            "justAField": "sad",
            "schemaVersion": "0.2.0",
            "anotherFieldToEmbed[0].thisone": "helloworld",
        },
    ]


def test_refactor_field_props():
    flat_fields_array = [
        {"justAField": "cool", "anotherFieldToEmbed[0].thisone": "helloworld"},
        {"justAField": "sad", "anotherFieldToEmbed[0].thisone": "helloworld"},
    ]
    flat_root, flat_fields = utils.refactor_field_props(flat_fields_array, schema_to_rearrange)

    assert flat_root.to_dict() == {"anotherFieldToEmbed[0].thisone": "helloworld"}
    assert flat_fields.to_dict(orient="records") == [
        {"justAField": "cool"},
        {"justAField": "sad"},
    ]
