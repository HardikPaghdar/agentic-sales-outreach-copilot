"""Personalized outreach drafts from user-provided prospect facts; never sends messages."""
from string import Template
TEMPLATES={
 "email":Template("Subject: $subject\n\nHi $first_name,\n\nI noticed $context. $relevance\n\nWould it be useful to compare notes on $offer? If this is not a priority, no worries.\n\nBest,\n$sender"),
 "linkedin":Template("Hi $first_name — $context. I work with teams on $offer and thought it might be relevant because $relevance. Open to connecting?")
}
def draft_outreach(prospect:dict,*,offer:str,sender:str,channel:str="email")->dict:
    required=("name","company","context","relevance")
    missing=[key for key in required if not str(prospect.get(key,"")).strip()]
    if missing: raise ValueError("missing prospect fields: "+", ".join(missing))
    if channel not in TEMPLATES: raise ValueError("channel must be email or linkedin")
    first_name=prospect["name"].strip().split()[0]
    if not offer.strip() or not sender.strip(): raise ValueError("offer and sender are required")
    message=TEMPLATES[channel].substitute(subject=f"Idea for {prospect['company'].strip()}",first_name=first_name,
      context=prospect["context"].strip(),relevance=prospect["relevance"].strip(),offer=offer.strip(),sender=sender.strip())
    return {"channel":channel,"company":prospect["company"].strip(),"message":message,"status":"draft_pending_human_review","checks":["Verify every prospect-specific statement","Check consent and applicable outreach rules","Review tone and remove unsupported claims"],"sent":False}
