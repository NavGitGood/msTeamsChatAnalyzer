from fpdf import FPDF

pdf = FPDF('P', 'mm', (210, 297))

def addPage():
    pdf.add_page()
    pdf.set_margins(5, 5, 5)
    pdf.set_auto_page_break(True, 5)
    pdf.set_line_width(1)
    # pdf.set_draw_color(255, 0, 0)
    pdf.line(5, 5, 5, 292)  # vleft
    pdf.line(205, 5, 205, 292)  # vright
    pdf.line(5, 5, 205, 5)  # top
    pdf.line(5, 292, 205, 292)  # bottom

def add_image(image_path1, image_path2, image_path3, image_path4):
    addPage()
    pdf.image(image_path1, x=20, y=10, w=170)
    addPage()
    pdf.image(image_path2, x=20, y=10, w=170)
    addPage()
    pdf.image(image_path3, x=20, y=10, w=170)
    addPage()
    pdf.image(image_path4, x=20, y=10, w=170)
    # pdf.set_font("Arial", size=12)
    # pdf.ln(3000)  # move 85 down
    # pdf.cell(80)
    # pdf.cell(200, 10, txt="{}".format(image_path1), ln=1)
    pdf.output("add_image.pdf")

# def addImageTitle(title):
