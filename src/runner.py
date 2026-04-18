from src.graph import agent
from langchain_core.messages import HumanMessage

def run_agent(usr_input):

    config = {"configurable":{"thread_id":"user-1"}}

    response = agent.invoke(
        {"messages": [HumanMessage(content=usr_input)]},
        config=config
    )
    return response["messages"][-1].content

# while True:
#     user_inp = input("You: ")

#     if user_inp.lower() == 'exit':
#         print("Goodbye!")
#         break
#     response = run_agent(user_inp)
#     print(response)
