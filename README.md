# Winlator Xclipse Bionic

Winlator Xclipse Bionic, ou WXB, é um projeto experimental focado em adaptar builds do Winlator/CMOD para dispositivos Samsung Exynos com GPU Xclipse.

## Status atual

- Versão: WXB v0.1
- Base: Winlator Cmod v13.1.1 oficial
- Package atual: `com.winlator.cmod`
- Nome visual atual: `Winlator WXB!`
- Método: patch binário seguro no APK oficial
- Status: abre e funciona

## Método da v0.1

A v0.1 usa o APK oficial funcional do Winlator Cmod v13.1.1 como base.

O patch altera apenas strings fora dos arquivos `classes*.dex`.

Isso é importante porque alterar diretamente arquivos DEX quebra o checksum interno e causa crash no Android.

Fluxo usado:

1. usar o APK oficial como base;
2. substituir `Winlator Cmod` por `Winlator WXB!`;
3. não alterar `classes*.dex`;
4. remover assinatura antiga;
5. aplicar `zipalign`;
6. assinar novamente.

## Objetivo

Criar uma base organizada para testes em Exynos/Xclipse, com foco futuro em presets, documentação, integração com MdiEx/ExynosTools e ajustes voltados para compatibilidade.

## Aviso

Projeto experimental. Nada aqui promete desempenho, estabilidade ou compatibilidade universal.

## Créditos

Baseado no trabalho do Winlator, Winlator CMOD e seus respectivos desenvolvedores/contribuidores.

## WinXclipse v0.5

A v0.5 adiciona a variante experimental Wrapper-LG, baseada no wrapper Leegao ETC2.

Essa versão mantém a base do Winlator Cmod v13.1.1 e usa patch binário seguro, sem alterar classes*.dex e sem recompilar resources via apktool.

### O que muda

- Wrapper-v2 foi substituído por Wrapper-LG no menu principal de Graphics Driver
- Wrapper-LG aponta para assets/graphics_driver/wrapper-lg.tzst
- wrapper-lg.tzst foi criado usando o wrapper.tzst original como base
- apenas usr/lib/libvulkan_wrapper.so foi trocado pelo wrapper Leegao ETC2
- a estrutura original do pacote foi mantida
- compressão usada: Zstandard

### Status

Experimental funcional.

A extração de graphics_driver/wrapper-lg.tzst foi validada sem erro de decompressão. Ainda precisa de testes maiores em containers, DXVK, Zink e jogos.

## WinXclipse v0.5

A v0.5 adiciona a variante experimental Wrapper-LG, baseada no wrapper Leegao ETC2.

Essa versão mantém a base do Winlator Cmod v13.1.1 e usa patch binário seguro, sem alterar classes*.dex e sem recompilar resources via apktool.

### O que muda

- Wrapper-v2 foi substituído por Wrapper-LG no menu principal de Graphics Driver
- Wrapper-LG aponta para assets/graphics_driver/wrapper-lg.tzst
- wrapper-lg.tzst foi criado usando o wrapper.tzst original como base
- apenas usr/lib/libvulkan_wrapper.so foi trocado pelo wrapper Leegao ETC2
- a estrutura original do pacote foi mantida
- compressão usada: Zstandard

### Status

Experimental funcional.

A extração de graphics_driver/wrapper-lg.tzst foi validada sem erro de decompressão. Ainda precisa de testes maiores em containers, DXVK, Zink e jogos.
