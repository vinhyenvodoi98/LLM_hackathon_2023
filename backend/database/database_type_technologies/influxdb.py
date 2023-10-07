influxdb = {
    "index": 7,
    "name": "InfluxDB",
    "website": "https://www.influxdata.com/",
    "data_type": {
        "question": "Which type of data can this database store?",
        "answer": [
            "Text",
            "Number",
            "Datetime",
            "Boolean",
        ]
    },
    "unstructured_data": {
        "question": "Can this database store unstructured data?",
        "answer": false
    },
    "time_series": {
        "question": "On a scale of 1 to 5, how suitable is this database for storing time series data?",
        "answer": 5
    },
    "relationship_centric": {
        "question": "On a scale of 0 to 5, how suitable is this database suitable for storing data which have a lot of complicated relationship?",
        "answer": 2
    },
    "volume": {
        "question": "How much data this database is suitable for? Less than 1 million records is small. Within 1 million and 100 million is medium. And above 100 million records is large.",
        "answer": [
            "medium",
            "large"
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
        "answer": true
    },
    "open_source": {
        "question": "Do this database have open source version?",
        "answer": true
    },
    "commercial": {
        "question": "Do this database have commercial version?",
        "answer": true
    }
}
