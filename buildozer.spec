
[buildozer]
log_level = 2
warn_on_root = 1

[app]
title = SIEDLIK SYSTEM
package.name = siedliksystem
package.domain = org.siedlik
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,yaml,txt
version = 3.5

# Stabilne wymagania dla Flet
requirements = python3, flet==0.21.0, setuptools

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# KLUCZOWE POPRAWKI POD GITHUB ACTIONS:
android.api = 31
android.minapi = 21
# android.ndk = 25b <--- zostaw zakomentowane, to naprawia Exit Code 1

android.archs = arm64-v8a
android.allow_backup = True

android.release_artifact = apk
android.debug_artifact = apk

# To pozwala Buildozerowi pobrać nowsze skrypty pakujące
p4a.branch = develop
