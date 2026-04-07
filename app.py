# qpc_app/app.py
"""
CARS2-QPC App — Parent/Caregiver Questionnaire
Bilingual (Arabic/English UI), English-only report sent via email.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
from datetime import date

from shared.cars2_data import QPC_SECTIONS, QPC_RATING_OPTIONS, UI_TEXT
from shared.qpc_report import generate_qpc_pdf
from shared.email_utils import send_report_email

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CARS2-QPC | Wijdan Therapy Center",
    page_icon="🧩",
    layout="centered",
)

# ── Minimal CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
  .stRadio > div { flex-direction: row; flex-wrap: wrap; gap: 8px; }
  .block-container { max-width: 800px; padding-top: 1.5rem; }
  .rtl-block { direction: rtl; text-align: right; }
  h1, h2, h3 { color: #1B2A4A; }
  .section-card {
    background: #EAF2FB; border-left: 4px solid #2D6BA0;
    padding: 12px 16px; border-radius: 4px; margin-bottom: 12px;
  }
  .thank-you {
    background: #D5F5E3; border: 2px solid #27AE60;
    padding: 24px; border-radius: 8px; text-align: center;
  }
</style>
""", unsafe_allow_html=True)


# ── Language toggle ───────────────────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state["lang"] = "en"

col_l, col_r = st.columns([4, 1])
with col_r:
    lang_choice = st.selectbox("🌐", ["English", "عربي"], label_visibility="collapsed",
                                key="lang_selector")
    st.session_state["lang"] = "ar" if lang_choice == "عربي" else "en"

lang = st.session_state["lang"]
T = UI_TEXT[lang]
is_ar = lang == "ar"
dir_attr = 'dir="rtl"' if is_ar else ''

# ── Show thank-you and stop if submitted ──────────────────────────────────────
if st.session_state.get("qpc_submitted"):
    st.markdown(f"""
    <div class="thank-you">
        <h2>{'شكراً جزيلاً 🙏' if is_ar else 'Thank You 🙏'}</h2>
        <p style="font-size:1.1em;">
        {'تم إرسال إجاباتك بنجاح. سيطّلع الأخصائي على البيانات قريباً.' 
         if is_ar else
         'Your responses have been submitted successfully. The clinician will review your information shortly.'}
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="background:#1B2A4A;padding:20px 24px;border-radius:8px;margin-bottom:20px;" {dir_attr}>
  <h1 style="color:white;margin:0;font-size:1.5em;">{'استبيان CARS-2 للوالدين' if is_ar else 'CARS-2 Parent/Caregiver Questionnaire'}</h1>
  <p style="color:#AED6F1;margin:4px 0 0 0;font-size:0.9em;">
  {'مقياس تصنيف اضطراب طيف التوحد عند الأطفال — الإصدار الثاني' if is_ar else
   'Childhood Autism Rating Scale – 2nd Edition  |  Wijdan Therapy Center'}
  </p>
</div>
""", unsafe_allow_html=True)

# ── Instructions ──────────────────────────────────────────────────────────────
with st.expander("📋 " + ("التوجيهات" if is_ar else "Instructions"), expanded=True):
    if is_ar:
        st.markdown("""
        <div dir="rtl">
        <ul>
        <li>يطرح هذا النموذج تساؤلات بشأن السلوكيات في عدة مجالات قد يواجه فيها الشخص صعوبات.</li>
        <li>رجاءً قم بوضع إجابة تحت أكثر ما يصف الشخص المفحوص.</li>
        <li>يمكنك وضع إجابة <b>لا أعرف</b> إن لم يكن لديك معلومات كافية عن هذا السلوك.</li>
        <li>لن يتم عرض التقرير هنا — سيُرسَل مباشرة إلى الأخصائي.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        - This form asks about behaviors in several areas where people may have difficulty.
        - For each behavior listed, select the option that **best describes** the person you are rating.
        - You can select **Don't Know** if you do not have enough information about a behavior.
        - **No report will be shown to you** — it will be sent directly to the clinician.
        """)

st.markdown("---")

# ── Demographic fields ────────────────────────────────────────────────────────
st.markdown(f"### {'البيانات الشخصية' if is_ar else 'Client Information'}")

with st.container():
    c1, c2 = st.columns(2)
    with c1:
        child_name = st.text_input(T["child_name"], key="qpc_child_name",
                                    placeholder="e.g. Ahmed Ali" if not is_ar else "مثال: أحمد علي")
        age_input = st.number_input(T["child_age"], min_value=1, max_value=25, value=5, key="qpc_age")
    with c2:
        gender_options = [T["male"], T["female"]]
        gender = st.radio(T["child_gender"], gender_options, horizontal=True, key="qpc_gender")
        rater_name = st.text_input(T["rater_name"], key="qpc_rater")

    notes_input = st.text_area(
        "Additional notes / ملاحظات إضافية",
        key="qpc_notes", height=80,
        placeholder=("Any additional observations..." if not is_ar else "أي ملاحظات إضافية...")
    )

st.markdown("---")

# ── QPC Questionnaire ─────────────────────────────────────────────────────────
responses = {}
all_answered = True

rating_options_map = QPC_RATING_OPTIONS[lang]
rating_keys   = list(rating_options_map.keys())
rating_labels = list(rating_options_map.values())

for sec in QPC_SECTIONS:
    sec_title = sec["ar"] if is_ar else sec["en"]
    st.markdown(f"""
    <div class="section-card" {dir_attr}>
        <b>{'القسم ' if is_ar else 'Section '}{sec['id'][1:]}: {sec_title}</b>
    </div>
    """, unsafe_allow_html=True)

    for item in sec["items"]:
        item_label = item["ar"] if is_ar else item["en"]
        iid = item["id"]

        if is_ar:
            st.markdown(f'<div dir="rtl" style="margin-bottom:2px;font-size:0.92em;">{item_label}</div>',
                        unsafe_allow_html=True)
        else:
            st.markdown(f"**{item_label}**")

        selected = st.radio(
            label=item_label,
            options=rating_labels,
            key=f"qpc_{iid}",
            horizontal=True,
            label_visibility="collapsed",
            index=4,  # default "Don't know"
        )
        # Map selected label back to key
        for k, v in rating_options_map.items():
            if v == selected:
                responses[iid] = k
                break

    st.markdown("")

st.markdown("---")

# ── Submit ────────────────────────────────────────────────────────────────────
col_submit, col_info = st.columns([2, 3])
with col_submit:
    submit_btn = st.button(
        f"{'إرسال الاستبيان ✅' if is_ar else '✅ Submit Questionnaire'}",
        type="primary", use_container_width=True
    )

if submit_btn:
    if not child_name or not child_name.strip():
        st.error("Please enter the child's name. / الرجاء إدخال اسم الطفل.")
    else:
        with st.spinner("Generating report and sending..." if not is_ar else "جاري إنشاء التقرير وإرساله..."):
            # Generate PDF
            pdf_bytes = generate_qpc_pdf(
                child_name=child_name,
                age=age_input,
                gender=gender,
                rater_name=rater_name or "Parent/Caregiver",
                test_date=date.today(),
                responses=responses,
                qpc_sections=QPC_SECTIONS,
                notes=notes_input,
            )
            # Send email
            subject = f"CARS2-QPC Submission: {child_name} | {date.today()}"
            body = (
                f"A new CARS2-QPC questionnaire has been submitted.\n\n"
                f"Child Name: {child_name}\n"
                f"Age: {age_input}\n"
                f"Gender: {gender}\n"
                f"Date: {date.today()}\n\n"
                f"Please find the PDF report attached.\n\n"
                f"-- Wijdan Therapy Center CARS2 System"
            )
            success = send_report_email(
                pdf_bytes=pdf_bytes,
                subject=subject,
                body=body,
                filename=f"QPC_{child_name.replace(' ','_')}_{date.today()}.pdf"
            )
        st.session_state["qpc_submitted"] = True
        st.rerun()
