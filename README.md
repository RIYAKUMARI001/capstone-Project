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
# Start the ADK web interface
adk web
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

#### Option 4: Windows Batch File
Double-click `START_WEB.bat` to choose your preferred interface.

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
├── agent.py                    # Official ADK agent implementation
├── wellcare_agent.py           # Original multi-agent version
├── wellcare_agent_simple.py    # Terminal-based version
├── app.py                      # Flask web interface
├── START_WEB.bat               # Windows batch launcher
├── requirements.txt            # Python dependencies
├── test_adk.py                 # ADK implementation tests
├── demo_adk.py                 # ADK demo
├── test_agent.py               # Component tests
├── example_usage.py            # Usage examples
├── templates/
│   └── index.html              # Web interface template
├── .env.example                # Environment variables template
├── README.md                   # This file
├── SETUP.md                    # Installation guide
├── RUN_ADK.md                  # ADK usage guide
└── QUICKSTART.md               # Quick start guide
```

## 🔧 Development

### Testing

Run component tests:
```bash
python test_agent.py
```

Test ADK implementation:
```bash
python test_adk.py
```

### Example Usage

See example interactions:
```bash
python example_usage.py
```

## 📚 Documentation

- [SETUP.md](SETUP.md): Complete installation guide
- [RUN_ADK.md](RUN_ADK.md): ADK-specific instructions
- [QUICKSTART.md](QUICKSTART.md): Fast track guide
- [FINAL_SETUP_GUIDE.md](FINAL_SETUP_GUIDE.md): Final configuration steps

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

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google's Agent Development Kit team
- Mental health professionals who informed the assessment tools
- Open source community for inspiration and support

---
*Agent WellCare: Making mental health support more accessible, one conversation at a time.*