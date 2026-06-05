from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_report(df):

    file_path = "reports/DeepHire_Report.pdf"

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "DeepHire AI Recruitment Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    for _, row in df.iterrows():

        text = f"""
        Candidate: {row['name']}
        <br/>
        ATS Score: {row['score']}
        <br/>
        Matched Skills: {row['matched']}
        <br/>
        Missing Skills: {row['missing']}
        """

        elements.append(
            Paragraph(
                text,
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 12)
        )

    doc.build(elements)

    return file_path