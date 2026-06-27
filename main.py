from agents.workbook_agent import workbook_agent

agent = workbook_agent()
result = agent.analyze_workbook("data/SIT Extract -W1-20260625.xlsx")
print(result)
