from app.graph.graph import graph

intial_state = {
    "messages": [
        ("human", "What is 125 multiplied by 37?")
    ]
}

result = graph.invoke(intial_state)
print(result)