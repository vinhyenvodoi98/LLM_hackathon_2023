mysql = {
    "index": 1,
    "name": "MySQL",
    "website": "https://www.mysql.com/",
    "data_type": {
        "question": "Which type of data can this database store?",
        "answer": [
            "Text",
            "Number",
            "Datetime",
            "Boolean",
            "Binary"
        ]
    },
    "unstructured_data": {
        "question": "Can this database store unstructured data?",
        "answer": False
    },
    "small_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is MySQL for storing a small set of SQL data?",
            "answer": 9
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is MySQL for storing a small set of time series data?",
            "answer": 8
        },
    },
    "medium_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is MySQL for storing a medium set of SQL data?",
            "answer": 7
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is MySQL for storing a medium set of time series data?",
            "answer": 6
        },
    },
    "large_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is MySQL for storing a large set of SQL data?",
            "answer": 5
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is MySQL for storing a large set of time series data?",
            "answer": 4
        },
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of MySQL?",
        "answer": 7
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can MySQL handle high-write workloads?",
        "answer": 7
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is MySQL?",
        "answer": 9
    },
    "open_source": {
        "question": "Do MySQL have open source version?",
        "answer": True
    },
    "commercial": {
        "question": "Do MySQL have commercial version?",
        "answer": True
    }
}
