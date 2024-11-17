/* Estilo básico para o corpo e a página */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    overflow: hidden; /* Para garantir que não haja barras de rolagem */
    background-color: #f4f4f4;
}

/* Estilo para o overlay da imagem do Batman como fundo */
#background-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('\myproject\frontend\images\batman-logo.jpg'); /* Caminho da imagem */
    background-size: cover; /* A imagem ocupa toda a tela */
    background-position: center; /* A imagem é centralizada */
    opacity: 0.1; /* A imagem terá 10% de opacidade (90% transparente) */
    z-index: -1; /* Coloca a imagem no fundo, atrás de outros conteúdos */
}

/* Estilo para o texto que aparece após 10 segundos */
#explore-text {
    display: none;
    text-align: center;
    margin-top: 20px;
}

/* Centralização do conteúdo */
.intro {
    margin-top: 50px;
}

.intro h1 {
    font-size: 2.5em;
    color: #333;
}

.intro p {
    font-size: 1.2em;
    color: #666;
}

/* Classe que torna o texto visível após 10 segundos */
.hidden {
    display: none;
}

.visible {
    display: block;
}
