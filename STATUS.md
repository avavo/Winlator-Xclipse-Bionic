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

## WinXclipse v0.5 - Wrapper-LG

Status: experimental funcional.

Mudanças principais:

- Base: Winlator Cmod v13.1.1 oficial
- Nome visual: WinXclipse
- Package mantido: com.winlator.cmod
- Método: patch binário seguro, sem recompilar resources e sem alterar classes*.dex
- Menu principal Graphics Driver:
  - Wrapper
  - Wrapper-LG
- Wrapper-LG usa o Leegao ETC2 como libvulkan_wrapper.so
- O pacote foi montado usando o wrapper.tzst original como base
- Estrutura preservada:
  - usr/lib/libadrenotools.so
  - usr/lib/libfile_redirect_hook.so
  - usr/lib/libgsl_alloc_hook.so
  - usr/lib/libhook_impl.so
  - usr/lib/libmain_hook.so
  - usr/lib/libvulkan_wrapper.so
  - usr/share/vulkan/icd.d/wrapper_icd.aarch64.json
- Compressão correta: Zstandard
- Caminho final dentro do APK:
  - assets/graphics_driver/wrapper-lg.tzst

Validação:

- A opção Wrapper-LG aparece no menu Graphics Driver
- O app chama graphics_driver/wrapper-lg.tzst
- A extração não apresenta mais erro de decompressão/Unknown frame descriptor
- Ainda precisa de teste maior com jogos e apps Vulkan/DXVK

Observação:

Wrapper-LG substitui temporariamente Wrapper-v2 no menu, porque o build de resources via apktool/aapt2 está falhando com exit code 139. Essa solução evita rebuild de resources e mantém o patch mais seguro.

## WinXclipse v0.6 - MultiWrapper

Status: experimental funcional.

Mudanças principais:

- Base: Winlator Cmod v13.1.1
- Nome visual corrigido para WinXclipse
- Logo e About corrigidos
- Package mantido: com.winlator.cmod
- Menu principal Graphics Driver agora inclui múltiplos wrappers:
  - Wrapper
  - Wrapper-v2
  - Wrapper-LG
  - Wrapper-1E
  - Wrapper-2E
  - Wrapper-KI

Implementação:

- Lista do menu Graphics Driver expandida via smali
- Sem depender de rebuild limpo de resources via aapt2
- Build feito com apktool usando aapt1 após correção dos PNGs problemáticos
- Packs wrapper montados com base no wrapper.tzst original
- Estrutura preservada em todos os wrappers:
  - usr/lib/libadrenotools.so
  - usr/lib/libfile_redirect_hook.so
  - usr/lib/libgsl_alloc_hook.so
  - usr/lib/libhook_impl.so
  - usr/lib/libmain_hook.so
  - usr/lib/libvulkan_wrapper.so
  - usr/share/vulkan/icd.d/wrapper_icd.aarch64.json

Wrappers adicionados:

- Wrapper-LG -> assets/graphics_driver/wrapper-lg.tzst
- Wrapper-1E -> assets/graphics_driver/wrapper-1e.tzst
- Wrapper-2E -> assets/graphics_driver/wrapper-2e.tzst
- Wrapper-KI -> assets/graphics_driver/wrapper-ki.tzst

Validação:

- Wrapper-LG extraindo corretamente
- Wrapper-1E extraindo corretamente
- Wrapper-2E extraindo corretamente
- Wrapper-KI extraindo corretamente
- Sem erro de decompression/Unknown frame descriptor nos packs testados
- Ainda precisa de testes maiores em jogos, DXVK, Zink e runtime Vulkan

## WinXclipse v0.7 - Driver cleanup

Status: experimental funcional.

Mudanças principais:

- Drivers Snapdragon/Turnip ocultados do menu de versão de wrapper graphics driver
- Removidas do menu as entradas:
  - v762
  - v805
  - turnip25.1.0
  - turnip25.3.0_R3_Auto
  - turnip25.3.0_R3_Gmem
- MultiWrapper mantido
- Branding atualizado para WinXclipse v0.7
- Foco mantido em Exynos/Xclipse

Observação:

Nesta etapa os drivers foram ocultados/removidos do menu primeiro. A remoção definitiva dos arquivos .tzst antigos do APK deve ser feita apenas após validação completa.

## WinXclipse v0.7.5 - Identity update

Status: experimental funcional.

Mudanças principais:

- Renomeado Adrenotools GPU Drivers para Xclipse GPU Drivers
- Adicionado crédito WinXclipse patch/mod by avavo / Álvaro
- Créditos originais mantidos
- MultiWrapper mantido
- Branding WinXclipse preservado
- Foco reforçado em Exynos/Xclipse

## WinXclipse v0.8.0 - FEXCore runtime delivery

Status: experimental funcional.

- Repositório atualizado para WinXclipse
- FEXCore 2601-aabdded publicado via GitHub Release
- FEXCore 2605 publicado via GitHub Release
- assets/contents.json atualizado para baixar FEXCore pela release
- Download e instalação do FEXCore testados com sucesso
- Branding/ícones corrigidos após rebuild

## WinXclipse v0.8.0 - Runtime + Identity Base

Status: experimental funcional.

Mudanças principais:

- Package name alterado para com.win.xclipse
- WinXclipse agora pode ser instalado lado a lado com Cmod
- FEXCore 2601-aabdded adicionado via GitHub Release
- FEXCore 2605 adicionado via GitHub Release
- assets/contents.json atualizado para FEXCore remoto
- Download e instalação do FEXCore testados com sucesso
- Texto antigo de Qualcomm/Adreno removido da instalação de drivers
- Branding e logos corrigidos após rebuild
- Xclipse GPU Drivers mantido
