# RESULTADO DO BENCHMARK (SIMULADO GPT): ASSISTENTE DE COPYWRITING

Este arquivo documenta os resultados simulados de um modelo GPT para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico (Simulação GPT)

**Prompt:** `Escreva uma copy para meu anúncio.`

**Resultado Simulado GPT:**

Absolutamente! Para criar uma copy de anúncio que realmente capture a atenção e gere resultados, preciso de um pouco mais de informação para afinar a mensagem.

Por favor, me diga:

1.  **Qual produto ou serviço** você está anunciando?
2.  **Quem é o seu público-alvo?** (Idade, interesses, problemas que seu produto resolve)
3.  **Qual é o principal benefício ou a emoção** que você quer despertar?
4.  **Onde este anúncio será veiculado?** (Instagram, Facebook, Google Ads, revista, etc.)
5.  **Qual ação você deseja que o público tome** após ver o anúncio? (Comprar, visitar o site, ligar, inscrever-se)

Com esses detalhes, posso te ajudar a criar uma copy irresistível!

---

## 2. Resposta ao Prompt Estruturado (JSON) (Simulação GPT)

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

**Resultado Simulado GPT:**

**Headline:** Sua paixão por fotos começa aqui!

**Corpo:**
Cansado de fotos sem vida? 📸 Transforme seu olhar e domine a arte da fotografia, mesmo com o celular!

Com nosso curso online para iniciantes, você vai:
✨ Aprender técnicas profissionais de forma simples.
💡 Desvendar os segredos da luz e composição.
🚀 Criar imagens incríveis com qualquer câmera que tiver!

Liberte o fotógrafo que existe em você. Sua jornada criativa espera!

**CTA:**
Inscreva-se agora e comece a clicar!

**Hashtags:**
#FotografiaParaTodos #CursoDeFoto #AprendaFotografia

---

## 3. Resposta ao Prompt Estruturado (KERNEL) (Simulação GPT)

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

**Resultado Simulado GPT:**

**Headline:** Clique. Aprenda. Crie. Sua foto perfeita!

**Corpo:**
Descubra o universo da fotografia sem complicação! Nosso curso online é ideal para quem está começando e quer resultados profissionais.

Você vai:
1.  Entender sua câmera (até a do celular!) como nunca.
2.  Compor cenas que contam histórias.
3.  Editar suas fotos para um toque mágico final.

Não adie mais seu sonho de fotografar! Abrace sua criatividade hoje.

**CTA:**
Inscreva-se agora e transforme seu olhar!

**Hashtags:**
#FotografiaIniciante #CursoOnline #DesperteSeuOlhar
