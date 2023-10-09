# TODO: Need to test the use of Output Parser and see if the result can be well-formatted.
requirement_analysis_prompt_config = {
    "context": "You are a veteran Database specialist and an experienced, detailed-oriented consultant. I will give you a short project description. I need you to analyze the description and output the analyzed result in a JSON format. Put null values for information you don't know. You will have to explain for each property why you chose that value among its corresponding accepted values, in a detailed way that can convince the user.\n",
    "example_input_variables": ["requirement", "analysis_result"],
    "example_template": """
        requirement: {requirement}
        analysis_result: {analysis_result},
    """,
    "prefix": "Here are some examples of requirement and its corresponding analysis result:\n\n",
    "suffix": "\n\nNow, given a new requirement, give me the analysis result:\nrequirement: {requirement}\nanalysis_result:",
    "actual_input_variable": "requirement",
    "examples": [
        {
            "requirement": "Create a mobile app that helps users incorporate mindfulness and meditation practices into their daily lives. The app could offer a variety of guided meditation sessions, mindfulness exercises, and relaxation techniques. Users could personalize their experience based on their goals, such as stress reduction, better sleep, or improved focus. The app might include features like progress tracking, reminders for mindfulness breaks, and a library of calming sounds or nature scenes. Additionally, it could provide insights into the user's meditation habits and the associated mental well-being benefits.",
            "analysis_result": {
                "data_model": {
                    "data_type": {
                        "value": ["text", "number", "datetime", "boolean", "binary"],
                        "reason": 'The choice of "Text" data type is used for storing textual information like usernames, goals, session names, etc. "Number" is used for storing numerical data, such as user IDs, session durations, and progress metrics. "Datetime" is used to capture timestamps for various events. "Boolean" is used for binary indicators like the status of reminders or goal achievements. "Binary" is used for storing audio files or images.',
                    },
                    "unstructured_data": {
                        "value": True,
                        "reason": "The data that will be mainly stored would be structured data, such as User Profiles, Progress Tracking, Goals and Preferences, Reminders, and Metadata of media files which will be likely to store in a separate storage.",
                    },
                    "time_series": {
                        "value": True,
                        "reason": " The need to track and analyze changes over time in features like progress tracking, reminders, and insights strongly suggests that the app would benefit from storing time-series data in its database. This allows the app to offer personalized insights and recommendations based on the user's historical data.",
                    },
                    "relationship_centric": {
                        "value": False,
                        "reason": "While there are relationships between different types of data, these relationships appear to be relatively straightforward and not excessively complex. Users have preferences and goals, and their interactions with features like progress tracking and reminders contribute to generating insights. The app's data model may involve linking various data entities, but it doesn't inherently suggest a need for highly intricate relationships that would make the database structure excessively complicated.",
                    },
                },
                "requirements": {
                    "volume": {
                        "value": "medium",
                        "reason": 'Given that the app includes features like progress tracking, reminders, and potentially generates insights, the data volume could fall within the "medium" category, ranging from 1 million to 100 million records. This is a just a general estimate and actual usage patterns, and user engagement would play a crucial role in determining the actual scale of data storage.',
                    },
                    "complex_query_patterns": {
                        "value": False,
                        "reason": "For a standard implementation of progress tracking, reminders, and content retrieval, the queries may not need to be excessively complex. However, if the app aims to provide highly personalized and detailed insights, more sophisticated queries may be necessary.",
                    },
                    "read_consistency": {
                        "value": False,
                        "reason": "It seems that read consistency may not be a critical requirement for the app. While users can personalize their experience based on goals, this information may not change frequently. Once users set their preferences and goals, they may remain relatively stable over short time intervals. The library of calming sounds or nature scenes and the available meditation sessions are content-based features. Once added to the app, this content may not change frequently and can be considered relatively static. Progress tracking and reminders could involve more dynamic data, but the frequency of updates may not be high. Insights into the user's meditation habits and mental well-being benefits may involve some dynamic data, but it's likely that the generation and presentation of insights don't require real-time consistency.",
                    },
                    "high_write_workloads": {
                        "value": True,
                        "reason": "While the app may not have an extremely high level of write workload compared to some other types of applications, there is likely a moderate write workload associated with features like progress tracking, reminders, and content personalization. If users can regularly log their progress, such as the duration and frequency of meditation sessions, this could contribute to a moderate level of write workload. If users actively set and modify reminders for mindfulness breaks, there could be write operations associated with updating reminder schedules. If users can personalize their library by adding or removing content, this could contribute to a write workload. Additionally, if there are dynamic recommendations or updates to the library based on user preferences, this might involve more frequent writes.",
                    },
                    "high_availability": {
                        "value": False,
                        "reason": "Considering that read consistency is not a critical requirement and write workload is rather moderate, we can assume that a less than 99.9% uptime is tolerable. The users are not expected to use the app frequently during a day and the amount of possible loss data during the downtime is not significant.",
                    },
                },
                "cost": {
                    "commercial_allow": {
                        "value": None,
                        "reason": "the description doesn't include information regarding budget, perferences of whether you want to use commercial or open-source database, or implications of the necessity to use commercial database.",
                    }
                },
            },
        },
        {
            "requirement": "EcoSwap is an online platform designed to promote sustainability and reduce waste. Users can create profiles to list items they no longer need but are still in good condition. These items could include clothing, furniture, electronics, and more. The platform encourages users to swap items with others rather than buying new ones, contributing to a more sustainable and circular economy. EcoSwap can include features like user ratings, a search function based on location, and categories to make it easy for users to find and exchange items that align with their needs and values. Additionally, the platform could have educational resources on sustainable living and reducing environmental impact.",
            "analysis_result": {
                "data_model": {
                    "data_type": {
                        "value": [
                            "text",
                            "number",
                            "datetime",
                            "boolean",
                            "binary",
                            "json",
                        ],
                        "reason": "The choice of data types is based on the following considerations:\n\nText: This data type is suitable for storing textual information such as user names, item descriptions, and categories.\n\nNumber: This data type is suitable for storing numeric information such as user ratings, item quantities, and prices.\n\nDatetime: This data type is suitable for storing timestamps, such as when an item was listed or when a swap was completed.\n\nBoolean: This data type is suitable for storing binary values such as whether an item is available or whether a user has been verified.\n\nBinary: This data type is suitable for storing images of items.\n\nJSON: This data type is suitable for storing complex data structures such as user profiles and item details.",
                    },
                    "unstructured_data": {
                        "value": False,
                        "reason": "The data that will be stored in the EcoSwap database is mostly structured, such as user profiles, item listings, and swap transactions. The data model will likely involve tables for users, items, and swaps, with relationships between these tables to represent the different entities and their interactions.",
                    },
                    "time_series": {
                        "value": False,
                        "reason": "The data that will be stored in the EcoSwap database is not time-series data. While there may be some temporal aspects to the data, such as when items are listed or when swaps are completed, these are not the primary focus of the database.",
                    },
                    "relationship_centric": {
                        "value": True,
                        "reason": "The data that will be stored in the EcoSwap database is relationship-centric. The relationships between users, items, and swaps are essential to the functioning of the platform. For example, users can only swap items with other users, and items can only be swapped if they are available.",
                    },
                },
                "requirements": {
                    "volume": {
                        "value": "medium",
                        "reason": "The EcoSwap platform is likely to have a medium amount of data. The number of users and items on the platform is likely to be in the hundreds of thousands or millions. The amount of data generated by user interactions, such as swaps and ratings, is also likely to be significant.",
                    },
                    "complex_query_patterns": {
                        "value": True,
                        "reason": "The EcoSwap platform is likely to require complex query patterns. For example, users may want to search for items based on multiple criteria, such as category, location, and condition. The platform may also need to generate reports on user activity and item swaps.",
                    },
                    "read_consistency": {
                        "value": False,
                        "reason": "It seems that the nature of the application doesn't necessitate strict read consistency where any read request returns the most recent write immediately. The primary function of EcoSwap is to allow users to list items they no longer need. In most cases, users searching for items on the platform would not require real-time consistency, as the inventory is not likely to change rapidly. The educational resources on sustainable living and reducing environmental impact are likely static or updated less frequently. Users accessing this content may not require the most recent updates instantly.",
                    },
                    "high_write_workloads": {
                        "value": False,
                        "reason": "It seems that the application may not inherently have a high write workload. The EcoSwap platform is not likely to have high write workloads. The majority of user interactions on the platform will be read operations, such as searching for items and viewing swap details. Write operations, such as creating new items and swaps, are likely to be less frequent.",
                    },
                    "high_availability": {
                        "value": False,
                        "reason": "The need for high availability may not be as critical compared to certain real-time or mission-critical applications. The act of listing items on the platform and searching for items may not require real-time availability. Users might engage with the platform at their convenience, and delays in availability might not significantly impact the overall user experience. While users may interact with each other through the platform, the nature of item swapping and the lack of immediate financial transactions may mean that the platform can tolerate brief periods of unavailability without severe consequences. Access to educational resources on sustainable living and reducing environmental impact is unlikely to be highly time sensitive. Users may visit these resources at their own pace. ",
                    },
                },
                "cost": {
                    "commercial_allow": {
                        "value": None,
                        "reason": "There is no information in the description about whether the user is willing to pay for a commercial database.",
                    }
                },
            },
        },
        {
            "requirement": "MoneyMinds is a user-friendly finance web application that simplifies money management. It offers robust features for budgeting, expense tracking, and setting financial goals. Users can link accounts for a holistic view of their financial landscape, receive personalized spending insights, and get timely alerts. MoneyMinds also provides tools for investment tracking, retirement planning, and credit score monitoring, empowering users to take control of their financial future with confidence and ease.",
            "analysis_result": {
                "data_model": {
                    "data_type": {
                        "value": ["text", "number", "datetime", "boolean", "json"],
                        "reason": "The choice of data types is based on the following considerations:\n\nText: This data type is suitable for storing textual information such as user names, account names, and transaction descriptions.\n\nNumber: This data type is suitable for storing numeric information such as account balances, transaction amounts, and financial goals.\n\nDatetime: This data type is suitable for storing timestamps, such as when transactions occur or when financial goals are set.\n\nBoolean: This data type is suitable for storing binary values such as whether a transaction is recurring or whether a financial goal has been achieved.\n\nJSON: This data type is suitable for storing complex data structures such as user profiles and financial transactions.",
                    },
                    "unstructured_data": {
                        "value": False,
                        "reason": "The data that will be stored in the MoneyMinds database is mostly structured, such as user profiles, financial accounts, transactions, and financial goals. The data model will likely involve tables for users, accounts, transactions, and goals, with relationships between these tables to represent the different entities and their interactions.",
                    },
                    "time_series": {
                        "value": True,
                        "reason": "The data that will be stored in the MoneyMinds database is time-series data. The transactions and financial goals are all associated with specific dates, and the user's financial situation will change over time. The database will need to be able to store and track these changes over time.",
                    },
                    "relationship_centric": {
                        "value": True,
                        "reason": "The data that will be stored in the MoneyMinds database is relationship-centric. The relationships between users, accounts, transactions, and financial goals are essential to the functioning of the application. For example, users can only view the transactions for their own accounts, and transactions can only be associated with one account.",
                    },
                },
                "requirements": {
                    "volume": {
                        "value": "large",
                        "reason": "The MoneyMinds application is likely to have a large amount of data. The number of users and transactions is likely to be in the millions or billions. The amount of data generated by user interactions, such as creating budgets and setting financial goals, is also likely to be significant.",
                    },
                    "complex_query_patterns": {
                        "value": True,
                        "reason": "The MoneyMinds application is likely to require complex query patterns. For example, users may want to see a list of all their transactions for a given month, or they may want to see a breakdown of their spending by category. The application may also need to generate reports on user activity and financial progress.",
                    },
                    "read_consistency": {
                        "value": True,
                        "reason": "Read consistency is likely to be an important requirement for the MoneyMinds application. Users need to be able to see an accurate representation of their financial situation at any time. If the data is not consistent, users may make incorrect decisions about their finances.",
                    },
                    "high_write_workloads": {
                        "value": True,
                        "reason": "The MoneyMinds application is likely to have high write workloads. Users will be constantly adding new transactions and updating their financial goals. The application will need to be able to handle these writes quickly and efficiently.",
                    },
                    "high_availability": {
                        "value": True,
                        "reason": "High availability is likely to be an important requirement for the MoneyMinds application. Users need to be able to access their financial information at any time, even if the application is experiencing technical difficulties. The application will need to be able to tolerate failures and recover quickly.",
                    },
                },
                "cost": {
                    "commercial_allow": {
                        "value": None,
                        "reason": "There is no information in the description about whether the user is willing to pay for a commercial database.",
                    }
                },
            },
        },
        {
            "requirement": "CitizenConnect is the official government website that serves as a centralized hub for citizens to access essential services and information. From renewing licenses and paying taxes to staying informed about local initiatives and policies, the platform ensures seamless interaction between citizens and government agencies. With user-friendly interfaces, secure portals, and timely updates, CitizenConnect is designed to enhance transparency, civic engagement, and the overall citizen-government relationship.",
            "analysis_result": {
                "data_model": {
                    "data_type": {
                        "value": ["text", "number", "datetime", "boolean", "json"],
                        "reason": "The choice of data types is based on the following considerations:\n\nText: This data type is suitable for storing textual information such as user names, addresses, and descriptions of government services.\n\nNumber: This data type is suitable for storing numeric information such as license numbers, tax amounts, and population statistics.\n\nDatetime: This data type is suitable for storing timestamps, such as when a license was issued or when a tax payment was made.\n\nBoolean: This data type is suitable for storing binary values such as whether a user has paid their taxes or whether a government agency is open.\n\nJSON: This data type is suitable for storing complex data structures such as user profiles and government agency information.",
                    },
                    "unstructured_data": {
                        "value": False,
                        "reason": "The data that will be stored in the CitizenConnect database is mostly structured, such as user profiles, government agency information, and details about government services. The data model will likely involve tables for users, government agencies, and services, with relationships between these tables to represent the different entities and their interactions.",
                    },
                    "time_series": {
                        "value": False,
                        "reason": "The data that will be stored in the CitizenConnect database is not time-series data. The functionalities described in CitizenConnect seem more aligned with providing static or dynamically updated information at a given point in time, rather than recording and analyzing data changes over specific intervals.",
                    },
                    "relationship_centric": {
                        "value": True,
                        "reason": "The data that will be stored in the CitizenConnect database is relationship-centric. The relationships between users, government agencies, and government services are essential to the functioning of the platform. For example, users can only access certain services if they are registered with the government agency that provides those services.",
                    },
                },
                "requirements": {
                    "volume": {
                        "value": "large",
                        "reason": "The CitizenConnect platform is likely to have a large amount of data. The number of users and government agencies is likely to be in the millions or billions. The amount of data generated by user interactions, such as renewing licenses and paying taxes, is also likely to be significant.",
                    },
                    "complex_query_patterns": {
                        "value": True,
                        "reason": "The CitizenConnect platform is likely to require complex query patterns. For example, users may want to search for a specific government service or find out about all the services that are available in their area. The platform may also need to generate reports on user activity and government agency performance.",
                    },
                    "read_consistency": {
                        "value": True,
                        "reason": "Read consistency is likely to be an important requirement for the CitizenConnect platform. Users need to be able to see an accurate representation of the information on the platform at any time. If the data is not consistent, users may make incorrect decisions about their government interactions.",
                    },
                    "high_write_workloads": {
                        "value": True,
                        "reason": "The CitizenConnect platform is likely to have high write workloads. Users will be constantly interacting with the platform, such as renewing licenses and paying taxes. The platform will need to be able to handle these writes quickly and efficiently.",
                    },
                    "high_availability": {
                        "value": True,
                        "reason": "High availability is likely to be an important requirement for the CitizenConnect platform. The application is meant to provide access to essential government services such as renewing licenses and paying taxes. Users may rely on these services for critical transactions, making high availability crucial to ensure users can access them when needed. Citizens need to stay informed about local initiatives and policies, requiring access to real-time or timely updates. High availability ensures that users can access the latest information promptly. The platform aims for seamless interaction between citizens and government agencies. High availability is essential to maintain a positive user experience and trust in the platform's reliability.",
                    },
                },
                "cost": {
                    "commercial_allow": {
                        "value": True,
                        "reason": "For a government website CitizenConnect, where security, scalability, and regulatory compliance are paramount, a commercial database may be the more suitable choice. However, the budget constraints, and the expertise of your development team should all be taken into account when making this decision.",
                    }
                },
            },
        },
    ],
}

basic_prompt_example_config = {
    "input_variable": "database",
    "template": """You are a veteran Database specialist and an experienced, detailed-oriented consultant.
            You will give a summary of this {database}'s features.
        """,
}
