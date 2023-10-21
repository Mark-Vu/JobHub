from flask import Blueprint
bp = Blueprint('job_board', __name__)

from src.job_board import routes