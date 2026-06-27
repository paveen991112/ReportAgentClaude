import pandas as pd
class workbook_agent:
    def __init__(self):
        print("workbook agent initialized")
    def analyze_workbook(self,file_path):
        excel_file = pd.ExcelFile(file_path)
        workbook_info = {
            "sheet_count": len(excel_file.sheet_names),
            "sheet_names": excel_file.sheet_names
        }
        for sheet in excel_file.sheet_names:
            df = pd.read_excel(excel_file, sheet_name=sheet)
            workbook_info[sheet] = {
                "row_count": len(df),
                "column_count": len(df.columns),
                "columns": df.columns.tolist()
            }
        return workbook_info