emailSchema = {
        "title": "Email Schema",
        "type" : "object",
        "properties" : {
            "to" : {"type" : "string"},
            "to_name" : {"type" : "string"},
            "from" : {"type" : "string"},
            "from_name" : {"type" : "string"},
            "subject" : {"type" : "string"},
            "body" : {"type" : "string"},
        },
        "required": ["to", "to_name","from", "from_name","subject", "body"]
    }