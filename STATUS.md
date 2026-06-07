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
