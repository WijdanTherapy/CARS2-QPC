# shared/cars2_data.py
# CARS2 assessment items, scoring logic, and translations

# ---------------------------------------------------------------------------
# CARS2-ST ITEMS (15 items)
# ---------------------------------------------------------------------------
CARS2_ST_ITEMS = [
    {
        "id": 1,
        "en": "Relating to People",
        "ar": "العلاقات مع الناس",
        "ratings": {
            1:   {"en": "No evidence of difficulty or abnormality in relating to people. Age-appropriate behavior.", "ar": "لا يوجد دليل على صعوبة أو خلل في العلاقات الشخصية."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal relationships. Avoids eye contact, overly shy, or slightly clingy.", "ar": "علاقات غير طبيعية بشكل بسيط."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal relationships. Indifferent to adults; minimal contact.", "ar": "علاقات غير طبيعية بدرجة متوسطة."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal relationships. Consistently aloof; persistent attempts have no effect.", "ar": "علاقات غير طبيعية بدرجة شديدة."},
        }
    },
    {
        "id": 2,
        "en": "Imitation",
        "ar": "المحاكاة",
        "ratings": {
            1:   {"en": "Appropriate imitation. Imitates sounds, words, and actions appropriately.", "ar": "قدرة مناسبة على التقليد."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal imitation. Imitates simple behaviors; may need prompting.", "ar": "قصور بسيط في التقليد."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal imitation. Imitates only part of the time; needs persistence.", "ar": "قصور متوسط في التقليد."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal imitation. Rarely or never imitates even with prompting.", "ar": "قصور شديد في التقليد."},
        }
    },
    {
        "id": 3,
        "en": "Emotional Response",
        "ar": "الاستجابة العاطفية",
        "ratings": {
            1:   {"en": "Age-appropriate emotional response. Appropriate type and degree of emotional response.", "ar": "استجابة عاطفية مناسبة للعمر والموقف."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal emotional response. Occasionally inappropriate type or degree.", "ar": "قصور بسيط في الاستجابات العاطفية."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal emotional response. Clearly inadequate; inhibited or excessive.", "ar": "مستوى متوسط من القصور في الاستجابات العاطفية."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal emotional response. Rarely appropriate; extreme mood rigidity.", "ar": "قصور شديد في الاستجابات العاطفية."},
        }
    },
    {
        "id": 4,
        "en": "Body Use",
        "ar": "استخدام الجسد",
        "ratings": {
            1:   {"en": "Age-appropriate body use. Moves with normal ease, agility, and coordination.", "ar": "استجابة جسدية ملائمة لعمره."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal body use. Some minor peculiarities; occasional strange movements.", "ar": "قصور بسيط في الاستجابة الجسدية."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal body use. Unusual postures, rocking, spinning, toe-walking.", "ar": "قصور متوسط في الاستجابة الجسدية."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal body use. Intense or frequent movements; self-directed aggression.", "ar": "قصور شديد في الاستجابات الجسدية."},
        }
    },
    {
        "id": 5,
        "en": "Object Use",
        "ar": "استخدام الأشياء",
        "ratings": {
            1:   {"en": "Appropriate interest in and use of toys and objects.", "ar": "استجابة مناسبة في الاهتمام والاستخدام للألعاب والأشياء."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly inappropriate interest in or use of objects. Unusual interest in one toy.", "ar": "قصور بسيط في الاهتمام واستخدام الأشياء."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately inappropriate use. Fascination with lights, spinning parts, or repetitive use.", "ar": "قصور متوسط في الاهتمام واستخدام الأشياء."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely inappropriate use. Repetitive or completely inappropriate object use.", "ar": "قصور شديد في الاهتمام واستخدام الأشياء."},
        }
    },
    {
        "id": 6,
        "en": "Adaptation to Change",
        "ar": "التكيف مع التغيير",
        "ratings": {
            1:   {"en": "Age-appropriate adaptation to change. Accepts changes without undue stress.", "ar": "قابلية ملائمة للتكيف مع التغيير."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal adaptation. Unusually quick to maintain same activity or routine.", "ar": "قصور بسيط في التكيف مع التغيير."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal adaptation. Resists routine changes; displeasure or frustration.", "ar": "قصور متوسط في التكيف مع التغيير."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal adaptation. Extreme reactions to change; extreme anger or refusal.", "ar": "قصور شديد في التكيف مع التغيير."},
        }
    },
    {
        "id": 7,
        "en": "Visual Response",
        "ar": "الاستجابة البصرية",
        "ratings": {
            1:   {"en": "Age-appropriate visual response. Eye contact well integrated with communication.", "ar": "استجابة بصرية متوافقة مع عمره."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal visual response. May stare or show inconsistent eye contact.", "ar": "قصور بسيط في الاستجابات البصرية."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal visual response. Fascination with lights, mirrors, or spinning.", "ar": "قصور متوسط في الاستجابات البصرية."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal visual response. Persistent avoidance of eye contact; extreme visual behaviors.", "ar": "قصور شديد في الاستجابات البصرية."},
        }
    },
    {
        "id": 8,
        "en": "Listening Response",
        "ar": "الاستجابة السمعية",
        "ratings": {
            1:   {"en": "Age-appropriate listening response. Normal and appropriate listening behavior.", "ar": "استجابة سمعية متوافقة مع عمره."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal listening response. Some difficulty responding to verbalizations.", "ar": "قصور بسيط في الاستجابات السمعية."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal listening response. Inconsistent responses; ignores or overreacts.", "ar": "قصور متوسط في الاستجابات السمعية."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal listening response. Extreme over/underreaction to sounds.", "ar": "قصور شديد في الاستجابات السمعية."},
        }
    },
    {
        "id": 9,
        "en": "Taste, Smell, and Touch Response and Use",
        "ar": "استجابات الشم، اللمس والتذوق",
        "ratings": {
            1:   {"en": "Normal use of and response to taste, smell, and touch.", "ar": "استخدام واستجابة طبيعية لأحاسيس التذوق والشم واللمس."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Occasionally smells/tastes objects; mild over- or underreaction.", "ar": "قصور بسيط في استخدام وعاستجابة أحاسيس التذوق والشم واللمس."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Obvious smelling/tasting; clear over- or underreaction to sensory input.", "ar": "قصور متوسط في استخدام واستجابة أحاسيس التذوق والشم واللمس."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Extreme sensory preoccupation or complete insensitivity.", "ar": "قصور شديد في استخدام واستجابة أحاسيس التذوق والشم واللمس."},
        }
    },
    {
        "id": 10,
        "en": "Fear or Nervousness",
        "ar": "المخاوف والعصبية",
        "ratings": {
            1:   {"en": "Normal fear or nervousness. Behavior appropriate to situation and age.", "ar": "مستوى طبيعي من المخاوف أو العصبية."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Occasional slight excess or deficit in fear compared to peers.", "ar": "مستوى بسيط من أعراض المخاوف والعصبية."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Shows quite a bit more or less fear than typical peers.", "ar": "مستوى متوسط من أعراض المخاوف والعصبية."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Pervasive fear or anxiety; very difficult to calm.", "ar": "مستوى شديد من أعراض المخاوف والعصبية."},
        }
    },
    {
        "id": 11,
        "en": "Verbal Communication",
        "ar": "التواصل اللفظي",
        "ratings": {
            1:   {"en": "Normal verbal communication, age and situation appropriate.", "ar": "مستوى طبيعي للتواصل اللغوي."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal verbal communication. Mild delay; some echolalia or pronoun reversal.", "ar": "مستوى بسيط من قصور التواصل اللفظي."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal verbal communication. May be absent or include jargon, echolalia.", "ar": "مستوى متوسط من قصور التواصل اللفظي."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal verbal communication. No meaningful speech; only noises or strange sounds.", "ar": "مستوى شديد من قصور التواصل اللفظي."},
        }
    },
    {
        "id": 12,
        "en": "Nonverbal Communication",
        "ar": "التواصل غير اللفظي",
        "ratings": {
            1:   {"en": "Normal use of nonverbal communication, age and situation appropriate.", "ar": "مستوى طبيعي للتواصل غير اللفظي."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Vague pointing; limited use of gestures.", "ar": "مستوى بسيط من قصور التواصل غير اللفظي."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Usually unable to express needs nonverbally.", "ar": "مستوى متوسط من قصور التواصل غير اللفظي."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Only bizarre gestures; no awareness of others' nonverbal cues.", "ar": "مستوى شديد من قصور التواصل غير اللفظي."},
        }
    },
    {
        "id": 13,
        "en": "Activity Level",
        "ar": "مستوى النشاط",
        "ratings": {
            1:   {"en": "Normal activity level for age and circumstances.", "ar": "مستوى طبيعي للنشاط الحركي."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal activity level. Slightly hyper or hypoactive; affects performance mildly.", "ar": "مستوى بسيط من قصور النشاط."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal activity level. Very active or lethargic; hard to contain.", "ar": "مستوى متوسط من قصور النشاط."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal activity level. Extreme hyperactivity or extreme lethargy.", "ar": "مستوى شديد من قصور النشاط."},
        }
    },
    {
        "id": 14,
        "en": "Level and Consistency of Intellectual Response",
        "ar": "مستوى وثبات الاستجابات الذهنية",
        "ratings": {
            1:   {"en": "Normal and reasonably consistent intellectual functioning across various areas.", "ar": "مستوى طبيعي للذكاء ومتسق عبر المجالات."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal intellectual functioning. Slightly below or inconsistent across areas.", "ar": "مستوى بسيط من قصور الوظائف الفكرية."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal intellectual functioning. Generally below average; some near-normal areas.", "ar": "مستوى متوسط من قصور الوظائف الفكرية."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal intellectual functioning. Below average but may have savant-type skill.", "ar": "مستوى شديد من قصور الوظائف الفكرية."},
        }
    },
    {
        "id": 15,
        "en": "General Impressions",
        "ar": "الانطباع العام",
        "ratings": {
            1:   {"en": "No autism spectrum disorder. No characteristic symptoms present.", "ar": "لا يوجد توحد."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mild autism spectrum disorder. Few symptoms; mild interference with daily functioning.", "ar": "مستوى بسيط من أعراض التوحد."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderate autism spectrum disorder. Moderate number of symptoms; moderate interference.", "ar": "مستوى متوسط من أعراض التوحد."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severe autism spectrum disorder. Many symptoms; extreme interference with daily functioning.", "ar": "مستوى شديد من أعراض التوحد."},
        }
    },
]

# ---------------------------------------------------------------------------
# CARS2-HF ITEMS (15 items — 3 items differ from ST)
# ---------------------------------------------------------------------------
CARS2_HF_ITEMS = [
    {
        "id": 1,
        "en": "Social-Emotional Understanding",
        "ar": "الفهم الاجتماعي-العاطفي",
        "ratings": {
            1:   {"en": "Age-appropriate social-emotional understanding. Clearly understands facial expressions, tone, and body language.", "ar": "فهم اجتماعي-عاطفي مناسب للعمر."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly impaired. Responsive to most cues but subtle expressions sometimes missed.", "ar": "ضعف بسيط في الفهم الاجتماعي-العاطفي."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately impaired. Understands only obvious cues; ignores subtle expressions.", "ar": "ضعف متوسط في الفهم الاجتماعي-العاطفي."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely impaired. Virtually no ability to understand facial expressions, gestures, or tone.", "ar": "ضعف شديد في الفهم الاجتماعي-العاطفي."},
        }
    },
    {
        "id": 2,
        "en": "Emotional Expression and Regulation of Emotions",
        "ar": "التعبير العاطفي وتنظيم المشاعر",
        "ratings": {
            1:   {"en": "Age-appropriate emotional expression. Appropriate type and degree; good emotional variation.", "ar": "تعبير عاطفي مناسب للعمر والموقف."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Flat, distorted, or slightly exaggerated emotional expressions.", "ar": "استجابة عاطفية غير طبيعية بسيطة."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Expression is flat, excessive, or frequently inconsistent with context.", "ar": "استجابة عاطفية غير طبيعية متوسطة."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Extreme problems with emotional regulation across settings.", "ar": "استجابة عاطفية غير طبيعية شديدة."},
        }
    },
    {
        "id": 3,
        "en": "Relating to People",
        "ar": "العلاقات مع الناس",
        "ratings": {
            1:   {"en": "No evidence of difficulty or abnormality in relating to people.", "ar": "لا يوجد دليل على صعوبة في العلاقات الشخصية."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Initiates interactions mainly around special interests.", "ar": "علاقات غير طبيعية بشكل بسيط."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Interactions almost totally around special interests.", "ar": "علاقات غير طبيعية بدرجة متوسطة."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Does not initiate directed interactions; minimal response to others.", "ar": "علاقات غير طبيعية بدرجة شديدة."},
        }
    },
    {
        "id": 4,
        "en": "Body Use",
        "ar": "استخدام الجسد",
        "ratings": {
            1:   {"en": "Age-appropriate body use. Moves with normal ease, agility, and coordination.", "ar": "استخدام جسد مناسب للعمر."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Some minor peculiarities; clumsiness or fine motor difficulties.", "ar": "استخدام جسد غير طبيعي بشكل بسيط."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Any unusual posture, mannerism, flapping, self-directed aggression.", "ar": "استخدام جسد غير طبيعي بدرجة متوسطة."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Intense or frequent movements of the type listed above.", "ar": "استخدام جسد غير طبيعي بدرجة شديدة."},
        }
    },
    {
        "id": 5,
        "en": "Object Use in Play",
        "ar": "استخدام الأشياء في اللعب",
        "ratings": {
            1:   {"en": "Appropriate interest in and creative use of toys and objects. Uses objects symbolically.", "ar": "اهتمام مناسب واستخدام إبداعي للألعاب."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly inappropriate. Play tends to be repetitive or reflect scripts.", "ar": "اهتمام وستخدام غير مناسب بشكل بسيط."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately inappropriate. Limited imaginative play; repetitive or unusual use of objects.", "ar": "اهتمام واستخدام غير مناسب بدرجة متوسطة."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely inappropriate. No creative play; objects used repetitively or inappropriately.", "ar": "اهتمام واستخدام غير مناسب بدرجة شديدة."},
        }
    },
    {
        "id": 6,
        "en": "Adaptation to Change / Restricted Interests",
        "ar": "التكيف مع التغيير / الاهتمامات المقيدة",
        "ratings": {
            1:   {"en": "Age-appropriate adaptation. May notice changes but accepts them without undue stress.", "ar": "استجابة مناسبة للتغيير وتنوع الاهتمامات."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Quick to develop routines; preferences for specific activities or topics.", "ar": "تكيف غير طبيعي بشكل بسيط مع التغيير."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Definite special interests; shows displeasure and resists change.", "ar": "تكيف غير طبيعي بدرجة متوسطة مع التغيير."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Extreme reaction to change; extreme anxiety, anger, or resistance.", "ar": "تكيف غير طبيعي بدرجة شديدة مع التغيير."},
        }
    },
    {
        "id": 7,
        "en": "Visual Response",
        "ar": "الاستجابة البصرية",
        "ratings": {
            1:   {"en": "Age-appropriate visual response. Eye contact integrated with actions and communication.", "ar": "استجابة بصرية متوافقة مع عمره."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. May stare or inconsistently integrate eye contact.", "ar": "قصور بسيط في الاستجابة البصرية."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Eye contact not integrated with verbalizations; visual fascinations.", "ar": "قصور متوسط في الاستجابة البصرية."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Persistent avoidance of eye contact; extreme visual behavior.", "ar": "قصور شديد في الاستجابة البصرية."},
        }
    },
    {
        "id": 8,
        "en": "Listening Response",
        "ar": "الاستجابة السمعية",
        "ratings": {
            1:   {"en": "Age-appropriate listening response. Normal and appropriate; responds to name.", "ar": "استجابة سمعية متوافقة مع عمره."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Some difficulty with verbalizations; atypical responses in one setting.", "ar": "قصور بسيط في الاستجابة السمعية."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Inconsistent responses; seldom responds to name; unusual across settings.", "ar": "قصور متوسط في الاستجابة السمعية."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Extreme over/underreaction; does not respond to repeated attempts.", "ar": "قصور شديد في الاستجابة السمعية."},
        }
    },
    {
        "id": 9,
        "en": "Taste, Smell, and Touch Response and Use",
        "ar": "استجابات الشم، اللمس والتذوق",
        "ratings": {
            1:   {"en": "Normal use and response. Explores appropriately by looking and feeling.", "ar": "استخدام واستجابة طبيعية لحواس التذوق والشم واللمس."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Occasional unusual smelling/tasting; mild over/underreaction.", "ar": "قصور بسيط في استخدام واستجابة الحواس."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Obvious clothing/food preferences; sensory issues create stress.", "ar": "قصور متوسط في استخدام واستجابة الحواس."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Extreme limits on foods/clothing; extreme sensory responses.", "ar": "قصور شديد في استخدام واستجابة الحواس."},
        }
    },
    {
        "id": 10,
        "en": "Fear or Anxiety",
        "ar": "الخوف والقلق",
        "ratings": {
            1:   {"en": "Normal fear or anxiety. Behavior appropriate to situation and age.", "ar": "مستوى طبيعي من الخوف أو القلق."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Occasional excess or deficit; only evident in one setting.", "ar": "خوف أو قلق غير طبيعي بشكل بسيط."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Quite a bit more/less fear; apparent across more than one setting.", "ar": "خوف أو قلق غير طبيعي بدرجة متوسطة."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Fear/anxiety pervasive across all settings; persists despite reassurance.", "ar": "خوف أو قلق غير طبيعي بدرجة شديدة."},
        }
    },
    {
        "id": 11,
        "en": "Verbal Communication",
        "ar": "التواصل اللفظي",
        "ratings": {
            1:   {"en": "Normal verbal communication. Carries on age-appropriate conversation; no oddities.", "ar": "تواصل لفظي طبيعي مناسب للعمر والموقف."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Limited exchanges; occasional made-up words or unusual intonation.", "ar": "قصور بسيط في التواصل اللفظي."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Minimal initiation; repetitive phrases; formal or pedantic language.", "ar": "قصور متوسط في التواصل اللفظي."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Inability to have a conversation; marked abnormal speech.", "ar": "قصور شديد في التواصل اللفظي."},
        }
    },
    {
        "id": 12,
        "en": "Nonverbal Communication",
        "ar": "التواصل غير اللفظي",
        "ratings": {
            1:   {"en": "Normal nonverbal communication. Uses a variety of facial expressions and gestures.", "ar": "تواصل غير لفظي طبيعي مناسب للعمر."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Uses instrumental gestures; descriptive gestures used infrequently.", "ar": "قصور بسيط في التواصل غير اللفظي."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Facial expressions often flat or exaggerated; limited gestures.", "ar": "قصور متوسط في التواصل غير اللفظي."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Flat or exaggerated expressions; no awareness of others' nonverbal cues.", "ar": "قصور شديد في التواصل غير اللفظي."},
        }
    },
    {
        "id": 13,
        "en": "Thinking / Cognitive Integration Skills",
        "ar": "مهارات التفكير / التكامل المعرفي",
        "ratings": {
            1:   {"en": "Age-appropriate thinking/cognitive integration. Understands meaning; central coherence intact.", "ar": "مهارات تفكير وتكامل معرفي مناسبة للعمر."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly impaired. Delayed thinking; difficulty with relevant vs irrelevant cues.", "ar": "ضعف بسيط في مهارات التفكير والتكامل المعرفي."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately impaired. Notable difficulty comprehending meaning; attends to concrete details.", "ar": "ضعف متوسط في مهارات التفكير والتكامل المعرفي."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severe delay. Persistent difficulty distinguishing relevant from irrelevant details.", "ar": "ضعف شديد في مهارات التفكير والتكامل المعرفي."},
        }
    },
    {
        "id": 14,
        "en": "Level and Consistency of Intellectual Response",
        "ar": "مستوى وثبات الاستجابات الذهنية",
        "ratings": {
            1:   {"en": "Intelligence at least normal and reasonably consistent. No unusual intellectual skills or problems.", "ar": "ذكاء طبيعي ومتسق عبر المجالات."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mildly abnormal. Not as smart as typical peers; skills evenly delayed.", "ar": "أداء فكري غير طبيعي بشكل بسيط."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderately abnormal. Overall functioning in normal range but significant discrepancy across areas.", "ar": "أداء فكري غير طبيعي بدرجة متوسطة."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severely abnormal. Has a skill significantly better than expected (savant skill).", "ar": "أداء فكري غير طبيعي بدرجة شديدة."},
        }
    },
    {
        "id": 15,
        "en": "General Impressions",
        "ar": "الانطباع العام",
        "ratings": {
            1:   {"en": "No autism spectrum disorder. Shows none of the symptoms characteristic of ASD.", "ar": "لا يوجد توحد."},
            1.5: {"en": "Between 1 and 2", "ar": "بين 1 و 2"},
            2:   {"en": "Mild autism spectrum disorder. Shows only a few symptoms or only mild degree.", "ar": "مستوى بسيط من أعراض التوحد."},
            2.5: {"en": "Between 2 and 3", "ar": "بين 2 و 3"},
            3:   {"en": "Moderate autism spectrum disorder. Shows a number of symptoms; moderate interference.", "ar": "مستوى متوسط من أعراض التوحد."},
            3.5: {"en": "Between 3 and 4", "ar": "بين 3 و 4"},
            4:   {"en": "Severe autism spectrum disorder. Shows many symptoms; extreme interference with daily functioning.", "ar": "مستوى شديد من أعراض التوحد."},
        }
    },
]

# ---------------------------------------------------------------------------
# SCORING LOGIC
# ---------------------------------------------------------------------------

def get_severity(form_type: str, raw_score: float, age: int) -> dict:
    """
    Returns severity group, label, and color for a given form/score/age.
    form_type: 'ST' or 'HF'
    age: integer years
    """
    if form_type == "ST":
        if age >= 13:
            if raw_score <= 27.5:
                return {"group": "Minimal-to-No", "label": "Minimal-to-No Symptoms of ASD", "color": "#2ecc71"}
            elif raw_score <= 34.5:
                return {"group": "Mild-Moderate", "label": "Mild-to-Moderate Symptoms of ASD", "color": "#f39c12"}
            else:
                return {"group": "Severe", "label": "Severe Symptoms of ASD", "color": "#e74c3c"}
        else:
            if raw_score <= 29.5:
                return {"group": "Minimal-to-No", "label": "Minimal-to-No Symptoms of ASD", "color": "#2ecc71"}
            elif raw_score <= 36.5:
                return {"group": "Mild-Moderate", "label": "Mild-to-Moderate Symptoms of ASD", "color": "#f39c12"}
            else:
                return {"group": "Severe", "label": "Severe Symptoms of ASD", "color": "#e74c3c"}
    else:  # HF
        if age >= 13:
            if raw_score <= 27.5:
                return {"group": "Minimal-to-No", "label": "Minimal-to-No Symptoms of ASD", "color": "#2ecc71"}
            elif raw_score <= 33.5:
                return {"group": "Mild-Moderate", "label": "Mild-to-Moderate Symptoms of ASD", "color": "#f39c12"}
            else:
                return {"group": "Severe", "label": "Severe Symptoms of ASD", "color": "#e74c3c"}
        else:
            if raw_score <= 27.5:
                return {"group": "Minimal-to-No", "label": "Minimal-to-No Symptoms of ASD", "color": "#2ecc71"}
            elif raw_score <= 33.5:
                return {"group": "Mild-Moderate", "label": "Mild-to-Moderate Symptoms of ASD", "color": "#f39c12"}
            else:
                return {"group": "Severe", "label": "Severe Symptoms of ASD", "color": "#e74c3c"}


# T-score / percentile lookup for CARS2-HF (all ages)
# raw_score -> (t_score, percentile)
HF_TSCORE_TABLE = {
    47: (70, ">97"), 46.5: (70, ">97"), 46: (69, "97"), 45.5: (68, "96"),
    45: (67, "95"), 44.5: (66, "95"), 44: (65, "93"), 43.5: (64, "92"),
    43: (63, "90"), 42.5: (62, "88"), 42: (62, "88"), 41.5: (61, "86"),
    41: (60, "84"), 40.5: (60, "84"), 40: (59, "82"), 39.5: (58, "79"),
    39: (58, "79"), 38.5: (57, "76"), 38: (56, "72"), 37.5: (56, "72"),
    37: (55, "69"), 36.5: (54, "65"), 36: (54, "65"), 35.5: (53, "62"),
    35: (52, "58"), 34.5: (52, "58"), 34: (51, "54"), 33.5: (51, "54"),
    33: (50, "50"), 32.5: (49, "46"), 32: (49, "46"), 31.5: (48, "42"),
    31: (47, "38"), 30.5: (47, "38"), 30: (46, "35"), 29.5: (45, "31"),
    29: (44, "28"), 28.5: (44, "28"), 28: (43, "24"), 27.5: (42, "21"),
    27: (41, "19"), 26.5: (40, "16"), 26: (39, "14"), 25.5: (38, "12"),
    25: (37, "10"), 24.5: (36, "8"), 24: (35, "7"), 23.5: (34, "6"),
    23: (33, "5"), 22.5: (32, "4"), 22: (31, "3"), 21.5: (30, "2"),
    21: (29, "1"), 20.5: (28, "<1"), 20: (27, "<1"), 19.5: (26, "<1"),
    19: (25, "<1"), 18.5: (24, "<1"), 18: (23, "<1"),
}

# T-score / percentile lookup for CARS2-ST (all ages combined approximation)
ST_TSCORE_TABLE = {
    55: (71, ">98"), 54: (70, "97"), 53.5: (69, "97"), 52.5: (68, "96"),
    51.5: (67, "95"), 51: (66, "95"), 50.5: (65, "93"), 50: (64, "92"),
    49.5: (63, "90"), 49: (62, "88"), 48.5: (61, "86"), 48: (60, "84"),
    47.5: (60, "84"), 47: (59, "82"), 46.5: (58, "79"), 46: (57, "76"),
    45.5: (56, "72"), 45: (56, "72"), 44.5: (55, "69"), 44: (54, "65"),
    43.5: (53, "62"), 43: (52, "58"), 42.5: (51, "54"), 42: (50, "50"),
    41.5: (49, "46"), 41: (48, "42"), 40.5: (47, "38"), 40: (47, "38"),
    39.5: (46, "35"), 39: (45, "31"), 38.5: (44, "28"), 38: (44, "28"),
    37.5: (43, "24"), 37: (42, "21"), 36.5: (41, "19"), 36: (40, "16"),
    35.5: (39, "14"), 35: (38, "12"), 34.5: (37, "10"), 34: (36, "8"),
    33.5: (35, "7"), 33: (34, "6"), 32.5: (33, "5"), 32: (32, "4"),
    31.5: (31, "3"), 31: (30, "2"), 30.5: (29, "1"), 30: (28, "<1"),
    29.5: (27, "<1"), 29: (26, "<1"), 28.5: (25, "<1"), 28: (24, "<1"),
    27.5: (23, "<1"), 27: (22, "<1"), 26.5: (21, "<1"), 26: (20, "<1"),
    25: (20, "<1"), 24: (20, "<1"), 23: (20, "<1"), 22: (20, "<1"),
    21: (20, "<1"), 20: (20, "<1"), 19: (20, "<1"),
}


def get_tscore_percentile(form_type: str, raw_score: float) -> tuple:
    """Returns (t_score, percentile_str) for a raw score."""
    table = HF_TSCORE_TABLE if form_type == "HF" else ST_TSCORE_TABLE
    # Exact match
    if raw_score in table:
        return table[raw_score]
    # Find closest
    keys = sorted(table.keys())
    closest = min(keys, key=lambda k: abs(k - raw_score))
    return table[closest]


# ---------------------------------------------------------------------------
# QPC ITEMS (Parent Questionnaire — unscored, but we collect severity labels)
# ---------------------------------------------------------------------------
QPC_SECTIONS = [
    {
        "id": "S1",
        "en": "How does the person communicate?",
        "ar": "كيف يتواصل الشخص؟",
        "items": [
            {"id": "S1Q1", "en": "Imitates sounds, words, and movements of others", "ar": "يقلد أصوات وكلمات ويحاكي حركات الآخرين"},
            {"id": "S1Q2", "en": "Responds to facial expressions, gestures, and different tones of voice", "ar": "يستجيب لتعبيرات الوجه والإيماءات ونبرات الصوت"},
            {"id": "S1Q3", "en": "Responds to their name being called", "ar": "يستجيب لاسمه عند مناداته"},
            {"id": "S1Q4", "en": "Directs facial expressions to others to show emotions", "ar": "يوجه تعبيرات وجه إلى الآخرين لكي يبين ما يشعر به"},
            {"id": "S1Q5", "en": "Uses a variety of gestures coordinated with words", "ar": "يستخدم مجموعة متنوعة من الإيماءات التي تتناسب مع الكلمات"},
        ]
    },
    {
        "id": "S2",
        "en": "How does the person relate to others and show emotion?",
        "ar": "كيف يتواصل مع الآخرين وكيف يعبر عواطفه؟",
        "items": [
            {"id": "S2Q1", "en": "Makes eye contact when speaking with or listening to another person", "ar": "ينظر في عين الشخص الذي يتحدث إليه"},
            {"id": "S2Q2", "en": "Points to and shares things of interest with others", "ar": "يوضح اهتماماته ويشاركها مع الآخرين"},
            {"id": "S2Q3", "en": "Follows another person's gaze or points toward an object out of reach", "ar": "يتبع نظرات شخص آخر ويشير إلى شيء يصعب وصوله إليه"},
            {"id": "S2Q4", "en": "Is responsive to social initiations from others", "ar": "يستجيب للمبادرات الاجتماعية من الآخرين"},
            {"id": "S2Q5", "en": "Initiates social interactions with adults and peers", "ar": "يبدأ التفاعلات الاجتماعية مع البالغين وأقرانه"},
            {"id": "S2Q6", "en": "Sustains an interaction in an easy, flowing manner", "ar": "يعزز علاقاته مع الآخرين بسهولة"},
            {"id": "S2Q7", "en": "Makes and maintains friendships with peers", "ar": "يمكنه تكوين صداقات والحفاظ عليها"},
            {"id": "S2Q8", "en": "Shows a range of emotional expressions that match the situation", "ar": "يظهر مجموعة من التعبيرات العاطفية المناسبة للمواقف"},
            {"id": "S2Q9", "en": "Understands and responds to how another person may be feeling", "ar": "يدرك ويستجيب لما يفكر أو يشعر به الآخر"},
        ]
    },
    {
        "id": "S3",
        "en": "How does the person move his or her body?",
        "ar": "كيف يحرك الشخص جسده؟",
        "items": [
            {"id": "S3Q1", "en": "Has unusual ways of moving fingers, hands, arms, legs; or spins or rocks body", "ar": "لديه طرق غير مألوفة في تحريك الأصابع والأيدي والذراع والساقين أو يدور أو يهز جسده"},
            {"id": "S3Q2", "en": "Does things that might result in self-injury (e.g., head banging, scratching skin)", "ar": "يقوم بعمل أمور قد تؤدي بإصابته مثل يحك رأسه بشدة أو يعبث بجلده"},
            {"id": "S3Q3", "en": "Is clumsy, stumbles, or has an awkward walk or run", "ar": "يسير كما لو كأن طفل أخرق يجري أو يسير بشكل غريب"},
            {"id": "S3Q4", "en": "Has difficulty tying shoes or with handwriting or fine motor tasks", "ar": "لديهم صعوبة في ربط الحذاء أو الكتابة أو المهام التي تتطلب المهارات الحركية الدقيقة"},
        ]
    },
    {
        "id": "S4",
        "en": "How does the person play?",
        "ar": "كيف يلعب الشخص؟",
        "items": [
            {"id": "S4Q1", "en": "Uses only parts of toys instead of whole toys, or plays with objects (spinning wheels, etc.)", "ar": "يستخدم أجزاء من اللعبة بدلاً من استخدامها كاملة"},
            {"id": "S4Q2", "en": "Plays with the same things in the same way over and over", "ar": "يلعب بنفس الأشياء بنفس الطريقة مراراً وتكراراً"},
            {"id": "S4Q3", "en": "Uses toys or materials to represent something they are not (symbolic play)", "ar": "يستخدم الألعاب أو غيرها من الأدوات كي يقدم أشياء غير موجودة بالأصل"},
            {"id": "S4Q4", "en": "Engages in make-believe play, taking on a role not based on scripts from movies/TV", "ar": "يمارس اللعب التخيلي ويأخذ دور غير مقتبس من فيلم أو عرض تليفزيوني"},
        ]
    },
    {
        "id": "S5",
        "en": "How does the person react to new experiences and changes in routine?",
        "ar": "كيف يكون رد فعله عند المرور بتجربة جديدة أو تغييرات في الروتين؟",
        "items": [
            {"id": "S5Q1", "en": "May show anxiety or worry in facial expression or body movement", "ar": "ربما يعبر عن قلقه أو فزعه في تعبيرات الوجه أو حركات الجسد"},
            {"id": "S5Q2", "en": "May show worry about the same thing over and over", "ar": "قد يعبر عن قلقه تجاه نفس الشيء مراراً وتكراراً"},
            {"id": "S5Q3", "en": "Copes with changes or specific ways things must be done", "ar": "يتكيف مع التغييرات التي تحدث"},
            {"id": "S5Q4", "en": "Has specific routines or specific ways things must be done", "ar": "لديه روتين خاص أو أمور محددة يجب أن يقوم بها"},
            {"id": "S5Q5", "en": "Has special interests or topics (e.g., dinosaurs, trains, clocks, weather)", "ar": "له اهتمامات أو موضوعات خاصة"},
        ]
    },
    {
        "id": "S6",
        "en": "How does the person use their senses (vision, hearing, touch, smell)?",
        "ar": "كيف يستخدم حواسه؟",
        "items": [
            {"id": "S6Q1", "en": "Tends to look at objects from unusual angles or out of the corner of the eyes", "ar": "يميل للنظر إلى الأشياء من زاوية غير معتادة أو من طرف عينه"},
            {"id": "S6Q2", "en": "Is overly interested in light from mirrors or light reflecting off objects", "ar": "هل هو شديد الاهتمام بالضوء المنعكس من المرآة أو من الأشياء"},
            {"id": "S6Q3", "en": "Is overly sensitive to some sounds, smells, or textures; seeks some out, actively avoids others", "ar": "ينتابه إحساس مفرط تجاه بعض الأصوات والروائح أو الأقمشة"},
            {"id": "S6Q4", "en": "Has an unusual response to touch; may overreact or not respond to pain", "ar": "لديه استجابة غير عادية عند اللمس أو الألم"},
        ]
    },
]

QPC_RATING_OPTIONS = {
    "en": {
        "0": "Not a problem (does very well)",
        "1": "Mild-to-moderate problem (sometimes a problem)",
        "2": "Severe problem (often or always a problem)",
        "3": "Not a problem now, but was in the past",
        "9": "Don't know",
    },
    "ar": {
        "0": "لا يوجد مشكلة على الإطلاق - الأمر على ما يرام",
        "1": "مشكلة بسيطة إلى متوسطة - تبدو مشكلة أحياناً",
        "2": "مشكلة خطيرة (مشكلة دائمة)",
        "3": "ليست مشكلة حالية ولكن ظهرت في وقت سابق",
        "9": "لا أعرف",
    }
}

# ---------------------------------------------------------------------------
# UI TRANSLATIONS
# ---------------------------------------------------------------------------
UI_TEXT = {
    "en": {
        "app_title_qpc": "CARS-2 Parent/Caregiver Questionnaire",
        "app_title_clinician": "CARS-2 Clinician Assessment",
        "language_toggle": "Language / اللغة",
        "child_name": "Child's Full Name",
        "child_age": "Age (years)",
        "child_gender": "Gender",
        "male": "Male",
        "female": "Female",
        "rater_name": "Rater's Name",
        "test_date": "Test Date",
        "submit": "Submit",
        "thank_you": "Thank you. Your responses have been submitted successfully.",
        "select_form": "Select Assessment Form",
        "form_st": "CARS2-ST (Standard – younger / lower functioning)",
        "form_hf": "CARS2-HF (High-Functioning – age 6+, IQ 80+)",
        "iq_level": "Estimated IQ",
        "verbal_fluent": "Verbally Fluent?",
        "yes": "Yes",
        "no": "No",
        "upload_qpc": "Upload QPC PDF (optional)",
        "upload_hint": "Upload the parent's QPC PDF to include in the report",
        "rating_label": "Rating",
        "clinician_notes": "Clinical Observations (optional)",
        "generating": "Generating report and sending email...",
        "sent": "Report sent to clinician's email.",
        "error_email": "Email failed. Report saved locally.",
        "recommendation": "Recommended Form",
        "override": "Override recommendation",
        "admin_password": "Admin Password",
        "admin_login": "Login",
        "admin_title": "Admin View",
        "ethnic_bg": "Ethnic Background",
        "dob": "Date of Birth",
        "case_id": "Case ID",
        "info_from": "Information Based On",
    },
    "ar": {
        "app_title_qpc": "استبيان CARS-2 للوالدين / مقدمي الرعاية",
        "app_title_clinician": "تقييم CARS-2 للأخصائي",
        "language_toggle": "Language / اللغة",
        "child_name": "الاسم الكامل للطفل",
        "child_age": "العمر (سنوات)",
        "child_gender": "الجنس",
        "male": "ذكر",
        "female": "أنثى",
        "rater_name": "اسم الفاحص",
        "test_date": "تاريخ الفحص",
        "submit": "إرسال",
        "thank_you": "شكراً. تم إرسال إجاباتك بنجاح.",
        "select_form": "اختيار نموذج التقييم",
        "form_st": "CARS2-ST (النموذج القياسي – أصغر سناً / أداء أدنى)",
        "form_hf": "CARS2-HF (النموذج المتقدم – العمر 6+، الذكاء 80+)",
        "iq_level": "معدل الذكاء التقديري",
        "verbal_fluent": "لديه طلاقة لفظية؟",
        "yes": "نعم",
        "no": "لا",
        "upload_qpc": "رفع ملف QPC (اختياري)",
        "upload_hint": "ارفع ملف QPC PDF الخاص بالوالدين لتضمينه في التقرير",
        "rating_label": "التقييم",
        "clinician_notes": "ملاحظات إكلينيكية (اختياري)",
        "generating": "جاري إنشاء التقرير وإرساله...",
        "sent": "تم إرسال التقرير إلى بريد الأخصائي.",
        "error_email": "فشل الإرسال. تم حفظ التقرير محلياً.",
        "recommendation": "النموذج الموصى به",
        "override": "تجاوز التوصية",
        "admin_password": "كلمة مرور المشرف",
        "admin_login": "دخول",
        "admin_title": "عرض المشرف",
        "ethnic_bg": "الخلفية العرقية",
        "dob": "تاريخ الميلاد",
        "case_id": "رقم الحالة",
        "info_from": "استناداً إلى المعلومات المقدمة من",
    }
}
