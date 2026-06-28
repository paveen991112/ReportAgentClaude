import pandas as pd
class execution_agent:
    def __init__(self):
        print("execution agent initialized")
    def execute_workbook(self,file_path,workbook_metadata):
        execution_sheet = "Execution-input"
        df = pd.read_excel(file_path, sheet_name=execution_sheet)
        #df['Status']=(df['Status'].str.strip().str.lower())
        total_rows = len(df)
        passed = len(df[df['Status'] == 'Passed'])
        failed = len(df[df['Status'] == 'Failed'])
        blocked = len(df[df['Status'] == 'Blocked'])
        inprogress = len(df[df['Status'] == 'In Progress'])
        unexecuted = len(df[df['Status'] == 'Unexecuted'])
        if(total_rows>0):
            pass_percentage = round((passed/total_rows)*100,2)
            execution_percentage = round(((passed + failed)/total_rows)*100,2)
        else:
            pass_percentage = 0
            execution_percentage = 0
        executed_rows = passed + failed 
        #check for total
        if(passed + failed + blocked + inprogress + unexecuted != total_rows):
            print("Warning: The sum of individual status counts does not match the total row count.")
        execution_summary = {
            "total_rows": total_rows,
            "passed": passed,
            "failed": failed,
            "blocked": blocked,
            "inprogress": inprogress,
            "unexecuted": unexecuted,
            "executed_rows": executed_rows,
            "pass % ":pass_percentage,
            "Execution %":execution_percentage
        }
        return execution_summary