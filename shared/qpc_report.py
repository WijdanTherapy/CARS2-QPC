# shared/qpc_report.py
"""
Generates the QPC PDF report (English only, premium look).
Includes machine-readable QPC_DATA block for later parsing by Clinician App.
"""

import io
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

# Brand colors
BRAND_DARK   = colors.HexColor("#1B2A4A")
BRAND_BLUE   = colors.HexColor("#2D6BA0")
BRAND_LIGHT  = colors.HexColor("#EAF2FB")
BRAND_GREEN  = colors.HexColor("#27AE60")
BRAND_ORANGE = colors.HexColor("#E67E22")
BRAND_RED    = colors.HexColor("#C0392B")
BRAND_GREY   = colors.HexColor("#7F8C8D")
WHITE        = colors.white

QPC_RATING_LABELS = {
    "0": "Not a problem (does very well)",
    "1": "Mild-to-moderate problem",
    "2": "Severe problem",
    "3": "Was a problem in the past",
    "9": "Don't know",
}

SECTION_TITLES = {
    "S1": "Section 1: Communication",
    "S2": "Section 2: Social Relating & Emotional Expression",
    "S3": "Section 3: Body Use & Motor Skills",
    "S4": "Section 4: Play Behavior",
    "S5": "Section 5: Adaptation to Change & Routines",
    "S6": "Section 6: Sensory Responses",
}


def _make_styles():
    base = getSampleStyleSheet()
    styles = {}

    styles["title"] = ParagraphStyle(
        "title", fontName="Helvetica-Bold", fontSize=18,
        textColor=WHITE, alignment=TA_CENTER, spaceAfter=4
    )
    styles["subtitle"] = ParagraphStyle(
        "subtitle", fontName="Helvetica", fontSize=11,
        textColor=WHITE, alignment=TA_CENTER, spaceAfter=2
    )
    styles["section_header"] = ParagraphStyle(
        "section_header", fontName="Helvetica-Bold", fontSize=12,
        textColor=BRAND_DARK, spaceBefore=12, spaceAfter=4
    )
    styles["body"] = ParagraphStyle(
        "body", fontName="Helvetica", fontSize=9,
        textColor=colors.black, spaceAfter=4, leading=14
    )
    styles["small"] = ParagraphStyle(
        "small", fontName="Helvetica", fontSize=8,
        textColor=BRAND_GREY, spaceAfter=2
    )
    styles["footer"] = ParagraphStyle(
        "footer", fontName="Helvetica", fontSize=7,
        textColor=BRAND_GREY, alignment=TA_CENTER
    )
    styles["label"] = ParagraphStyle(
        "label", fontName="Helvetica-Bold", fontSize=9,
        textColor=BRAND_DARK
    )
    styles["machine"] = ParagraphStyle(
        "machine", fontName="Courier", fontSize=7,
        textColor=BRAND_GREY, spaceAfter=2
    )
    return styles


def _header_table(child_name, age, gender, rater_name, test_date, styles):
    """Returns a styled demographics table."""
    data = [
        [Paragraph("<b>Child Name:</b>", styles["body"]),
         Paragraph(child_name or "—", styles["body"]),
         Paragraph("<b>Date:</b>", styles["body"]),
         Paragraph(str(test_date), styles["body"])],
        [Paragraph("<b>Age:</b>", styles["body"]),
         Paragraph(f"{age} years", styles["body"]),
         Paragraph("<b>Gender:</b>", styles["body"]),
         Paragraph(gender or "—", styles["body"])],
        [Paragraph("<b>Rater:</b>", styles["body"]),
         Paragraph(rater_name or "—", styles["body"]),
         Paragraph("<b>Form:</b>", styles["body"]),
         Paragraph("CARS2-QPC", styles["body"])],
    ]
    t = Table(data, colWidths=[3*cm, 7*cm, 3*cm, 5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BRAND_LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.5, BRAND_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#BDC3C7")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def _section_table(section_id, section_title, items, responses, styles):
    """Returns a KeepTogether block for one QPC section."""
    elements = []
    elements.append(Paragraph(section_title, styles["section_header"]))
    elements.append(HRFlowable(width="100%", thickness=1, color=BRAND_BLUE, spaceAfter=4))

    # Table header
    header = [
        Paragraph("<b>#</b>", styles["label"]),
        Paragraph("<b>Item</b>", styles["label"]),
        Paragraph("<b>Rating</b>", styles["label"]),
    ]
    rows = [header]
    for item in items:
        iid = item["id"]
        rating_val = responses.get(iid, "9")
        rating_text = QPC_RATING_LABELS.get(str(rating_val), "Don't know")
        # Color-code rating
        if str(rating_val) == "2":
            rc = BRAND_RED
        elif str(rating_val) == "1":
            rc = BRAND_ORANGE
        elif str(rating_val) == "0":
            rc = BRAND_GREEN
        else:
            rc = BRAND_GREY
        rows.append([
            Paragraph(iid.replace(section_id, ""), styles["body"]),
            Paragraph(item["en"], styles["body"]),
            Paragraph(f'<font color="#{rc.hexval()[2:]}"><b>{rating_text}</b></font>', styles["body"]),
        ])

    t = Table(rows, colWidths=[1.2*cm, 11.3*cm, 5.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BRAND_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, BRAND_LIGHT]),
        ("BOX", (0, 0), (-1, -1), 0.5, BRAND_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#BDC3C7")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    elements.append(t)
    return KeepTogether(elements)


def _summary_table(all_responses, qpc_sections, styles):
    """Summary: count of 0/1/2/3/9 per section."""
    elements = []
    elements.append(Paragraph("QPC Summary by Section", styles["section_header"]))
    elements.append(HRFlowable(width="100%", thickness=1, color=BRAND_BLUE, spaceAfter=4))

    header = [
        Paragraph("<b>Section</b>", styles["label"]),
        Paragraph("<b>Not a Problem</b>", styles["label"]),
        Paragraph("<b>Mild-Moderate</b>", styles["label"]),
        Paragraph("<b>Severe</b>", styles["label"]),
        Paragraph("<b>Past Only</b>", styles["label"]),
        Paragraph("<b>Don't Know</b>", styles["label"]),
    ]
    rows = [header]
    for sec in qpc_sections:
        counts = {"0": 0, "1": 0, "2": 0, "3": 0, "9": 0}
        for item in sec["items"]:
            val = str(all_responses.get(item["id"], "9"))
            counts[val] = counts.get(val, 0) + 1
        rows.append([
            Paragraph(SECTION_TITLES.get(sec["id"], sec["id"]).split(":")[1].strip(), styles["body"]),
            Paragraph(str(counts["0"]), styles["body"]),
            Paragraph(str(counts["1"]), styles["body"]),
            Paragraph(str(counts["2"]), styles["body"]),
            Paragraph(str(counts["3"]), styles["body"]),
            Paragraph(str(counts["9"]), styles["body"]),
        ])
    t = Table(rows, colWidths=[5.5*cm, 2.5*cm, 2.5*cm, 2*cm, 2*cm, 2.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BRAND_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, BRAND_LIGHT]),
        ("BOX", (0, 0), (-1, -1), 0.5, BRAND_BLUE),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#BDC3C7")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
    ]))
    elements.append(t)
    return KeepTogether(elements)


def _machine_block(responses, styles):
    """Embeds machine-readable QPC_DATA block at the end."""
    lines = ["QPC_DATA_START"]
    for k, v in sorted(responses.items()):
        lines.append(f"{k}={v}")
    lines.append("QPC_DATA_END")
    text = "\n".join(lines)
    return Paragraph(text.replace("\n", "<br/>"), styles["machine"])


def generate_qpc_pdf(
    child_name: str,
    age,
    gender: str,
    rater_name: str,
    test_date,
    responses: dict,
    qpc_sections: list,
    notes: str = "",
) -> bytes:
    """
    Generate a full QPC PDF report and return as bytes.
    """
    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf,
        pagesize=A4,
        leftMargin=1.8*cm, rightMargin=1.8*cm,
        topMargin=2*cm, bottomMargin=2*cm,
        title=f"CARS2-QPC Report – {child_name}",
        author="Wijdan Therapy Center",
    )
    styles = _make_styles()
    story = []

    # ── HEADER BANNER ────────────────────────────────────────────────────────
    header_data = [[
        Paragraph("Wijdan Therapy Center", styles["title"]),
        Paragraph("CARS-2 Parent/Caregiver Questionnaire (QPC)<br/>"
                  "<font size='9'>Childhood Autism Rating Scale – 2nd Edition</font>",
                  styles["subtitle"]),
    ]]
    header_t = Table(header_data, colWidths=[18*cm])
    header_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BRAND_DARK),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(header_t)
    story.append(Spacer(1, 8))

    # ── DEMOGRAPHICS ─────────────────────────────────────────────────────────
    story.append(_header_table(child_name, age, gender, rater_name, test_date, styles))
    story.append(Spacer(1, 10))

    # ── NOTICE ───────────────────────────────────────────────────────────────
    notice = (
        "<b>Important Notice:</b> This questionnaire was completed by a parent or caregiver "
        "and is intended to provide supplementary information to the clinician. "
        "It is <b>not</b> a diagnostic instrument and should not be interpreted in isolation. "
        "Results should be integrated with direct clinical observation using the CARS2-ST or CARS2-HF."
    )
    story.append(Paragraph(notice, styles["body"]))
    story.append(Spacer(1, 8))

    # ── SUMMARY ──────────────────────────────────────────────────────────────
    story.append(_summary_table(responses, qpc_sections, styles))
    story.append(Spacer(1, 10))

    # ── SECTION TABLES ───────────────────────────────────────────────────────
    for sec in qpc_sections:
        title = SECTION_TITLES.get(sec["id"], sec["id"])
        story.append(_section_table(sec["id"], title, sec["items"], responses, styles))
        story.append(Spacer(1, 8))

    # ── NOTES ────────────────────────────────────────────────────────────────
    if notes and notes.strip():
        story.append(Paragraph("Additional Notes / Comments", styles["section_header"]))
        story.append(HRFlowable(width="100%", thickness=1, color=BRAND_BLUE, spaceAfter=4))
        story.append(Paragraph(notes, styles["body"]))
        story.append(Spacer(1, 8))

    # ── MACHINE-READABLE BLOCK ───────────────────────────────────────────────
    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BRAND_GREY, spaceAfter=4))
    story.append(Paragraph(
        "<font color='#BDC3C7'><i>Machine-readable data block (for clinician system use):</i></font>",
        styles["small"]
    ))
    story.append(_machine_block(responses, styles))

    # ── FOOTER ───────────────────────────────────────────────────────────────
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=0.5, color=BRAND_GREY, spaceAfter=4))
    story.append(Paragraph(
        f"CARS2-QPC Report  |  Generated: {date.today().strftime('%B %d, %Y')}  |  "
        "Wijdan Therapy Center  |  Confidential – For clinical use only",
        styles["footer"]
    ))

    doc.build(story)
    buf.seek(0)
    return buf.read()
