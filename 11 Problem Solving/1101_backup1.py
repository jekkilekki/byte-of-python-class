# 1101_backup1.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['"C:\\Users\\User\\Desktop\\Aaron Python\\9 Modules\\insta"']

# 2. The backup must be stored in a main backup directory
target_dir = 'C:\\Users\\User\\Desktop\\Aaron Python\\9 Modules\\insta_backup'

# 3. Files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make dir

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Backed up to: ', target)
else:
    print('Backup FAILED')
