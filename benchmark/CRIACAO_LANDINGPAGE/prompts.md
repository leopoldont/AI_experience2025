# PROMPTS PARA ASSISTENTE DE CRIAÇÃO DE LANDING PAGE

---

## 1. Prompt Genérico

Crie uma landing page.

---

## 2. Prompt Estruturado (JSON)

```json
{
  "task": "gerar_codigo_html_css_para_landing_page",
  "context": {
    "background": "Uma startup está lançando um novo aplicativo de meditação e precisa de uma landing page para capturar leads.",
    "user_goal": "Gerar o código HTML e CSS para uma landing page simples, moderna e responsiva."
  },
  "instructions": {
    "sections": [
      {
        "name": "Header",
        "content": "Logo à esquerda, menu de navegação ('Sobre', 'Recursos', 'Preços') à direita."
      },
      {
        "name": "Hero",
        "content": "Título chamativo, subtítulo explicando o app, e um botão de CTA ('Baixe Grátis')."
      },
      {
        "name": "Recursos",
        "content": "Seção com 3 colunas, cada uma com um ícone, título e breve descrição de um recurso do app."
      },
      {
        "name": "Depoimentos",
        "content": "Uma seção com 2 ou 3 cards de depoimentos de usuários."
      },
      {
        "name": "Footer",
        "content": "Links para redes sociais e informações de contato."
      }
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

---

## 3. Prompt Estruturado (KERNEL)

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
