dyamondb = {
    "index": 11,
    "name": "Amazon DynamoDB",
    "website": "https://aws.amazon.com/dynamodb/",
    "data_type": {
        "question": "Which type of data can this database store?",
        "answer": [
        "Text",
        "Number",
        "Datetime",
        "Boolean",
        "Binary",
        "JSON",
        "GeoJSON",
        "Protobufs"
        ]
    },
    "unstructured_data": {
        "question": "Can this database store unstructured data?",
        "answer": True
    },
    "small_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is DynamoDB for storing a small set of SQL data?",
        "answer": 7
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is DynamoDB for storing a small set of time series data?",
        "answer": 8
        }
    },
    "medium_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is DynamoDB for storing a medium set of SQL data?",
        "answer": 8
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is DynamoDB for storing a medium set of time series data?",
        "answer": 9
        }
    },
    "large_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is DynamoDB for storing a large set of SQL data?",
        "answer": 9
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is DynamoDB for storing a large set of time series data?",
        "answer": 10
        }
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of DynamoDB?",
        "answer": 8
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can DynamoDB handle high-write workloads?",
        "answer": 10
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is DynamoDB?",
        "answer": 9
    },
    "open_source": {
        "question": "Do DynamoDB have open source version?",
        "answer": False
    },
    "commercial": {
        "question": "Do DynamoDB have commercial version?",
        "answer": True
    }
}
