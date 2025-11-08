# RESULTADO DO BENCHMARK: ASSISTENTE DE CRIAÇÃO DE LANDING PAGE

Este arquivo documenta os resultados gerados por um modelo de IA para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico

**Prompt:** `Crie uma landing page.`

**Resultado:**

Com certeza! Eu posso gerar o código HTML e CSS para uma landing page. Para criar exatamente o que você precisa, me diga:

1.  **Qual é o objetivo da página?** (Vender um produto, capturar e-mails, promover um evento?)
2.  **Qual é o nome do seu produto/serviço?**
3.  **Quais seções a página deve ter?** (Ex: Cabeçalho, seção principal, recursos, depoimentos, rodapé)
4.  **Qual é a paleta de cores e o estilo visual** que você prefere? (Ex: minimalista, corporativo, vibrante)
5.  **Qual texto e quais imagens** devem ser incluídos?

Com esses detalhes, posso construir a página para você.

---

## 2. Resposta ao Prompt Estruturado (JSON)

**Prompt:**
```json
{
  "task": "gerar_codigo_html_css_para_landing_page",
  "context": {
    "background": "Uma startup está lançando um novo aplicativo de meditação e precisa de uma landing page para capturar leads.",
    "user_goal": "Gerar o código HTML e CSS para uma landing page simples, moderna e responsiva."
  },
  "instructions": {
    "sections": [
      {"name": "Header", "content": "Logo à esquerda, menu de navegação ('Sobre', 'Recursos', 'Preços') à direita."},
      {"name": "Hero", "content": "Título chamativo, subtítulo explicando o app, e um botão de CTA ('Baixe Grátis')."},
      {"name": "Recursos", "content": "Seção com 3 colunas, cada uma com um ícone, título e breve descrição de um recurso do app."},
      {"name": "Depoimentos", "content": "Uma seção com 2 ou 3 cards de depoimentos de usuários."},
      {"name": "Footer", "content": "Links para redes sociais e informações de contato."}
    ],
    "output_format": "Um único arquivo HTML com o CSS incorporado na tag `<style>`."
  },
  "constraints": [
    "O design deve ser limpo e minimalista, usando uma paleta de cores de azul e branco.",
    "A página deve ser responsiva e funcionar bem em desktops e dispositivos móveis.",
    "Usar fontes do Google Fonts (ex: 'Lato' para corpo e 'Montserrat' for títulos)."
  ],
  "user_input": "App 'ZenMind'. Foco em simplicidade e bem-estar."
}
```

**Resultado:**

**Código HTML com CSS incorporado:**
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZenMind - Sua Pausa para o Bem-Estar</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Montserrat:wght@700&display=swap');

        :root {
            --primary-color: #2a7a9f;
            --secondary-color: #f4f4f4;
            --text-color: #333;
            --light-text: #fff;
        }

        body {
            font-family: 'Lato', sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
            color: var(--text-color);
        }

        .container {
            max-width: 1100px;
            margin: auto;
            padding: 0 20px;
            overflow: hidden;
        }

        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
            color: var(--primary-color);
        }

        /* Header */
        .main-header {
            background: #fff;
            padding: 1rem 0;
            border-bottom: 1px solid #ddd;
        }

        .main-header .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .main-header .logo {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.5rem;
            color: var(--primary-color);
            text-decoration: none;
        }

        .main-nav ul {
            display: flex;
            list-style: none;
            padding: 0;
        }

        .main-nav a {
            color: var(--text-color);
            text-decoration: none;
            margin-left: 20px;
            font-weight: 700;
        }

        /* Hero Section */
        .hero {
            background: var(--secondary-color);
            text-align: center;
            padding: 4rem 0;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto 2rem auto;
        }

        .cta-button {
            display: inline-block;
            background: var(--primary-color);
            color: var(--light-text);
            padding: 1rem 2rem;
            border-radius: 5px;
            text-decoration: none;
            font-weight: 700;
            font-family: 'Montserrat', sans-serif;
        }

        /* Recursos Section */
        .recursos {
            padding: 4rem 0;
            text-align: center;
        }

        .recursos-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin-top: 2rem;
        }

        .recurso-item {
            background: #fff;
            padding: 2rem;
        }
        
        .recurso-item .icon {
            font-size: 3rem;
            color: var(--primary-color);
        }

        /* Depoimentos Section */
        .depoimentos {
            background: var(--secondary-color);
            padding: 4rem 0;
            text-align: center;
        }

        .depoimentos-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
            margin-top: 2rem;
        }

        .depoimento-card {
            background: #fff;
            padding: 2rem;
            border-radius: 5px;
            text-align: left;
        }

        .depoimento-card p {
            font-style: italic;
        }

        .depoimento-card .author {
            font-weight: 700;
            margin-top: 1rem;
            text-align: right;
        }

        /* Footer */
        .main-footer {
            background: var(--primary-color);
            color: var(--light-text);
            text-align: center;
            padding: 2rem 0;
        }

        .social-links a {
            color: var(--light-text);
            text-decoration: none;
            margin: 0 10px;
            font-size: 1.5rem;
        }

        /* Responsividade */
        @media (max-width: 768px) {
            .main-header .container {
                flex-direction: column;
            }
            .main-nav ul {
                margin-top: 1rem;
            }
            .recursos-grid, .depoimentos-grid {
                grid-template-columns: 1fr;
            }
            .hero h1 {
                font-size: 2.5rem;
            }
        }
    </style>
</head>
<body>

    <header class="main-header">
        <div class="container">
            <a href="#" class="logo">ZenMind</a>
            <nav class="main-nav">
                <ul>
                    <li><a href="#sobre">Sobre</a></li>
                    <li><a href="#recursos">Recursos</a></li>
                    <li><a href="#precos">Preços</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <h1>Encontre sua calma interior.</h1>
            <p>ZenMind é o seu guia pessoal para a meditação e o bem-estar, ajudando você a encontrar um momento de paz no seu dia a dia agitado.</p>
            <a href="#" class="cta-button">Baixe Grátis</a>
        </div>
    </section>

    <section id="recursos" class="recursos">
        <div class="container">
            <h2>Recursos para uma vida mais leve</h2>
            <div class="recursos-grid">
                <div class="recurso-item">
                    <div class="icon">🧘</div>
                    <h3>Meditações Guiadas</h3>
                    <p>Sessões para todos os níveis, do iniciante ao avançado, focadas em ansiedade, foco e sono.</p>
                </div>
                <div class="recurso-item">
                    <div class="icon">🎵</div>
                    <h3>Paisagens Sonoras</h3>
                    <p>Sons relaxantes da natureza e músicas tranquilas para ajudar você a se concentrar ou a dormir melhor.</p>
                </div>
                <div class="recurso-item">
                    <div class="icon">📊</div>
                    <h3>Acompanhe seu Progresso</h3>
                    <p>Veja sua evolução e mantenha a motivação com nosso sistema de acompanhamento de sessões.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="depoimentos" class="depoimentos">
        <div class="container">
            <h2>O que nossos usuários dizem</h2>
            <div class="depoimentos-grid">
                <div class="depoimento-card">
                    <p>"O ZenMind mudou minhas manhãs. Começo o dia com muito mais calma e foco. Recomendo a todos!"</p>
                    <div class="author">- Ana P.</div>
                </div>
                <div class="depoimento-card">
                    <p>"Finalmente um app de meditação que é simples e direto ao ponto. As paisagens sonoras são incríveis para trabalhar."</p>
                    <div class="author">- Carlos M.</div>
                </div>
            </div>
        </div>
    </section>

    <footer id="contato" class="main-footer">
        <div class="container">
            <p>ZenMind - Todos os direitos reservados &copy; 2025</p>
            <div class="social-links">
                <a href="#">Instagram</a>
                <a href="#">Facebook</a>
                <a href="#">Twitter</a>
            </div>
        </div>
    </footer>

</body>
</html>
```

---

## 3. Resposta ao Prompt Estruturado (KERNEL)

**Prompt:**
- **K (Keep it simple):** Gerar o código HTML e CSS para uma landing page de um aplicativo de meditação.
- **E (Easy to verify):** O código deve renderizar uma página com 5 seções (Header, Hero, Recursos, Depoimentos, Footer) e ser responsivo.
- **R (Reproducible results):** O prompt descreve a estrutura da página de forma clara.
- **N (Narrow scope):** A tarefa é focada apenas na geração do código front-end da página.
- **E (Explicit constraints):** Design limpo, paleta azul/branco, responsivo, CSS incorporado, fontes do Google.
- **L (Logical structure):**
    1.  **Task:** Gerar o código HTML e CSS para uma landing page responsiva.
    2.  **Input:** App 'ZenMind', 5 seções estruturadas, foco em simplicidade.
    3.  **Constraints:** Design minimalista, paleta de cores azul/branco, CSS in-file, responsividade.
    4.  **Output:** Arquivo HTML único com CSS incorporado.
    5.  **Verify:** Abrir o arquivo HTML em um navegador, verificar se todas as seções estão presentes e se o layout se adapta a diferentes tamanhos de tela.

**Resultado:**

**Código HTML com CSS incorporado:**
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZenMind | Meditação e Simplicidade</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">
    <style>
        /* Reset e Configurações Globais */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Lato', sans-serif;
            background-color: #ffffff;
            color: #333;
        }
        .wrapper {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
        }
        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
            color: #0D47A1; /* Azul escuro */
        }
        section {
            padding: 60px 0;
        }

        /* Header */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
            border-bottom: 1px solid #e0e0e0;
        }
        .header .logo {
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            font-size: 24px;
            color: #0D47A1;
            text-decoration: none;
        }
        .header-nav a {
            margin-left: 25px;
            text-decoration: none;
            color: #333;
            font-weight: 700;
        }

        /* Hero */
        .hero-section {
            text-align: center;
            padding: 80px 0;
            background-color: #E3F2FD; /* Azul claro */
        }
        .hero-section h1 {
            font-size: 48px;
        }
        .hero-section p {
            font-size: 18px;
            max-width: 600px;
            margin: 20px auto 30px;
        }
        .hero-section .cta-button {
            background-color: #1976D2; /* Azul primário */
            color: #fff;
            padding: 15px 30px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: 700;
            font-family: 'Montserrat', sans-serif;
        }

        /* Recursos */
        .recursos-section {
            text-align: center;
        }
        .recursos-section h2 {
            margin-bottom: 40px;
        }
        .recursos-container {
            display: flex;
            justify-content: space-around;
            gap: 30px;
        }
        .recurso {
            flex-basis: 30%;
        }
        .recurso h3 {
            margin: 15px 0;
        }

        /* Depoimentos */
        .depoimentos-section {
            background-color: #E3F2FD;
            text-align: center;
        }
        .depoimentos-section h2 {
            margin-bottom: 40px;
        }
        .depoimentos-container {
            display: flex;
            gap: 30px;
        }
        .depoimento {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            flex-basis: 50%;
        }
        .depoimento p {
            font-style: italic;
        }
        .depoimento .author {
            margin-top: 10px;
            font-weight: 700;
            text-align: right;
        }

        /* Footer */
        .footer {
            background-color: #0D47A1;
            color: #fff;
            text-align: center;
            padding: 40px 0;
        }
        .footer .social-media a {
            color: #fff;
            margin: 0 15px;
            text-decoration: none;
        }
        .footer p {
            margin-bottom: 15px;
        }

        /* Media Queries para Responsividade */
        @media (max-width: 768px) {
            .header {
                flex-direction: column;
            }
            .header-nav {
                margin-top: 15px;
            }
            .recursos-container, .depoimentos-container {
                flex-direction: column;
            }
            .hero-section h1 {
                font-size: 36px;
            }
        }
    </style>
</head>
<body>
    <header class="header wrapper">
        <a href="#" class="logo">ZenMind</a>
        <nav class="header-nav">
            <a href="#sobre">Sobre</a>
            <a href="#recursos">Recursos</a>
            <a href="#precos">Preços</a>
        </nav>
    </header>

    <main>
        <section class="hero-section">
            <div class="wrapper">
                <h1>Respire Fundo, Viva o Momento</h1>
                <p>ZenMind é o seu refúgio digital para meditação e mindfulness. Encontre a paz interior com nossas sessões guiadas e sons relaxantes.</p>
                <a href="#" class="cta-button">Baixe Grátis</a>
            </div>
        </section>

        <section id="recursos" class="recursos-section wrapper">
            <h2>Ferramentas para seu Bem-Estar</h2>
            <div class="recursos-container">
                <div class="recurso">
                    <h3>Meditações Guiadas</h3>
                    <p>Nossas meditações são perfeitas para iniciantes e ajudam a reduzir a ansiedade e o estresse.</p>
                </div>
                <div class="recurso">
                    <h3>Sons da Natureza</h3>
                    <p>Durma melhor ou se concentre no trabalho com nossa biblioteca de sons relaxantes de alta qualidade.</p>
                </div>
                <div class="recurso">
                    <h3>Exercícios de Respiração</h3>
                    <p>Aprenda técnicas de respiração simples para acalmar sua mente e corpo em poucos minutos.</p>
                </div>
            </div>
        </section>

        <section id="depoimentos" class="depoimentos-section">
            <div class="wrapper">
                <h2>Amado por Mentes Tranquilas</h2>
                <div class="depoimentos-container">
                    <div class="depoimento">
                        <p>"Uso todos os dias antes de dormir. A qualidade do meu sono melhorou drasticamente."</p>
                        <p class="author">- Julia S.</p>
                    </div>
                    <div class="depoimento">
                        <p>"O ZenMind me ajuda a manter o foco durante o home office. Os sons de chuva são os melhores!"</p>
                        <p class="author">- Marcos L.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer id="contato" class="footer">
        <div class="wrapper">
            <p>Contato: contato@zenmind.app</p>
            <div class="social-media">
                <a href="#">Instagram</a>
                <a href="#">Facebook</a>
            </div>
        </div>
    </footer>
</body>
</html>
```
