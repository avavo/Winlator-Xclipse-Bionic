# WinXclipse v0.6 - MultiWrapper

## Base

- Winlator Cmod v13.1.1
- Package mantido: com.winlator.cmod
- Nome visual: WinXclipse

## Objetivo

Adicionar múltiplos wrappers Vulkan em um único APK, diretamente no menu principal de Graphics Driver.

## Menu

A v0.6 adiciona:

- Wrapper-LG
- Wrapper-1E
- Wrapper-2E
- Wrapper-KI

Mantém:

- Wrapper
- Wrapper-v2

## Assets

- Wrapper-LG -> assets/graphics_driver/wrapper-lg.tzst
- Wrapper-1E -> assets/graphics_driver/wrapper-1e.tzst
- Wrapper-2E -> assets/graphics_driver/wrapper-2e.tzst
- Wrapper-KI -> assets/graphics_driver/wrapper-ki.tzst

## Estrutura dos packs

Todos os packs mantêm a estrutura do wrapper original:

```txt
usr/
usr/lib/
usr/lib/libadrenotools.so
usr/lib/libfile_redirect_hook.so
usr/lib/libgsl_alloc_hook.so
usr/lib/libhook_impl.so
usr/lib/libmain_hook.so
usr/lib/libvulkan_wrapper.so
usr/share/
usr/share/vulkan/
usr/share/vulkan/icd.d/
usr/share/vulkan/icd.d/wrapper_icd.aarch64.json
```

## Validação

Confirmado via logcat:

- graphics_driver/wrapper-lg.tzst
- graphics_driver/wrapper-1e.tzst
- graphics_driver/wrapper-2e.tzst
- graphics_driver/wrapper-ki.tzst

Os packs não apresentaram erro de decompression/Unknown frame descriptor durante a extração.

## Status

Experimental funcional.

Ainda precisa de validação maior em jogos e workloads Vulkan reais.
