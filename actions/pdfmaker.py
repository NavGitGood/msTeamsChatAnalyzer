from fpdf import FPDF

def addPage(pdf):
    pdf.add_page()
    pdf.set_margins(5, 5, 5)
    pdf.set_auto_page_break(True, 5)
    pdf.set_line_width(1)
    # pdf.set_draw_color(255, 0, 0)
    pdf.line(5, 5, 5, 292)  # vleft
    pdf.line(205, 5, 205, 292)  # vright
    pdf.line(5, 5, 205, 5)  # top
    pdf.line(5, 292, 205, 292)  # bottom

def add_image(pdf, image):
    pdf.image(image, x=20, y=10, w=170)

def new_pdf(image_list, file_name):
    pdf = FPDF('P', 'mm', (210, 297))
    for image in image_list:
        addPage(pdf)
        add_image(pdf, image)
    pdf.output(f'output/{file_name}.pdf')

# def addImageTitle(title):
