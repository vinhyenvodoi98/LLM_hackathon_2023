tidb = {
    "index": 3,
    "name": "TiDB",
    "website": "https://pingcap.com/products/tidb/",
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
            "question": "On a scale of 0 to 10, how suitable is TiDB for storing a small set of SQL data?",
            "answer": 9
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is TiDB for storing a small set of time series data?",
            "answer": 9
        }
    },
    "medium_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is TiDB for storing a medium set of SQL data?",
            "answer": 8
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is TiDB for storing a medium set of time series data?",
            "answer": 8
        }
    },
    "large_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is TiDB for storing a large set of SQL data?",
            "answer": 9
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is TiDB for storing a large set of time series data?",
            "answer": 9
        }
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of this database?",
        "answer": 9
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can this database high-write workloads?",
        "answer": 9
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is TiDB?",
        "answer": 8
    },
    "open_source": {
        "question": "Do this database have open source version?",
        "answer": True
    },
    "commercial": {
        "question": "Do this database have commercial version?",
        "answer": True
    }
}
