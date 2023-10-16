bigtable = {
    "index": 17,
    "name": "Bigtable",
    "website": "https://cloud.google.com/bigtable/",
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
        "question": "On a scale of 0 to 10, how suitable is Bigtable for storing a small set of SQL data?",
        "answer": 6
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is Bigtable for storing a small set of time series data?",
        "answer": 6
        }
    },
    "medium_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is Bigtable for storing a medium set of SQL data?",
        "answer": 7
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is Bigtable for storing a medium set of time series data?",
        "answer": 7
        }
    },
    "large_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is Bigtable for storing a large set of SQL data?",
        "answer": 8
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is Bigtable for storing a large set of time series data?",
        "answer": 8
        }
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of Bigtable?",
        "answer": 9
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can Bigtable handle high-write workloads?",
        "answer": 9
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is Bigtable?",
        "answer": 9
    },
    "open_source": {
        "question": "Do Bigtable have open source version?",
        "answer": False
    },
    "commercial": {
        "question": "Do Bigtable have commercial version?",
        "answer": True
    }
}
