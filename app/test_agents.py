from app.agent import run_agent


print("TEST 1: Calculator")
print(run_agent("What is 125 multiplied by 37?"))

print("\nTEST 2: Current Time")
print(run_agent("What time is it right now?"))

print("\nTEST 3: General Question")
print(run_agent("What is LangGraph?"))