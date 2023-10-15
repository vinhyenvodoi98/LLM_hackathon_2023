mongodb = {
    "index": 10,
    "name": "MongoDB",
    "website": "https://www.mongodb.com/",
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
        "question": "On a scale of 0 to 10, how suitable is MongoDB for storing a small set of SQL data?",
        "answer": 8
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is MongoDB for storing a small set of time series data?",
        "answer": 9
        }
    },
    "medium_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is MongoDB for storing a medium set of SQL data?",
        "answer": 8
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is MongoDB for storing a medium set of time series data?",
        "answer": 9
        }
    },
    "large_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is MongoDB for storing a large set of SQL data?",
        "answer": 8
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is MongoDB for storing a large set of time series data?",
        "answer": 10
        }
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of MongoDB?",
        "answer": 9
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can MongoDB handle high-write workloads?",
        "answer": 10
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is MongoDB?",
        "answer": 9
    },
    "open_source": {
        "question": "Do MongoDB have open source version?",
        "answer": True
    },
    "commercial": {
        "question": "Do MongoDB have commercial version?",
        "answer": True
    }
}
