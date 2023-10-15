mariadb = {
    "index": 4,
    "name": "MariaDB",
    "website": "https://mariadb.org/",
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
            "question": "On a scale of 0 to 10, how suitable is MariaDB for storing a small set of SQL data?",
            "answer": 10
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is MariaDB for storing a small set of time series data?",
            "answer": 9
        },
    },
    "medium_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is MariaDB for storing a medium set of SQL data?",
            "answer": 9
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is MariaDB for storing a medium set of time series data?",
            "answer": 8
        },
    },
    "large_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is MariaDB for storing a large set of SQL data?",
            "answer": 8
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is MariaDB for storing a large set of time series data?",
            "answer": 7
        },
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of MariaDB?",
        "answer": 7
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can MariaDB handle high-write workloads?",
        "answer": 7
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is MariaDB?",
        "answer": 9
    },
    "open_source": {
        "question": "Do MariaDB have open source version?",
        "answer": True
    },
    "commercial": {
        "question": "Do MariaDB have commercial version?",
        "answer": True
    }
}
