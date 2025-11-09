# RESULTADO DO BENCHMARK (SIMULADO GPT): ASSISTENTE DE CRIAÇÃO DE LANDING PAGE

Este arquivo documenta os resultados simulados de um modelo GPT para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico (Simulação GPT)

**Prompt:** `Crie uma landing page.`

**Resultado Simulado GPT:**

Com certeza! Posso te ajudar a criar uma landing page eficaz. Para que o resultado seja exatamente o que você precisa, por favor, me forneça mais detalhes:

1.  **Qual é o objetivo principal** desta landing page? (Ex: Capturar leads, vender um produto, promover um evento, download de um e-book)
2.  **Qual é o produto/serviço/oferta** que será promovido?
3.  **Quem é o público-alvo** que você deseja atrair?
4.  **Quais informações essenciais** devem estar na página? (Ex: Título, subtítulo, benefícios, depoimentos, formulário de contato)
5.  **Qual o estilo visual desejado?** (Ex: Minimalista, vibrante, corporativo, cores preferidas)
6.  **Existe algum texto ou imagem específica** que você já tenha em mente?

Com essas informações, posso gerar o código HTML e CSS para uma landing page personalizada!

---

## 2. Resposta ao Prompt Estruturado (JSON) (Simulação GPT)

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

**Resultado Simulado GPT:**

**Código HTML com CSS incorporado:**
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZenMind - Meditação e Bem-Estar</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&family=Montserrat:wght@600;700&display=swap" rel="stylesheet">
    <style>
        /* Reset Básico */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Lato', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f8f8; /* Quase branco */
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 20px;
        }

        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
            color: #2196F3; /* Azul primário */
            margin-bottom: 15px;
        }

        a {
            text-decoration: none;
            color: #2196F3;
        }

        /* Header */
        .header {
            background: #ffffff;
            padding: 15px 0;
            border-bottom: 1px solid #eee;
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 28px;
            font-weight: 700;
            color: #2196F3;
        }

        .nav ul {
            list-style: none;
            display: flex;
        }

        .nav ul li {
            margin-left: 25px;
        }

        .nav ul li a {
            font-weight: 600;
            color: #555;
            transition: color 0.3s ease;
        }

        .nav ul li a:hover {
            color: #2196F3;
        }

        /* Hero Section */
        .hero {
            background: #E3F2FD; /* Azul claro */
            text-align: center;
            padding: 80px 0;
        }

        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
            color: #1976D2; /* Azul mais escuro */
        }

        .hero p {
            font-size: 18px;
            max-width: 700px;
            margin: 0 auto 30px auto;
        }

        .btn-primary {
            display: inline-block;
            background: #2196F3;
            color: #fff;
            padding: 15px 30px;
            border-radius: 5px;
            font-weight: 700;
            font-family: 'Montserrat', sans-serif;
            transition: background-color 0.3s ease;
        }

        .btn-primary:hover {
            background-color: #1976D2;
        }

        /* Recursos Section */
        .features {
            padding: 60px 0;
            text-align: center;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin-top: 40px;
        }

        .feature-item {
            background: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .feature-item .icon {
            font-size: 40px;
            color: #2196F3;
            margin-bottom: 15px;
        }

        /* Depoimentos Section */
        .testimonials {
            background: #E3F2FD;
            padding: 60px 0;
            text-align: center;
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
            margin-top: 40px;
        }

        .testimonial-card {
            background: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            text-align: left;
        }

        .testimonial-card p {
            font-style: italic;
            margin-bottom: 15px;
        }

        .testimonial-card .author {
            font-weight: 700;
            color: #555;
            text-align: right;
        }

        /* Footer */
        .footer {
            background: #1976D2; /* Azul mais escuro */
            color: #fff;
            text-align: center;
            padding: 40px 0;
        }

        .footer .social-links a {
            color: #fff;
            margin: 0 10px;
            font-size: 24px;
            transition: color 0.3s ease;
        }

        .footer .social-links a:hover {
            color: #E3F2FD;
        }

        /* Responsividade */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
            }
            .nav ul {
                margin-top: 20px;
                flex-direction: column;
                align-items: center;
            }
            .nav ul li {
                margin: 10px 0;
            }
            .hero h1 {
                font-size: 36px;
            }
            .features-grid, .testimonials-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

    <header class="header">
        <div class="container header-content">
            <a href="#" class="logo">ZenMind</a>
            <nav class="nav">
                <ul>
                    <li><a href="#about">Sobre</a></li>
                    <li><a href="#features">Recursos</a></li>
                    <li><a href="#pricing">Preços</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <h1>Sua Jornada para a Calma Começa Aqui.</h1>
            <p>ZenMind é o aplicativo de meditação e mindfulness que te ajuda a encontrar equilíbrio e paz no dia a dia, com sessões guiadas e sons relaxantes.</p>
            <a href="#" class="btn-primary">Baixe Grátis</a>
        </div>
    </section>

    <section id="features" class="features">
        <div class="container">
            <h2>Recursos que Transformam seu Dia</h2>
            <div class="features-grid">
                <div class="feature-item">
                    <div class="icon">🧘</div>
                    <h3>Meditações Guiadas</h3>
                    <p>Sessões para todos os níveis, focadas em reduzir o estresse, melhorar o sono e aumentar o foco.</p>
                </div>
                <div class="feature-item">
                    <div class="icon">🎶</div>
                    <h3>Sons da Natureza</h3>
                    <p>Coleção de sons ambientes para relaxar, meditar ou criar um ambiente de trabalho tranquilo.</p>
                </div>
                <div class="feature-item">
                    <div class="icon">📈</div>
                    <h3>Acompanhamento de Progresso</h3>
                    <p>Monitore suas sessões, veja seu avanço e mantenha-se motivado em sua prática diária.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="testimonials" class="testimonials">
        <div class="container">
            <h2>O que nossos usuários estão dizendo</h2>
            <div class="testimonials-grid">
                <div class="testimonial-card">
                    <p>"ZenMind se tornou parte essencial da minha rotina matinal. Sinto-me mais centrado e produtivo."</p>
                    <div class="author">- Sofia L.</div>
                </div>
                <div class="testimonial-card">
                    <p>"A variedade de meditações é incrível, e os sons para dormir realmente funcionam. Recomendo!"</p>
                    <div class="author">- Pedro G.</div>
                </div>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 ZenMind. Todos os direitos reservados.</p>
            <div class="social-links">
                <a href="#">Facebook</a>
                <a href="#">Instagram</a>
                <a href="#">Twitter</a>
            </div>
        </div>
    </footer>

</body>
</html>
```

---

## 3. Resposta ao Prompt Estruturado (KERNEL) (Simulação GPT)

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

**Resultado Simulado GPT:**

**Código HTML com CSS incorporado:**
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZenMind App - Encontre seu Equilíbrio</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <style>
        /* Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Open Sans', sans-serif;
            line-height: 1.6;
            color: #444;
            background-color: #f0f4f8; /* Light blue-gray */
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
            color: #007bff; /* Primary blue */
        }

        a {
            text-decoration: none;
            color: #007bff;
        }

        /* Header */
        .app-header {
            background: #ffffff;
            padding: 15px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .app-logo {
            font-size: 26px;
            font-weight: 700;
            color: #007bff;
        }

        .main-nav ul {
            list-style: none;
            display: flex;
        }

        .main-nav ul li {
            margin-left: 30px;
        }

        .main-nav ul li a {
            font-weight: 600;
            color: #555;
            transition: color 0.3s ease;
        }

        .main-nav ul li a:hover {
            color: #007bff;
        }

        /* Hero Section */
        .hero-section {
            background: #e9f2fa; /* Lighter blue */
            text-align: center;
            padding: 100px 0;
        }

        .hero-section h1 {
            font-size: 52px;
            margin-bottom: 25px;
            color: #0056b3; /* Darker blue */
        }

        .hero-section p {
            font-size: 19px;
            max-width: 800px;
            margin: 0 auto 40px auto;
        }

        .btn-download {
            display: inline-block;
            background: #007bff;
            color: #fff;
            padding: 18px 35px;
            border-radius: 8px;
            font-weight: 700;
            font-family: 'Montserrat', sans-serif;
            font-size: 18px;
            transition: background-color 0.3s ease;
        }

        .btn-download:hover {
            background-color: #0056b3;
        }

        /* Features Section */
        .features-section {
            padding: 80px 0;
            text-align: center;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 40px;
            margin-top: 50px;
        }

        .feature-card {
            background: #ffffff;
            padding: 35px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }

        .feature-card .icon {
            font-size: 45px;
            color: #007bff;
            margin-bottom: 20px;
        }

        /* Testimonials Section */
        .testimonials-section {
            background: #e9f2fa;
            padding: 80px 0;
            text-align: center;
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 40px;
            margin-top: 50px;
        }

        .testimonial-card {
            background: #ffffff;
            padding: 35px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            text-align: left;
        }

        .testimonial-card p {
            font-style: italic;
            margin-bottom: 20px;
            font-size: 17px;
        }

        .testimonial-card .client-name {
            font-weight: 700;
            color: #555;
            text-align: right;
        }

        /* Footer */
        .app-footer {
            background: #0056b3; /* Darker blue */
            color: #fff;
            text-align: center;
            padding: 50px 0;
        }

        .app-footer .social-media a {
            color: #fff;
            margin: 0 15px;
            font-size: 26px;
            transition: color 0.3s ease;
        }

        .app-footer .social-media a:hover {
            color: #e9f2fa;
        }

        /* Responsive Design */
        @media (max-width: 992px) {
            .hero-section h1 {
                font-size: 42px;
            }
            .features-grid, .testimonials-grid {
                grid-template-columns: 1fr;
            }
            .main-nav ul {
                flex-direction: column;
                margin-top: 20px;
            }
            .main-nav ul li {
                margin: 10px 0;
            }
            .header-content {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>

    <header class="app-header">
        <div class="container header-content">
            <a href="#" class="app-logo">ZenMind</a>
            <nav class="main-nav">
                <ul>
                    <li><a href="#about">Sobre</a></li>
                    <li><a href="#features">Recursos</a></li>
                    <li><a href="#pricing">Preços</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="hero-section">
        <div class="container">
            <h1>Encontre a Paz Interior com ZenMind.</h1>
            <p>Nosso aplicativo de meditação e mindfulness é seu guia diário para reduzir o estresse, melhorar o foco e dormir melhor. Comece sua jornada para um bem-estar duradouro.</p>
            <a href="#" class="btn-download">Baixe Grátis Agora</a>
        </div>
    </section>

    <section id="features" class="features-section">
        <div class="container">
            <h2>Recursos Essenciais para o Seu Bem-Estar</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="icon">🧘</div>
                    <h3>Meditações Guiadas</h3>
                    <p>Centenas de sessões para todos os níveis, focadas em ansiedade, sono, gratidão e muito mais.</p>
                </div>
                <div class="feature-card">
                    <div class="icon">🎵</div>
                    <h3>Sons Relaxantes</h3>
                    <p>Coleção de paisagens sonoras e músicas para meditar, relaxar ou criar um ambiente tranquilo.</p>
                </div>
                <div class="feature-card">
                    <div class="icon">📊</div>
                    <h3>Acompanhe seu Progresso</h3>
                    <p>Monitore suas sessões, veja suas estatísticas e celebre suas conquistas na jornada mindfulness.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="testimonials" class="testimonials-section">
        <div class="container">
            <h2>O que Nossos Usuários Dizem</h2>
            <div class="testimonials-grid">
                <div class="testimonial-card">
                    <p>"ZenMind transformou minhas manhãs. Sinto-me mais calma e preparada para o dia. É um presente!"</p>
                    <div class="client-name">- Ana C.</div>
                </div>
                <div class="testimonial-card">
                    <p>"Finalmente um app de meditação que consigo usar. As meditações para dormir são incríveis."</p>
                    <div class="client-name">- Lucas M.</div>
                </div>
            </div>
        </div>
    </section>

    <footer class="app-footer">
        <div class="container">
            <p>&copy; 2025 ZenMind App. Todos os direitos reservados.</p>
            <div class="social-media">
                <a href="#">Facebook</a>
                <a href="#">Instagram</a>
                <a href="#">Twitter</a>
            </div>
        </div>
    </footer>

</body>
</html>
```
