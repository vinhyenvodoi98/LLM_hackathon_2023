redis = {
    "index": 11,
    "name": "Redis",
    "website": "https://redis.io/",
    "data_type": {
        "question": "Which type of data can this database store?",
        "answer": [
            "Text",
            "Number",
            "Datetime",
            "Boolean",
            "Binary",
            "JSON",
            "XML"
        ]
    },
    "unstructured_data": {
        "question": "Can this database store unstructured data?",
        "answer": true
    },
    "time_series": {
        "question": "On a scale of 1 to 5, how suitable is this database for storing time series data?",
        "answer": 3
    },
    "relationship_centric": {
        "question": "On a scale of 1 to 5, how suitable is this database suitable for storing data which have a lot of complicated relationship?",
        "answer": 1
    },
    "volume": {
        "question": "How much data this database is suitable for? Less than 1 million records is small. Within 1 million and 100 million is medium. And above 100 million records is large.",
        "answer": [
            "small",
            "medium"
        ]
    },
    "read_consistency": {
        "question": "On a scale of 1 to 5, what is the read consistency of this database?",
        "answer": 4
    },
    "complex_query_patterns": {
        "question": "On a scale of 1 to 5, how good can this database handle a lot of complex queries?",
        "answer": 2
    },
    "high_write_workloads": {
        "question": "On a scale of 1 to 5, how good can this database high-write workloads?",
        "answer": 5
    },
    "high_availability": {
        "question": "Can this database guarantee 99.9% uptime?",
        "answer": false
    },
    "open_source": {
        "question": "Do this database have open source version?",
        "answer": true
    },
    "commercial": {
        "question": "Do this database have commercial version?",
        "answer": false
    }
}
