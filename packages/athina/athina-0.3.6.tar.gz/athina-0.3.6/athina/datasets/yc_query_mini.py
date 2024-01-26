data = [
    # Incorrect - Unfaithful
    {
        "query": "What are some successful companies that went through YC?",
        "context": "Y Combinator has invested in companies in various fields like FinTech, Healthcare, AI, etc.",
        "response": "Airbnb, Dropbox, Stripe, Reddit, Coinbase, Instacart.",
    },
    {
        "query": "In which city is YC located?",
        "context": "Y Combinator is located in Mountain View, California.",
        "response": "Y Combinator is located in San Francisco",
    },
    # Incorrect - Insufficient Context + Unfaithful
    {
        "query": "How much equity does YC take?",
        "context": "Y Combinator invests $500k in 200 startups twice a year.",
        "response": "YC invests $150k for 7%.",
    },
    # Incorrect - Insufficient Answer
    {
        "query": "How much equity does YC take?",
        "context": "Y Combinator invests $500k in 200 startups twice a year.",
        "response": "I cannot answer this question as I do not have enough information.",
    },
    {
        "query": "Who founded YC and when was it founded?",
        "context": "Y Combinator was founded in March 2005 by Paul Graham, Jessica Livingston, Trevor Blackwell, and Robert Tappan Morris.",
        "response": "Y Combinator was founded in 2005",
    },
    # Correct answers
    {
        "query": "Does Y Combinator invest in startups outside the US?",
        "context": "Y Combinator invests in startups from all over the world.",
        "response": "Yes, Y Combinator invests in international startups as well as US startups.",
    },
    {
        "query": "How much does YC invest in startups?",
        "context": "YC invests $150k for 7%.",
        "response": "$150k",
    },
    {
        "query": "What is YC's motto?",
        "context": "Y Combinator's motto is 'Make something people want'.",
        "response": "Make something people want",
    },
]
