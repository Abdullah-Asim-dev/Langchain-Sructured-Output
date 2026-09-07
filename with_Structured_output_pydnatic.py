import os
from langchain_groq import ChatGroq
from typing import TypedDict, Annotated, Optional, List,Literal
from pydantic import BaseModel,Field
from dotenv import load_dotenv

# Environment variables load karein
load_dotenv()

# 1. Model define karein (Temperature structured data ke liye 0.1 ya 0 best hai)
model = ChatGroq(model='openai/gpt-oss-20b', temperature=0.1)

# 2. Schema define karein (Sari fields class ke andar honi chahiye)
class Review(BaseModel):

    key_themes:list[str]=Field(description=  'write down all the key themes discuss in the review in a list format')
    summary:list[str]=Field(description='A brief summary of the review')
    sentiment:Literal["pos","neg"]=Field(description= 'return a sentiment of the review either negative, positive or neutral')
    pros:list[str]=Field(default=None,description='write down all the pros inside the list')
    cons:list[str]=Field(default=None,description='write down all the consos inside the list')
    name=Optional[str]=Field(description='write down the namen of the reviwer ')
# 3. Class se BAHAR small 's' ke sath structured output attach karein
structured_model = model.with_structured_output(BaseModel)

# 4. Input text
text = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Abdullah Asim ."""

# 5. Invoke karein aur result print karein
result = structured_model.invoke(text)
print("--- Full Result ---")
print(result)

# Yeh type check karne ke liye
print("\n--- Type Check ---")
print(type(result))

# Yeh summary aur sentiment ko print karane ke liye
print("\n--- Specific Fields ---")
print("Summary:", result.summary)
print("Sentiment:", result.sentiment)
print("Pros:", result.pros)
print("name:" ,result.name)
