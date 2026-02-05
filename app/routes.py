from fastapi import APIRouter
import dal

router = APIRouter(
    prefix="/employees",
    tags=["test"])


@router.get("/engineering/high-salary")
def get_all():
    return dal.get_engineering_high_salary_employees()


@router.get("/by-age-and-role")
def get_all():
    return dal.get_employees_by_age_and_role()


@router.get("/top-seniority")
def get_all():
    return dal.get_top_seniority_employees_excluding_hr()


@router.get("/age-or-seniority")
def get_all():
    return dal.get_employees_by_age_or_seniority()


@router.get("/managers/excluding-departments")
def get_all():
    return dal.get_managers_excluding_departments()


@router.get("/managers/by-lastname-and-age")
def get_all():
    return dal.get_employees_by_lastname_and_age()
