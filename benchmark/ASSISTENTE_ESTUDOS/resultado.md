# RESULTADO DO BENCHMARK: ASSISTENTE DE ESTUDOS

Este arquivo documenta os resultados gerados por um modelo de IA para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico

**Prompt:** `Me ajude a estudar.`

**Resultado:**

Claro, estou aqui para isso! Para que eu possa te ajudar da melhor forma, me diga:

1.  **O que você está estudando?** (Qual matéria ou tópico?)
2.  **Qual é o seu objetivo?** (Se preparar para uma prova, entender um conceito, fazer um trabalho?)
3.  **Que tipo de ajuda você precisa?** (Um resumo, um plano de estudos, explicações, exemplos, exercícios?)
4.  **Existe algum material de base** que você está usando (livro, artigos, anotações de aula)?

Com essas informações, posso criar um material de apoio perfeito para você!

---

## 2. Resposta ao Prompt Estruturado (JSON)

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

**Resultado:**

### **Plano de Estudos: Revolução Francesa em 5 Dias**

| Dia | Tópico Principal | Atividade Sugerida |
| :-- | :--- | :--- |
| **1** | **As Causas da Revolução** | **Leitura e Anotação:** Focar na crise do Antigo Regime, a desigualdade dos Três Estados, a crise econômica e as ideias do Iluminismo. Anote os principais pontos. |
| **2** | **As Fases Iniciais (1789-1792)** | **Assistir a um Vídeo:** Procure um documentário curto sobre a Queda da Bastilha, a Assembleia Nacional Constituinte e a Declaração dos Direitos do Homem e do Cidadão. |
| **3** | **A Convenção Nacional e o Terror (1792-1794)** | **Resumo e Mapa Mental:** Ler sobre a ascensão dos Jacobinos, a execução de Luís XVI e a figura de Robespierre. Crie um mapa mental conectando os eventos. |
| **4*** | **O Diretório e a Ascensão de Napoleão (1795-1799)** | **Responder a Perguntas:** Responda a questões sobre a instabilidade do Diretório e como ela abriu caminho para o Golpe de 18 de Brumário de Napoleão Bonaparte. |
| **5** | **Consequências e Revisão Geral** | **Revisão Ativa:** Releia suas anotações, explique o processo todo em voz alta para si mesmo e faça as perguntas de autoavaliação abaixo. |

---

### **Resumo do Tópico: A Revolução Francesa (1789-1799)**

A Revolução Francesa foi um dos eventos mais transformadores da história moderna, abalando as fundações do Antigo Regime e espalhando ideais de "Liberdade, Igualdade e Fraternidade". Suas causas são complexas, envolvendo uma profunda crise econômica, a fome que assolava a população mais pobre (o Terceiro Estado), e a imensa desigualdade social, onde clero (Primeiro Estado) e nobreza (Segundo Estado) gozavam de privilégios e isenção de impostos. As ideias do Iluminismo, que questionavam o absolutismo e defendiam os direitos individuais, forneceram a base ideológica para a revolta.

O estopim ocorreu em 1789 com a convocação dos Estados Gerais, que levou à proclamação da Assembleia Nacional Constituinte pelo Terceiro Estado. O evento simbólico que marcou o início da revolução foi a **Queda da Bastilha** em 14 de julho de 1789. Logo depois, foi promulgada a **Declaração dos Direitos do Homem e do Cidadão**, um documento fundamental que defendia direitos universais.

A revolução se radicalizou na fase da **Convenção Nacional** (1792-1795), marcada pela ascensão dos **Jacobinos**, liderados por Maximilien de Robespierre. O rei Luís XVI foi guilhotinado em 1793, e o Período do Terror se instaurou, com milhares de "inimigos da revolução" sendo executados.

Após a queda de Robespierre, a fase do **Diretório** (1795-1799) tentou estabilizar o país, mas foi marcada por corrupção e instabilidade política. Esse cenário de caos permitiu a ascensão de uma figura militar popular: **Napoleão Bonaparte**. Com o Golpe de 18 de Brumário (1799), Napoleão tomou o poder, encerrando o período revolucionário e iniciando a Era Napoleônica. As consequências da revolução foram duradouras, incluindo o fim do absolutismo na França, a ascensão da burguesia e a disseminação de ideais republicanos e liberais pelo mundo.

---

### **Autoavaliação**

1.  Qual evento é considerado o marco simbólico do início da Revolução Francesa?
    a) A execução do Rei Luís XVI
    b) O Golpe de 18 de Brumário
    c) A Queda da Bastilha
    d) A Declaração dos Direitos do Homem

2.  Durante o Período do Terror, o grupo político que estava no poder era o dos:
    a) Girondinos
    b) Jacobinos
    c) Realistas
    d) Iluministas

3.  A ascensão de Napoleão Bonaparte ao poder está diretamente ligada à instabilidade de qual fase da Revolução?
    a) Assembleia Nacional Constituinte
    b) O Diretório
    c) O Período do Terror
    d) Os Estados Gerais

*(Respostas: 1-c, 2-b, 3-b)*

---

## 3. Resposta ao Prompt Estruturado (KERNEL)

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

**Resultado:**

#### **Plano de Estudos: Revolução Francesa**

*   **Dia 1: Contexto e Causas.** Foco: Crise financeira da França, divisão da sociedade em três estados, influência das ideias iluministas. Atividade: Criar uma lista com os principais motivos que levaram à revolução.
*   **Dia 2: A Primeira Fase (1789-1791).** Foco: Queda da Bastilha, a Grande Medo no campo, e a Declaração dos Direitos do Homem. Atividade: Escrever um parágrafo sobre a importância da Queda da Bastilha.
*   **Dia 3: A Monarquia Constitucional e a República (1791-1793).** Foco: Fuga do rei, guerra contra Áustria e Prússia, proclamação da República e execução de Luís XVI. Atividade: Assistir a um vídeo sobre o julgamento de Luís XVI.
*   **Dia 4: O Terror Jacobino (1793-1794).** Foco: O governo de Robespierre, o Comitê de Salvação Pública e a Lei dos Suspeitos. Atividade: Fazer um mapa mental ligando Robespierre, os Jacobinos e o "Terror".
*   **Dia 5: O Diretório e a Chegada de Napoleão.** Foco: A reação termidoriana, a instabilidade do Diretório e o Golpe de 18 de Brumário. Atividade: Responder às perguntas de autoavaliação e revisar todo o conteúdo.

#### **Resumo do Tópico: Revolução Francesa**

A Revolução Francesa (1789-1799) foi um período de intensa agitação política e social que pôs fim ao Antigo Regime na França. Suas raízes estão na profunda crise econômica e na injusta estrutura social do país, onde o Terceiro Estado (burguesia, camponeses e trabalhadores) arcava com pesados impostos enquanto a nobreza e o clero eram isentos. Inspirados pelos ideais de liberdade e razão do Iluminismo, os membros do Terceiro Estado passaram a exigir maior representação política.

A revolução eclodiu em 1789 com a Tomada da Bastilha, uma prisão que simbolizava a opressão do absolutismo. Este ato marcou o início de uma série de mudanças, incluindo a abolição dos privilégios feudais e a publicação da Declaração dos Direitos do Homem e do Cidadão, que afirmava que todos os homens nascem livres e iguais em direitos.

A fase mais radical foi a Convenção Nacional, dominada pelos jacobinos sob a liderança de Robespierre. Este período, conhecido como o Terror, viu a execução do rei Luís XVI e de milhares de supostos opositores da revolução na guilhotina. A violência e a instabilidade levaram à queda dos jacobinos.

A fase final, o Diretório, foi um governo mais conservador que, no entanto, falhou em trazer estabilidade. Em meio ao caos, o general Napoleão Bonaparte emergiu como uma figura de autoridade. Em 1799, ele liderou o Golpe de 18 de Brumário, tomando o poder e efetivamente encerrando a revolução. O legado da Revolução Francesa, no entanto, perdura, tendo influenciado movimentos republicanos e democráticos em todo o mundo.

#### **Perguntas de Teste**

1.  A sociedade francesa pré-revolucionária era dividida em três estados. Qual deles arcava com a maior parte dos impostos?
    a) O Primeiro Estado (Clero)
    b) O Segundo Estado (Nobreza)
    c) O Terceiro Estado (Povo e Burguesia)
    d) Todos os estados pagavam impostos iguais.

2.  O Período do Terror foi liderado principalmente por qual grupo político?
    a) Os Girondinos
    b) Os Jacobinos
    c) Os Monarquistas
    d) Os Burgueses

3.  O que foi o Golpe de 18 de Brumário?
    a) A invasão da Bastilha que deu início à revolução.
    b) A execução do rei Luís XVI na guilhotina.
    c) A tomada do poder por Napoleão Bonaparte, encerrando o Diretório.
    d) A declaração de guerra contra a Áustria e a Prússia.

*(Respostas: 1-c, 2-b, 3-c)*
