import plotly.express as px
class graph_agent:
    def __init__(self):
        print("graph agent initialized")
    def _empty_pie(self, title, message):
        # Plotly renders equal slices when every value is 0, which is misleading.
        # Show an explicit empty state instead.
        fig = px.pie(values=[1], names=[message], title=title)
        fig.update_traces(textinfo='none', marker=dict(colors=['#e0e0e0']))
        fig.add_annotation(text=message, showarrow=False,
                           font=dict(size=16, color='#888'),
                           x=0.5, y=0.5, xref='paper', yref='paper')
        fig.update_layout(showlegend=False)
        return fig
    def generate_execution_graph_1(self,execution_metrics):
        labels = [ "Passed", "Failed", "Blocked", "In Progress", "Unexecuted"]
        values = [ execution_metrics["passed"],
                   execution_metrics["failed"],
                   execution_metrics["blocked"], 
                   execution_metrics["inprogress"], 
                   execution_metrics["unexecuted"]]
        fig = px.bar(x=labels, y=values, title='Execution Metrics', orientation='v')
        return fig
    def generate_execution_graph_2(self,execution_metrics):
        labels = ["total_rows", "executed_rows"]
        values = [execution_metrics["total_rows"], execution_metrics["executed_rows"]]
        fig = px.bar(x=labels, y=values, title='Execution Metrics', orientation='v')
        return fig
    def generate_defect_graph_1(self,defect_metrics):
        labels = ["Open Defects", "Closed Defects", "Ready for Test Defects"]
        values = [defect_metrics["open_defects"], defect_metrics["closed_defects"], defect_metrics["ready_for_test_defects"]]
        if sum(values) == 0:
            return self._empty_pie('Defect Metrics', 'No defects')
        fig = px.pie(values=values, names=labels, title='Defect Metrics')
        return fig
    def generate_defect_graph_2(self,defect_metrics):
        labels = ["Critical", "High", "Medium", "Low"]
        values = [defect_metrics["open_critical_defects"], defect_metrics["open_high_defects"], defect_metrics["open_medium_defects"], defect_metrics["open_low_defects"]]
        if sum(values) == 0:
            return self._empty_pie('Defect Severity Metrics', 'No open defects')
        fig = px.pie(values=values, names=labels, title='Defect Severity Metrics')
        return fig
    def generate_graphs(self, execution_metrics, defect_metrics):
        execution_graph_1 = self.generate_execution_graph_1(execution_metrics)
        execution_graph_2 = self.generate_execution_graph_2(execution_metrics)
        defect_graph_1 = self.generate_defect_graph_1(defect_metrics)
        defect_graph_2 = self.generate_defect_graph_2(defect_metrics)
        return {
            "execution_graph_1": execution_graph_1,
            "execution_graph_2": execution_graph_2,
            "defect_graph_1": defect_graph_1,
            "defect_graph_2": defect_graph_2
        }