[buildozer]
log_level = 2
warn_on_root = 1

[app]
title = SIEDLIK SYSTEM
package.name = siedliksystem
package.domain = org.siedlik
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,yaml,txt
version = 1.1

# POPRAWIONE WYMAGANIA (Linię 25 u Ciebie zastąp tym):
requirements = python3, flet==0.21.0, kivy, cython, hostpython3, openssl, sqlite3, certifi, chardet, idna, urllib3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True
android.release_artifact = apk
android.debug_artifact = apk
p4a.branch = master
