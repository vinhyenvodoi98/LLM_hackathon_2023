timescaledb = {
    "index": 5,
    "name": "TimescaleDB",
    "website": "https://www.timescale.com/",
    "data_type": {
        "question": "Which type of data can this database store?",
        "answer": [
            "Text",
            "Number",
            "Datetime",
            "Boolean",
            "Binary",
            "JSON",
        ]
    },
    "unstructured_data": {
        "question": "Can this database store unstructured data?",
        "answer": False
    },
    "small_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is TimescaleDB for storing a small set of SQL data?",
            "answer": 9
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is TimescaleDB for storing a small set of time series data?",
            "answer": 10
        }
    },
    "medium_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is TimescaleDB for storing a medium set of SQL data?",
            "answer": 8
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is TimescaleDB for storing a medium set of time series data?",
            "answer": 10
        }
    },
    "large_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is TimescaleDB for storing a large set of SQL data?",
            "answer": 7
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is TimescaleDB for storing a large set of time series data?",
            "answer": 10
        }
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of TimescaleDB?",
        "answer": 9
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can TimescaleDB handle high-write workloads?",
        "answer": 8
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is TimescaleDB?",
        "answer": 8
    },
    "open_source": {
        "question": "Do TimescaleDB have open source version?",
        "answer": True
    },
    "commercial": {
        "question": "Do TimescaleDB have commercial version?",
        "answer": True
    }
}
