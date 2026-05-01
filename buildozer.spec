[buildozer]
# (str) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage, indended to be a shared cache
warn_on_root = 1

[app]
# (str) Title of your application
title = SIEDLIK SYSTEM

# (str) Package name
package.name = siedliksystem

# (str) Package domain (needed for android packaging)
package.domain = org.siedlik

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0

# (list) Application requirements
# UWAGA: Dla Flet ważne jest dodanie tych zależności
requirements = python3,flet,hostpython3

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK directory
# android.sdk_path = 

# (str) Android NDK directory
# android.ndk_path = 

# (list) Architecture to build for (keep only what you need)
android.archs = arm64-v8a

# (bool) allows Android to issue a warning if the disk space is too low
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk)
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aar)
android.debug_artifact = apk
