from fpdf import FPDF

with open("algorithm_notes.txt", "r", encoding="utf-8") as file:
    content = file.readlines()

# clean curly apostrophes
content = [line.replace("’", "'") for line in content]

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=10)
pdf.add_page()
pdf.set_font("Courier", size=10)

for line in content:
    line = line.rstrip()
    if line == "":
        pdf.ln(5)
    else:
        pdf.multi_cell(0, 5, line)

pdf.output("AlgoNotes.pdf")
