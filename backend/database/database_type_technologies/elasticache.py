elasticache = {
    "index": 13,
    "name": "Amazon ElastiCache",
    "website": "https://aws.amazon.com/elasticache/",
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
        "question": "On a scale of 0 to 10, how suitable is Amazon ElastiCache for storing a small set of SQL data?",
        "answer": 7
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is Amazon ElastiCache for storing a small set of time series data?",
        "answer": 8
        }
    },
    "medium_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is Amazon ElastiCache for storing a medium set of SQL data?",
        "answer": 8
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is Amazon ElastiCache for storing a medium set of time series data?",
        "answer": 9
        }
    },
    "large_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is Amazon ElastiCache for storing a large set of SQL data?",
        "answer": 7
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is Amazon ElastiCache for storing a large set of time series data?",
        "answer": 10
        }
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of Amazon ElastiCache?",
        "answer": 9
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can Amazon ElastiCache handle high-write workloads?",
        "answer": 10
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is Amazon ElastiCache?",
        "answer": 9
    },
    "open_source": {
        "question": "Do Amazon ElastiCache have open source version?",
        "answer": False
    },
    "commercial": {
        "question": "Do Amazon ElastiCache have commercial version?",
        "answer": True
    }
}
