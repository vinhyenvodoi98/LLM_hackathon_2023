postgresql = {
    "index": 2,
    "name": "PostgreSQL",
    "website": "https://www.postgresql.org/",
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
        "answer": False
    },
    "small_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is PostgreSQL for storing a small set of SQL data?",
            "answer": 9
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is PostgreSQL for storing a small set of time series data?",
            "answer": 8
        }
    },
    "medium_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is PostgreSQL for storing a medium set of SQL data?",
            "answer": 8
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is PostgreSQL for storing a medium set of time series data?",
            "answer": 7
        }
    },
    "large_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is PostgreSQL for storing a large set of SQL data?",
            "answer": 7
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is PostgreSQL for storing a large set of time series data?",
            "answer": 6
        }
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of PostgreSQL?",
        "answer": 8
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can PostgreSQL handle high-write workloads?",
        "answer": 7
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is PostgreSQL?",
        "answer": 9
    },
    "open_source": {
        "question": "Do PostgreSQL have open source version?",
        "answer": True
    },
    "commercial": {
        "question": "Do PostgreSQL have commercial version?",
        "answer": True
    }
}
