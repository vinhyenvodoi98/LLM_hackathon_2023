microsoft_sql_server = {
    "index": 6,
    "name": "Microsoft SQL Server",
    "website": "https://www.microsoft.com/sql-server/",
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
        "answer": True
    },
    "small_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is Microsoft SQL Server for storing a small set of SQL data?",
            "answer": 9
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is Microsoft SQL Server for storing a small set of time series data?",
            "answer": 8
        },
    },
    "medium_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is Microsoft SQL Server for storing a medium set of SQL data?",
            "answer": 8
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is Microsoft SQL Server for storing a medium set of time series data?",
            "answer": 7
        },
    },
    "large_volume": {
        "sql": {
            "question": "On a scale of 0 to 10, how suitable is Microsoft SQL Server for storing a large set of SQL data?",
            "answer": 7
        },
        "time_series": {
            "question": "On a scale of 0 to 10, how suitable is Microsoft SQL Server for storing a large set of time series data?",
            "answer": 6
        },
    },
    "read_consistency": {
        "question": "On a scale of 0 to 10, what is the read consistency of Microsoft SQL Server?",
        "answer": 9
    },
    "high_write_workloads": {
        "question": "On a scale of 0 to 10, how good can Microsoft SQL Server handle high-write workloads?",
        "answer": 8
    },
    "maturity": {
        "question": "On a scale of 0 to 10, how mature is Microsoft SQL Server?",
        "answer": 10
    },
    "open_source": {
        "question": "Do Microsoft SQL Server have open source version?",
        "answer": False
    },
    "commercial": {
        "question": "Do Microsoft SQL Server have commercial version?",
        "answer": True
    }
}
