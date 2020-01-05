from fpdf import FPDF

def add_page(pdf):
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
    addImageTitle(pdf, image[1])
    pdf.image(image[0], x=20, y=25, w=170)

def new_pdf(image_list, file_name, **summary_data):
    pdf = FPDF('P', 'mm', (210, 297))
    if 'table_data' in summary_data:
         # add a table in first page
        add_page(pdf)
        for table_data in summary_data.get('table_data'):
            add_table(pdf, table_data)
    elif 'line_data' in summary_data:
        add_page(pdf)
        for line_data in summary_data.get('line_data'):
            pdf.ln(15)
            add_key_value_line(pdf, line_data)
    for image in image_list:
        add_page(pdf)
        add_image(pdf, image)
    pdf.output(f'output/{file_name}.pdf')

def add_table(pdf, table_data):  # two column table
    # setting title
    pdf.set_line_width(0.5)
    pdf.set_font("Arial", size=18)
    pdf.set_x(10)
    pdf.cell(40, 6, f'{str(table_data[3])}: ', 0, 1)
    pdf.ln(2)
    # setting headers
    pdf.set_fill_color(48, 205, 205)
    pdf.set_font("Arial", size=15)
    pdf.set_x(25)
    pdf.cell(40, 6, str(table_data[1]), 1, 0, 'C', 1)
    pdf.cell(40, 6, str(table_data[2]), 1, 1, 'C', 1)
    pdf.set_font("Arial", size=12)
    for row in table_data[0]:
        pdf.set_fill_color(198, 198, 198)
        pdf.set_x(25)
        pdf.cell(40, 6, str(row[0]), 1, 0, 'C', 1)
        pdf.cell(40, 6, str(row[1]), 1, 1, 'C', 1)
    pdf.ln(10)

def add_key_value_line(pdf, table_data):
    pdf.set_font("Arial", size=18)
    pdf.set_x(10)
    pdf.cell(100, 6, f'{str(table_data[0])} ', 0, 0, 'L', 0)
    pdf.cell(5, 6, str(table_data[1][0][1]), 0, 0, 'C', 0)
    pdf.ln(15)


def addImageTitle(pdf, title):
    pdf.set_font("Arial", size=18)
    pdf.set_xy(10, 15)
    pdf.cell(40, 6, f'{title}: ', 0, 1)