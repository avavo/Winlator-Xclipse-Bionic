# WinXclipse v0.4

Base: **Winlator Cmod v13.1.1 oficial**

Esta versão continua usando patch binário seguro sobre o APK oficial do CMOD, preservando todos os arquivos `classes*.dex` para evitar erros de checksum e crashes no Android.

## Mudanças

- Nome visual ajustado para **WinXclipse**
- Ícone WinXclipse aplicado
- Versão visual ajustada para **Version WinX-v0.4**
- Scripts de patch/build v0.4 adicionados
- Método seguro mantido, sem modificar `classes*.dex`

## Validação

Testado no dispositivo:

- Criação de container: OK
- Abertura de container: OK
- Persistência do container após fechar e abrir o app: OK

## Notas conhecidas

- O package ainda é `com.winlator.cmod`
- O cabeçalho principal ainda pode mostrar `Winlator Cmod`
- Alguns créditos originais permanecem porque estão dentro de `classes*.dex`
- Android pode mostrar avisos de app feito para versão antiga, app depurável ou compatibilidade 16 KB, herdados da base CMOD

## Aviso

Projeto experimental.  
Não há promessa de ganho de desempenho, compatibilidade universal ou estabilidade garantida.
