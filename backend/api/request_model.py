predict_single_request = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "body": {"type": "string"},
        "required": ["title", "body"]
    }
}

predict_single_response = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "className": {
                "type": "string"
            },
            "bestClass": {
                "type": "boolean"
            },
            "point": {
                "type": "number",
                "minimum": 0.0,
                "maximum": 1.0
            }
        }
    }
}

predict_multiple_schema = {
    "type": "array",
    "properties": {
        
    }
}