SYSTEM_PROMPT = """
You are a certified financial advisor AI.

Strict Rules:
- Do NOT recommend specific stocks.
- Provide educational advice only.
- Keep responses structured.

Response Format:
1. Financial Health Score (1-10)
2. Risk Category
3. Suggested Asset Allocation (%)
4. Monthly Savings Strategy
5. 3 Action Steps
6. Risk Warnings
"""

def build_prompt(user_input, history, profile):
    conversation = ""
    for msg in history:
        conversation += f"{msg['role']}: {msg['content']}\n"

    profile_info = f"""
User Financial Profile:
Income: {profile['income']}
Expenses: {profile['expenses']}
Savings: {profile['savings']}
Risk Tolerance: {profile['risk']}
"""

    return SYSTEM_PROMPT + profile_info + "\nConversation:\n" + conversation + "\nUser: " + user_input