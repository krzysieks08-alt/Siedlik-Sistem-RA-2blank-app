[buildozer]
log_level = 2
warn_on_root = 1

[app]
# (str) Title of your application
title = SIEDLIK SYSTEM

# (str) Package name
package.name = siedliksystem

# (str) Package domain
package.domain = org.siedlik

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,txt,yaml

# (str) Application versioning
version = 1.0

# (list) KLUCZOWE: Wymagania dla Flet (dodane openssl, sqlite i certyfikaty)
requirements = python3, flet, hostpython3, openssl, sqlite3, certifi, chardet, idna, urllib3

# (str) Supported orientations
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (list) Architecture
android.archs = arm64-v8a

# (bool) Allow backup
android.allow_backup = True

# (str) Format
android.release_artifact = apk
android.debug_artifact = apk

# (str) Python-for-android branch
p4a.branch = master
