# RESULTADO DO BENCHMARK (SIMULADO GPT): ASSISTENTE DE ESTUDOS

Este arquivo documenta os resultados simulados de um modelo GPT para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico (Simulação GPT)

**Prompt:** `Me ajude a estudar.`

**Resultado Simulado GPT:**

Com certeza! Estou aqui para ser seu parceiro de estudos. Para que eu possa te oferecer a melhor ajuda possível, preciso de algumas informações:

1.  **Qual é a matéria ou o tópico específico** que você está estudando? (Ex: História da Revolução Francesa, Cálculo Diferencial, Biologia Celular)
2.  **Qual é o seu objetivo?** (Ex: Preparar-se para uma prova, entender um conceito difícil, fazer um trabalho, revisar para um exame final)
3.  **Que tipo de material de estudo** você prefere ou precisa? (Ex: Resumos, mapas mentais, exercícios, explicações detalhadas, plano de estudos)
4.  **Qual o seu prazo?** (Ex: Tenho uma prova na próxima semana, preciso entender isso hoje)

Com esses detalhes, posso personalizar a ajuda para você!

---

## 2. Resposta ao Prompt Estruturado (JSON) (Simulação GPT)

**Prompt:**
```json
{
  "task": "criar_plano_de_estudos_e_resumo",
  "context": {
    "background": "Um estudante precisa de ajuda para se preparar para uma prova de história.",
    "user_goal": "Gerar um plano de estudos semanal e um resumo sobre a Revolução Francesa."
  },
  "instructions": {
    "steps": [
      "Criar um plano de estudos de 5 dias, dividindo os principais tópicos da Revolução Francesa (Causas, Fases, Consequências).",
      "Para cada dia, sugerir um tópico específico e uma atividade (ex: leitura, assistir a um vídeo, responder a perguntas).",
      "Gerar um resumo conciso (máximo 500 palavras) sobre a Revolução Francesa, destacando os eventos e personagens principais.",
      "No final, criar 3 perguntas de múltipla escolha sobre o tema para autoavaliação."
    ],
    "output_format": "Documento de texto com duas seções: 'Plano de Estudos' e 'Resumo do Tópico'."
  },
  "constraints": [
    "A linguagem deve ser clara e didática.",
    "O resumo deve ser imparcial e focado nos fatos históricos.",
    "As perguntas devem cobrir diferentes aspectos do resumo."
  ],
  "user_input": "Tenho uma prova sobre a Revolução Francesa na próxima semana."
}
```

**Resultado Simulado GPT:**

### **Plano de Estudos e Resumo: Revolução Francesa**

#### **Plano de Estudos (5 Dias)**

| Dia | Tópico Principal | Atividade Sugerida |
| :-- | :--- | :--- |
| **1** | **As Raízes da Revolução:** Antigo Regime, crise econômica, sociedade estamental, Iluminismo. | **Leitura:** Capítulos do livro didático sobre as causas da Revolução. **Anotações:** Crie um esquema dos fatores que levaram à revolta. |
| **2** | **O Início da Revolução (1789-1791):** Queda da Bastilha, Assembleia Nacional Constituinte, Declaração dos Direitos do Homem e do Cidadão. | **Vídeo:** Assista a um documentário curto sobre os eventos de 1789. **Discussão:** Pense nas implicações da Declaração. |
| **3** | **A Radicalização (1792-1794):** Monarquia Constitucional, Convenção Nacional, Jacobinos, Período do Terror (Robespierre). | **Resumo:** Elabore um resumo dos principais eventos e figuras do Período do Terror. **Análise:** Quais foram as justificativas e consequências? |
| **4** | **O Diretório e o Fim da Revolução (1795-1799):** Reação Termidoriana, instabilidade política, ascensão de Napoleão Bonaparte. | **Pesquisa:** Entenda o contexto do Golpe de 18 de Brumário. **Conexão:** Como a Revolução abriu caminho para Napoleão? |
| **5** | **Revisão Geral e Impacto:** Consequências da Revolução na França e no mundo. | **Autoavaliação:** Responda às perguntas de múltipla escolha abaixo. **Revisão:** Revise seus resumos e anotações. |

---

#### **Resumo do Tópico: A Revolução Francesa (1789-1799)**

A Revolução Francesa foi um divisor de águas na história ocidental, marcando o fim do absolutismo monárquico e do sistema feudal na França, e disseminando ideais de liberdade, igualdade e fraternidade. Suas origens remontam a uma profunda crise social, econômica e política no final do século XVIII. A sociedade era rigidamente dividida em três estados: o clero (Primeiro Estado), a nobreza (Segundo Estado), ambos privilegiados e isentos de impostos, e o Terceiro Estado (burguesia, camponeses e trabalhadores urbanos), que arcava com a maior parte da carga tributária e não possuía direitos políticos. A crise financeira do Estado, agravada por gastos excessivos e guerras, somada à influência das ideias iluministas que questionavam o poder divino dos reis, criou um cenário explosivo.

O estopim da revolução foi a convocação dos Estados Gerais em 1789, que rapidamente evoluiu para a formação da Assembleia Nacional Constituinte pelo Terceiro Estado. A **Tomada da Bastilha**, em 14 de julho de 1789, tornou-se o símbolo da revolta popular. A **Declaração dos Direitos do Homem e do Cidadão**, proclamada em agosto do mesmo ano, estabeleceu princípios de liberdade, igualdade e soberania popular.

A revolução passou por fases de radicalização. Após a tentativa de fuga do rei Luís XVI e a crescente ameaça externa, a monarquia foi abolida e a República proclamada em 1792. O período mais intenso foi o **Período do Terror** (1793-1794), liderado pelos jacobinos e seu líder, **Maximilien de Robespierre**. Milhares de opositores reais ou supostos foram guilhotinados.

A queda de Robespierre em 1794 levou à fase do **Diretório** (1795-1799), um governo mais conservador, mas marcado pela instabilidade e corrupção. Esse cenário abriu caminho para a ascensão de um jovem e carismático general, **Napoleão Bonaparte**, que, através do Golpe de 18 de Brumário (1799), assumiu o poder, pondo fim à Revolução e iniciando uma nova era na história europeia. As consequências da Revolução Francesa foram vastas, influenciando movimentos revolucionários e a formação de estados-nação modernos em todo o mundo.

---

#### **Perguntas de Múltipla Escolha para Autoavaliação**

1.  Qual dos seguintes fatores NÃO foi uma causa principal da Revolução Francesa?
    a) A crise financeira do Estado.
    b) A desigualdade social entre os Três Estados.
    c) A ascensão de Napoleão Bonaparte.
    d) A influência das ideias iluministas.

2.  O evento que simbolizou o início da Revolução Francesa e a queda do absolutismo foi:
    a) A execução de Luís XVI.
    b) A Tomada da Bastilha.
    c) A convocação dos Estados Gerais.
    d) O Golpe de 18 de Brumário.

3.  O líder mais proeminente do Período do Terror foi:
    a) Luís XVI.
    b) Napoleão Bonaparte.
    c) Maximilien de Robespierre.
    d) Jean-Jacques Rousseau.

*(Respostas: 1-c, 2-b, 3-c)*

---

## 3. Resposta ao Prompt Estruturado (KERNEL) (Simulação GPT)

**Prompt:**
- **K (Keep it simple):** Criar um plano de estudos e um resumo sobre a Revolução Francesa.
- **E (Easy to verify):** O resultado deve conter um plano de 5 dias, um resumo de até 500 palavras e 3 perguntas de múltipla escolha.
- **R (Reproducible results):** O conteúdo histórico é factual e não muda.
- **N (Narrow scope):** A tarefa está focada em um único tópico histórico.
- **E (Explicit constraints):** Resumo com no máximo 500 palavras, linguagem didática.
- **L (Logical structure):**
    1.  **Task:** Gerar um plano de estudos semanal e um resumo sobre a Revolução Francesa.
    2.  **Input:** Prova de história sobre a Revolução Francesa.
    3.  **Constraints:** Resumo limitado a 500 palavras. Linguagem clara. Incluir 3 perguntas de teste.
    4.  **Output:** Documento com as seções 'Plano de Estudos' e 'Resumo do Tópico'.
    5.  **Verify:** Verificar a estrutura do plano, a contagem de palavras do resumo e a presença das 3 perguntas.

**Resultado Simulado GPT:**

### **Guia de Estudos: Revolução Francesa**

#### **Plano de Estudos de 5 Dias**

| Dia | Tema | Atividade Sugerida |
| :-- | :--- | :--- |
| **1** | **Contexto Pré-Revolucionário:** Crise do Antigo Regime, sociedade estamental, ideias iluministas. | **Leitura:** Artigos e capítulos sobre as causas da Revolução. **Esquema:** Crie um diagrama das classes sociais e seus privilégios. |
| **2** | **Eventos Iniciais (1789-1791):** Queda da Bastilha, Grande Medo, Declaração dos Direitos do Homem e do Cidadão. | **Análise de Documentos:** Leia trechos da Declaração e discuta seus princípios. **Linha do Tempo:** Crie uma linha do tempo dos principais eventos de 1789. |
| **3** | **A Fase Radical (1792-1794):** Proclamação da República, Jacobinos, Robespierre, Período do Terror. | **Estudo de Caso:** Pesquise sobre a figura de Robespierre e o Comitê de Salvação Pública. **Debate Interno:** Quais os dilemas morais do Terror? |
| **4** | **O Diretório e o Fim (1795-1799):** Reação Termidoriana, instabilidade, ascensão de Napoleão. | **Conexão:** Como a instabilidade do Diretório favoreceu a ascensão de um líder militar? **Consequências:** Liste as principais consequências da Revolução. |
| **5** | **Revisão e Teste:** Consolidação do conhecimento. | **Revisão Ativa:** Explique os tópicos para um "colega imaginário". **Teste:** Responda às perguntas de múltipla escolha abaixo. |

---

#### **Resumo: A Revolução Francesa**

A Revolução Francesa (1789-1799) foi um período de profundas transformações sociais e políticas na França, que reverberou por toda a Europa e o mundo. Impulsionada por uma grave crise econômica, a insatisfação do Terceiro Estado (burguesia, camponeses e trabalhadores) com os privilégios da nobreza e do clero, e a influência das ideias iluministas de liberdade e igualdade, a revolução buscou derrubar o absolutismo monárquico.

O marco inicial foi a **Tomada da Bastilha** em 14 de julho de 1789. Rapidamente, a Assembleia Nacional Constituinte aboliu os privilégios feudais e proclamou a **Declaração dos Direitos do Homem e do Cidadão**, estabelecendo princípios de igualdade perante a lei e direitos individuais. A monarquia foi derrubada e a República proclamada em 1792.

A fase mais radical foi o **Período do Terror** (1793-1794), liderado pelos **Jacobinos** e seu principal expoente, **Maximilien de Robespierre**. Milhares de pessoas consideradas inimigas da revolução foram guilhotinadas. Após a queda de Robespierre, o governo passou para o **Diretório** (1795-1799), que tentou estabilizar o país, mas enfrentou grande instabilidade política e econômica.

Esse cenário de caos e a necessidade de um governo forte para defender a França das coalizões estrangeiras abriram caminho para a ascensão de **Napoleão Bonaparte**. Em 1799, com o Golpe de 18 de Brumário, Napoleão tomou o poder, encerrando a Revolução Francesa e iniciando a era napoleônica. O legado da Revolução inclui o fim do absolutismo, a ascensão da burguesia, a disseminação de ideais democráticos e nacionalistas, e a inspiração para futuras revoluções.

---

#### **Perguntas de Múltipla Escolha**

1.  Qual documento fundamental da Revolução Francesa estabeleceu princípios de liberdade e igualdade?
    a) A Constituição de 1791
    b) A Declaração dos Direitos do Homem e do Cidadão
    c) O Código Napoleônico
    d) O Tratado de Versalhes

2.  O Período do Terror foi caracterizado pela forte atuação de qual grupo político?
    a) Girondinos
    b) Monarquistas
    c) Jacobinos
    d) Sans-culottes

3.  A Revolução Francesa foi encerrada com:
    a) A Queda da Bastilha.
    b) A execução de Luís XVI.
    c) O Golpe de 18 de Brumário de Napoleão.
    d) A formação da Assembleia Nacional Constituinte.

*(Respostas: 1-b, 2-c, 3-c)*
