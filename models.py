from sqlalchemy import Column, String, DateTime
from database import Base

class PhishReport(Base):
    __tablename__ = "phish_reports"

    report_id = Column(String, primary_key=True, index=True)
    phish_url = Column(String)
    timestamp = Column(DateTime)
    review_type = Column(String)
    screenshot = Column(String, nullable=True)
    match_text = Column(String, nullable=True)
    match_regex = Column(String, nullable=True)
    callback_url = Column(String, nullable=True)
    organization_id = Column(String)
    status = Column(String)
    processor = Column(String, nullable=True)
    processed_timestamp = Column(DateTime, nullable=True)
