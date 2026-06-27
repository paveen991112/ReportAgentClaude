import pandas as pd
class Defect_agent:
    def _init_(self):
        print("Defect agent initialized")
    def defect_analyze(self,file_path,workbook_metadata):
        defect_sheet = "Defects-INPUT"
        df = pd.read_excel(file_path, sheet_name=defect_sheet)
        total_rows = len(df)

        #Status wise split up All defects
        open_defects = (len(df[df['Status'] == 'In Progress'])+
                       len(df[df['Status'] == 'In Analysis'])+
                       len(df[df['Status'] == 'New'])+
                       len(df[df['Status'] == 'Reopened']))
        closed_defects = (len(df[df['Status'] == 'Closed'])+
                         len(df[df['Status'] == 'Resolved']))
        ready_for_test_defects = len(df[df['Status'] == 'Ready for Retest'])
        if(total_rows>0):
            open_defects_percentage = round((open_defects/total_rows)*100,2)
            closed_defects_percentage = round((closed_defects/total_rows)*100,2)
            ready_for_test_defects_percentage = round((ready_for_test_defects/total_rows)*100,2)
        else:
            open_defects_percentage = 0
            closed_defects_percentage = 0
            ready_for_test_defects_percentage = 0

        #Severity wise split up All defects
        critical_defects = len(df[df['Severity'] == 'Critical'])
        high_defects = len(df[df['Severity'] == 'High'])
        medium_defects = len(df[df['Severity'] == 'Medium'])
        low_defects = len(df[df['Severity'] == 'Low'])

        #Severity wise split up open defects
        open_critical_defects = len(df[(df['Severity'] == 'Critical') & (df['Status'].isin(['In Progress', 'In Analysis', 'New', 'Reopened']))])
        open_high_defects = len(df[(df['Severity'] == 'High') & (df['Status'].isin(['In Progress', 'In Analysis', 'New', 'Reopened']))])
        open_medium_defects = len(df[(df['Severity'] == 'Medium') & (df['Status'].isin(['In Progress', 'In Analysis', 'New', 'Reopened']))])
        open_low_defects = len(df[(df['Severity'] == 'Low') & (df['Status'].isin(['In Progress', 'In Analysis', 'New', 'Reopened']))])

        defect_summary = {
            "total_rows": total_rows,
            "open_defects": open_defects,
            "closed_defects": closed_defects,
            "ready_for_test_defects": ready_for_test_defects,
            "open_defects_percentage": open_defects_percentage,
            "closed_defects_percentage": closed_defects_percentage,
            "ready_for_test_defects_percentage": ready_for_test_defects_percentage,
            "critical_defects": critical_defects,
            "high_defects": high_defects,
            "medium_defects": medium_defects,
            "low_defects": low_defects,
            "open_critical_defects": open_critical_defects,
            "open_high_defects": open_high_defects,
            "open_medium_defects": open_medium_defects,
            "open_low_defects": open_low_defects
        }

        return defect_summary