from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Startup Idea Validator Bot Backend Running"

@app.route("/validate", methods=["POST"])
def validate_idea():

    data = request.get_json()
    idea = data.get("idea", "").lower()

    score = 5
    innovation = 50
    scalability = 50
    profitability = 50
    market_demand = 50

    if "ai" in idea:
        score += 3
        innovation += 35
        scalability += 20

    if "delivery" in idea:
        market_demand += 30
        profitability += 15

    if "student" in idea or "education" in idea:
        market_demand += 20
        innovation += 10

    if "health" in idea:
        profitability += 20
        market_demand += 25

    if "blockchain" in idea:
        innovation += 30
        scalability += 15

    score = min(10, score + random.randint(0, 2))
    innovation = min(100, innovation + random.randint(0, 15))
    scalability = min(100, scalability + random.randint(0, 15))
    profitability = min(100, profitability + random.randint(0, 15))
    market_demand = min(100, market_demand + random.randint(0, 15))

    if "ai" in idea:
        strengths = ["High automation potential"]
        weaknesses = ["Requires quality AI models"]
        opportunities = ["Growing AI adoption"]
        threats = ["Rapid AI competition"]

    elif "delivery" in idea:
        strengths = ["High customer demand"]
        weaknesses = ["Logistics management"]
        opportunities = ["Local market expansion"]
        threats = ["Established delivery companies"]

    elif "student" in idea or "education" in idea:
        strengths = ["Large student audience"]
        weaknesses = ["Low initial revenue"]
        opportunities = ["College partnerships"]
        threats = ["Free alternatives"]

    elif "health" in idea:
        strengths = ["Strong social impact"]
        weaknesses = ["Regulatory compliance"]
        opportunities = ["Healthcare digitization"]
        threats = ["Legal requirements"]

    elif "blockchain" in idea:
        strengths = ["High transparency"]
        weaknesses = ["Complex implementation"]
        opportunities = ["Emerging technology market"]
        threats = ["Government regulations"]

    else:
        strengths = ["Unique business concept"]
        weaknesses = ["Needs market validation"]
        opportunities = ["Scalable business model"]
        threats = ["Market competition"]

    avg = (
        innovation +
        scalability +
        profitability +
        market_demand
    ) / 4

    if avg >= 80:
        verdict = "Excellent Startup Idea"
        risk = "Low"
    elif avg >= 65:
        verdict = "Strong Potential"
        risk = "Medium"
    else:
        verdict = "Needs Improvement"
        risk = "High"

    return jsonify({
        "summary": f"The idea '{idea}' has been analyzed based on innovation, scalability, profitability and market demand.",
        "score": score,
        "innovation": innovation,
        "scalability": scalability,
        "profitability": profitability,
        "market_demand": market_demand,
        "verdict": verdict,
        "risk": risk,
        "success_probability": int(avg),
        "strengths": strengths,
        "weaknesses": weaknesses,
        "opportunities": opportunities,
        "threats": threats
    })

if __name__ == "__main__":
    app.run(debug=True)