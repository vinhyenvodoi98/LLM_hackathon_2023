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
                        "value": ["Text", "Number", "Datetime", "Boolean", "Binary"],
                        "reason": 'The choice of "Text" data type is used for storing textual information like usernames, goals, session names, etc. "Number" is used for storing numerical data, such as user IDs, session durations, and progress metrics. "Datetime" is used to capture timestamps for various events. "Boolean" is used for binary indicators like the status of reminders or goal achievements. "Binary" is used for storing audio files or images.',
                    },
                    "unstructured_data": {
                        "value": False,
                        "reason": "The data that will be mainly stored would be structured data, such as User Profiles, Progress Tracking, Goals and Preferences, Reminders, and Metadata of media files which will be likely to store in a separate storage.",
                    },
                    "time_series": {
                        "value": True,
                        "reason": " The need to track and analyze changes over time in features like progress tracking, reminders, and insights strongly suggests that the app would benefit from storing time-series data in its database. This allows the app to offer personalized insights and recommendations based on the user's historical data.",
                    },
                },
                "requirements": {
                    "volume": {
                        "value": None,
                        "reason": 'Given that the app includes features like progress tracking, reminders, and potentially generates insights, the data volume could fall within the "medium" category, ranging from 1 million to 100 million records. This is a just a general estimate and actual usage patterns, and user engagement would play a crucial role in determining the actual scale of data storage.',
                    },
                    "fast_response_time": {
                        "value": False,
                        "reason": "Users typically engage in mindfulness and meditation exercises over more extended periods, and they don't expect real-time, split-second. The data is not complex or real-time required. It primarily includes user preferences, meditation session data, and progress tracking. These data types don't require microsecond response times.",
                    },
                    "read_consistency": {
                        "value": False,
                        "reason": "It seems that read consistency may not be a critical requirement for the app. While users can personalize their experience based on goals, this information may not change frequently. Once users set their preferences and goals, they may remain relatively stable over short time intervals. The library of calming sounds or nature scenes and the available meditation sessions are content-based features. Once added to the app, this content may not change frequently and can be considered relatively static. Progress tracking and reminders could involve more dynamic data, but the frequency of updates may not be high. Insights into the user's meditation habits and mental well-being benefits may involve some dynamic data, but it's likely that the generation and presentation of insights don't require real-time consistency.",
                    },
                    "high_write_workloads": {
                        "value": True,
                        "reason": "While the app may not have an extremely high level of write workload compared to some other types of applications, there is likely a moderate write workload associated with features like progress tracking, reminders, and content personalization. If users can regularly log their progress, such as the duration and frequency of meditation sessions, this could contribute to a moderate level of write workload. If users actively set and modify reminders for mindfulness breaks, there could be write operations associated with updating reminder schedules. If users can personalize their library by adding or removing content, this could contribute to a write workload. Additionally, if there are dynamic recommendations or updates to the library based on user preferences, this might involve more frequent writes.",
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
                            "Text",
                            "Number",
                            "Datetime",
                            "Boolean",
                            "Binary",
                            "JSON",
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
                },
                "requirements": {
                    "volume": {
                        "value": ["medium"],
                        "reason": "The EcoSwap platform is likely to have a medium amount of data. The number of users and items on the platform is likely to be in the hundreds of thousands or millions. The amount of data generated by user interactions, such as swaps and ratings, is also likely to be significant.",
                    },
                    "fast_response_time": {
                        "value": False,
                        "reason": "The data involved in a platform like EcoSwap primarily includes user profiles, item listings, and user interactions. While there may be a substantial amount of data, it's not real-time data, and millisecond or sub-millisecond response times should be sufficient to manage user accounts, item listings, and search functionalities.",
                    },
                    "read_consistency": {
                        "value": False,
                        "reason": "It seems that the nature of the application doesn't necessitate strict read consistency where any read request returns the most recent write immediately. The primary function of EcoSwap is to allow users to list items they no longer need. In most cases, users searching for items on the platform would not require real-time consistency, as the inventory is not likely to change rapidly. The educational resources on sustainable living and reducing environmental impact are likely static or updated less frequently. Users accessing this content may not require the most recent updates instantly.",
                    },
                    "high_write_workloads": {
                        "value": False,
                        "reason": "It seems that the application may not inherently have a high write workload. The EcoSwap platform is not likely to have high write workloads. The majority of user interactions on the platform will be read operations, such as searching for items and viewing swap details. Write operations, such as creating new items and swaps, are likely to be less frequent.",
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
                        "value": [
                            "Text",
                            "Number",
                            "Datetime",
                            "Boolean",
                            "JSON",
                        ],
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
                },
                "requirements": {
                    "volume": {
                        "value": ["large"],
                        "reason": "The MoneyMinds application is likely to have a large amount of data. The number of users and transactions is likely to be in the millions or billions. The amount of data generated by user interactions, such as creating budgets and setting financial goals, is also likely to be significant.",
                    },
                    "fast_response_time": {
                        "value": True,
                        "reason": "It seems that the tracking investment function needs microsecond data return time. While real-time stock prices may not be necessary, data related to investment portfolios and asset allocation should be updated with minimal latency to provide accurate insights.",
                    },
                    "read_consistency": {
                        "value": True,
                        "reason": "Read consistency is likely to be an important requirement for the MoneyMinds application. Users need to be able to see an accurate representation of their financial situation at any time. If the data is not consistent, users may make incorrect decisions about their finances.",
                    },
                    "high_write_workloads": {
                        "value": True,
                        "reason": "The MoneyMinds application is likely to have high write workloads. Users will be constantly adding new transactions and updating their financial goals. The application will need to be able to handle these writes quickly and efficiently.",
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
                        "value": [
                            "Text",
                            "Number",
                            "Datetime",
                            "Boolean",
                            "JSON",
                        ],
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
                },
                "requirements": {
                    "volume": {
                        "value": ["large"],
                        "reason": "The CitizenConnect platform is likely to have a large amount of data. The number of users and government agencies is likely to be in the millions or billions. The amount of data generated by user interactions, such as renewing licenses and paying taxes, is also likely to be significant.",
                    },
                    "fast_response_time": {
                        "value": True,
                        "reason": "Citizens usually interact with government platforms in a less time-sensitive manner, such as adhering to annual deadlines or specific timelines set by government agencies. While timely access to government policies, local initiatives, and updates is important, the content delivery itself does not typically require microsecond response times. Citizens expect accurate and up-to-date information, but they don't expect the same real-time responsiveness as in, for example, high-frequency trading platforms.",
                    },
                    "read_consistency": {
                        "value": True,
                        "reason": "Read consistency is likely to be an important requirement for the CitizenConnect platform. Users need to be able to see an accurate representation of the information on the platform at any time. If the data is not consistent, users may make incorrect decisions about their government interactions.",
                    },
                    "high_write_workloads": {
                        "value": True,
                        "reason": "The CitizenConnect platform is likely to have high write workloads. Users will be constantly interacting with the platform, such as renewing licenses and paying taxes. The platform will need to be able to handle these writes quickly and efficiently.",
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
        {
            "requirement": "I want to develop a website that provides spot trading services and price forecasts of tokens in the crypto field. The system will collect information about the price of 2000 tokens at each of the following time points: 5 minutes, 15 minutes, 30 minutes, 1 hour, 4 hours, 1 day, 1 week, 1 month. The system will then store this data in the database for analysis and prediction. Users can buy and sell tokens listed on this website. The system needs to update the latest information accurately every time. I want to use a quality database and have the least possible risk of disruption.",
            "analysis_result": {
                "data_model": {
                    "data_type": {
                        "value": ["Text", "Number", "Datetime", "Boolean", "JSON"],
                        "reason": "The choice of data types is based on the following considerations:\n\nText: This data type is suitable for storing textual information such as token names, symbols, and descriptions.\n\nNumber: This data type is suitable for storing numeric information such as token prices, volumes, and market capitalizations.\n\nDatetime: This data type is suitable for storing timestamps, such as when a token price was updated.\n\nBoolean: This data type is suitable for storing binary values such as whether a token is tradable or not.\n\nJSON: This data type is suitable for storing complex data structures such as order books and trade histories.",
                    },
                    "unstructured_data": {
                        "value": False,
                        "reason": "The data that will be stored in the database is mostly structured, such as token prices, volumes, and market capitalizations. There is no mention of unstructured data such as images or videos.",
                    },
                    "time_series": {
                        "value": True,
                        "reason": "The data that will be stored in the database is time-series data. The token prices will be updated at regular intervals, and the system will need to be able to store and analyze this data over time.",
                    },
                },
                "requirements": {
                    "volume": {
                        "value": ["large"],
                        "reason": "The system will need to store a large amount of data. The token prices will be updated at regular intervals, and the system will need to store this data for analysis and prediction. Additionally, the system will need to store user data such as account balances and order histories.",
                    },
                    "fast_response_time": {
                        "value": True,
                        "reason": "Cryptocurrency markets are highly volatile and operate around the clock. The system needs to collect and update price information in real time to provide accurate and up-to-date data for analysis. Delays in data collection and storage can result in outdated information and hinder prediction accuracy.",
                    },
                    "read_consistency": {
                        "value": True,
                        "reason": "Read consistency is important for this system because users need to be able to see the latest token prices and make informed trading decisions.",
                    },
                    "high_write_workloads": {
                        "value": True,
                        "reason": "The system will have a high write workload because the token prices will be updated at regular intervals. Additionally, users will be able to buy and sell tokens, which will also generate write operations.",
                    },
                },
                "cost": {
                    "commercial_allow": {
                        "value": True,
                        "reason": "A commercial database is likely to be the best choice for this system. Commercial databases are typically more reliable and scalable than open-source databases. Additionally, commercial databases offer a wider range of features and support options.",
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
