cassandra = {
    "index": 12,
    "name": "Apache Cassandra",
    "website": "https://cassandra.apache.org/",
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
        "question": "On a scale of 0 to 10, how suitable is Cassandra for storing a small set of SQL data?",
        "answer": 5
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is Cassandra for storing a small set of time series data?",
        "answer": 7
        }
    },
    "medium_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is Cassandra for storing a medium set of SQL data?",
        "answer": 6
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is Cassandra for storing a medium set of time series data?",
        "answer": 8
        }
    },
    "large_volume": {
        "sql": {
        "question": "On a scale of 0 to 10, how suitable is Cassandra for storing a large set of SQL data?",
        "answer": 7
        },
        "time_series": {
        "question": "On a scale of 0 to 10, how suitable is Cassandra for storing a large set of time series data?",
        "answer": 9
        }
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of Cassandra?",
        "answer": 8
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can Cassandra handle high-write workloads?",
        "answer": 9
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is Cassandra?",
        "answer": 9
    },
    "open_source": {
        "question": "Do Cassandra have open source version?",
        "answer": True
    },
    "commercial": {
        "question": "Do Cassandra have commercial version?",
        "answer": True
    }
}
