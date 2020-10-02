import os
import fileinput

baseDirectory = "../src/"
directories = ["people","fragments","useful"]

# -----
# Add links to markdown file
# -----
def add_links(filedata, note_ids_to_filenames, note_titles_to_paths):
  filedata = filedata.replace("bear://x-callback-url/open-note?id=", "")

  # Add markdown note links
  for item in note_ids_to_filenames:
    filedata = filedata.replace(item[0], item[1])

  # Add wiki links
  for item in note_titles_to_paths:
    filedata = filedata.replace("[[" + item[0] + "]]", "[" + item[0] +"](" + item[1] +")")

  return filedata
# -----

# -----
# Parse YAML if present
# -----
def parse_yaml(filedata):
  file_lines = filedata.splitlines()

  # If a YAML block is present at top of note, remove it and everything preceding,
  # except the first line of the file (the title).

  file_parts = filedata.split('---')
  if len(file_parts) > 1:
    yaml_block = file_parts[1]
    filedata = file_lines[0] + file_parts[2]

  return filedata
# -----

# -----
# Replace spaces with underscores in filenames.
# -----
for directory in directories:
  filenames = os.listdir(baseDirectory + directory)

  for filename in filenames:
    updatedFilename = filename.replace(" ", "-").lower()
    updatedFilename = updatedFilename.replace(",", "")
    os.rename(os.path.join(baseDirectory + directory, filename), os.path.join(baseDirectory + directory, updatedFilename))

# -----
# Add links to markdown files
# -----

# Build a note id => filename array (for note links)
note_ids_to_filenames = []

# Build a note title => filename array (for Wiki links)
note_titles_to_paths = []

for directory in directories:
  for filename in os.listdir(baseDirectory + directory):
    with open(os.path.join(baseDirectory + directory, filename), 'r', encoding="utf8", errors='ignore') as f:
      lines = f.read().splitlines()
      last_line = lines[-1]
      last_line = last_line.replace('<!-- {BearID:', '')
      last_line = last_line.replace('} -->', '')
      note_id = last_line.strip()
      note_ids_to_filenames.append([note_id, filename])
      note_title = lines[0].replace('# ', '')
      note_titles_to_paths.append([note_title, "/" + directory + "/" + filename])

for directory in directories:
  for filename in os.listdir(baseDirectory + directory):

    # Read in the file
    with open(os.path.join(baseDirectory + directory, filename), 'r', encoding="utf8", errors='ignore') as file :
      filedata = file.read()

    # -----
    # Add links to markdown files
    # -----
    filedata = add_links(filedata, note_ids_to_filenames, note_titles_to_paths)


    # -----
    # Parse YAML if present
    # -----
    filedata = parse_yaml(filedata)

    # Write the file out again
    with open(os.path.join(baseDirectory + directory, filename), 'w') as file:
      file.write(filedata)
