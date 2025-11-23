# Agent WellCare - Mental Health Support System

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![ADK](https://img.shields.io/badge/ADK-Google%20Agent%20Development%20Kit-orange)](https://github.com/google/genai)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Agent WellCare is a multi-agent system providing accessible mental health support to underserved communities. Built with Google's official Agent Development Kit (ADK), it conducts wellness assessments, generates personalized self-care plans, offers crisis intervention, and connects users with community resources.

## 🌟 Key Features

- **Multi-Agent Architecture**: Specialized agents for different aspects of mental health support
- **Evidence-Based Assessments**: PHQ-9 (depression) and GAD-7 (anxiety) screenings
- **Crisis Intervention**: Immediate support and resource connection during emergencies
- **Personalized Wellness Plans**: Customized evidence-based strategies (CBT, mindfulness, etc.)
- **Progress Tracking**: Mood logging and trend analysis
- **Community Resources**: Local mental health service connections
- **Safety Protocols**: Built-in crisis detection and escalation

## 🏗️ Architecture

Agent WellCare follows a hierarchical multi-agent architecture:

```
interactive_wellcare_agent (Orchestrator)
├── wellness_assessor_agent
├── crisis_support_agent
├── personalized_wellness_planner
├── wellness_progress_agent
└── community_resource_agent
```

### Core Agents

1. **Interactive WellCare Agent**: Central orchestrator handling user interaction
2. **Wellness Assessor Agent**: Conducts PHQ-9 and GAD-7 assessments
3. **Crisis Support Agent**: Provides immediate crisis intervention
4. **Personalized Wellness Planner**: Creates evidence-based wellness plans
5. **Wellness Progress Agent**: Tracks mood and progress over time
6. **Community Resource Agent**: Finds local mental health services

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Google API Key (Gemini Pro access)
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agent-wellcare
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Google ADK:
   ```bash
   pip install google-adk
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your GOOGLE_API_KEY
   ```

### Running the Agent

#### Option 1: ADK Web Interface (Recommended)
```bash
# Start the ADK web interface on port 8000
adk web agents

# Or start on a different port (e.g., 8001)
adk web agents --port 8001
```

#### Option 2: Flask Web Interface
```bash
# Start the Flask web server
python app.py
```

#### Option 3: Terminal Interface
```bash
# Run in terminal mode
python wellcare_agent_simple.py
```

## 🛠️ Tools & Capabilities

### Assessment Tools
- `conduct_phq9_assessment`: Depression screening
- `conduct_gad7_assessment`: Anxiety screening
- `assess_crisis_risk`: Crisis detection

### Planning Tools
- `generate_cbt_exercises`: Cognitive Behavioral Therapy exercises
- `create_mindfulness_plan`: Mindfulness-based interventions
- `suggest_physical_activities`: Exercise recommendations
- `design_sleep_hygiene_plan`: Sleep improvement strategies

### Resource Tools
- `find_local_resources`: Community mental health services
- `get_crisis_hotlines`: Emergency contact information
- `save_wellness_plan`: Export plans to file

### Tracking Tools
- `log_mood_entry`: Record daily mood and feelings
- `analyze_progress_trends`: Identify patterns and improvements
- `generate_progress_report`: Summarize progress over time

## 📁 Project Structure

```
agent-wellcare/
├── agents/                     # ADK agent directory
│   └── wellcare/               # WellCare agent
│       └── agent.py            # Main ADK agent implementation
├── agent.py                    # Main ADK agent implementation
├── app.py                      # Flask web interface
├── wellcare_agent_simple.py    # Terminal-based version
├── start_adk.py                # ADK startup script
├── START_WEB.bat               # Windows batch launcher
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # Web interface template
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore file
├── README.md                   # This file
└── LICENSE                     # MIT License
```

## 🔧 Development

The project includes development tools for testing and extending the agent functionality.

Refer to the ADK documentation for implementation details and testing procedures.

## 📚 Documentation

Refer to the official Google ADK documentation for detailed setup and usage instructions.

## ⚠️ Important Disclaimers

**This is NOT a replacement for professional mental health care.**

Agent WellCare is designed to:
- Provide accessible mental health support
- Offer evidence-based wellness guidance
- Connect users with professional resources
- Support mental health journeys

Agent WellCare is NOT intended to:
- Diagnose mental health conditions
- Provide medical advice
- Replace professional therapy or psychiatric care
- Handle life-threatening emergencies (call 911)

**In crisis situations, always contact emergency services or crisis hotlines:**
- US: 988 (Suicide & Crisis Lifeline)
- UK: 116 123 (Samaritans)
- Emergency: 911/999/112


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google's Agent Development Kit team
- Mental health professionals who informed the assessment tools
- Open source community for inspiration and support

---
*Agent WellCare: Making mental health support more accessible, one conversation at a time.*
