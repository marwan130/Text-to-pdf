from fpdf import FPDF

with open("algorithm_notes.txt", "r", encoding="utf-8") as file:
    content = file.readlines()

def clean_line(line):
    replacements = {
        "’": "'",
        "‘": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "—": "-",  # em-dash
        "≤": "<=", # replace ≤ with <=
    }
    for orig, repl in replacements.items():
        line = line.replace(orig, repl)
    # Do NOT remove/replace non latin characters
    return line

content = [clean_line(line) for line in content]

pdf = FPDF()
pdf.add_page()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", size=10)
pdf.set_auto_page_break(auto=True, margin=10)

for line in content:
    line = line.rstrip()
    if line == "":
        pdf.ln(5)
    else:
        pdf.multi_cell(0, 5, line)

pdf.output("AlgoNotes.pdf")
