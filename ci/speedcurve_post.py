import os, json, requests

SPEEDCURVE_KEY = os.getenv("SPEEDCURVE_KEY")
SITE_ID = os.getenv("SPEEDCURVE_SITE_ID")

if not SPEEDCURVE_KEY or not SITE_ID:
    raise SystemExit("SpeedCurve credentials missing")

url = f"https://api.speedcurve.com/v1/sites/{SITE_ID}/runs"

headers = {
    "Authorization": f"Bearer {SPEEDCURVE_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "notes": "Triggered by CircleCI pipeline"
}

resp = requests.post(url, headers=headers, json=payload)
result = {
    "status": resp.status_code,
    "response": resp.text
}

with open("speedcurve_response.json", "w") as f:
    json.dump(result, f, indent=2)

print("SpeedCurve test triggered")
