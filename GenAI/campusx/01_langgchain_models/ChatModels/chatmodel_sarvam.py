from sarvamai import SarvamAI
import os

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)


response = client.chat.completions(
    messages=[
        {"role": "user", "content": "Hey, what is the capital of India?"}
    ]
)


print(response)