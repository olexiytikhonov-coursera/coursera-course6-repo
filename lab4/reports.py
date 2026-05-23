#!/usr/bin/env python3

import reportlab

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, paragraph):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(paragraph, styles["BodyText"])
  empty_line = Spacer(1,10)
  report.build([report_title, empty_line, report_info])


if __name__ == "__main__":
  # code that runs only when the file is executed directly
  generate_report("report.pdf", "Title of report", "Body text <BR/>More text<BR/><BR/>And more text")