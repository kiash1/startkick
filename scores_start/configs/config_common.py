__author__ = 'milu'

# standard library
import os

from pytz import timezone
import pytz


# third-party
from dateutil.relativedelta import relativedelta

# django

# local django

# constant
CREDIT_RATE = 1.0
CREDIT_CURRENCY = 'BDT'
CREDIT_PER_INVESTIGATION = 1
MIN_CREDIT_BALANCE = -10
TIME_ZONE = 'UTC' #TODO put into config.py
# get timezone in env file
GET_DEPLOY_ZONE = os.environ.get('ENV_DEPLOY_ZONE', None)
DEPLOY_ZONE = GET_DEPLOY_ZONE
DEPLOY_UTC = "UTC+00:00"
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
HW_MODULE = True
PAYMENT_MODULE = True


def UTC_to_DEPLOY_ZONE(utc0_datetime):
    if utc0_datetime.tzinfo:
        return utc0_datetime.astimezone(timezone(DEPLOY_ZONE))

    utc0_datetime = utc0_datetime.replace(tzinfo=pytz.UTC)
    return utc0_datetime.astimezone(timezone(DEPLOY_ZONE))


def DEPLOY_ZONE_to_UTC(DEPLOY_ZONE_datetime):
    print(('Converting time:{0}'.format(DEPLOY_ZONE_datetime,)))

    tz = timezone(DEPLOY_ZONE)
    tm_utc = DEPLOY_ZONE_datetime.replace(tzinfo=None)
    tzoffset = tz.utcoffset(tm_utc)

    rt_time = tm_utc - tzoffset

    return rt_time.replace(tzinfo=pytz.UTC)


def make_datetime_from_string(subject_str, datetime_format=DATETIME_FORMAT):
    from datetime import datetime
    return datetime.strptime(subject_str, datetime_format)


def convert_string_to_deploy_zone_datetime(subject_str, datetime_format=DATETIME_FORMAT):
    from django.core.exceptions import ValidationError
    try:
        timezone = pytz.timezone(DEPLOY_ZONE)
        tz_unaware_datetime = make_datetime_from_string(subject_str, datetime_format)
        tz_aware_datetime = timezone.localize(tz_unaware_datetime)
        return tz_aware_datetime
    except Exception:
        raise ValidationError("parameter --> {} has to be datetime and should be in {} format".format(subject_str,
                                                                                                      datetime_format))

def time_travel_in_days(date,days):
    date += relativedelta(days=+days)

    return date


def time_travel_in_week(date,weeks):

    date += relativedelta(weeks=+weeks)

    return date


def time_travel_in_month(date,month):
    date += relativedelta(months=+month)

    return date


def get_credit_settings():
    return CREDIT_RATE,CREDIT_CURRENCY,MIN_CREDIT_BALANCE


def get_credit_per_investigation():
    return 1


def get_min_emergency_balance():
    return -1


def get_currency():
    return 'BDT'
