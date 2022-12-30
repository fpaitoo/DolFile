from datetime import date, datetime

from flask import Blueprint, render_template, request, current_app as app
from sqlalchemy import func, cast, Date
from flask_login import login_required
from models import FileDetail, User, FileStat
from Helpers import Aux as aux
import calendar

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@dashboard.route("/")
@login_required
def index():
    year_start = datetime.strptime(aux.get_twelve_month_date(), '%Y-%m-%d')
    end_date = date.today()
    all_files = FileDetail.query.count()
    all_files_size = FileDetail.query.with_entities(func.sum(FileDetail.file_size).label('total')).first().total
    if all_files_size:
        all_files_size = aux.convert_size(all_files_size * 1024)
    download_requests = FileDetail.query.with_entities(func.sum(FileDetail.download_requests)
                                                       .label('total')).first().total
    number_of_users = User.query.count()
    saved_files_stats = FileDetail.query.with_entities(
        func.extract('month', FileDetail.created_at).label('f_date'),
        func.count(FileDetail.id).label('upload_count')) \
        .filter(FileDetail.created_at.between(year_start, end_date)).group_by('f_date')
    months, d_months, n_s, d_n_s = [], [], [], []
    # print(saved_files_stats)
    for data in saved_files_stats:
        d = data['f_date']
        months.append(calendar.month_abbr[int(d)])
        n_s.append(data['upload_count'])
    months = ','.join(months)
    n_s = ','.join(map(str, n_s))

    download_files_stats = FileStat.query.with_entities(func.extract('month', FileStat.accessed_at).label('f_date'),
                                                        func.count(FileStat.id).label('download_count')).group_by(
        'f_date').all()
    # print(download_files_stats)
    for dt in download_files_stats:
        d = dt['f_date']
        d_months.append(calendar.month_abbr[int(d)])
        d_n_s.append(dt['download_count'])
    d_months = ','.join(d_months)
    d_n_s = ','.join(map(str, n_s))

    image_count = get_file_type_count('image')

    return render_template('dashboard.html', all_files=all_files, all_files_size=all_files_size,
                           download_requests=download_requests, number_of_users=number_of_users, upload_months=months,
                           upload_count=n_s, download_months=d_months, download_count=d_n_s,
                           image_count=get_file_type_count('image'), image_size=get_file_type_size('image'),
                           video_size=get_file_type_size('video'), video_count=get_file_type_count('video'),
                           zip_size=get_file_type_size('zip'), zip_count=get_file_type_count('zip'),
                           other_size=get_file_type_size('other'), other_count=get_file_type_count('other'))


def get_file_type_size(file_type):
    file_size = FileDetail.query.with_entities(func.sum(FileDetail.file_size).label('total')).filter(
        FileDetail.file_type == file_type).first().total
    if file_size:
        return aux.convert_size(file_size * 1024)
    else:
        return 0


def get_file_type_count(file_type):
    return FileDetail.query.filter(FileDetail.file_type == file_type).count()