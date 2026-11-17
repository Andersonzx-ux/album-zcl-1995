# Zezé Di Camargo & Luciano — 1995 (player)

Player estático (HTML/CSS/JS, sem build) para GitHub Pages. Dados em `data/album.js`.

## Paleta (medida nos pixels da capa)
| Papel | Cor | Origem |
|---|---|---|
| night | `#1C0F13` | couro, calças e letras do nome |
| wine | `#391E1B` | rocha em sombra profunda |
| deep | `#884132` | rocha avermelhada em sombra |
| rock | `#C16848` | arenito (tom dominante) |
| bright | `#D18358` | arenito iluminado |
| sky | `#D6E0EF` | céu |
| denim | `#DAC9C6` | jeans claro |
| hill | `#B39480` | colinas ao fundo |

## Identidade
- **Progresso = o nome da capa**: as letras pretas "ZEZÉ DI CAMARGO & LUCIANO" ficam esmaecidas até a faixa passar por elas (máscara real das letras, `assets/nome-mask.webp`); linha-guia na cor do arenito. Clique/arraste no nome para buscar na faixa.
- **Dia / Noite**: Dia usa o céu da capa e texto no preto do couro; Noite usa couro e rocha em sombra com o arenito iluminado como destaque. A escolha fica salva.
- A divisória é a faixa de rocha do chão da capa (`assets/rocha.jpg`); o fundo da página é a capa desfocada.
- Fontes: Alfa Slab One (título "1995", lembra as letras da capa) e Jost (texto), ambas OFL em `assets/fonts/`.
- Central de mídia (Media Session) com capa, anterior/próxima e seek.

## Arquivos
`index.html`, `css/style.css`, `js/{app,player,ui}.js`, `data/album.js` (só ganhou o bloco `palette`), `assets/{cover.jpg, cover-1000.jpg, cover-640.jpg, cover-512.jpg, cover-256.jpg, nome-mask.webp, rocha.jpg, fonts/}`, `tools/` (scripts que geraram os recortes e mediram as cores).
`assets/zcl.png` e `assets/zclogo.png` não são mais usados.
