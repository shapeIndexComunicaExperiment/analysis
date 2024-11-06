import json
from texttable import Texttable 
import latextable
from tabulate import tabulate
from typing import Optional, Dict
import os


artefactFolder = "./artefact/query_containment_execution_time"

datasets: Dict[str, str] = {
    "fully_bounded": "./results/shape-containment/fully_bounded/time_eval_summary_with_warm_up.json",
    "inner_dataset": "./results/shape-containment/inner_dataset/time_eval_summary_with_warm_up.json",
    "minimal": "./results/shape-containment/minimal/time_eval_summary_with_warm_up.json"
}
ignoreQueries = ["interactive-short-1-nocity", "interactive-short-3-unidir", "interactive-short-4-creator"]


for key, filePath in datasets.items():
    os.makedirs(os.path.join(artefactFolder, key), exist_ok=True)

    results: Optional[Dict[str,float]] = None
    
    with open(filePath, 'rb') as rf:
        results = json.load(rf)

    head = ["Query Template", "Average (ms)", "std (ms)", "max (ms)"]
    rows = []

    for query, value in results.items():
        if query not in ignoreQueries:
            row = [query, value["average"],value["std"],value["max"] ]
            rows.append(row)
    
    caption= "Query-Shape containment computation time is negligeable with the most restrictive shapes of our experiments."
    label="tab:queryShapeContainmentEval"

    textTable = Texttable()
    textTable.add_rows([head]+ rows)

    latexTable = latextable.draw_latex(textTable, caption=caption, label=label)
    markdownTable = tabulate(rows, headers=head, tablefmt="github")
    
    with open(os.path.join(artefactFolder,key, "table_query_shape_containment_exec.tex"), "w") as file:
        file.write(latexTable)

    with open(os.path.join(artefactFolder,key, "table_query_shape_containment_exec.md"), "w") as file:
        file.write(markdownTable)