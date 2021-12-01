def split_into_groups(lines: list) -> list:
  """Splits a list of lines of input into a list of sublists, using falsy values
  (empty lines) as a delimiter.

  Arguments:
  lines -- the list of lines of input
  """
  groups = []
  group = []
  for line in lines:
    if line:
      group.append(line)
    else:
      groups.append(group)
      group = []
  if group:
    groups.append(group)
  return groups
