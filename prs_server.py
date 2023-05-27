from fastapi import FastAPI, Header, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel
import datetime
from database import SessionLocal, engine, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class PhishReport(BaseModel):
    reportId: str
    phishURL: str
    timestamp: str
    reviewType: str
    screenshot: Optional[str] = None
    matchText: Optional[str] = None
    matchRegex: Optional[str] = None
    callbackURL: Optional[str] = None

@app.post("/submitPhishReport")
async def submit_phish_report(phish_report: PhishReport, authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if authorization is None:
        raise HTTPException(status_code=400, detail="No authorization provided")

    new_report = models.PhishReport(
        report_id = phish_report.reportId,
        phish_url = phish_report.phishURL,
        timestamp = phish_report.timestamp,
        review_type = phish_report.reviewType,
        screenshot = phish_report.screenshot,
        match_text = phish_report.matchText,
        match_regex = phish_report.matchRegex,
        callback_url = phish_report.callbackURL,
        organization_id = authorization,  # for simplicity, we are using the authorization header as org ID
        status = 'new',
        processor = None
    )

    db.add(new_report)
    db.commit()

    return {"reportId": phish_report.reportId}

@app.get("/checkStatus")
async def check_status(reportId: str, authorization: Optional[str] = Header(None), db: Session = Depends(get_db)):
    if authorization is None:
        raise HTTPException(status_code=400, detail="No authorization provided")

    report = db.query(models.PhishReport).filter(models.PhishReport.report_id == reportId).first()

    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    return {"reportId": report.report_id, "status": report.status, "submissionTimestamp": report.timestamp, "processingTimestamp": report.processed_timestamp}

@app.get("/unprocessedReports")
async def get_unprocessed_reports(db: Session = Depends(get_db)):
    unprocessed_reports = db.query(models.PhishReport).filter(models.PhishReport.status == 'new').all()
    return unprocessed_reports

@app.patch("/updateReport/{reportId}")
async def update_report_status(reportId: str, status: str, processor: str, db: Session = Depends(get_db)):
    report = db.query(models.PhishReport).filter(models.PhishReport.report_id == reportId).first()

    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")

    report.status = status
    report.processor = processor
    report.processed_timestamp = datetime.datetime.now().isoformat()

    db.commit()

    return {"reportId": reportId, "status": status}
