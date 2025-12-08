import os, json, requests, sys

OPENAI_KEY = os.getenv("OPENAI_KEY")

# Feature flag (IMPORTANT)
AI_ENABLED = os.getenv("AI_ENABLED", "false").lower() == "true"

if not AI_ENABLED:
    print("AI disabled by feature flag")
    sys.exit(0)

if not OPENAI_KEY:
    print("AI disabled (no key)")
    sys.exit(0)

headers = {
    "Authorization": f"Bearer {OPENAI_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Summarize K6 load test results"}
    ],
    "max_tokens": 200
}

r = requests.post(
    "https://api.openai.com/v1/chat/completions",
    json=payload,
    headers=headers,
    timeout=15
)

with open("ai_response.json", "w") as f:
    json.dump(r.json(), f, indent=2)

print("AI response saved")
