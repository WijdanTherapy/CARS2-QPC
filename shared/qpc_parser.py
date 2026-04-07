# shared/qpc_parser.py
"""
Parses the QPC_DATA block from a QPC PDF.
Returns dict of {item_id: rating_value} or empty dict.
"""
import re


def parse_qpc_pdf(pdf_bytes: bytes) -> dict:
    """
    Extract the QPC_DATA block from a QPC PDF.
    Returns a dict like {"S1Q1": "0", "S1Q2": "1", ...}
    or empty dict if parsing fails.
    """
    try:
        from pypdf import PdfReader
        import io
        reader = PdfReader(io.BytesIO(pdf_bytes))
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() or ""
    except Exception:
        return {}

    return _extract_from_text(full_text)


def _extract_from_text(text: str) -> dict:
    """Extract QPC_DATA block from raw text."""
    pattern = r"QPC_DATA_START\s*(.*?)\s*QPC_DATA_END"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if not match:
        return {}

    block = match.group(1)
    result = {}
    for line in block.splitlines():
        line = line.strip()
        if "=" in line:
            k, _, v = line.partition("=")
            result[k.strip()] = v.strip()
    return result


def get_qpc_summary(qpc_data: dict) -> dict:
    """
    Returns summary counts: {0: int, 1: int, 2: int, 3: int, 9: int}
    """
    counts = {"0": 0, "1": 0, "2": 0, "3": 0, "9": 0}
    for v in qpc_data.values():
        key = str(v)
        if key in counts:
            counts[key] += 1
    return counts
