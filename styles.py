from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import TableStyle, Spacer, HRFlowable

line_spacing = 10
font = "Times-Roman"
font_bold = f"{font}-Bold"

# create styles
styles = getSampleStyleSheet()

styles.add(
    ParagraphStyle(
        name="Section1",
        parent=styles["Normal"],
        fontName=font,
        wordWrap="LTR",
        alignment=TA_CENTER,
        fontSize=12,
        leading=line_spacing + 3,
#        textTransform="uppercase",
        borderPadding=0,
        leftIndent=0,
        rightIndent=0,
        spaceAfter=1,
        spaceBefore=0,
        splitLongWords=True,
        spaceShrinkage=0.05,
    )
)

styles.add(
    ParagraphStyle(
        name="Main_Section1",
        parent=styles["Section1"],
        fontSize=14,
        spaceAfter=3,
    )
)

styles.add(
    ParagraphStyle(
        name="Body1_Left",
        alignment=TA_LEFT,
        fontName=font,
        fontSize=10,
        leading=line_spacing,
        wordWrap="LTR",
        splitLongWords=True,
        spaceShrinkage=0.05,
    )
)

styles.add(
    ParagraphStyle(
        name="Body1_Right",
        parent=styles["Body1_Left"],
        alignment=TA_RIGHT,
    )
)

styles.add(
    ParagraphStyle(
        name="Body1_Center", parent=styles["Body1_Left"], alignment=TA_CENTER
    )
)

styles.add(
    ParagraphStyle(
        name="Sub_Body1_Left",
        parent=styles["Body1_Left"],
        fontSize=9,
    )
)

styles.add(
    ParagraphStyle(
        name="Sub_Body1_Right",
        parent=styles["Body1_Right"],
        fontSize=9,
    )
)

styles.add(
    ParagraphStyle(
        name="Bullet_Indent_Body1",
        parent=styles["Body1_Left"],
        #leftIndent=4,  # indent the bullet and text
        #bulletIndent=12,  # indent bullet position relative to left edge
        spaceAfter=2
    )
)

styles.add(
    ParagraphStyle(
        name="Bullet_Indent_Sub_Body1",
        parent=styles["Sub_Body1_Left"],
    )
)


"""
define exports
"""

# set table format
table_style = TableStyle(
    [
        ("ALIGN", (0, 0), (0, 0), "LEFT"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("TOPPADDING", (0, 0), (-1, -1), 0.5),
    ]
)

# set newline spacings
newline_chunk = [Spacer(1, 0.1 * inch)]
newline_sub_chunk = [Spacer(1, 0.05 * inch)]

# create a line_break component
line_break = [Spacer(1, 0.05 * inch), HRFlowable(width='100%', thickness=1, color=colors.black)]

# assign font styles
main_title_style = styles['Main_Section1']
title_style = styles['Section1']
body_style_l = styles['Body1_Left']
body_style_r = styles['Body1_Right']
body_style_c = styles['Body1_Center']
sub_body_style_l = styles['Sub_Body1_Left']
sub_body_style_r = styles['Sub_Body1_Right']
bullet_style = styles['Bullet_Indent_Body1']
sub_bullet_style = styles['Bullet_Indent_Sub_Body1']


