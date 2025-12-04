from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from agent.state import AgentState
from agent.tools import TOOLS
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

lc_agent = create_agent(model=llm, tools=TOOLS)

def build_agent_graph():
    workflow = StateGraph(AgentState)

    def call_lc_agent(state):
        question = state["question"]
        try:
            system_prompt = (
                "You are an intelligent coding assistant.\n"
                "1. When suggesting code improvements, ALWAYS provide the specific code changes in markdown code blocks (```language ... ```). Ensure there is a blank line before and after the code block.\n"
                "2. At the end of your response, ALWAYS provide a brief 'Summary' section summarizing your analysis and suggestions.\n"
                "3. CRITICAL: If the user mentions a file name, you MUST IMMEDIATELY use the 'file_lookup' tool to find it. DO NOT ask the user for the file content or path. YOU have the tools to find it. USE THEM."
            )
            inputs = {"messages": [("system", system_prompt), ("user", question)]}
            result = lc_agent.invoke(inputs)

            messages = result.get("messages", [])
            if messages:
                last_msg = messages[-1]
                answer_text = getattr(last_msg, "content", "") or str(last_msg)
                return {"answer": answer_text}
            
            return {"answer": "No response from agent."}

        except Exception as e:
            return {"answer": f"Agent error: {e}"}

    workflow.add_node("agent_node", call_lc_agent)
    workflow.set_entry_point("agent_node")
    workflow.add_edge("agent_node", END)

    return workflow.compile()
    
agent_graph = build_agent_graph()
