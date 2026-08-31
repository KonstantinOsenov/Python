# !pip install fpdf2

from fpdf import FPDF

# save FPDF() class into a
# variable pdf
pdf = FPDF()
# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)
 
# create a cell
pdf.cell(200, 10, "Challenge", new_x="LMARGIN", new_y="NEXT", align='C')

pdf.set_font("Arial", size = 9)

pdf.cell(200, 10, "Cart ID - " + output_cart_id, new_x="LMARGIN", new_y="NEXT", align='R')
pdf.cell(200, 10, "Order code - " + output_order_code, new_x="LMARGIN", new_y="NEXT", align='R')
pdf.cell(200, 10, "Order net price - " + str(output_order_net_price), new_x="LMARGIN", new_y="NEXT", align='R')
pdf.cell(200, 10, "Order summary:", new_x="LMARGIN", new_y="NEXT", align='L')


pdf.set_font("helvetica", "B", 5)
with pdf.table() as table:
    for data_row in items_to_pdf_list:
        row = table.row()
        for datum in data_row:
            row.cell(str(datum))


# save the pdf with name .pdf
pdf.output("output_test_delete3.pdf") 



#############################

# save FPDF() class into a
# variable pdf
pdf = FPDF()
# Add a page
pdf.add_page()


pdf.image(
    "data:image/png;base64,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", 
    0, 0, 50, 0, ""
)

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)
 
# create a cell
pdf.cell(200, 10, "Defense materials", new_x="LMARGIN", new_y="NEXT", align='C')

pdf.set_font("helvetica", "B", 5)

# Main info
pdf.ln()
with pdf.table(
    cell_fill_color=(192, 192, 192),
    col_widths=(25, 25),
    text_align=("LEFT", "LEFT"),
    width=50,
    align="RIGHT",
    first_row_as_headings=False,
    borders_layout = "NONE"
) as table:
    for data_row in items_to_pdf_list_exa_excel:
        row = table.row()
        for datum in data_row:
            row.cell(str(datum))

pdf.ln()

pdf.set_font("Arial", style = "B", size = 9)
pdf.cell(200, 5, "Dear Sir/Madam", new_x="LMARGIN", new_y="NEXT", align='L')

text_to_show_line_1 = f"""
We are contacting you regarding the following dispute on behalf of hm.com_us, order: {output_order_code}
"""
text_to_show_line_2 = f"""
As a store... 
"""
text_to_show_line_3 = f"""
Below is a summary of the relevant evidence gathered.
"""

pdf.set_font("Arial", size = 5)
pdf.cell(200, 3, text_to_show_line_1, new_x="LMARGIN", new_y="NEXT", align='L')
pdf.cell(200, 3, text_to_show_line_2, new_x="LMARGIN", new_y="NEXT", align='L')
pdf.cell(200, 3, text_to_show_line_3, new_x="LMARGIN", new_y="NEXT", align='L')

pdf.set_font("Arial", size = 9)
pdf.cell(200, 10, "Shipping information:", new_x="LMARGIN", new_y="NEXT", align='L')

pdf.set_font("helvetica", "B", 5)
headings_style = FontFace(color=255, fill_color=(255, 100, 0)) # emphasis="BOLD", 

# main info about order
with pdf.table(
    cell_fill_color=(192, 192, 192),
    col_widths=(25, 25),
    text_align=("LEFT", "LEFT"),
    width=50,
    align="LEFT"
) as table:
    for data_row in items_to_pdf_list_ldw_order:
        row = table.row()
        for datum in data_row:
            row.cell(str(datum))

pdf.ln()
# billing address info
with pdf.table(
    cell_fill_color=(192, 192, 192),
    col_widths=(25, 25),
    text_align=("LEFT", "LEFT"),
    width=50,
    align="LEFT"
) as table:
    for data_row in items_to_pdf_list_excel_billing:
        row = table.row()
        for datum in data_row:
            row.cell(str(datum))
            
# shipping address info
with pdf.table(
    cell_fill_color=(192, 192, 192),
    col_widths=(25, 25),
    text_align=("LEFT", "LEFT"),
    width=50,
    align="LEFT"
) as table:
    for data_row in items_to_pdf_list_excel_ship:
        row = table.row()
        for datum in data_row:
            row.cell(str(datum))

# first status info          
pdf.ln()
with pdf.table(
    cell_fill_color=(192, 192, 192),
    col_widths=(25, 25),
    text_align=("LEFT", "LEFT"),
    width=50,
    align="LEFT"
) as table:
    for data_row in items_to_pdf_list_ldw_earliest:
        row = table.row()
        for datum in data_row:
            row.cell(str(datum))

# last status info
pdf.ln()
with pdf.table(
    cell_fill_color=(192, 192, 192),
    col_widths=(25, 25),
    text_align=("LEFT", "LEFT"),
    width=50,
    align="LEFT"
) as table:
    for data_row in items_to_pdf_list_ldw_latest:
        row = table.row()
        for datum in data_row:
            row.cell(str(datum))
        
# items info 
pdf.ln()
pdf.set_font("Arial", size = 9)
pdf.cell(200, 10, "Order summary:", new_x="LMARGIN", new_y="NEXT", align='L')

pdf.set_font("helvetica", "B", 5)
with pdf.table(
    col_widths=(20, 100, 20, 20),
    width=160,
    align="LEFT"
) as table:
    for data_row in items_to_pdf_list_exa_items:
        row = table.row()
        for datum in data_row:
            row.cell(str(datum))
            
# save the pdf with name .pdf
pdf.output("defense_materials_test.pdf") 


#####################################################################################
# TTTTTTTTTTEEEEEEEEEEEESSSSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTTT
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
pdf.cell(200, 10, "Defense materials", new_x="LMARGIN", new_y="NEXT", align='C')

pdf.set_font("Arial", size = 7)
pdf.write_html(
    f"""
    <table border="0">
    <thead>
    <tr>
        <th width="10%"> </th>
        <th width="40%"> </th>
        <th width="10%"> </th>
        <th width="40%"> </th>
    </tr>
    </thead>
    <tbody>

    <tr>
        <td colspan="2"><font size="10">Billing and Shipping address match</font></td>
        <td> </td>
        <td> </td>
        <td> </td>
    </tr>
    <tr> <td> </td> <td> </td> <td> </td> <td> </td> </tr>
    <tr>
        <td colspan="2"><b>Billing address</b></td>
        <td> </td>
        <td colspan="2"><b>Shipping address</b></td>
        <td> </td>
    </tr>
    
    <tr>
        <td> State</td>
        <td> | {items_to_pdf_list_excel_billing[0][1]} </td>
        <td> State</td>
        <td> | {items_to_pdf_list_excel_ship[0][1]} </td>
    </tr>
    <tr>
        <td> City</td>
        <td> | {items_to_pdf_list_excel_billing[1][1]} </td>
        <td> City</td>
        <td> | {items_to_pdf_list_excel_ship[1][1]} </td>
    </tr>
    <tr>
        <td> ZIP</td>
        <td> | {items_to_pdf_list_excel_billing[2][1]} </td>
        <td> ZIP</td>
        <td> | {items_to_pdf_list_excel_ship[2][1]} </td>
    </tr>
    <tr>
        <td> Address</td>
        <td> | {items_to_pdf_list_excel_billing[3][1]} </td>
        <td> Address</td>
        <td> | {items_to_pdf_list_excel_ship[3][1]} </td>
    </tr>
    
    
    
    <tr>
        <td> </td>
        <td> </td>
        <td> </td>
        <td> </td>
    </tr>
    </tbody></table>
    
    <table border="1">
    <thead>
    <tr>
        <th width="25%">{TABLE_DATA[0][0]}</th>
        <th width="25%">{TABLE_DATA[0][1]}</th>
        <th width="15%">{TABLE_DATA[0][2]}</th>
        <th width="35%">{TABLE_DATA[0][3]}</th>
    </tr></thead>
    <tbody><tr>
    <td>{'</td><td>'.join(items_to_pdf_list_excel_billing[0])}</td>
    </tr><tr bgcolor="grey">
    <td>{'</td><td>'.join(items_to_pdf_list_excel_billing[1])}</td>
    </tr><tr>
    <td>{'</td><td>'.join(items_to_pdf_list_excel_billing[2])}</td>
    </tr><tr>
    <td>{'</td><td>'.join(items_to_pdf_list_excel_billing[3])}</td>
    </tr>
    <tr>
        <td> <b><em> normal text </em></b> </td>
        <td> pdf.cell(200, 10, "Test:", 1, new_x="LMARGIN", new_y="NEXT", align='L') </td>
        <td> pdf.cell(200, 10, "Test:", 1, new_x="LMARGIN", new_y="NEXT", align='L') </td>
        <td> pdf.cell(200, 10, "Test:", 1, new_x="LMARGIN", new_y="NEXT", align='L') </td>
    </tr>
    </tbody></table>""",
    table_line_separators=True,
)            

# save the pdf with name .pdf
pdf.output("defense_materials_test_html.pdf") 


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# TTTTTTTTTTEEEEEEEEEEEESSSSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTTT
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
pdf.cell(200, 10, "Defense materials", new_x="LMARGIN", new_y="NEXT", align='C')

pdf.set_font("Arial", size = 7)
pdf.write_html(
    f"""
    
    <table>
    <thead></thead>
    <tbody>

    <tr>
        <td width="7%" colspan="2"><font size="10">Billing and Shipping address match</font></td>
        <td width="43%"> </td>
        <td width="7%"> </td>
        <td width="43%"> </td>
    </tr>
    <tr> <td> </td> <td> </td> <td> </td> <td> </td> </tr>
    <tr>
        <td colspan="2"><b>Billing address</b></td>
        <td> </td>
        <td colspan="2"><b>Shipping address</b></td>
        <td> </td>
    </tr>
    <tr> <td> </td> <td> </td> <td> </td> <td> </td> </tr>
    <tr>
        <td> State</td>
        <td> | {items_to_pdf_list_excel_billing[0][1]} </td>
        <td> State</td>
        <td> | {items_to_pdf_list_excel_ship[0][1]} </td>
    </tr>
    <tr>
        <td> City</td>
        <td> | {items_to_pdf_list_excel_billing[1][1]} </td>
        <td> City</td>
        <td> | {items_to_pdf_list_excel_ship[1][1]} </td>
    </tr>
    <tr>
        <td> ZIP</td>
        <td> | {items_to_pdf_list_excel_billing[2][1]} </td>
        <td> ZIP</td>
        <td> | {items_to_pdf_list_excel_ship[2][1]} </td>
    </tr>
    <tr>
        <td> Address</td>
        <td> | {items_to_pdf_list_excel_billing[3][1]} </td>
        <td> Address</td>
        <td> | {items_to_pdf_list_excel_ship[3][1]} </td>
    </tr>
    </tbody></table>
    
    
    
    <table>
    <thead></thead>
    <tbody>

    <tr>
        <td width="10%" colspan="2"><font size="10">Delivery info</font></td>
        <td width="40%"> </td>
        <td width="10%"> </td>
        <td width="40%"> </td>
    </tr>
    <tr> <td> </td> <td> </td> <td> </td> <td> </td> </tr>
    <tr>
        <td colspan="2"><b>Earliest carrier info</b></td>
        <td> </td>
        <td colspan="2"><b>Latest carrier info</b></td>
        <td> </td>
    </tr>
    <tr> <td> </td> <td> </td> <td> </td> <td> </td> </tr>
    <tr>
        <td> Status date</td>
        <td> | {items_to_pdf_list_ldw_earliest[0][1]} </td>
        <td> Status date</td>
        <td> | {items_to_pdf_list_ldw_latest[0][1]} </td>
    </tr>
    <tr>
        <td> Delivery status</td>
        <td> | {items_to_pdf_list_ldw_earliest[1][1]} </td>
        <td> Delivery status</td>
        <td> | {items_to_pdf_list_ldw_latest[1][1]} </td>
    </tr>
    <tr>
        <td> Carrier status</td>
        <td> | {items_to_pdf_list_ldw_earliest[2][1]} </td>
        <td> Carrier status</td>
        <td> | {items_to_pdf_list_ldw_latest[2][1]} </td>
    </tr>
    </tbody></table> 
    """,
    table_line_separators=True,
)            

# save the pdf with name .pdf
pdf.output("defense_materials_test_html.pdf") 
