# RESULTADO DO BENCHMARK: ASSISTENTE DE EMERGÊNCIA

Este arquivo documenta os resultados gerados por um modelo de IA para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico

**Prompt:** `O que fazer em uma emergência?`

**Resultado:**

**Esta é uma pergunta muito séria. A resposta depende inteiramente do tipo de emergência.**

**Se for uma emergência médica, de segurança ou risco de vida, a primeira e mais importante ação é contatar os serviços de emergência locais imediatamente.**

*   **Brasil:** 192 (SAMU - Emergência Médica), 193 (Corpo de Bombeiros), 190 (Polícia Militar)
*   **Outros países:** Verifique o número de emergência local (como 911, 112, etc.).

Para que eu possa fornecer informações úteis (que **NÃO** substituem a ajuda profissional), por favor, especifique o tipo de emergência. Por exemplo:
*   "O que fazer em caso de queimadura?"
*   "Como proceder em caso de engasgamento?"
*   "Quais os primeiros socorros para um corte profundo?"

**AVISO: Eu sou um modelo de linguagem e não posso fornecer aconselhamento médico. As informações são para fins educacionais. Sempre procure ajuda profissional qualificada em uma emergência.**

---

## 2. Resposta ao Prompt Estruturado (JSON)

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

**Resultado:**

### **Instruções para Engasgamento em Adulto**

**LIGUE PARA A EMERGÊNCIA (192 - SAMU) IMEDIATAMENTE SE A PESSOA NÃO CONSEGUIR RESPIRAR.**

1.  **AVALIE A SITUAÇÃO:**
    *   Pergunte: "Você está engasgado?".
    *   Verifique se a pessoa consegue tossir com força ou falar.
    *   **Se a pessoa tossir com força,** incentive-a a continuar tossindo. Não faça nada.

2.  **SE A PESSOA NÃO CONSEGUE TOSSIR, FALAR OU RESPIRAR:**
    *   Aja imediatamente.
    *   **Dê 5 batidas nas costas:** Fique ao lado e um pouco atrás da pessoa. Apoie o peito dela com uma mão e incline-a para a frente. Dê 5 batidas fortes entre as omoplatas com a base da sua outra mão.

3.  **SE NÃO FUNCIONAR, INICIE A MANOBRA DE HEIMLICH:**
    *   Fique de pé atrás da pessoa.
    *   Passe seus braços ao redor da cintura dela.
    *   Feche uma das mãos em punho e posicione-a um pouco acima do umbigo da pessoa.
    *   Com a outra mão, agarre seu punho e pressione a barriga da pessoa com um movimento rápido para dentro e para cima, como se fosse a letra "J".
    *   Repita o movimento até o objeto ser expelido ou a ajuda chegar.

4.  **APÓS O DESENGASGO:**
    *   Procure atendimento médico mesmo que o objeto tenha sido expelido, pois podem ocorrer lesões internas.

**AVISO LEGAL:** Estas instruções são para fins informativos e de primeiros socorros. Elas **NÃO SUBSTITUEM** o atendimento por um profissional de saúde qualificado ou o chamado ao serviço de emergência. Ações de primeiros socorros mal aplicadas podem causar danos.

---

## 3. Resposta ao Prompt Estruturado (KERNEL)

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

**Resultado:**

### **Ação Rápida: Engasgamento em Adulto**

**PRIMEIRO PASSO: LIGUE PARA EMERGÊNCIA (192) se a pessoa não respira ou está ficando azul.**

#### **1. Avalie a Vítima**
*   A pessoa consegue tossir ou falar?
*   **SIM:** Incentive a tosse. Não interfira. A tosse é o método mais eficaz.
*   **NÃO:** A pessoa não emite som ou a tosse é muito fraca. Aja imediatamente.

#### **2. Manobra de Desobstrução (Manobra de Heimlich)**
*   **Posicione-se:** Fique por trás da vítima.
*   **Enlace a cintura:** Passe os braços ao redor do abdômen da pessoa.
*   **Posicione as mãos:** Cerre um punho e coloque o lado do polegar contra o abdômen, na linha média, um pouco acima do umbigo. Agarre seu punho com a outra mão.
*   **Execute as compressões:** Puxe o punho para dentro e para cima, com força. Faça compressões rápidas e vigorosas.
*   **Continue:** Repita até que o objeto saia ou a pessoa perca a consciência.

#### **3. Após a Desobstrução**
*   Mesmo que o objeto seja expelido, a vítima deve ser avaliada por um profissional de saúde.

---
**AVISO LEGAL PROEMINENTE**

**As informações acima são um guia de primeiros socorros e não substituem, em hipótese alguma, o atendimento médico profissional. A aplicação incorreta das manobras pode causar ferimentos. A prioridade é sempre acionar o serviço de emergência local (SAMU - 192).**
---
