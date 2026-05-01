[buildozer]
log_level = 2
warn_on_root = 1

[app]
title = SIEDLIK SYSTEM
package.name = siedliksystem
package.domain = org.siedlik
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,yaml,txt
version = 6.0

requirements = python3, flet==0.21.0, setuptools

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# ZMIANY POD GITHUB ACTIONS (WERSJA LEKKA):
android.api = 31
android.minapi = 21
android.archs = armeabi-v7a

android.allow_backup = True
android.release_artifact = apk
android.debug_artifact = apk

p4a.branch = develop
