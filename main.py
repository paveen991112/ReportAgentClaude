from agents.workbook_agent import workbook_agent
from agents.execution_agent import execution_agent

agent = workbook_agent()
result = agent.analyze_workbook("data/SIT Extract -W1-20260625.xlsx")
execution_agent_instance = execution_agent()
execution_result = execution_agent_instance.execute_workbook("data/SIT Extract -W1-20260625.xlsx", result)
print(execution_result)
