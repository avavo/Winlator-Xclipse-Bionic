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
