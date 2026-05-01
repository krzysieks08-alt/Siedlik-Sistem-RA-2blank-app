[buildozer]
log_level = 2
warn_on_root = 1

[app]
title = SIEDLIK SYSTEM
package.name = siedliksystem
package.domain = org.siedlik
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,yaml,txt

version = 3.0
# Minimalne, stabilne wymagania
requirements = python3, flet==0.21.0, hostpython3, openssl, sqlite3, certifi

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Ustawienia stabilności - cofamy API do 33 i NDK do 25b
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True

android.release_artifact = apk
android.debug_artifact = apk

p4a.branch = master
