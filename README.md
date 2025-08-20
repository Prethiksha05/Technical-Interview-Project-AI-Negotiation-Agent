# Technical Interview Project: AI Negotiation Agent

## 🎯 The Challenge
Build a BUYER agent using Google DeepMind's Concordia framework that can successfully negotiate against our hidden SELLER agent. If your agent achieves profitable deals while maintaining character consistency, you advance to the next interview round.

**Time Limit**: 3-4 hours  
**Success Criteria**: Achieve at least 2 profitable deals out of 3 test scenarios

---

## 📋 Project Overview

### Your Mission
Create an AI-powered buyer agent that can:
1. Negotiate effectively for mangoes and other perishable goods
2. Stay within budget constraints while maximizing savings
3. Maintain a consistent personality throughout negotiations
4. Close deals before timeout (10 rounds max)

### What We Provide
- Base template with Concordia integration
- Sample products and test scenarios
- Mock seller for local testing
- Evaluation framework

### What You Build
- A complete BUYER agent with unique personality
- Negotiation strategy using Concordia components
- Memory system for tracking conversation context
- Decision logic for when to accept/counter/walk away

---

## 🛠️ Technical Requirements

### 1. **Framework**: Google DeepMind's Concordia (Required)
```bash
# Install Concordia
pip install git+https://github.com/google-deepmind/concordia.git
```

### 2. **Core Components to Implement**

#### Required Concordia Components:
- **Memory Component**: Store and retrieve negotiation history
- **Personality Component**: Define consistent character traits
- **Observation Component**: Process seller messages and offers
- **Decision Component**: Implement negotiation strategy

#### Component Structure:
```python
class BuyerPersonalityComponent(entity_component.ContextComponent):
    """Your agent's personality definition"""
    
    def make_pre_act_value(self) -> str:
        # Return personality context for LLM
        pass
    
    def get_state(self):
        # Return current state for serialization
        pass
    
    def set_state(self, state):
        # Restore from saved state
        pass
```

### 3. **Language Model**
- Use Llama-3-8B via ollama or AWS Bedrock or HuggingFace

---

## 🎮 Game Rules

### The Negotiation Process
1. **Roles**: You build a BUYER, we test it against our SELLER
2. **Hidden Information**: 
   - Your agent knows its maximum budget
   - Seller's minimum price is hidden
3. **Win Conditions**:
   - Close deal within budget
   - Achieve meaningful savings
   - Complete within 10 rounds

### Scoring Breakdown
- **Deal Success** (40%): Did you close the deal?
- **Savings Achieved** (30%): How much below budget?
- **Character Consistency** (20%): Did you maintain personality?
- **Code Quality** (10%): Clean, modular implementation

---

## 🎭 Choose Your Agent's Personality

Pick one archetype or create your own:

### Option 1: The Aggressive Negotiator
- Starts with low offers (60-70% of market)
- Uses pressure tactics
- Threatens to walk away
- Makes large jumps when necessary

### Option 2: The Diplomatic Buyer  
- Builds rapport first
- Makes reasonable offers (80-85% of market)
- Seeks win-win outcomes
- Gradual concessions

### Option 3: The Data Analyst
- Quotes market research
- Uses logical arguments
- Calculates fair prices
- Decisions based on data

### Option 4: Custom Personality
- Define your own unique traits
- Document the strategy
- Bonus points for creativity

---

## 📝 Implementation Template

```python
from concordia.agents import entity_agent_with_logging
from concordia.components import agent as agent_components
from concordia.associative_memory import associative_memory
from concordia.language_model import language_model
import json

class YourBuyerAgent:
    """
    Implement your buyer agent here.
    
    Requirements:
    1. Use Concordia components
    2. Maintain personality consistency
    3. Never exceed budget
    4. Implement smart negotiation logic
    """
    
    def __init__(self, name: str, personality_type: str, model: language_model.LanguageModel):
        self.name = name
        self.personality_type = personality_type
        self.model = model
        
        # Initialize Concordia components
        self._build_components()
    
    def _build_components(self):
        """Build required Concordia components"""
        # TODO: Implement memory, personality, observation components
        pass
    
    def negotiate(self, product: Product, budget: int, seller_message: str) -> NegotiationResponse:
        """
        Main negotiation method
        
        Args:
            product: Product being negotiated
            budget: Your maximum budget (NEVER exceed)
            seller_message: Latest message from seller
            
        Returns:
            NegotiationResponse with your action and message
        """
        # TODO: Implement negotiation logic
        pass
```

---

## 🧪 Test Scenarios

Your agent will face 3 scenarios:

### Scenario 1: Easy Market
- Product: 100 boxes Grade-A Alphonso Mangoes
- Market Price: ₹180,000
- Your Budget: ₹200,000
- Hidden Seller Min: ~₹150,000

### Scenario 2: Tight Budget
- Product: 150 boxes Grade-B Kesar Mangoes  
- Market Price: ₹150,000
- Your Budget: ₹140,000
- Hidden Seller Min: ~₹125,000

### Scenario 3: Premium Product
- Product: 50 boxes Export-Grade Mangoes
- Market Price: ₹200,000
- Your Budget: ₹190,000
- Hidden Seller Min: ~₹175,000

---

## 📊 Evaluation Process

### Round 1: Automated Testing (This Project)
1. We run your agent against our seller in 3 scenarios
2. Must achieve 2+ successful deals to advance
3. Evaluated on savings, consistency, and code quality

### Round 2: Live Interview (If You Pass)
1. Discuss your design decisions
2. Modify agent for new requirements
3. Explain Concordia integration choices
4. Debug edge cases live

---

## 🚀 Getting Started

### Step 1: Setup Environment
```bash
# Clone template repository
git clone [template-repo-url]

# Install dependencies
pip install -r requirements.txt

# Verify Concordia installation
python -c "import concordia; print('Concordia ready!')"
```

### Step 2: Run Baseline Test
```bash
# Test with example agent
python test_negotiation.py --agent example

# Should see sample negotiation output
```

### Step 3: Implement Your Agent
1. Choose personality type
2. Implement Concordia components
3. Define negotiation strategy
4. Test locally with mock seller

### Step 4: Validate & Submit
```bash
# Run validation suite
python validate_agent.py --agent your_agent.py

# Package for submission
python package_submission.py
```

---

## 📎 Submission Requirements

### Required Files
1. `buyer_agent.py` - Your Concordia-based implementation
2. `personality_config.json` - Agent personality definition
3. `strategy.md` - 1-page strategy explanation
4. `requirements.txt` - Any additional dependencies

### Code Standards
- Clean, documented code
- Type hints required
- Docstrings for main methods
- No hardcoded values

### Submission Command
```bash
python submit_project.py --name "Your Name" --email "your.email@example.com"
```

---

## 💡 Tips for Success

### Strategy Tips
1. **Opening Offers**: Start strong but realistic
2. **Concession Pattern**: Plan your negotiation trajectory
3. **Deadline Awareness**: Don't let negotiations timeout
4. **Personality Consistency**: Stay in character even under pressure

### Technical Tips
1. **Memory Usage**: Store key information from each round
2. **Component Design**: Keep components modular and testable
3. **Error Handling**: Handle edge cases gracefully
4. **State Management**: Properly implement get/set state

### Common Pitfalls
- ❌ Exceeding budget constraints
- ❌ Breaking character when desperate
- ❌ Ignoring seller's messages
- ❌ Poor time management (timeout)

---

## 🎯 Success Metrics

To advance to the next round, your agent must:

| Metric | Requirement | Weight |
|--------|-------------|--------|
| **Successful Deals** | ≥ 2 out of 3 | 40% |
| **Average Savings** | ≥ 10% below budget | 30% |
| **Character Score** | ≥ 80% consistency | 20% |
| **Code Quality** | Clean, modular, documented | 10% |

---

## ❓ FAQ

**Q: Can I see the seller's strategy?**  
A: No, the seller's logic is hidden. You must adapt to its behavior.

**Q: What if I can't close any deals?**  
A: Focus on understanding why. The mock seller helps you practice.

**Q: How is personality consistency measured?**  
A: We analyze language patterns, decision consistency, and trait adherence.

**Q: Can I use multiple personalities?**  
A: No, pick one and stick with it throughout all negotiations.

**Q: What version of Concordia should I use?**  
A: Latest version (2.0+) with prefab support.



**Good luck! May your negotiation skills—and code—speak for themselves.**
