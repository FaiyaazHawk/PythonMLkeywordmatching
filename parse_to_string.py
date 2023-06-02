def parse_to_string():
    import fitz
    import json

    pdf_path = "/home/faiyaaz/python/transformers/Resume_SoftwareEng-Intern.pdf"

    doc = fitz.open(pdf_path)

    data = []

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        data.append(text)

    result = " ".join(data)

    return result