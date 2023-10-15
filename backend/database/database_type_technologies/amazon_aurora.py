amazon_aurora = {
    "index": 7,
    "name": "Amazon Aurora",
    "website": "https://aws.amazon.com/rds/aurora/",
    "data_type": {
        "question": "Which type of data can this database store?",
        "answer": [
            "Text",
            "Number",
            "Datetime",
            "Boolean",
            "Binary",
            "JSON"
        ]
    },
    "unstructured_data": {
        "question": "Can this database store unstructured data?",
        "answer": True
    },
    "small_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is Amazon Aurora for storing a small set of SQL data?",
            "answer": 9
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is Amazon Aurora for storing a small set of time series data?",
            "answer": 9
        }
    },
    "medium_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is Amazon Aurora for storing a medium set of SQL data?",
            "answer": 10
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is Amazon Aurora for storing a medium set of time series data?",
            "answer": 10
        }
    },
    "large_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is Amazon Aurora for storing a large set of SQL data?",
            "answer": 10
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is Amazon Aurora for storing a large set of time series data?",
            "answer": 10
        }
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of Amazon Aurora?",
        "answer": 10
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can Amazon Aurora handle high-write workloads?",
        "answer": 10
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is Amazon Aurora?",
        "answer": 9
    },
    "open_source": {
        "question": "Do Amazon Aurora have open source version?",
        "answer": False
    },
    "commercial": {
        "question": "Do Amazon Aurora have commercial version?",
        "answer": True
    }
}
