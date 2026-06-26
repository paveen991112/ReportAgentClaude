import pandas as pd
class worbook_agent:
    def __init__(self):
        print("workbook agent initialized")
    def analyze_workbook(self,file_path):
        excel_file = pd.ExcelFile(file_path)
        print("Workbook loaded successfully")
        print("Available sheets")
        for sheet in excel_file.sheet_names:
            print(sheet)    