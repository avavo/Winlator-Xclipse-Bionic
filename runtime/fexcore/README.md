# FEXCore runtime packages

Pacotes FEXCore em formato `.wcp` para uso no WinXclipse.

## Pacotes

- `FEX-2605.wcp`
- `FEXCore-2601-aabdded.wcp`

## Estrutura esperada

Cada pacote contém:

```txt
profile.json
system32/libarm64ecfex.dll
system32/libwow64fex.dll

Depois aperta `Ctrl+D`.

## 3. Commitar os pacotes

Como eles são pequenos, 923 KB e 1,3 MB, dá pra colocar no repo sem cometer crime contra o Git. Se fossem 200 MB, aí eu chamava a polícia do versionamento.

```fish
git add runtime/fexcore
git commit -m "Add FEXCore runtime packages"
git pull --rebase origin main
git push -u origin main

