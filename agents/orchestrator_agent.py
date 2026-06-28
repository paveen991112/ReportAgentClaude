from agents.workbook_agent import workbook_agent
from agents.execution_agent import execution_agent
from agents.Defect_agent import Defect_agent

class orchestrator_agent:
    def __init__(self):
        print("orchestrator agent initialized")
        self.workbook_agent_instance = workbook_agent()
        self.execution_agent_instance = execution_agent()
        self.defect_agent_instance = Defect_agent()
    
    def generate_report(self, file_path):
        # Step 1: Analyze the workbook
        workbook_result = self.workbook_agent_instance.analyze_workbook(file_path)
        
        # Step 2: Execute the workbook
        execution_result = self.execution_agent_instance.execute_workbook(file_path, workbook_result)
        
        # Step 3: Analyze defects
        defect_result = self.defect_agent_instance.defect_analyze(file_path, workbook_result)
        
        result = {
            "workbook_analysis": workbook_result,
            "execution_summary": execution_result,
            "defect_summary": defect_result
        }
        return result