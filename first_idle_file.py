question = input("How is the weather today").strip().lower()

def response(question):
    while True:
        if question in ["hot", "sunny", "warm", "sweaty", "bad"]:
            print("Seems typical for Arizona")
            question = input("How is the weather today").strip().lower()
        else:
            print("Really? that seems suprising for Arizona")
            question = input("How is the weather today").strip().lower()


response(question)
