from agents.orchestrator_agent import orchestrator_agent
from agents.graph_agent import graph_agent
from agents.Report_agent import Report_agent

orchestrator = orchestrator_agent()
graph_gen = graph_agent()
reporter = Report_agent()

report = orchestrator.generate_report("data/SIT Extract -W1-20260625.xlsx")
graphs = graph_gen.generate_graphs(report["execution_summary"], report["defect_summary"])
output_path = reporter.generate_report(report, graphs, output_path="output/report.html")

print(f"Report available at: {output_path}")
