import os
from datetime import datetime

class Report_agent:
    def __init__(self):
        print("Report agent initialized")

    def generate_report(self, report, graphs, output_path="output/report.html"):
        print("Generating report...")

        # Load the Plotly.js version that matches the installed plotly package on the
        # first chart only ('cdn'); the rest reuse it (False). Using a hardcoded
        # plotly-latest.min.js CDN tag breaks newer charts because that URL is frozen
        # at Plotly.js v1.x, which can't read the binary typed-array data format.
        execution_html_1 = graphs["execution_graph_1"].to_html(full_html=False, include_plotlyjs="cdn")
        execution_html_2 = graphs["execution_graph_2"].to_html(full_html=False, include_plotlyjs=False)
        defect_html_1 = graphs["defect_graph_1"].to_html(full_html=False, include_plotlyjs=False)
        defect_html_2 = graphs["defect_graph_2"].to_html(full_html=False, include_plotlyjs=False)

        ex = report["execution_summary"]
        df = report["defect_summary"]
        generated_at = datetime.now().strftime("%d %b %Y, %H:%M")

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SIT Test Report</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #f0f2f5;
            color: #333;
        }}
        header {{
            background: linear-gradient(135deg, #1a237e, #283593);
            color: white;
            padding: 28px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        header h1 {{ font-size: 1.8rem; font-weight: 600; }}
        header .meta {{ font-size: 0.85rem; opacity: 0.8; text-align: right; }}
        main {{ padding: 32px 40px; max-width: 1400px; margin: 0 auto; }}
        h2 {{
            font-size: 1.1rem;
            font-weight: 600;
            color: #1a237e;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 16px;
            padding-bottom: 8px;
            border-bottom: 2px solid #1a237e;
        }}
        .section {{ margin-bottom: 40px; }}
        .cards {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
            gap: 16px;
            margin-bottom: 8px;
        }}
        .card {{
            background: white;
            border-radius: 8px;
            padding: 20px 16px;
            text-align: center;
            box-shadow: 0 1px 4px rgba(0,0,0,0.08);
            border-top: 4px solid #ccc;
        }}
        .card .value {{
            font-size: 2rem;
            font-weight: 700;
            line-height: 1.1;
        }}
        .card .label {{
            font-size: 0.78rem;
            color: #666;
            margin-top: 6px;
            text-transform: uppercase;
            letter-spacing: 0.03em;
        }}
        .card.total   {{ border-color: #1a237e; }} .card.total .value   {{ color: #1a237e; }}
        .card.passed  {{ border-color: #2e7d32; }} .card.passed .value  {{ color: #2e7d32; }}
        .card.failed  {{ border-color: #c62828; }} .card.failed .value  {{ color: #c62828; }}
        .card.blocked {{ border-color: #e65100; }} .card.blocked .value {{ color: #e65100; }}
        .card.inprog  {{ border-color: #f9a825; }} .card.inprog .value  {{ color: #f9a825; }}
        .card.unexec  {{ border-color: #78909c; }} .card.unexec .value  {{ color: #78909c; }}
        .card.pct     {{ border-color: #00695c; }} .card.pct .value     {{ color: #00695c; }}
        .card.open    {{ border-color: #c62828; }} .card.open .value    {{ color: #c62828; }}
        .card.closed  {{ border-color: #2e7d32; }} .card.closed .value  {{ color: #2e7d32; }}
        .card.retest  {{ border-color: #1565c0; }} .card.retest .value  {{ color: #1565c0; }}
        .card.critical{{ border-color: #b71c1c; }} .card.critical .value{{ color: #b71c1c; }}
        .card.high    {{ border-color: #e64a19; }} .card.high .value    {{ color: #e64a19; }}
        .card.medium  {{ border-color: #f57f17; }} .card.medium .value  {{ color: #f57f17; }}
        .card.low     {{ border-color: #558b2f; }} .card.low .value     {{ color: #558b2f; }}
        .table-wrap {{ overflow-x: auto; margin-top: 8px; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        }}
        th {{
            background: #1a237e;
            color: white;
            padding: 12px 16px;
            text-align: left;
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}
        td {{
            padding: 11px 16px;
            border-bottom: 1px solid #eee;
            font-size: 0.9rem;
        }}
        tr:last-child td {{ border-bottom: none; }}
        tr:nth-child(even) td {{ background: #f8f9ff; }}
        .badge {{
            display: inline-block;
            padding: 2px 10px;
            border-radius: 12px;
            font-size: 0.78rem;
            font-weight: 600;
        }}
        .badge-red    {{ background: #fce4e4; color: #c62828; }}
        .badge-orange {{ background: #fdebd0; color: #e64a19; }}
        .badge-yellow {{ background: #fef9e7; color: #f57f17; }}
        .badge-green  {{ background: #e8f5e9; color: #2e7d32; }}
        .charts-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
        }}
        .chart-card {{
            background: white;
            border-radius: 8px;
            padding: 16px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        }}
        @media (max-width: 768px) {{
            main {{ padding: 20px; }}
            .charts-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>

<header>
    <div>
        <h1>SIT Test Execution Report</h1>
        <div style="font-size:0.9rem; margin-top:4px; opacity:0.85;">System Integration Testing — Daily Summary</div>
    </div>
    <div class="meta">
        <div>Generated on</div>
        <div style="font-size:1rem; font-weight:600; margin-top:2px;">{generated_at}</div>
    </div>
</header>

<main>

    <!-- ── Execution Summary ── -->
    <div class="section">
        <h2>Test Execution Summary</h2>
        <div class="cards">
            <div class="card total">
                <div class="value">{ex['total_rows']}</div>
                <div class="label">Total Test Cases</div>
            </div>
            <div class="card passed">
                <div class="value">{ex['passed']}</div>
                <div class="label">Passed</div>
            </div>
            <div class="card failed">
                <div class="value">{ex['failed']}</div>
                <div class="label">Failed</div>
            </div>
            <div class="card blocked">
                <div class="value">{ex['blocked']}</div>
                <div class="label">Blocked</div>
            </div>
            <div class="card inprog">
                <div class="value">{ex['inprogress']}</div>
                <div class="label">In Progress</div>
            </div>
            <div class="card unexec">
                <div class="value">{ex['unexecuted']}</div>
                <div class="label">Unexecuted</div>
            </div>
            <div class="card pct">
                <div class="value">{ex['pass % ']}%</div>
                <div class="label">Pass Rate</div>
            </div>
            <div class="card pct">
                <div class="value">{ex['Execution %']}%</div>
                <div class="label">Execution Rate</div>
            </div>
        </div>
    </div>

    <!-- ── Defect Summary ── -->
    <div class="section">
        <h2>Defect Summary</h2>
        <div class="cards">
            <div class="card total">
                <div class="value">{df['total_rows']}</div>
                <div class="label">Total Defects</div>
            </div>
            <div class="card open">
                <div class="value">{df['open_defects']}</div>
                <div class="label">Open ({df['open_defects_percentage']}%)</div>
            </div>
            <div class="card closed">
                <div class="value">{df['closed_defects']}</div>
                <div class="label">Closed ({df['closed_defects_percentage']}%)</div>
            </div>
            <div class="card retest">
                <div class="value">{df['ready_for_test_defects']}</div>
                <div class="label">Ready for Retest ({df['ready_for_test_defects_percentage']}%)</div>
            </div>
            <div class="card critical">
                <div class="value">{df['critical_defects']}</div>
                <div class="label">Critical</div>
            </div>
            <div class="card high">
                <div class="value">{df['high_defects']}</div>
                <div class="label">High</div>
            </div>
            <div class="card medium">
                <div class="value">{df['medium_defects']}</div>
                <div class="label">Medium</div>
            </div>
            <div class="card low">
                <div class="value">{df['low_defects']}</div>
                <div class="label">Low</div>
            </div>
        </div>
    </div>

    <!-- ── Open Defects by Severity ── -->
    <div class="section">
        <h2>Open Defects by Severity</h2>
        <div class="table-wrap">
            <table>
                <thead>
                    <tr>
                        <th>Severity</th>
                        <th>Open Defects</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><span class="badge badge-red">Critical</span></td>
                        <td>{df['open_critical_defects']}</td>
                    </tr>
                    <tr>
                        <td><span class="badge badge-orange">High</span></td>
                        <td>{df['open_high_defects']}</td>
                    </tr>
                    <tr>
                        <td><span class="badge badge-yellow">Medium</span></td>
                        <td>{df['open_medium_defects']}</td>
                    </tr>
                    <tr>
                        <td><span class="badge badge-green">Low</span></td>
                        <td>{df['open_low_defects']}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- ── Charts ── -->
    <div class="section">
        <h2>Execution Charts</h2>
        <div class="charts-grid">
            <div class="chart-card">{execution_html_1}</div>
            <div class="chart-card">{execution_html_2}</div>
        </div>
    </div>

    <div class="section">
        <h2>Defect Charts</h2>
        <div class="charts-grid">
            <div class="chart-card">{defect_html_1}</div>
            <div class="chart-card">{defect_html_2}</div>
        </div>
    </div>

</main>
</body>
</html>"""

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"Report saved to {output_path}")
        return output_path
