[buildozer]
log_level = 2
warn_on_root = 1

[app]
title = SIEDLIK SYSTEM
package.name = siedliksystem
package.domain = org.siedlik
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,yaml,txt
version = 2.0

# Absolutne minimum - Flet sam dociągnie resztę
requirements = python3, flet==0.21.0

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Ustawienia "bezpieczne" dla serwerów GitHub
android.api = 31
android.minapi = 21
android.archs = arm64-v8a
android.allow_backup = True

android.release_artifact = apk
android.debug_artifact = apk

p4a.branch = master
