import os
from collections import defaultdict


def generate_report(path: str, depth=1) -> None:
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path):
            if len(full_name := item.split(".")) > 1:
                suffix = full_name[-1]

            else:
                suffix = "<None>"

            report[suffix].append(item)

        elif os.path.isdir(item_path) and depth:
            generate_report(item_path, depth - 1)


script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "data")

cwd = os.getcwd()
input(f"Current working directory: {cwd}\n"
      "Press Enter create a report about file types: ")

report = defaultdict(list)
generate_report(path=cwd, depth=1)  # -1 for full report

report_formatted = []
for extension, files in sorted(report.items()):
    report_formatted.append(f"{extension} - {len(files)}")

    for file in sorted(files):
        report_formatted.append(f" > {file}")

if not os.path.exists(data_path):
    os.mkdir(data_path)

with open(os.path.join(data_path, "report.txt"), "w", encoding="utf-8") as file:
    file.write("\n".join(report_formatted))
