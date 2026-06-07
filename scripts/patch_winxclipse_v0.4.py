import zipfile
from pathlib import Path
from PIL import Image
import sys

if len(sys.argv) != 4:
    print("Uso: patch_winxclipse_v0.4.py base.apk icon.png output-unsigned.apk")
    sys.exit(1)

base_apk = Path(sys.argv[1])
icon_path = Path(sys.argv[2])
out_apk = Path(sys.argv[3])

# As substituições precisam manter o mesmo tamanho.
# Winlator Cmod = 13 chars
# WinXclipse + 3 espaços = 13 chars
replacements = {
    # App/about name. Same length as original.
    "Winlator Cmod": "WinXclipse   ",
    "Winlator CMOD": "WinXclipse   ",

    # Version labels. Same length as original.
    "Version Cmod-v13.1": "Version WinX-v0.4 ",
    "Version 7.1.4x-cmod": "Version WinX-v0.4  ",
    "Cmod-v13.1": "WinX-v0.4 ",
    "Big Picture Mode Music by Fumer": "WinXclipse patch by avavo      ",

    # Credit/additional branding, only if found outside DEX.
    "Winlator Cmod by": "WinXclipse by   ",
}

sizes = {
    "mipmap-mdpi-v4": 48,
    "mipmap-hdpi-v4": 72,
    "mipmap-xhdpi-v4": 96,
    "mipmap-xxhdpi-v4": 144,
    "mipmap-xxxhdpi-v4": 192,
}

icon = Image.open(icon_path).convert("RGBA")

def make_padded_png(size, scale=0.72):
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    inner = int(size * scale)
    img = icon.resize((inner, inner), Image.Resampling.LANCZOS)
    pos = ((size - inner) // 2, (size - inner) // 2)
    canvas.alpha_composite(img, pos)

    temp = Path(f"/tmp/winx_icon_{size}.png")
    canvas.save(temp, "PNG")
    data = temp.read_bytes()
    temp.unlink()
    return data

png_cache = {s: make_padded_png(s) for s in sizes.values()}

changed_text = 0
changed_icons = 0

def apply_replacements(data):
    global changed_text

    for old, new in replacements.items():
        if len(old) != len(new):
            raise ValueError(f"Replacement length mismatch: {old!r} -> {new!r}")

        old8 = old.encode()
        new8 = new.encode()
        old16 = old.encode("utf-16le")
        new16 = new.encode("utf-16le")

        n = data.count(old8) + data.count(old16)
        if n:
            data = data.replace(old8, new8).replace(old16, new16)
            changed_text += n

    return data

with zipfile.ZipFile(base_apk, "r") as zin, zipfile.ZipFile(out_apk, "w", compression=zipfile.ZIP_DEFLATED) as zout:
    for info in zin.infolist():
        name = info.filename

        # Remove assinatura antiga.
        if name.startswith("META-INF/"):
            continue

        data = zin.read(name)

        # Nunca tocar em DEX. DEX tem checksum interno e quebra o app.
        if not (name.startswith("classes") and name.endswith(".dex")):
            data = apply_replacements(data)

        for folder, size in sizes.items():
            targets = (
                f"res/{folder}/ic_launcher.png",
                f"res/{folder}/ic_launcher_round.png",
                f"res/{folder}/ic_launcher_foreground.png",
                f"res/{folder}/ic_launcher_background.png",
                f"res/{folder}/ic_launcher_monochrome.png",
            )

            if name in targets:
                data = png_cache[size]
                changed_icons += 1

        zout.writestr(info, data)

print("substituições de texto:", changed_text)
print("ícones substituídos:", changed_icons)
print("APK gerado:", out_apk)
