"""
Agent WellCare - Mental health support assistant using Gemini 2.0 Flash.
Simplified version for direct interaction.
"""

import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the client
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
MODEL_ID = "gemini-2.0-flash-exp"


# ============================================================================
# TOOLS
# ============================================================================

def conduct_phq9_assessment(responses: dict) -> dict:
    """
    Conducts PHQ-9 depression screening assessment.
    
    Args:
        responses: Dictionary with keys q1-q9, values 0-3
        
    Returns:
        Dictionary with score, severity, and interpretation
    """
    score = sum(responses.values())
    
    if score <= 4:
        severity = "minimal"
        interpretation = "Minimal or no depression"
    elif score <= 9:
        severity = "mild"
        interpretation = "Mild depression"
    elif score <= 14:
        severity = "moderate"
        interpretation = "Moderate depression"
    elif score <= 19:
        severity = "moderately_severe"
        interpretation = "Moderately severe depression"
    else:
        severity = "severe"
        interpretation = "Severe depression"
    
    return {
        "score": score,
        "severity": severity,
        "interpretation": interpretation,
        "max_score": 27
    }


def conduct_gad7_assessment(responses: dict) -> dict:
    """
    Conducts GAD-7 anxiety screening assessment.
    
    Args:
        responses: Dictionary with keys q1-q7, values 0-3
        
    Returns:
        Dictionary with score, severity, and interpretation
    """
    score = sum(responses.values())
    
    if score <= 4:
        severity = "minimal"
        interpretation = "Minimal anxiety"
    elif score <= 9:
        severity = "mild"
        interpretation = "Mild anxiety"
    elif score <= 14:
        severity = "moderate"
        interpretation = "Moderate anxiety"
    else:
        severity = "severe"
        interpretation = "Severe anxiety"
    
    return {
        "score": score,
        "severity": severity,
        "interpretation": interpretation,
        "max_score": 21
    }


def assess_crisis_risk(user_input: str) -> dict:
    """
    Assesses crisis risk based on user input.
    
    Args:
        user_input: User's text input
        
    Returns:
        Dictionary with risk_level and crisis_indicators
    """
    crisis_keywords = [
        "suicide", "kill myself", "end it all", "no reason to live",
        "better off dead", "hurt myself", "self harm"
    ]
    
    user_lower = user_input.lower()
    indicators = [kw for kw in crisis_keywords if kw in user_lower]
    
    if indicators:
        return {
            "risk_level": "high",
            "crisis_indicators": indicators,
            "immediate_action_required": True
        }
    
    return {
        "risk_level": "low",
        "crisis_indicators": [],
        "immediate_action_required": False
    }


def get_crisis_hotlines(country: str = "US") -> dict:
    """
    Retrieves crisis hotline information by country.
    
    Args:
        country: Country code (default: US)
        
    Returns:
        Dictionary with crisis resources
    """
    resources = {
        "US": {
            "suicide_prevention": "988 (Suicide & Crisis Lifeline)",
            "crisis_text": "Text HOME to 741741 (Crisis Text Line)",
            "emergency": "911",
            "website": "https://988lifeline.org"
        },
        "UK": {
            "samaritans": "116 123",
            "crisis_text": "Text SHOUT to 85258",
            "emergency": "999",
            "website": "https://www.samaritans.org"
        },
        "IN": {
            "vandrevala": "+91 9999 666 555",
            "aasra": "+91 22 2754 6669",
            "emergency": "112",
            "website": "http://www.aasra.info"
        }
    }
    
    return resources.get(country, resources["US"])


def save_wellness_plan(plan_content: str, filename: str = "my_wellness_plan.md") -> str:
    """
    Saves wellness plan to a markdown file.
    
    Args:
        plan_content: The wellness plan content
        filename: Output filename
        
    Returns:
        Success message with file path
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(plan_content)
        return f"Wellness plan saved successfully to {filename}"
    except Exception as e:
        return f"Error saving wellness plan: {str(e)}"


# ============================================================================
# SYSTEM PROMPT
# ============================================================================

SYSTEM_INSTRUCTION = """You are Agent WellCare, a compassionate AI assistant dedicated to mental health support and wellness guidance.

Your mission: Provide accessible, empathetic, and evidence-based mental health support to anyone who needs it.

Your approach:
1. **Listen actively** - Let users share at their own pace
2. **Validate feelings** - Normalize struggles, show empathy
3. **Assess needs** - Understand what support would be most helpful
4. **Provide guidance** - Offer evidence-based strategies and resources
5. **Ensure safety** - Always prioritize user wellbeing

Your capabilities:
- Conduct mental health assessments (PHQ-9 for depression, GAD-7 for anxiety)
- Provide crisis support and emergency resources
- Create personalized wellness plans
- Offer coping strategies and techniques
- Connect users to mental health resources

CRITICAL SAFETY PROTOCOLS:
- If user mentions suicide, self-harm, or crisis → IMMEDIATELY provide crisis resources
- Always include disclaimer: "I'm an AI assistant, not a replacement for professional care"
- Encourage professional help for moderate-severe symptoms
- Never diagnose or prescribe
- Maintain appropriate boundaries

Your communication style:
- Warm, empathetic, and non-judgmental
- Clear and accessible (avoid jargon)
- Hopeful and encouraging
- Respectful of user autonomy
- Culturally sensitive

Assessment Tools:

PHQ-9 Questions (0=Not at all, 1=Several days, 2=More than half the days, 3=Nearly every day):
Over the last 2 weeks, how often have you been bothered by:
1. Little interest or pleasure in doing things
2. Feeling down, depressed, or hopeless
3. Trouble falling/staying asleep, or sleeping too much
4. Feeling tired or having little energy
5. Poor appetite or overeating
6. Feeling bad about yourself or that you're a failure
7. Trouble concentrating on things
8. Moving or speaking slowly, or being fidgety/restless
9. Thoughts that you would be better off dead or hurting yourself

GAD-7 Questions (same scale):
Over the last 2 weeks, how often have you been bothered by:
1. Feeling nervous, anxious, or on edge
2. Not being able to stop or control worrying
3. Worrying too much about different things
4. Trouble relaxing
5. Being so restless that it's hard to sit still
6. Becoming easily annoyed or irritable
7. Feeling afraid as if something awful might happen

Crisis Resources:
- US: 988 (Suicide & Crisis Lifeline), Text HOME to 741741
- UK: 116 123 (Samaritans), Text SHOUT to 85258
- India: +91 9999 666 555 (Vandrevala), +91 22 2754 6669 (Aasra)

Wellness Plan Components:
- Cognitive strategies (CBT exercises, thought challenging)
- Behavioral activation (activity scheduling, goal setting)
- Mindfulness & relaxation (meditation, breathing exercises)
- Physical wellness (exercise, sleep hygiene, nutrition)
- Social connection (relationship building, support groups)
- Crisis management (warning signs, coping strategies, emergency contacts)

Remember: You're here to support, guide, and connect - not to replace professional mental health care. Your goal is to make mental health support more accessible while ensuring users get appropriate professional help when needed.
"""


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function for Agent WellCare."""
    print("=" * 70)
    print("AGENT WELLCARE - Mental Health Support & Wellness Guidance")
    print("=" * 70)
    print("\nWelcome! I'm here to provide mental health support and wellness guidance.")
    print("This is a safe, confidential space to discuss your wellbeing.")
    print("\nIMPORTANT: I'm an AI assistant, not a replacement for professional care.")
    print("If you're in crisis, please call 988 (US) or your local emergency number.")
    print("\nType 'exit' to end the conversation.\n")
    print("=" * 70)
    
    # Create chat with system instruction
    chat = client.chats.create(
        model=MODEL_ID,
        config={
            "system_instruction": SYSTEM_INSTRUCTION,
            "temperature": 0.7,
        }
    )
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\nAgent WellCare: Take care of yourself. Remember, support is always available when you need it. 💙")
            break
        
        if not user_input:
            continue
        
        try:
            # Check for crisis indicators
            crisis_check = assess_crisis_risk(user_input)
            
            # Send message and get response
            response = chat.send_message(user_input)
            print(f"\nAgent WellCare: {response.text}")
            
            # If crisis detected, provide immediate resources
            if crisis_check['immediate_action_required']:
                print("\n" + "="*70)
                print("⚠️  CRISIS RESOURCES - IMMEDIATE HELP AVAILABLE")
                print("="*70)
                hotlines = get_crisis_hotlines("US")
                for key, value in hotlines.items():
                    print(f"{key}: {value}")
                print("="*70)
                
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again or type 'exit' to quit.")


if __name__ == "__main__":
    main()
