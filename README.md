# 🦜🔗 LangChain Structured Output - Native Data Extraction

This repository is built based on the **CampusX Generative AI Tutorial (Video 5)** by Nitish Singh. It demonstrates how to leverage Language Models (LLMs) to interact with databases, external APIs, and downstream code frameworks by converting unstructured text data into highly formatted, programmatic **JSON structures**.

Instead of scraping raw string outputs, this workflow uses LangChain's native structural features to achieve deterministic responses ready for integration.

---

## 📌 What is Covered (From the Tutorial)

1. **Unstructured vs Structured Outputs:** Why raw text response limits machine-to-machine connection and how JSON objects solve database ingestion hurdles.
2. **`with_structured_output` Implementation:** Direct schema mapping using LangChain's native function orchestration.
3. **Three Core Schema Configurations:**
   - **`TypedDict`:** Python-native structural dictionaries supported with `Annotated` parameters.
   - **`Pydantic (BaseModel)`:** Robust class modeling with internal data parsing, automatic casting, type checking, and constraints (`Field`).
   - **`JSON Schema`:** Universal object configurations ensuring multi-language flexibility (Python-Backend to JavaScript-Frontend cross-compatibility).
4. **LLM Execution Methods:** Differentiating structural pipelines via *Function Calling* vs. native *JSON Mode*.

---

## 🛠️ Tech Stack & Requirements

- **Framework:** LangChain (Core & Community)
- **Validation Engine:** Pydantic v2
- **Hardware/Provider:** Groq Cloud API (Utilizing ultra-fast LPU inference models)
- **Environment Handling:** Python-Dotenv

---

## 🚀 Installation & System Setup

### 1. Project Cloning
```bash
git clone https://github.com
cd YOUR_REPO_NAME
```

### 2. Dependency Management
Install the official LangChain packages alongside Pydantic configuration systems:
```bash
pip install langchain langchain-groq pydantic python-dotenv email-validator
```

### 3. API Key Injection
Create an environment variable tracking layer by constructing a `.env` file at the root level:
```env
GROQ_API_KEY=gsk_your_private_groq_api_key_here
```
> ⚠️ **Security Warning:** Ensure your `.env` target is indexed safely inside your `.gitignore` profile to shield your Cloud environment balances from scraping vulnerabilities.

---

## 📖 System Implementations

The project processes an exhaustive flagship mobile device review, slicing the multi-paragraph analysis layout dynamically into the following precise components:

### 🧩 1. The Pydantic Protocol (Strict Type Check Variant)
```python
from pydantic import BaseModel, Field
from typing import List, Optional

class ReviewSchema(BaseModel):
    key_themes: List[str] = Field(description="Extract all core topics covered into an array.")
    summary: str = Field(description="A concise summary capture of the text segment.")
    sentiment: str = Field(description="Context evaluation limiting tokens to positive, negative, or neutral.")
    pros: Optional[List[str]] = Field(default=None, description="Array mapping user value-adds.")
    cons: Optional[List[str]] = Field(default=None, description="Array tracking user complaints.")
    name: Optional[str] = Field(default=None, description="The specific structural signature author.")
```

### 📦 2. Execution Run Block
```python
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Instantiating the ultra-fast LPU backbone model
model = ChatGroq(model='openai/gpt-oss-20b', temperature=0.1)

# Attaching structural constraints
structured_engine = model.with_structured_output(ReviewSchema)

# Extracting data programmatically
result = structured_engine.invoke("...your unstructured text review chunk...")
print(result)
```

---

## 📊 Parsed Structural Validation Layout

Regardless of whichever schema variant you execute (`TypedDict`, `Pydantic`, or `JSON Schema`), your application runtime reliably guarantees raw outputs mapped strictly inside native programmatic dictionaries like this:

```json
{
  "key_themes": ["Performance", "Camera Quality", "Battery Degradation", "UI Overhead"],
  "summary": "The flagship device presents cutting edge raw compute metrics but stumbles significantly across bloatware parameters.",
  "sentiment": "positive",
  "pros": ["Snapdragon 8 Gen 3 performance throughput", "Excellent low light clarity performance"],
  "cons": ["One UI stock software overhead layer", "Cumbersome weight thresholds"],
  "name": "Nitish Singh"
}
```

## 🎯 Production Rule of Thumb

* Use **`Pydantic`** if your ecosystem runs cleanly through dedicated Python architectures needing explicit runtime validation layers.
* Use **`JSON Schema`** when exposing pipeline requirements across decoupled system boundaries (e.g., cross-communicating data pipelines shared with JavaScript/Node frameworks).

## 🎓 Acknowledgments
Special credits to **Nitish Singh (CampusX)** for compiling these technical frameworks across the Generative AI processing layers.
