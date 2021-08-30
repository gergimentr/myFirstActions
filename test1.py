import os
import time
while True:
    if os.path.exists('/tmp/gitclone'):
        os.system('rm -rf /tmp/gitclone')
    os.system('git clone  https://github.com/nextcloud/server.git /tmp/gitclone')
    time.sleep(60)
