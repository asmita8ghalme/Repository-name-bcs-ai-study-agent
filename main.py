from src.llm import ask_gemini

print("=" * 50)
print("        BCS AI STUDY AGENT 🤖")
print("=" * 50)

print("\nYour AI-powered study assistant for BCS students")
print("\nType 'exit' to close the agent.\n")

while True:
    question = input("Ask your BCS question:\n> ")

    if question.lower() == "exit":
        print("\nThank you for using BCS AI Study Agent! 👋")
        break

    if not question.strip():
        print("\nPlease enter a question.")
        continue

    print("\nThinking... 🤖\n")

    try:
        answer = ask_gemini(question)

        print("=" * 50)
        print("AI AGENT ANSWER")
        print("=" * 50)
        print(answer)
        print()

    except Exception as e:
        print("\nSomething went wrong:")
        print(e)