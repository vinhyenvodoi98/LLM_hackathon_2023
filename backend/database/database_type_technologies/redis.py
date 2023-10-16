redis = {
  "index": 15,
  "name": "Redis",
  "website": "https://redis.io/",
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
      "question": "On a scale of 0 to 10, how suitable is Redis for storing a small set of SQL data?",
      "answer": 5
    },
    "time_series": {
      "question": "On a scale of 0 to 10, how suitable is Redis for storing a small set of time series data?",
      "answer": 7
    }
  },
  "medium_volume": {
    "sql": {
      "question": "On a scale of 0 to 10, how suitable is Redis for storing a medium set of SQL data?",
      "answer": 4
    },
    "time_series": {
      "question": "On a scale of 0 to 10, how suitable is Redis for storing a medium set of time series data?",
      "answer": 8
    }
  },
  "large_volume": {
    "sql": {
      "question": "On a scale of 0 to 10, how suitable is Redis for storing a large set of SQL data?",
      "answer": 3
    },
    "time_series": {
      "question": "On a scale of 0 to 10, how suitable is Redis for storing a large set of time series data?",
      "answer": 9
    }
  },
  "read_consistency": {
    "question": "On a scale of 0 to 10, what is the read consistency of Redis?",
    "answer": 8
  },
  "high_write_workloads": {
    "question": "On a scale of 0 to 10, how good can Redis handle high-write workloads?",
    "answer": 10
  },
  "maturity": {
    "question": "On a scale of 0 to 10, how mature is Redis?",
    "answer": 10
  },
  "open_source": {
    "question": "Do Redis have open source version?",
    "answer": True
  },
  "commercial": {
    "question": "Do Redis have commercial version?",
    "answer": True
  }
}
