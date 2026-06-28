from agents.orchestrator_agent import orchestrator_agent
from agents.graph_agent import graph_agent

orchestrator = orchestrator_agent()
graph = graph_agent()
report = orchestrator.generate_report("data/SIT Extract -W1-20260625.xlsx")
print(report.keys())
graph_agent = graph.generate_graphs(report["execution_summary"],report["defect_summary"])
#print(type(execution_graph))
for graph in graph_agent.values():
    graph.show()

