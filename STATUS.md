# WXB v0.1 Status

## Base

- Base: Winlator Cmod v13.1.1 oficial
- Package: `com.winlator.cmod`
- Nome visual: `Winlator WXB!`

## Resultado

- APK instala
- Nome visual alterado
- App abre
- Patch funcional sem alterar DEX

## Problemas encontrados

### Source pública

A source pública testada compilou, mas o APK gerado não se comportou igual ao APK oficial. O botão de criar container não funcionou.

### Patch direto inicial

O primeiro patch direto alterou `classes8.dex`, causando erro de checksum e crash:

- `Bad checksum`
- `ClassNotFoundException`
- falha no provider `WinlatorFilesProvider`

## Solução usada

Refazer o patch pulando todos os arquivos `classes*.dex`.

## Atualização v0.2.1

- Ícone WXB aplicado.
- Padding ajustado para evitar zoom excessivo no Android.
- APK gerado como `Winlator-Xclipse-v0.2.1.apk`.

## Próximos passos

1. Validar criação de container.
2. Criar script automático do patch.
3. Ajustar tela About/créditos.
4. Ajustar tela About/créditos.
5. Pensar em package próprio.
6. Estudar integração futura com MdiEx/ExynosTools.


## WXB v0.2.1

- Ícone WXB aplicado.
- Padding do ícone ajustado para evitar zoom excessivo no Android.
- APK gerado como `Winlator-Xclipse-v0.2.1.apk`.
- Método seguro mantido: sem alterar `classes*.dex`.



## WinXclipse v0.3 Validation

Validation passed on device.

Tested:
- Container creation: OK
- Container launch: OK
- App close/reopen: OK
- Container persistence after restart: OK

Known Android warnings:
- Android may warn that the app was made for an older Android version because the base uses targetSdkVersion 28.
- Android may show that the app was installed via ADB when installed through adb.

Current status:
- WinXclipse v0.3 is functional and suitable for release.


## WinXclipse v0.3.1 Validation

Validation passed.

Changes:
- About title shows `WinXclipse`.
- About version shows `Version WinX-v0.3`.
- Icon remains applied with corrected padding.
- Container creation works.
- Container launch works.
- Container persists after app restart.

Known remaining issue:
- Main header may still show `Winlator Cmod`, likely from a DEX-side string or unsafe resource path. It is intentionally left unchanged to avoid breaking the APK.

Current status:
- WinXclipse v0.3.1 is suitable for release.


## WinXclipse v0.4 Validation

Validation passed.

Changes:
- About version updated to `Version WinX-v0.4`.
- WinXclipse icon retained.
- v0.4 patch/build scripts added.
- DEX files remain untouched.

Known limitations:
- Main header still shows `Winlator Cmod`.
- Some About credits remain original because the strings are stored in `classes*.dex`.
- DEX patching is intentionally avoided because direct modification breaks internal checksums and causes crashes.

Current status:
- WinXclipse v0.4 is functional and suitable for release.
