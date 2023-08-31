def add_time(start, duration, dayd=None):
  #initial time
  rw = start.split(':')
  sh = rw[0]
  sm = rw[1].split()[0]
  g = rw[1].split()[1]
  days = [
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
    'sunday'
  ]

  #duration time
  dh = duration.split(':')[0]
  dm = duration.split(':')[1]
  new_time = ''
  seg = ''

  if g == 'AM':
    fh = int(sh) + int(dh)
    fm = int(sm) + int(dm)
    fh = fh + (fm // 60)
    if dayd:
      de = days.index(dayd.lower()) + (fh // 24)
      seg = f', {str(days[de%7]).title()}'

    if fh // 24 == 0:
      if fh // 12 == 0:
        new_time = f"{fh}:{fm%60:02} AM{seg}"
      else:
        if fh % 12 == 0:
          new_time = f"{12}:{fm%60:02} PM{seg}"
        else:
          new_time = f"{fh%12}:{fm%60:02} PM{seg}"

    if fh // 24 == 1:
      if (fh // 12) % 2 == 1:
        if fh % 12 == 0:
          new_time = f"{12}:{fm%60:02} PM{seg} (next day)"
        else:
          new_time = f"{fh%12}:{fm%60:02} PM{seg} (next day)"
      else:
        if fh % 12 == 0:
          new_time = f"{12}:{fm%60:02} AM{seg} (next day)"
        else:
          new_time = f"{fh%12}:{fm%60:02} AM{seg} (next day)"

    if fh // 24 > 1:
      if (fh // 12) % 2 == 0:
        if fh % 12 == 0:
          new_time = f"{12}:{fm%60:02} AM{seg} ({fh//24} days after)"
        else:
          new_time = f"{fh%12}:{fm%60:02} AM{seg} ({fh//24} days after)"
      else:
        if fh % 12 == 0:
          new_time = f"{12}:{fm%60:02} PM{seg} ({fh//24} days after)"
        else:
          new_time = f"{fh%12}:{fm%60:02} PM{seg} ({fh//24} days after)"

  if g == 'PM':
    fh = int(sh) + int(dh) + 12
    fm = int(sm) + int(dm)
    fh = fh + (fm // 60)

    if dayd:
      de = days.index(dayd.lower()) + (fh // 24)
      seg = f', {str(days[de%7]).title()}'

    if fh // 24 == 0:
      if fh % 12 == 0:
        new_time = f'{12}:{fm % 60} PM{seg}'
      else:
        new_time = f'{fh%12}:{fm % 60} PM{seg}'

    if fh // 24 == 1:
      if (fh // 12) % 2 == 1:
        if fh % 12 == 0:
          new_time = f"{12}:{fm%60:02} PM{seg} (next day)"
        else:
          new_time = f"{fh%12}:{fm%60:02} PM{seg} (next day)"
      else:
        if fh % 12 == 0:
          new_time = f"{12}:{fm%60:02} AM{seg} (next day)"
        else:
          new_time = f"{fh%12}:{fm%60:02} AM{seg} (next day)"

    if fh // 24 > 1:
      if (fh // 12) % 2 == 0:
        if fh % 12 == 0:
          new_time = f"{12}:{fm%60:02} AM{seg} ({fh//24} days later)"
        else:
          new_time = f"{fh%12}:{fm%60:02} AM{seg} ({fh//24} days later)"
      else:
        if fh % 12 == 0:
          new_time = f"{12}:{fm%60:02} PM{seg} ({fh//24} days later)"
        else:
          new_time = f"{fh%12}:{fm%60:02} PM{seg} ({fh//24} days later)"

  return new_time
