# Import Required libraries
import requests
import os
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import logging
import openai
 
# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Define Request and Response Models
class AIRequest(Model):
    prompt: str

class AIResponse(Model):
    response: str

class ErrorResponse(Model):
    error : str
 
# Add a new function to get feedback from OpenAI
async def fetch_openai_feedback(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "system",
            "content": "Convert the input text into an easy-to-understand, compassionate message suitable for a religious leader in a developing country, such as South Africa, to use in a campaign. The message should address the input's core topic while incorporating relevant religious principles, scriptures, or values. Make the tone approachable, empathetic, and respectful to religious sensitivities. Keep the message concise and relatable to the daily lives of religious communities"},
            {
            "role": "user",
            "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1
        )
    return response.choices[0].message.content
 
# Define AI Agent
AIAgent = Agent(
    name="AIAgent",
    port=8000,
    seed="AI Agent secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)
 
# Registering agent on Almanac and funding it.
fund_agent_if_low(AIAgent.wallet.address())
 
# On agent startup printing address
@AIAgent.on_event('startup')
async def agent_details(ctx: Context):
    ctx.logger.info(f'Search Agent Address is {AIAgent.address}')
 
# On_query handler for news request
@AIAgent.on_query(model=AIRequest, replies={AIResponse, ErrorResponse})
async def query_handler(ctx: Context, sender: str, msg: AIRequest):
    try:
        ctx.logger.info(f'Fetching OpenAI feedback for: {msg.prompt}')
        ctx.logger.info(f"Sender: {sender}")
        feedback = await fetch_openai_feedback(f"Provide feedback for {msg.prompt}")
        ctx.logger.info(f"Feedback received: {feedback}")
        await ctx.send(sender, AIResponse(response=str(feedback)))
        ctx.logger.info(f"Feedback sent")
    except Exception as e:
        error_message = f"Error fetching feedback: {str(e)}"
        ctx.logger.error(error_message)
        await ctx.send(sender, ErrorResponse(error=str(error_message)))
 
if __name__ == "__main__":
    AIAgent.run() 