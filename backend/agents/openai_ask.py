from uagents import Agent, Context, Model


class ContextPrompt(Model):
    context: str
    text: str


class Response(Model):
    text: str


agent = Agent(
    name="user",
    endpoint="http://localhost:8000/submit",
)


AI_AGENT_ADDRESS = "agent1qdhe4d3ucjusk6s2aw8av3fsj6ulz3ghyp7dsuhux23cq3vkljepxd8ujfl"


code = """
    vaccine is important for children
    """

prompt = ContextPrompt(
    context="Convert the input text into an easy-to-understand, compassionate message suitable for a religious leader in a developing country, such as South Africa, to use in a campaign. The message should address the input's core topic while incorporating relevant religious principles, scriptures, or values. Make the tone approachable, empathetic, and respectful to religious sensitivities. Keep the message concise and relatable to the daily lives of religious communities",
    text=code,
)


@agent.on_event("startup")
async def send_message(ctx: Context):
    await ctx.send(AI_AGENT_ADDRESS, prompt)


@agent.on_message(Response)
async def handle_response(ctx: Context, sender: str, msg: Response):
    ctx.logger.info(f"Received response from {sender}: {msg.text}")

@agent.on_query(ContextPrompt)
async def handle_query(ctx: Context):
    ctx.logger.info(f"Received query")


if __name__ == "__main__":
    agent.run()