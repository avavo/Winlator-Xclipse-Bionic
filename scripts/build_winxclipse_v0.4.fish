#!/usr/bin/env fish

set BASE_APK "$argv[1]"
set ICON_PNG "$argv[2]"
set OUT_APK "$argv[3]"

if test -z "$BASE_APK"
    echo "Uso:"
    echo "./scripts/build_winxclipse_v0.4.fish /caminho/base.apk /caminho/icon.png /caminho/WinXclipse-v0.4.apk"
    exit 1
end

if test -z "$ICON_PNG"
    echo "Faltou o ícone PNG."
    exit 1
end

if test -z "$OUT_APK"
    echo "Faltou o caminho do APK final."
    exit 1
end

if not test -f "$BASE_APK"
    echo "APK base não encontrado: $BASE_APK"
    exit 1
end

if not test -f "$ICON_PNG"
    echo "Ícone não encontrado: $ICON_PNG"
    exit 1
end

set WORKDIR (mktemp -d)
set UNSIGNED "$WORKDIR/WinXclipse-v0.4-unsigned.apk"
set ALIGNED "$WORKDIR/WinXclipse-v0.4-aligned.apk"

python3 scripts/patch_winxclipse_v0.4.py "$BASE_APK" "$ICON_PNG" "$UNSIGNED"; or exit 1

$ANDROID_HOME/build-tools/35.0.0/zipalign -p -f 4 "$UNSIGNED" "$ALIGNED"; or exit 1

$ANDROID_HOME/build-tools/35.0.0/apksigner sign \
    --ks "$HOME/.android/debug.keystore" \
    --ks-key-alias androiddebugkey \
    --ks-pass pass:android \
    --key-pass pass:android \
    --out "$OUT_APK" \
    "$ALIGNED"; or exit 1

echo "APK final:"
echo "$OUT_APK"
