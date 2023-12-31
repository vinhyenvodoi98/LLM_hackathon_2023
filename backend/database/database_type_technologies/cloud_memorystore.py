cloud_memorystore = {
    "index": 14,
    "name": "Cloud Memorystore",
    "website": "https://cloud.google.com/memorystore/",
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
            "question": "On a scale of 0 to 10, how suitable is Cloud Memorystore for storing a small set of SQL data?",
            "answer": 9
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is Cloud Memorystore for storing a small set of time series data?",
            "answer": 8
        }
    },
    "medium_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is Cloud Memorystore for storing a medium set of SQL data?",
            "answer": 8
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is Cloud Memorystore for storing a medium set of time series data?",
            "answer": 9
        }
    },
    "large_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is Cloud Memorystore for storing a large set of SQL data?",
            "answer": 7
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is Cloud Memorystore for storing a large set of time series data?",
            "answer": 10
        }
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of Cloud Memorystore?",
        "answer": 9
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can Cloud Memorystore handle high-write workloads?",
        "answer": 10
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is Cloud Memorystore?",
        "answer": 9
    },
    "open_source": {
        "question": "Do Cloud Memorystore have open source version?",
        "answer": False
    },
    "commercial": {
        "question": "Do Cloud Memorystore have commercial version?",
        "answer": True
    }
}
