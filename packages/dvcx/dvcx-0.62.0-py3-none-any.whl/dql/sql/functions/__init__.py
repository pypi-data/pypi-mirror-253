from sqlalchemy.sql.expression import func

from . import path  # noqa: F401

count = func.count
sum = func.sum
avg = func.avg
min = func.min
max = func.max
