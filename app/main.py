from app.llm import llm

def main():
    response = llm.invoke(
         "You are an AI assistant. Introduce yourself in one sentence."
    )
    print(response.content)

if __name__ == "__main__":
    main()
