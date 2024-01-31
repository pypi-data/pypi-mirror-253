"""Tests for job manager module"""
from roche_datachapter_lib.job_manager import JobManager

JOBNAME = 'AB_TestJOB_LUCAS_PYTHON'
USER = 'RNUMDMAS\\osirisl'
PATH = 'C:\\Users\\Lucas\\run_app.bat'
JobManager.create_or_update_python_job(JOBNAME, USER, PATH)
