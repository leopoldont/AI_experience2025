# RESULTADO DO BENCHMARK (SIMULADO GPT): ASSISTENTE DE EMERGÊNCIA

Este arquivo documenta os resultados simulados de um modelo GPT para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico (Simulação GPT)

**Prompt:** `O que fazer em uma emergência?`

**Resultado Simulado GPT:**

Em uma emergência, a primeira e mais crucial ação é **garantir a segurança e buscar ajuda profissional imediatamente.**

**AVISO IMPORTANTE:** Eu sou uma inteligência artificial e não posso substituir o julgamento humano ou o atendimento de profissionais de emergência. Minhas informações são para fins educativos e não constituem aconselhamento médico ou de segurança.

Para que eu possa fornecer a informação mais relevante, por favor, especifique o tipo de emergência:

*   É uma emergência médica (ex: ataque cardíaco, engasgamento, acidente)?
*   É uma situação de segurança (ex: incêndio, invasão, desastre natural)?
*   Qual é a sua localização para que eu possa sugerir números de emergência locais?

**Em caso de risco de vida imediato, ligue para os serviços de emergência do seu país (ex: 192 SAMU, 193 Bombeiros, 190 Polícia no Brasil; 911 nos EUA; 112 na Europa).**

---

## 2. Resposta ao Prompt Estruturado (JSON) (Simulação GPT)

**Prompt:**
```json
{
  "task": "fornecer_instrucoes_de_primeiros_socorros",
  "context": {
    "background": "Um usuário está buscando informações sobre como agir em uma situação de emergência médica.",
    "user_goal": "Obter instruções claras e imediatas para um caso de engasgamento em um adulto."
  },
  "instructions": {
    "steps": [
      "Avaliar a situação: verificar se a pessoa consegue tossir ou falar.",
      "Se não conseguir, iniciar a Manobra de Heimlich.",
      "Descrever o passo a passo da Manobra de Heimlich de forma clara e concisa.",
      "Indicar quando e como chamar o serviço de emergência (ex: SAMU 192 no Brasil).",
      "Incluir um aviso para procurar ajuda médica mesmo que o objeto seja expelido."
    ],
    "output_format": "Lista de instruções numerada, com frases curtas e diretas."
  },
  "constraints": [
    "A informação deve ser apresentada de forma que possa ser lida e compreendida em segundos.",
    "**NÃO DEVE, EM HIPÓTESE ALGUMA, SUBSTITUIR O ATENDIMENTO MÉDICO PROFISSIONAL.**",
    "Incluir um aviso legal destacando que as instruções são para fins informativos e não substituem a consulta a um profissional qualificado."
  ],
  "user_input": "Como ajudar um adulto que está engasgado?"
}
```

**Resultado Simulado GPT:**

### **Primeiros Socorros: Engasgamento em Adultos**

**EM CASO DE EMERGÊNCIA GRAVE (PESSOA NÃO RESPIRA OU ESTÁ INCONSCIENTE), LIGUE PARA 192 (SAMU) IMEDIATAMENTE!**

1.  **Avalie a Vítima:**
    *   Pergunte: "Você está engasgado?"
    *   Observe se a pessoa consegue tossir, falar ou respirar.
    *   **Se a tosse for forte e eficaz:** Incentive a pessoa a tossir. Não interfira.
    *   **Se a tosse for fraca, a pessoa não conseguir falar ou respirar:** Aja rapidamente.

2.  **Manobra de Heimlich (Consciente):**
    *   **Posicione-se:** Fique atrás da pessoa, envolvendo-a com seus braços na altura da cintura.
    *   **Punho:** Feche uma das mãos em punho e posicione-a logo acima do umbigo da pessoa.
    *   **Outra Mão:** Segure o punho com a outra mão.
    *   **Compressões:** Faça compressões rápidas e fortes para dentro e para cima, como se estivesse tentando levantar a pessoa.
    *   **Repita:** Continue as compressões até que o objeto seja expelido ou a pessoa perca a consciência.

3.  **Após o Engasgo:**
    *   Mesmo que o objeto seja expelido e a pessoa pareça bem, é recomendável procurar atendimento médico para verificar possíveis lesões internas.

---
**AVISO LEGAL:** Estas instruções são para fins informativos e de primeiros socorros. Elas **NÃO SUBSTITUEM** o atendimento médico profissional ou o chamado aos serviços de emergência. A aplicação incorreta pode causar danos.
---

## 3. Resposta ao Prompt Estruturado (KERNEL) (Simulação GPT)

**Prompt:**
- **K (Keep it simple):** Fornecer instruções de primeiros socorros para um adulto engasgado.
- **E (Easy to verify):** O resultado deve incluir a avaliação da situação, os passos da Manobra de Heimlich, a instrução para chamar a emergência e o aviso legal.
- **R (Reproducible results):** O procedimento da Manobra de Heimlich é padronizado.
- **N (Narrow scope):** A tarefa foca apenas em engasgamento em adultos.
- **E (Explicit constraints):** Linguagem simples e direta. Incluir aviso legal sobre não substituir ajuda profissional.
- **L (Logical structure):**
    1.  **Task:** Gerar instruções de primeiros socorros para um adulto engasgado.
    2.  **Input:** Usuário precisa de ajuda imediata para um caso de engasgamento.
    3.  **Constraints:** As instruções devem ser rápidas de ler. **DEVE** conter um aviso legal claro.
    4.  **Output:** Lista numerada com o passo a passo da Manobra de Heimlich e quando chamar a emergência.
    5.  **Verify:** Checar se a lista de passos está correta e se o aviso legal foi incluído de forma proeminente.

**Resultado Simulado GPT:**

### **Guia Rápido: Engasgamento em Adultos**

**SE A PESSOA NÃO CONSEGUE RESPIRAR OU ESTÁ INCONSCIENTE, LIGUE PARA 192 (SAMU) IMEDIATAMENTE!**

#### **1. Verifique a Situação**
*   Pergunte à pessoa: "Você está engasgado?"
*   Observe se ela consegue tossir, falar ou respirar.
*   **Se a tosse for forte:** Encoraje a tosse. Não faça mais nada.
*   **Se a tosse for fraca, a pessoa não conseguir falar ou respirar:** Prossiga para a Manobra de Heimlich.

#### **2. Realize a Manobra de Heimlich**
*   **Posição:** Fique atrás da pessoa, com um pé ligeiramente à frente do outro para manter o equilíbrio.
*   **Braços:** Envolva a cintura da pessoa com seus braços.
*   **Punho:** Feche uma das mãos em punho e coloque-a logo acima do umbigo da pessoa.
*   **Mão Livre:** Segure o punho com a outra mão.
*   **Impulsos:** Faça compressões rápidas e fortes para dentro e para cima, como se estivesse tentando levantar a pessoa.
*   **Continue:** Repita até que o objeto seja expelido ou a pessoa perca a consciência.

#### **3. Após o Incidente**
*   É crucial que a pessoa seja examinada por um profissional de saúde, mesmo que o objeto tenha sido removido.

---
**AVISO LEGAL:** Este conteúdo é apenas para fins informativos e de primeiros socorros. **NÃO SUBSTITUI** o aconselhamento, diagnóstico ou tratamento médico profissional. Em qualquer emergência, procure ajuda médica qualificada.
---
