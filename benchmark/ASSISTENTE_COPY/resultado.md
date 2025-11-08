# RESULTADO DO BENCHMARK: ASSISTENTE DE COPYWRITING

Este arquivo documenta os resultados gerados por um modelo de IA para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico

**Prompt:** `Escreva uma copy para meu anúncio.`

**Resultado:**

Eu adoraria ajudar a criar uma copy incrível para o seu anúncio! Para ser o mais persuasivo possível, preciso de alguns detalhes:

1.  **O que você está anunciando?** (Um produto, serviço, evento, etc.)
2.  **Para quem é este anúncio?** (Qual é o seu público-alvo?)
3.  **Onde o anúncio será veiculado?** (Instagram, Facebook, Google Ads, outdoor, etc.)
4.  **Qual é o principal benefício ou diferencial** do que você está oferecendo?
5.  **Qual ação você quer que as pessoas tomem** depois de ver o anúncio? (Ex: "Comprar agora", "Saber mais", "Inscrever-se")

Com essas respostas, posso criar uma copy que realmente gera resultados!

---

## 2. Resposta ao Prompt Estruturado (JSON)

**Prompt:**
```json
{
  "task": "criar_copy_para_anuncio",
  "context": {
    "background": "A campanha é para o lançamento de um novo curso online de fotografia para iniciantes.",
    "user_goal": "Gerar uma copy persuasiva para um anúncio no Instagram, com foco em conversão."
  },
  "instructions": {
    "steps": [
      "Escrever uma headline que chame a atenção em menos de 10 palavras.",
      "Desenvolver um corpo de texto que destaque os 3 principais benefícios do curso.",
      "Criar uma chamada para ação (CTA) clara e direta para 'inscreva-se agora'.",
      "Incluir 3 hashtags relevantes."
    ],
    "output_format": "Texto curto e direto, ideal para feed do Instagram, com quebras de linha para facilitar a leitura."
  },
  "constraints": [
    "O texto completo não deve ultrapassar 150 palavras.",
    "Usar uma linguagem energética e motivacional.",
    "Evitar promessas exageradas."
  ],
  "user_input": "O curso ensina a usar qualquer câmera, até mesmo a do celular."
}
```

**Resultado:**

**Headline:** Desbloqueie seu olhar de fotógrafo hoje!

**Corpo:**
Sua câmera do celular ou aquela câmera guardada na gaveta têm um poder que você nem imagina! ✨

Com nosso curso de fotografia para iniciantes, você vai:

📸 Dominar os fundamentos da fotografia, sem complicação.
📱 Aprender a tirar fotos incríveis com QUALQUER equipamento.
🚀 Transformar seus registros comuns em imagens espetaculares.

Chega de fotos sem graça! É hora de capturar o mundo com a sua visão.

**CTA:**
Inscreva-se agora e comece sua jornada!

**Hashtags:**
#CursoDeFotografia #FotografiaParaIniciantes #AprendaFotografia

---

## 3. Resposta ao Prompt Estruturado (KERNEL)

**Prompt:**
- **K (Keep it simple):** Criar a copy para um anúncio de Instagram de um curso de fotografia.
- **E (Easy to verify):** A copy deve ter menos de 150 palavras, uma headline, 3 benefícios, um CTA e 3 hashtags.
- **R (Reproducible results):** O prompt é autocontido e não depende de dados externos voláteis.
- **N (Narrow scope):** A tarefa é focada apenas na criação da copy do anúncio.
- **E (Explicit constraints):** Limite de 150 palavras, linguagem energética, sem promessas exageradas.
- **L (Logical structure):**
    1.  **Task:** Gerar uma copy persuasiva para um anúncio no Instagram.
    2.  **Input:** Lançamento de um curso online de fotografia para iniciantes.
    3.  **Constraints:** Máximo de 150 palavras. Linguagem motivacional. CTA para 'inscreva-se agora'.
    4.  **Output:** Texto curto para Instagram com headline, 3 benefícios, CTA e 3 hashtags.
    5.  **Verify:** Conferir o limite de palavras, a estrutura e a presença de todos os elementos solicitados.

**Resultado:**

**Headline:** Transforme suas fotos comuns em extraordinárias.

**Corpo:**
Você ama fotografar, mas sente que suas fotos poderiam ser melhores? Nosso curso foi feito para você!

Liberte seu potencial e aprenda a:
1.  Entender a luz e a composição para criar imagens impactantes.
2.  Usar os recursos da sua câmera (até a do celular!) como um profissional.
3.  Editar suas fotos de forma rápida e com resultados surpreendentes.

Dê vida às suas ideias e comece a criar as fotos que você sempre sonhou! A jornada para se tornar um fotógrafo confiante começa aqui.

**CTA:**
Inscreva-se agora e veja a diferença no seu primeiro clique!

**Hashtags:**
#FotografiaIniciante #CursoDeFoto #DomineSuaCamera
