from fpdf import FPDF
import datetime
import os
import webbrowser
import shutil


def pdf_report(df, totalList):
    time_title = datetime.datetime.now().strftime("%m-%d-%Y")
    pdf_name = f"ROI Report {time_title}.pdf"
    pdf = FPDF()
    pdf.add_page()
    col_width = 190/5
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(190, 10, f'{pdf_name}', 0, 0, 'C')
    pdf.ln(10)
    pdf.cell(col_width, 10, "", 1, 0, 'C')
    offset = pdf.x
    top = pdf.y
    pdf.set_fill_color(168, 168, 168)
    for row in df:
        pdf.multi_cell(col_width, 10, str(row), border=1, align='C',
            max_line_height=pdf.font_size, fill=True)
        offset += col_width
        pdf.set_x(offset)
        pdf.y = top
    pdf.ln(10)
    pdf.set_font('Arial', '', 10)
    count = 1
    color_flag = False
    for x in range(df.shape[0]):
        pdf.set_fill_color(168, 168, 168)
        pdf.cell(col_width, 10, f"Year {count}", 1, 0, 'C', fill=True)
        if count % 2 == 1:
                pdf.set_fill_color(240, 240, 240)
                color_flag = True
        else:
            color_flag = False
        pdf.cell(col_width, 10, str(df['Baseline'][x]), border=1, align='C', fill=True)
        pdf.cell(col_width, 10, str(df['Percent Decrease'][x]), border=1, align='C', fill=True)
        pdf.cell(col_width, 10, str(df['No. of Orders'][x]), border=1, align='C', fill=True)
        pdf.cell(col_width, 10, str(df['No. of Spares'][x]), border=1, align='C', fill=True)


        pdf.ln(10)
        count += 1


    pdf.add_page()
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(190, 10, f'Total Values Table', 0, 0, 'C')
    pdf.ln(10)

    pdf.set_fill_color(168, 168, 168)
    for each in totalList:
        pdf.cell(50, 10, str(each[0]), fill=True, border=1, align='C')
        pdf.cell(45, 10, str(each[1]), border=1, align='C')
        pdf.ln(10)

    pdf.output(name=pdf_name, dest="F")
    current_path = os.getcwd()
    home_path = os.path.expanduser('~/Downloads')
    try:
        os.remove(f"{home_path}/{pdf_name}")
        shutil.move(f"{current_path}/{pdf_name}",
                    f"{home_path}/{pdf_name}")
        webbrowser.open_new(f"file://{home_path}/{pdf_name}")
        return pdf_name, True
    except FileNotFoundError:
        shutil.move(f"{current_path}/{pdf_name}",
                    f"{home_path}/{pdf_name}")
        webbrowser.open_new(f"file://{home_path}/{pdf_name}")
        return pdf_name, True
    except OSError:
        pass

# def total_report(totalList):
#     time_title = datetime.datetime.now().strftime("%m-%d-%Y")
#     pdf_name = f"Total ROI Report {time_title}.pdf"
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", 'B', 12)
#     pdf.cell(190, 10, f'Total Values Table', 0, 0, 'C')
#     pdf.ln(10)
#
#     pdf.set_fill_color(168, 168, 168)
#     for each in totalList:
#         pdf.cell(50, 10, str(each[0]), fill=True, border=1, align='C')
#         pdf.cell(45, 10, str(each[1]), border=1, align='C')
#         pdf.ln(10)
#
#     pdf.output(name=pdf_name, dest="F")
#     current_path = os.getcwd()
#     home_path = os.path.expanduser('~/Downloads')
#     try:
#         os.remove(f"{home_path}/{pdf_name}")
#         shutil.move(f"{current_path}/{pdf_name}",
#                     f"{home_path}/{pdf_name}")
#         webbrowser.open_new(f"file://{home_path}/{pdf_name}")
#         return pdf_name, True
#     except FileNotFoundError:
#         shutil.move(f"{current_path}/{pdf_name}",
#                     f"{home_path}/{pdf_name}")
#         webbrowser.open_new(f"file://{home_path}/{pdf_name}")
#         return pdf_name, True
#     except OSError:
#         pass
