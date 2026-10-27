# Agentic Sales Outreach Copilot

A human-in-the-loop outreach drafting demo. It turns prospect facts supplied by the user into a concise email or LinkedIn connection draft.

## What it does
- Requires explicit context and relevance rather than inventing prospect research.
- Supports email and LinkedIn-style drafts.
- Marks every result as pending human review and never sends messages.
- Returns a checklist for fact checking, consent, and tone review.

## Run
Requires Python 3.10+.

```bash
python - <<'PY'
import json
from app import draft_outreach
sample = json.load(open("examples/prospect.json", encoding="utf-8"))
print(draft_outreach(sample["prospect"], offer=sample["offer"], sender=sample["sender"], channel=sample["channel"])["message"])
PY
```

## Tests
`python -m unittest discover -s tests -v`

## Safety and limitations
This demo does not browse the web, verify company news, access a CRM, or send messages. Only include prospect details you have a legitimate basis to use. Check consent, opt-out requirements, platform policies, and applicable anti-spam laws before outreach. Do not use personalization that implies a relationship or fact that does not exist.

## Explore more

- [AI Lead Qualification Agent](https://github.com/HardikPaghdar/ai-lead-qualification-agent) — transparent rule-based lead triage.
- [LLM Cost Optimization Gateway](https://github.com/HardikPaghdar/llm-cost-optimization-gateway) — policy-based model selection prototype.
- [More projects on my portfolio](https://hardikpaghdar.netlify.app/).
