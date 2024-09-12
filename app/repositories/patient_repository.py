from sqlalchemy import func

from app.models import Patient
from sqlalchemy.orm import Session
from datetime import datetime, timedelta


class PatientRepository:
    def __init__(self, db):
        self.db = db

    def add_patient(self, name: str, date_of_birth: str):
        patient = Patient(name=name, date_of_birth=date_of_birth)
        self.db.add(patient)
        self.db.commit()

    def get_today_patients(self):
        today = datetime.utcnow().date()
        return self.db.query(Patient).filter(Patient.added_on >= today).all()

    def get_patients_count_by_day(self):
        today = datetime.now()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        counts = (
            self.db.query(func.date(Patient.added_on), func.count(Patient.id))
            .filter(Patient.added_on >= start_of_week, Patient.added_on <= end_of_week)
            .group_by(func.date(Patient.added_on))
            .all()
        )

        return counts
