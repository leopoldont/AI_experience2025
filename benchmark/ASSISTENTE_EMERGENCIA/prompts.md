# PROMPTS PARA ASSISTENTE DE EMERGÊNCIA

---

## 1. Prompt Genérico

O que fazer em uma emergência?

---

## 2. Prompt Estruturado (JSON)

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

---

## 3. Prompt Estruturado (KERNEL)

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
