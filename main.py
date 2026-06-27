from agents.workbook_agent import workbook_agent
from agents.execution_agent import execution_agent
from agents.Defect_agent import Defect_agent

agent = workbook_agent()
result = agent.analyze_workbook("data/SIT Extract -W1-20260625.xlsx")
execution_agent_instance = execution_agent()
execution_result = execution_agent_instance.execute_workbook("data/SIT Extract -W1-20260625.xlsx", result)

defect_agent_instance = Defect_agent()
defect_result = defect_agent_instance.defect_analyze("data/SIT Extract -W1-20260625.xlsx", result)
print(result)
print(execution_result)
print(defect_result)
