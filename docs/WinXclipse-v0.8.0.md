# WinXclipse v0.8.0 - Runtime + Identity Base

## Objetivo

Transformar o WinXclipse em um app mais independente da base Cmod, com package próprio e entrega inicial de runtime via GitHub Releases.

## Mudanças

- Package name alterado:
  - de \`com.winlator.cmod\`
  - para \`com.win.xclipse\`
- Instalação lado a lado com Cmod funcionando
- FEXCore 2601-aabdded e FEXCore 2605 publicados em GitHub Releases
- \`assets/contents.json\` atualizado para baixar FEXCore remoto
- Download e instalação do FEXCore testados com sucesso
- Textos de instalação de driver atualizados para WinXclipse/Xclipse
- Removidas menções antigas a Qualcomm/Adreno no aviso de instalação de driver
- Branding e logos corrigidos

## Package

\`\`\`txt
com.win.xclipse
\`\`\`

## FEXCore links

- https://github.com/avavo/WinXclipse/releases/download/runtime-fexcore-v0.8/FEXCore-2601-aabdded.wcp
- https://github.com/avavo/WinXclipse/releases/download/runtime-fexcore-v0.8/FEX-2605.wcp

## Status

Experimental funcional.

## Observação

Wine e Proton ainda não foram adicionados nesta versão. Eles devem entrar em uma etapa separada, pois exigem validação de estrutura, binPath, libPath e prefixPack.
