[buildozer]
log_level = 2
warn_on_root = 1

[app]
title = SIEDLIK SYSTEM
package.name = siedliksystem
package.domain = org.siedlik
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,yaml,txt
version = 1.2

# Uproszczone wymagania - tylko to, co niezbędne
requirements = python3, flet==0.21.0, hostpython3, openssl, sqlite3, certifi

orientation = portrait
fullscreen = 0

# Podstawowe uprawnienia
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Aktualne wersje API dla Google Play i stabilności
android.api = 34
android.minapi = 21
android.ndk = 26b
android.archs = arm64-v8a
android.allow_backup = True

# Formaty wyjściowe
android.release_artifact = apk
android.debug_artifact = apk

p4a.branch = master
