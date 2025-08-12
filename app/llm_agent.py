### llm_agent.py
import os
import logging
from dotenv import load_dotenv

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Logging config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AgentLogger")

# Load secrets
load_dotenv()
token = os.getenv("GITHUB_TOKEN")

# Set up Azure inference client
client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=AzureKeyCredential(token),
)

def read_file_local(path: str) -> str:
    logger.info(f"Reading file locally: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def run_agent():
    # Define paths
    selected_file = "data/analytics-2025-post-event-8.csv"
    current_season_context_file = "data/analytics_context.txt"
    history_file = "data/motogp_2024_season_summary.txt"

    # Load contexts
    summary = read_file_local(selected_file)
    current_season_file_context = read_file_local(current_season_context_file)
    history = read_file_local(history_file)

    context = f"MotoGP historical context:\n{history}\n\nCurrent season summary:\n{summary}\n Current season csv file description, to understand the dataset: \n {current_season_file_context}"

    logger.info("Sending prompt to LLM...")
    query = (
    "You are a MotoGP analyst. Use the current season's data to write a fluent, natural analysis focusing only on the top 3 riders. "
    "Your analysis should go beyond simply describing statistics – use them as evidence to support deep, well-reasoned insights.\n\n"
    "Approach the task like this:\n"
    "1. Begin by identifying the most significant patterns and outliers in the current data.\n"
    "2. Compare these with key benchmarks or trends from the previous season.\n"
    "3. Ask yourself: What has changed? What has remained consistent? Why?\n"
    "4. Formulate hypotheses or narratives that explain these developments.\n"
    "5. Support your conclusions with data points, but prioritize interpretation over enumeration.\n\n"
    "Your goal is to extract meaning, anticipate underlying causes, and highlight implications. "
    "Think like an expert who is uncovering the deeper story behind the numbers."
    f"\n\n{context}"
    )


    response = client.complete(
        messages=[
            SystemMessage("You are a MotoGP analyst with a lot of knowledge about the history of the sport and have access to current data of the season."),
            UserMessage(query)
        ],
        temperature=0.1,
        top_p=1.0,
        max_tokens=1000,
        model="mistral-ai/mistral-medium-2505"
    )

    print("\n--- ANALYSIS ---\n")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    run_agent()
