class Report_agent:
    def __init__(self):
        print("Report agent initialized")
    def generate_report(self, report,graphs):
        print("Generating report...")
        execution_html_1 = graphs["execution_graph_1"].to_html(full_html=False, include_plotlyjs='cdn')
        execution_html_2 = graphs["execution_graph_2"].to_html(full_html=False)
        defect_html_1 = graphs["defect_graph_1"].to_html(full_html=False)
        defect_html_2 = graphs["defect_graph_2"].to_html(full_html=False)
        execution_summary = report["execution_summary"]
        defect_summary = report["defect_summary"]
        html_content = f"""
        